# Multi Region Failover Planner walkthrough

## Business problem

A healthy standby region may lack capacity or have stale data. Failover review needs to consider all three signals before recommending a target.

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
