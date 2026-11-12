# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 failover_planner.py sample_regions.csv
us-west
test_selects_healthy_capacity_region (test_failover_planner.FailoverPlannerTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
