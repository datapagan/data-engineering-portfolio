------- creates an audit log table
CREATE OR REPLACE TABLE DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.LOAD_AUDIT_LOG (
    audit_id INTEGER AUTOINCREMENT START 1 INCREMENT 1,
    file_name STRING,
    target_table STRING,
    load_timestamp TIMESTAMP_NTZ,
    rows_loaded INTEGER,
    load_status STRING
);
