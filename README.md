Sales Dashboard with SQL Integration
This project focuses on analyzing sales performance of active sellers using Python and MySQL. It is based on a dataset containing merchant-level information such as units sold, product pricing, ratings, and urgency metrics.

What the Project Includes
A Python dashboard (sales_dashboard.py) that reads a CSV file and creates visual charts using Seaborn and Matplotlib.
A MySQL connection script (sql_connect.py) that uploads the data into a MySQL database using SQLAlchemy and pymysql.
A SQL query file (sql_queries.sql) with some useful queries for extracting insights.
Visualizations Created
Listed products per seller (bar chart)
Rating distribution (histogram)
Distribution of product prices
Urgency text rate vs urgency count (scatter plot)
Tools & Libraries Used
Python (pandas, matplotlib, seaborn)
MySQL database
SQLAlchemy & pymysql for database connection
VS Code for development
How to Use
Clone the repository.
Make sure Python and MySQL are installed.
Run sql_connect.py to upload the CSV data into MySQL.
Run sales_dashboard.py to generate visualizations.
About the Dataset
The data includes:

merchantid
totalunitssold
meanproductprices
rating
urgencytextrate
and more columns useful for sales performance analysis.
