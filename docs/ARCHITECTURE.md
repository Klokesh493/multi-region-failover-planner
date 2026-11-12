# Multi Region Failover Planner architecture

Chooses the safest failover region based on health, capacity, and replication lag.

```mermaid
flowchart LR
    N0["sample_regions.csv"]
    N1["failover_planner.py"]
    N2["choose region"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
