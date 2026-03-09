# data-engineering-portfolio

## File Upload to Snowflake Stage

The sample workforce file was uploaded to the Snowflake internal stage using SnowSQL.

Example command:

  PUT file://C:/Users/YourUser/Downloads/workforce_headcount.csv
  @DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.STG_WORKFORCE_FILES
  AUTO_COMPRESS=TRUE
  OVERWRITE=TRUE;

The staged file was then validated with:

  LIST @DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.STG_WORKFORCE_FILES;

This approach reflects a realistic command-line ingestion pattern for loading files into Snowflake before executing COPY INTO.
