CREATE OR REPLACE TABLE CURATED.BLS_METRICS_MONTHLY (
    series_id         STRING,
    report_month      DATE,
    period_name       STRING,
    metric_value      NUMBER(18,4),
    data_quality_flag STRING,
    load_timestamp    TIMESTAMP_NTZ
);