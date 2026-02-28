# dataset-cleaner-report-generator
Python application that validates and cleans raw CSV datasets, converts valid records into JSONL format, logs rejected rows with reasons, and generates a detailed data quality report.
## Task 3: Dataset Cleaner + Report Generator (CSV → Clean JSONL + Report)

### Objective

To build a Python-based dataset cleaning system that validates raw CSV data, filters invalid records, converts clean data into JSONL format, and generates a data quality report.

### Description

In this task, a Dataset Cleaner and Report Generator was developed to process raw CSV datasets efficiently. The application reads dataset records row-by-row, validates data based on predefined schema rules, converts valid records into structured JSONL format, and logs invalid records along with rejection reasons. A summary report is also generated to analyze dataset quality.

### Tasks Performed

* Defined expected dataset schema with required columns and data types
* Implemented parsing helper functions (`safe_int`, `safe_float`)
* Applied validation rules for dataset fields
* Checked missing values and invalid entries
* Validated numerical ranges (e.g., age limits, negative income)
* Processed CSV data row-by-row
* Separated valid and invalid records
* Stored cleaned records into JSONL format
* Logged rejected records with error reasons
* Generated dataset summary report
* Added execution logging (rows processed, valid count, invalid count)
* Displayed preview of first 5 cleaned records

### Tools Used

* Python
* CSV Module
* JSON Handling
* Logging Module
* VS Code

### Output Files

* **clean.jsonl** – Valid cleaned dataset records
* **errors.jsonl** – Invalid records with rejection reasons
* **report.json** – Dataset quality summary report
* **log.txt** – Processing logs and execution details

### Result

The Dataset Cleaner successfully validates raw CSV data, separates clean and invalid records, and generates structured JSONL outputs along with a detailed report summarizing dataset quality metrics such as total rows processed, valid records, invalid records, and error rate.

