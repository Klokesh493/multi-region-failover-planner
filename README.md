# Multi Region Failover Planner

A healthy standby region may lack capacity or have stale data. Failover review needs to consider all three signals before recommending a target.

## What I built

I built a failover selection CLI that keeps green regions with at least 25% free capacity and no more than 60 seconds of replication lag. It ranks eligible regions by available capacity, then by lowest lag.

## How it works

```mermaid
flowchart LR
    A["Region health, capacity, and replication lag"]
    B["Keep green regions with at least 25% capacity and at most 60 s lag"]
    C{"Any eligible region?"}
    D["Rank by free capacity then replication lag"]
    E["No safe failover"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [failover_planner.py](failover_planner.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 failover_planner.py sample_regions.csv
```

The fixture selects us-west. If no region passes all checks, the tool returns no-safe-failover. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 failover_planner.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The recommendation uses a local snapshot. Verify replication and routing health before changing traffic.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
