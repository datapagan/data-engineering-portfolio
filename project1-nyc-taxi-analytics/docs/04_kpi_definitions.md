@'
# KPI Definitions

## Demand KPIs
- Total Trips: Count of trip records
- Trips by Pickup Zone: Count of trips grouped by pickup zone
- Trips by Dropoff Zone: Count of trips grouped by dropoff zone
- Trips by Hour: Count of trips grouped by pickup hour
- Trips by Day of Week: Count of trips grouped by weekday

## Revenue KPIs
- Total Revenue: Sum of total_amount
- Average Fare: Average of fare_amount
- Average Tip: Average of tip_amount
- Average Tip Percent: Sum of tip_amount divided by sum of fare_amount
- Revenue by Pickup Zone: Sum of total_amount grouped by pickup zone
- Revenue by Dropoff Zone: Sum of total_amount grouped by dropoff zone

## Efficiency KPIs
- Average Trip Distance: Average of trip_distance
- Average Trip Duration Minutes: Average trip duration in minutes
- Revenue per Mile: Sum of total_amount divided by sum of trip_distance
- Revenue per Trip: Sum of total_amount divided by count of trips

## Quality and Operational KPIs
- Null Zone Rate: Percent of trips with missing pickup or dropoff zone
- Invalid Fare Count: Trips with negative fare or invalid total
- Invalid Distance Count: Trips with zero or negative distance when business rules exclude them
'@ | Set-Content docs\04_kpi_definitions.md