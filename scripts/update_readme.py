"""
Regenerate the connector list in README.md.

Queries GitHub for all repos tagged `sila2-connector` across every org
listed in orgs.txt (one org name per line), then rewrites the section
between <!-- CONNECTORS-START --> and <!-- CONNECTORS-END -->.
"""

import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).parent.parent

orgs = [
    line.strip()
    for line in (ROOT / "orgs.txt").read_text().splitlines()
    if line.strip() and not line.startswith("#")
]

org_filters = "+".join(f"org:{org}" for org in orgs)
query = f"topic:sila2-connector+{org_filters}&per_page=100"

result = subprocess.run(
    ["gh", "api", f"/search/repositories?q={query}",
     "--jq", '.items[] | select(.name != "sila2-connectors") | {name, description, html_url, private, full_name}'],
    capture_output=True, text=True, check=True,
)

repos = [json.loads(line) for line in result.stdout.strip().splitlines() if line]
repos.sort(key=lambda r: r["full_name"])

lines = []
for r in repos:
    lock = " 🔒" if r["private"] else ""
    desc = f" — {r['description']}" if r["description"] else ""
    lines.append(f"- [{r['full_name']}]({r['html_url']}){lock}{desc}")

block = "\n".join(lines) if lines else "_No connectors found._"

readme = ROOT / "README.md"
content = readme.read_text()
content = re.sub(
    r"<!-- CONNECTORS-START -->.*?<!-- CONNECTORS-END -->",
    f"<!-- CONNECTORS-START -->\n{block}\n<!-- CONNECTORS-END -->",
    content,
    flags=re.DOTALL,
)
readme.write_text(content)
print(f"Updated {len(repos)} connector(s) from {len(orgs)} org(s): {', '.join(orgs)}")
