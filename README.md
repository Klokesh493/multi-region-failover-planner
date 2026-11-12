# Multi Region Failover Planner

Chooses the safest failover region based on health, capacity, and replication lag.

Focus: Consumer-scale SRE resilience.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 failover_planner.py sample_regions.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

A healthy standby region may lack capacity or have stale data. Failover review needs to consider all three signals before recommending a target.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
