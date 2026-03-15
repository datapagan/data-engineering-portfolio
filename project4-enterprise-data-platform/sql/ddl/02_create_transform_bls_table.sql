CREATE OR REPLACE TABLE P4_TRANSFORM.BLS_TIME_SERIES_CLEAN (
    series_id           STRING,
    year                NUMBER(4,0),
    period              STRING,
    period_name         STRING,
    value_num           NUMBER(18,4),
    invalid_value_flag  BOOLEAN,
    report_month        DATE,
    load_timestamp      TIMESTAMP_NTZ
);