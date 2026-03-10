-- Project 2 - API Workforce Data Pipeline
-- Create schema-level objects for the project

create database if not exists DATA_ENGINEERING_PORTFOLIO;
create schema if not exists DATA_ENGINEERING_PORTFOLIO.API_WORKFORCE_PIPELINE;

use database DATA_ENGINEERING_PORTFOLIO;
use schema API_WORKFORCE_PIPELINE;

create or replace file format FF_WORKFORCE_CSV
    type = csv
    skip_header = 1
    field_optionally_enclosed_by = '"'
    null_if = ('NULL', 'null', '');

create or replace stage STG_WORKFORCE_API_FILES
    file_format = FF_WORKFORCE_CSV;
