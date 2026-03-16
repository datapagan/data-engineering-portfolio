@'
# Assumptions and Limits

## Assumptions
- This project will start with yellow taxi trip data only.
- The first implementation will focus on one manageable time slice before scaling to more months.
- Taxi zones will be mapped using the official taxi zone lookup table.
- Raw data will be preserved as landed from source before transformations.
- Curated tables will prioritize analytics use cases over full operational reconstruction.

## Limits
- Public trip data may contain anomalies, nulls, and business outliers.
- A portfolio project will simulate enterprise design patterns, but not every production control will be implemented.
- Some fields may vary across taxi types or source file versions.
- Weather, events, and traffic context are not included in the first phase.
- This project is intended for analytics and portfolio demonstration, not regulatory reporting.
'@ | Set-Content docs\05_assumptions_and_limits.md