Data collection is a crucial step in the data science process. Here are some techniques and tools commonly used for data collection:

1. **Web Scraping:**
- **Beautiful Soup:** A Python library for parsing HTML and XML documents, commonly used for web scraping.
- **Scrapy:** An open-source web crawling framework for Python.
- **Selenium:** A tool for automating web browser interactions, often used for scraping websites with dynamic content.

2. **APIs (Application Programming Interfaces):**
- Many websites and online services offer APIs that allow you to access and retrieve data programmatically. Common tools for working with APIs include `requests` (Python library) and Postman (API testing tool).
  
  - RESTful APIs: Many web services provide APIs that allow you to programmatically retrieve data. You can use tools like Python's requests library to interact with RESTful APIs.
  
  - GraphQL: If available, GraphQL APIs offer more flexible querying of data compared to REST APIs.

3. **Surveys and Questionnaires:**
- Tools like Typeform, Google Forms, SurveyMonkey, and Qualtrics can be used to create and distribute surveys for collecting structured data.

4. Data Collection Tools:
   - Import.io: A tool for extracting data from websites and turning it into structured data.
   - Octoparse: A visual web scraping tool for extracting data from websites without coding.
   - ParseHub: A web scraping tool that allows you to turn websites into structured data.

5. **IoT Devices:**
- Sensors and IoT devices can collect data on various physical parameters, such as temperature, humidity, and motion. Platforms like Raspberry Pi and Arduino are commonly used for IoT projects.

6. **Logs and Server Data:**
- Server logs, application logs, and event logs can provide valuable data for system monitoring and analysis. Tools like Logstash, Elasticsearch, and Kibana (ELK Stack) are often used for log analysis.

7. **Database Queries:**
- SQL and NoSQL databases are common sources of structured data.    
    - SQL Databases: Tools like MySQL, PostgreSQL, and Microsoft SQL Server are used to collect and store structured data.
    
    - NoSQL Databases: Such as MongoDB, Cassandra, and Redis, are used for collecting unstructured or semi-structured data.

8. **File Formats:**
- Data can be collected from various file formats, such as CSV, Excel, JSON, XML, and more. Libraries like Pandas (Python) and Excel can help with data extraction and manipulation.

9. **Data Lakes and Data Warehouses:**
- Platforms like Amazon S3, Google Cloud Storage, and Azure Data Lake Storage are used to store and manage large volumes of data for later analysis.

10. **Data Streaming and Real-time Data Collection:**

- Apache Kafka: A distributed streaming platform for collecting and processing real-time data streams.

- Flume: A distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data.

When collecting data, it's essential to consider ethical and legal considerations, including data privacy and consent, and to document the data collection process thoroughly to ensure data quality and reproducibility.