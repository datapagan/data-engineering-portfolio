INSERT INTO P4_CURATED.BLS_METRICS_MONTHLY (
    series_id,
    report_month,
    period_name,
    metric_value,
    data_quality_flag,
    load_timestamp
)
SELECT
    series_id,
    report_month,
    period_name,
    value_num AS metric_value,
    CASE
        WHEN invalid_value_flag = TRUE THEN 'INVALID_SOURCE_VALUE'
        WHEN value_num IS NULL THEN 'MISSING_VALUE'
        ELSE 'VALID'
    END AS data_quality_flag,
    load_timestamp
FROM P4_TRANSFORM.BLS_TIME_SERIES_CLEAN;