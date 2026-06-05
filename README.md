# SiLA2 Instrument Connectors

This repository is the home page for SiLA2 instrument connectors developed at the [Acceleration Consortium](https://acceleration.utoronto.ca/).

Each connector exposes a laboratory instrument as a [SiLA2](https://sila-standard.com/) gRPC service, making it addressable from any orchestration platform that speaks SiLA2 (e.g. [UniteLabs GroundControl](https://unitelabs.ch)).

## Browse All Connectors

**[→ View all connectors](https://github.com/orgs/AccelerationConsortium/repositories?q=topic%3Asila2-connector+sort%3Astars)**

This list is live — every new connector repo tagged `sila2-connector` appears there automatically.

To find connectors for a specific instrument family, combine topics:

| Filter | Link |
|--------|------|
| All connectors | [topic:sila2-connector](https://github.com/orgs/AccelerationConsortium/repositories?q=topic%3Asila2-connector) |
| Opentrons OT-2 | [topic:sila2-connector + topic:ot2](https://github.com/orgs/AccelerationConsortium/repositories?q=topic%3Asila2-connector+topic%3Aot2) |

## Structure

Each connector is a standalone repository named `sila2-<manufacturer>-<model>` and follows a common layout:

- **`src/`** — SiLA2 feature implementations
- **`workflows/`** — Prefect workflows that call the connector
- **`tests/`** — Unit and integration tests
- **`deploy.sh`** — One-command deploy to the instrument's onboard computer

## Contributing

To add a new connector:

1. Create a repo in `AccelerationConsortium` named `sila2-<manufacturer>-<model>`
2. Add the topic `sila2-connector` (and any device-specific topics)
3. It will appear in the connector list above automatically

For questions, open an issue in this repository.
