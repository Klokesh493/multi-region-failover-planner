# Multi Region Failover Planner architecture

Chooses the safest failover region based on health, capacity, and replication lag.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
