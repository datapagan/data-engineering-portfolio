INSERT INTO P4_TRANSFORM.BLS_TIME_SERIES_CLEAN (
    series_id,
    year,
    period,
    period_name,
    value_num,
    invalid_value_flag,
    report_month,
    load_timestamp
)
SELECT
    series_id,
    TRY_TO_NUMBER(year) AS year,
    period,
    period_name,
    TRY_TO_NUMBER(value_raw) AS value_num,
    CASE
        WHEN TRY_TO_NUMBER(value_raw) IS NULL AND value_raw IS NOT NULL THEN TRUE
        ELSE FALSE
    END AS invalid_value_flag,
    CASE
        WHEN period LIKE 'M__' THEN TO_DATE(year || '-' || RIGHT(period, 2) || '-01')
        ELSE NULL
    END AS report_month,
    load_timestamp
FROM P4_RAW.BLS_TIME_SERIES_RAW;