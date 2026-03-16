-- sql/03_create_raw_table.sql

CREATE OR REPLACE TABLE RAW_MES_PRODUCTION (
    FILE_NAME               STRING,
    LOAD_TIMESTAMP          TIMESTAMP_NTZ,
    ROW_NUMBER_IN_FILE      NUMBER,

    PRODUCTION_DATE         DATE,
    PLANT_CODE              STRING,
    LINE_CODE               STRING,
    SHIFT_CODE              STRING,
    WORK_ORDER_ID           STRING,
    PRODUCT_ID              STRING,
    PRODUCT_DESCRIPTION     STRING,
    QUANTITY_PLANNED        NUMBER(18,2),
    QUANTITY_PRODUCED       NUMBER(18,2),
    QUANTITY_SCRAPPED       NUMBER(18,2),
    UOM                     STRING,
    RUN_TIME_MINUTES        NUMBER(18,2),
    DOWNTIME_MINUTES        NUMBER(18,2),
    OPERATOR_ID             STRING,
    MACHINE_ID              STRING,
    SOURCE_SYSTEM           STRING
);