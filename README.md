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
