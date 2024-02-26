Section A: Definitions

1.    
Define the following key terms related to databases:

1.1.1.     Database

A database is an organized collection of structured information, or data, typically stored electronically in a computer system.
1.1.2.     Table

Tables are database objects that contain all the data in a database. 
1.1.3.     Record

A record is simply a set of data stored in a table
1.1.4.     Field

field refers to a set of values arranged in a table and has the same data type
1.1.5.     Primary Key

A primary key is the column or columns that contain values that uniquely identify each row in a table.
1.1.6.     SQL

programming language for storing and processing information in a relational database.
1.1.7.     Query

 a request for data.
1.1.8.     Index

 an index is a pointer to data in a table.
1.1.9.     Normalization

Normalization is the process of organizing data in a database.
1.1.10.  Database Management System (DBMS)
 software tool that enables users to manage a database easily. 
2.  Section B: Discussions
1.1.1.     Describe the purpose of a primary key in a database table and provide an example.

In a database table, a primary key serves as a unique identifier for each row or record. Its main purpose is to ensure data integrity by uniquely identifying each record in the table. Here's a breakdown of its purpose and significance:

Uniqueness: A primary key must be unique within the table. This means that no two rows can have the same value for the primary key column. This uniqueness ensures that each record is uniquely identifiable.

Identification: The primary key uniquely identifies each row in the table. It provides a reliable and efficient way to access, update, and delete specific records within the table.

Data Integrity: By enforcing uniqueness, the primary key helps maintain data integrity within the database. It prevents duplicate records and ensures that each record can be uniquely identified, avoiding inconsistencies and data redundancy.

Relationships: Primary keys are often used to establish relationships between tables in a relational database. For example, in a one-to-many relationship, the primary key of one table may serve as a foreign key in another table, linking the two tables together.

Indexing: Primary keys are usually indexed by the database management system for faster retrieval of data. This indexing improves the performance of queries that involve searching, sorting, or joining tables based on the primary key.

Example:
Consider a table named "Employees" in a human resources database. Each row in this table represents an employee, and we want to ensure that each employee can be uniquely identified. We can use the "EmployeeID" column as the primary key for this table
1.1.2.     Explain the difference between a database management system (DBMS) and a database.

The terms "Database Management System (DBMS)" and "database" are related but refer to different components in the context of managing and storing data. Here's an explanation of the difference between the two:

Database:

A database refers to an organized collection of structured data or information.
It typically consists of one or more tables, each containing rows and columns that represent entities and their attributes.
Databases can store various types of data, such as text, numbers, dates, and multimedia files.
Examples of databases include MySQL, PostgreSQL, Oracle Database, MongoDB, etc.
Database Management System (DBMS):

A Database Management System (DBMS) is software designed to manage, manipulate, and interact with databases.
It provides an interface for users and applications to access and manage the data stored in the database.
DBMS handles tasks such as data storage, retrieval, querying, updating, and security.
It offers functionalities like creating, modifying, and deleting databases, tables, and indexes, as well as defining data structures, enforcing constraints, and managing transactions.
DBMS acts as an intermediary between the users/applications and the database, handling tasks related to data storage and retrieval efficiently.
Examples of DBMS include MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server, SQLite, etc.
In summary, a database is the structured collection of data, while a Database Management System (DBMS) is the software used to manage and interact with that data. The DBMS provides tools and functionalities to create, access, manipulate, and maintain databases, ensuring efficient data management and retrieval.
1.1.3.     Discuss in short, the importance of normalization in database design and provide an example of how it can improve data integrity.

Normalization is a crucial concept in database design aimed at organizing data efficiently and minimizing redundancy while maintaining data integrity. Here's a brief explanation of the importance of normalization and an example of how it can improve data integrity:

Importance of Normalization:

Reduction of Redundancy: Normalization helps reduce data redundancy by breaking down large tables into smaller, more manageable ones. This minimizes the storage space required and avoids inconsistencies that may arise from duplicate data.

Data Integrity: By reducing redundancy, normalization helps improve data integrity. It ensures that each piece of information is stored in only one place, reducing the risk of inconsistencies or anomalies such as update anomalies, insertion anomalies, and deletion anomalies.

Efficient Updates and Modifications: Normalization simplifies the process of updating and modifying data. Since data is stored in a more structured and normalized manner, changes can be made in one place without affecting multiple records, leading to fewer errors and smoother operations.

Improved Query Performance: Normalized databases often result in better query performance. With smaller, more focused tables, queries can be executed more efficiently, leading to faster retrieval of data.

Example of Improving Data Integrity through Normalization:

Consider a database for a university with a table named "Students" containing student information such as student ID, name, age, and course. 
