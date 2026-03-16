-- sql/04_load_raw.sql

COPY INTO RAW_MES_PRODUCTION (
    FILE_NAME,
    LOAD_TIMESTAMP,
    ROW_NUMBER_IN_FILE,
    PRODUCTION_DATE,
    PLANT_CODE,
    LINE_CODE,
    SHIFT_CODE,
    WORK_ORDER_ID,
    PRODUCT_ID,
    PRODUCT_DESCRIPTION,
    QUANTITY_PLANNED,
    QUANTITY_PRODUCED,
    QUANTITY_SCRAPPED,
    UOM,
    RUN_TIME_MINUTES,
    DOWNTIME_MINUTES,
    OPERATOR_ID,
    MACHINE_ID,
    SOURCE_SYSTEM
)
FROM (
    SELECT
        METADATA$FILENAME                                 AS FILE_NAME,
        CURRENT_TIMESTAMP()                               AS LOAD_TIMESTAMP,
        METADATA$FILE_ROW_NUMBER                          AS ROW_NUMBER_IN_FILE,
        TO_DATE($1)                                       AS PRODUCTION_DATE,
        $2                                                AS PLANT_CODE,
        $3                                                AS LINE_CODE,
        $4                                                AS SHIFT_CODE,
        $5                                                AS WORK_ORDER_ID,
        $6                                                AS PRODUCT_ID,
        $7                                                AS PRODUCT_DESCRIPTION,
        TO_NUMBER($8, 18, 2)                              AS QUANTITY_PLANNED,
        TO_NUMBER($9, 18, 2)                              AS QUANTITY_PRODUCED,
        TO_NUMBER($10, 18, 2)                             AS QUANTITY_SCRAPPED,
        $11                                               AS UOM,
        TO_NUMBER($12, 18, 2)                             AS RUN_TIME_MINUTES,
        TO_NUMBER($13, 18, 2)                             AS DOWNTIME_MINUTES,
        $14                                               AS OPERATOR_ID,
        $15                                               AS MACHINE_ID,
        'MES_CSV'                                         AS SOURCE_SYSTEM
    FROM @MES_PRODUCTION_STAGE
)
FILE_FORMAT = (FORMAT_NAME = MES_CSV_FORMAT);