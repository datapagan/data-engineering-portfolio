@'
# Data Dictionary

## Primary Source
NYC TLC Trip Record Data

## Reference Source
Taxi Zone Lookup Table

## Core Trip Fields
- VendorID: Trip data provider identifier
- tpep_pickup_datetime: Pickup timestamp
- tpep_dropoff_datetime: Dropoff timestamp
- passenger_count: Number of passengers
- trip_distance: Trip distance reported for the trip
- PULocationID: Pickup taxi zone identifier
- DOLocationID: Dropoff taxi zone identifier
- RatecodeID: Rate code in effect for the trip
- store_and_fwd_flag: Whether the record was held before sending to the vendor
- payment_type: Payment method
- fare_amount: Base fare amount
- extra: Extra charges
- mta_tax: MTA tax amount
- tip_amount: Tip amount
- tolls_amount: Tolls charged
- improvement_surcharge: Improvement surcharge
- total_amount: Total charged amount
- congestion_surcharge: Congestion surcharge
- airport_fee: Airport-related fee when applicable

## Taxi Zone Lookup Fields
- LocationID: Zone key used in trip data
- Borough: Borough name
- Zone: Zone name
- service_zone: TLC service zone grouping

## Business Notes
- PULocationID and DOLocationID connect trip data to the taxi zone lookup table.
- Pickup and dropoff timestamps support hour, day, weekday, and monthly trend analysis.
- Fare, tip, total amount, and trip distance support revenue and efficiency KPIs.
'@ | Set-Content docs\03_data_dictionary.md