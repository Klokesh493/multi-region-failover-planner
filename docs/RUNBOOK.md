# Multi Region Failover Planner runbook

## What the project does

A healthy standby region may lack capacity or have stale data. Failover review needs to consider all three signals before recommending a target.

See the [architecture and data flow](ARCHITECTURE.md) and [project case study](CASE_STUDY.md).

## Run from a clean checkout

Use Python 3 and Make. Install the pinned developer tools in a local environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

Run a bundled scenario from the repository root.

```sh
python3 failover_planner.py sample_regions.csv
```

## Expected result

- Demo 1. `us-west` [Baseline](../examples/Demo%201.stdout.txt)
- Last sample record in isolation. `no-safe-failover` [Baseline](../examples/Last%20sample%20record%20in%20isolation.stdout.txt)

Run `make replay` to compare results with the baselines and regenerate the [replay report](../reports/replay.md).
The [rules page](RULES.md) links to the code behind the decision.

## Verify a change

Run `make check PYTHON=python` inside the virtual environment. This runs the application checks, Ruff lint, and the Bandit static gate.
The [development guide](DEVELOPMENT.md) explains the tools and the [local report](../reports/devsecops.md) records what passed.

## If a check fails

Run the first failing command on its own. For a replay mismatch, inspect the diff and compare the input, rule, and expected output before updating the baseline.
For a lint or Bandit finding, review the reported source line and rerun the relevant target.

## Golden note

Recheck health, capacity, and replication lag at decision time. A snapshot recommendation does not move traffic.

## Operating limits

Use the [case study](CASE_STUDY.md) to check assumptions before applying a result to a live environment.
