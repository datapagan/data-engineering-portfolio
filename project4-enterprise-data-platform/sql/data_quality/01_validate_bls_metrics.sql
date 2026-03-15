SELECT
    series_id,
    report_month,
    metric_value,
    data_quality_flag,
    CASE
        WHEN report_month IS NULL THEN 'FAIL'
        WHEN metric_value IS NULL AND data_quality_flag = 'VALID' THEN 'FAIL'
        ELSE 'PASS'
    END AS validation_status
FROM CURATED.BLS_METRICS_MONTHLY;