USE DATABASE DATA_ENGINEERING_PORTFOLIO;
USE SCHEMA P4_RAW;
CREATE OR REPLACE TABLE P4_RAW.BLS_TIME_SERIES_RAW (
    series_id       STRING,
    year            STRING,
    period          STRING,
    period_name     STRING,
    latest          STRING,
    value_raw       STRING,
    footnotes_raw   STRING,
    load_timestamp  TIMESTAMP_NTZ
);

SHOW TABLES IN SCHEMA P4_RAW;