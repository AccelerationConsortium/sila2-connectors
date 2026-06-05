# SiLA2 Instrument Connectors

SiLA2 instrument connectors developed at the [Acceleration Consortium](https://acceleration.utoronto.ca/). Each connector exposes a laboratory instrument as a [SiLA2](https://sila-standard.com/) gRPC service, making it addressable from any SiLA2-compatible orchestration platform.

## Connectors

<!-- CONNECTORS-START -->
- [opentrons-ot2](https://github.com/AccelerationConsortium/opentrons-ot2) 🔒 — Opentrons OT2 Unite Labs Connector built for deployment on OT2 hardware as a drop-in replacement for their HTTP server
<!-- CONNECTORS-END -->

_🔒 = private repository. Access restricted to org members._

This list updates automatically when repos tagged `sila2-connector` are added to the org.

## UniteLabs Connectors

UniteLabs maintains a library of connectors on GitLab:

> _GitLab org URL to be added._

## Structure

Each connector is a standalone repository named `sila2-<manufacturer>-<model>` and follows a common layout:

- **`src/`** — SiLA2 feature implementations
- **`workflows/`** — Prefect workflows that call the connector
- **`tests/`** — Unit and integration tests
- **`deploy.sh`** — One-command deploy to the instrument's onboard computer

## Contributing

To add a new connector:

1. Create a repo in `AccelerationConsortium` named `sila2-<manufacturer>-<model>`
2. Add the topic `sila2-connector` (plus any device-specific topics e.g. `ot2`)
3. It will appear in the list above within 24 hours, or immediately via [manual trigger](../../actions/workflows/update-readme.yml)
