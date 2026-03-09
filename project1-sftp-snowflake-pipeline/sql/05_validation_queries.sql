--------- counts how many rows were loaded into the table.
  SELECT COUNT(*) AS row_count
  FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.WORKFORCE_RAW;

----------- checks if the primary identifier is missing, every employee must have an ID
  SELECT *
  FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.WORKFORCE_RAW
  WHERE employee_id IS NULL;

---------- calculates the average salary by department (sanity check)
  SELECT department, AVG(salary) AS avg_salary
  FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.WORKFORCE_RAW
  GROUP BY department
  ORDER BY avg_salary DESC;

/*--------------------------------------------------------------------------- 
counts employees per department
This verifies that:
categorical fields loaded correctly
data distributions make sense
-----------------------------------------------------------------------------*/
  SELECT department, COUNT(*) AS employee_count
  FROM DATA_ENGINEERING_PORTFOLIO.SFTP_PIPELINE.WORKFORCE_RAW
  GROUP BY department
  ORDER BY employee_count DESC;
