# SiLA2 Instrument Connectors

Collection of links to repositories that contain SiLA2 instrument connectors; each connector exposes a laboratory instrument as a [SiLA2](https://sila-standard.com/) gRPC service, making it addressable from any SiLA2-compatible orchestration platform.

## Connectors

<!-- CONNECTORS-START -->
- [AccelerationConsortium/openflexure-microscope-connector](https://github.com/AccelerationConsortium/openflexure-microscope-connector) — OpenFlexure Microscope UniteLabs Connector: SiLA 2 interface to the OpenFlexure Microscope Server v2 (stage, camera, captures, autofocus)
- [AccelerationConsortium/opentrons-flex](https://github.com/AccelerationConsortium/opentrons-flex) — Opentrons Flex Connector built for deployment on OTFlex hardware as a drop-in replacement for their HTTP server
- [AccelerationConsortium/opentrons-ot2](https://github.com/AccelerationConsortium/opentrons-ot2) — Opentrons OT2 UniteLabs Connector built for deployment on OT2 hardware as a drop-in replacement for their HTTP server
- [AccelerationConsortium/sainsmart-relay-sila](https://github.com/AccelerationConsortium/sainsmart-relay-sila) 🔒 — SiLA 2 connector for the SainSmart 16-channel USB relay (CH340) - UniteLabs CDK
- [AccelerationConsortium/ur5e-sila-connector](https://github.com/AccelerationConsortium/ur5e-sila-connector) — Cross-platform UR5e connector using SiLA 2 and the UniteLabs CDK, with a visual six-axis Action Composer, simulation, live telemetry, reusable tasks and trajectory export. macOS, Linux and Windows.
<!-- CONNECTORS-END -->

_🔒 = private repository. Access restricted to org members._

This list updates automatically when repos tagged `sila2-connector` are added to a tracked org. Connectors from multiple GitHub organizations can appear here — see [Contributing](#contributing).

## UniteLabs

- **[Connector Development Docs](https://docs.unitelabs.io/connector-development)** — getting started guide for building SiLA2 connectors with the UniteLabs CDK
- **[Connectors](https://gitlab.com/unitelabs/connectors)** — UniteLabs' GitLab library of SiLA2 connectors for commercial instruments
- **[Python CDK](https://gitlab.com/unitelabs/cdk/python-cdk)** — the SDK used to build and run these connectors

## Structure

Each connector is a standalone repository named `sila2-<manufacturer>-<model>` and follows a common layout:

- **`src/`** — SiLA2 feature implementations
- **`workflows/`** — Prefect workflows that call the connector
- **`tests/`** — Unit and integration tests
- **`deploy.sh`** — One-command deploy to the instrument's onboard computer

## Contributing

### Adding a connector within AccelerationConsortium

1. Create a repo in `AccelerationConsortium` named `sila2-<manufacturer>-<model>`
2. Add the topic `sila2-connector` (plus any device-specific topics e.g. `ot2`)
3. It will appear in the list above within 24 hours, or immediately via [manual trigger](../../actions/workflows/update-readme.yml)

### Listing connectors from another GitHub organization

Any organization building SiLA2 connectors is welcome to have them listed here.

**Step 1 — Tag your repos.** Add the topic `sila2-connector` to each connector repo in your GitHub organization. The topic must be exactly `sila2-connector` (no variations).

**Step 2 — Open a pull request.** Add your GitHub organization name as a new line in [`orgs.txt`](orgs.txt) in this repository and open a pull request. Once merged, your connectors will appear in the list above automatically.

If you have questions or would like to discuss before opening a PR, [open an issue](../../issues/new).
