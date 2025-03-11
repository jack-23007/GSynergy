# GSynergy
Data Processing Flow in Azure Data Factory (ADF)
Step 1: Notebook Activity (Initial Processing)
Execute an Azure Databricks Notebook using a Notebook Activity in ADF.
Read data from the source system.
Perform initial transformations and data cleansing.
Store the processed data in Azure Blob Storage.

Step 2: Blob Storage (Staging Layer)
Store the transformed data in Azure Blob Storage as a temporary staging layer.
Ensure that data is available for further processing and validation.

Step 3: Notebook Activity (Validation Activity)
Execute another Azure Databricks Notebook to perform validation checks on the staged data.
Validate schema, data types, and missing values.
Apply business rules and generate an error log if validation fails.
Store the validated data in an intermediate storage layer.

Step 4: Joins (Notebook Activity)
Execute a Databricks Notebook to perform joins between multiple datasets.
Use PySpark or SQL queries to merge datasets based on business logic.
Ensure data consistency and integrity after the join operations.

Step 5: Aggregations
Perform aggregations on the joined data.
Apply summarization techniques such as SUM, COUNT, AVERAGE, GROUP BY operations.
Optimize the processing to handle large-scale data efficiently.
Step 6: Team Activity (Final Processing and Writing)

Team members review the processed data.
The final dataset is written back to Azure Blob Storage or Azure Synapse Analytics for further analysis.
Generate reports and logs to monitor data quality and pipeline performance.

Final Outcome
Validated, joined, and aggregated data is stored for downstream processing and business insights.