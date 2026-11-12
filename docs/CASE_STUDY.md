# Multi Region Failover Planner walkthrough

## Business problem

Chooses the safest failover region based on health, capacity, and replication lag.

## Reproduce the workflow

Run `python3 failover_planner.py sample_regions.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
us-west
```

The sample supplies these fields. `region`, `health`, `free_capacity_pct`, `replication_lag_sec`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
