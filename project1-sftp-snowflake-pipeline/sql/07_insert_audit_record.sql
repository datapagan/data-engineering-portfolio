INSERT INTO DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.LOAD_AUDIT_LOG (
    file_name,
    target_table,
    load_timestamp,
    rows_loaded,
    load_status
)
SELECT
    'workforce_headcount.csv.gz' AS file_name,
    'WORKFORCE_RAW' AS target_table,
    CURRENT_TIMESTAMP() AS load_timestamp,
    COUNT(*) AS rows_loaded,
    'SUCCESS' AS load_status
FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.WORKFORCE_RAW;
