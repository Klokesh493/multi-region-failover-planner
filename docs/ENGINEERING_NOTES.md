# Skills and verification

## What this repository demonstrates

A failover selection CLI that keeps green regions with at least 25% free capacity and no more than 60 seconds of replication lag. It ranks eligible regions by available capacity, then by lowest lag.

## Reproduce the result

The fixture selects us-west. If no region passes all checks, the tool returns no-safe-failover. Reproduce the primary fixture with `python3 failover_planner.py sample_regions.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The recommendation uses a local snapshot. Verify replication and routing health before changing traffic.

Recheck health, capacity, and replication lag at decision time. A snapshot recommendation does not move traffic.

[failover_planner.py](../failover_planner.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
