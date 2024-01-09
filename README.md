# Salesforce Import File Prep

Small script that takes all CSVs in a directory, copies files while appending 'staging' to end of filename, then appends "__c' to all column headers. 

Meant to assist with data migraton projects where SF objects are built as staging tables to match a source system but prior to import the source system's CSV export's headers need to be udpated to match SF's api.
