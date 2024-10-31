
# MySQL-Flask API Project

This project is a Flask-based API that connects to a MySQL database. It includes basic functions such as creating a database, creating a table, inserting data, and fetching data from the database via a POST API endpoint.

---

## Features

- Connect to MySQL database and manage tables.
- Create a new database and table.
- Insert data into the table.
- Fetch data using a POST request.

---

## Technologies Used

- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)  
  **Flask** - A Python-based micro web framework used for building APIs.

- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)  
  **MySQL** - A relational database management system for data storage.

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
  **Python** - The programming language used for backend logic.

---

## Prerequisites

Before running this application, ensure you have the following installed:
- [Python 3](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/) (`pip install flask`)
- MySQL Connector (`pip install mysql-connector-python`)

---

## Project Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies:**
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
   > **Note**: If `requirements.txt` does not exist, install manually:
   ```bash
   pip install flask mysql-connector-python
   ```

3. **Database Configuration:**
   Ensure that MySQL is running on your local system and update the connection details in the code if necessary (default settings assume `user='root'` and `passwd='password'`).

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

---

## Endpoints and Functionality

1. **Database Functions**

   - `show_database()`: Lists all available databases.
   - `createdb()`: Creates a new database named `db1`.
   - `create_table()`: Creates a table named `dbai` in `db1` with columns `studentid`, `fname`, `lname`, `regid`, and `classname`.
   - `insert_data()`: Inserts sample data into the `dbai` table.
   - `show_tables()`: Lists all tables within the `db1` database.

2. **API Endpoints**

   - **POST /fetch**: Fetches all records from the specified table.

     **Request**:  
     ```json
     {
       "name": "dbai"
     }
     ```

     **Response**:
     ```json
     [
       [333654, "Deepak", "Mohanty", 245546652, "Full Stack Data Science"],
       [656654, "Chandrakanta", "Satapathy", 245546543, "Full Stack Web Dev"]
     ]
     ```

---

## Usage

1. **Creating a Database and Table**  
   Use the `createdb()` function to create a database named `db1`, and then use `create_table()` to create a table in that database.

2. **Inserting Data**  
   Call `insert_data()` to insert sample records into the `dbai` table in `db1`.

3. **Fetching Data**  
   Send a POST request to `localhost:5000/fetch` with JSON data specifying the table name:
   ```json
   {
     "name": "dbai"
   }
   ```

---

## Screenshots

1. **Database and Table Creation**
   ![Database and Table Creation](path/to/your/database-creation-image.png)

1. **App Running**
   ![Data Insertion](https://github.com/Deepak8260/fetch-data-from-sql-using-api/blob/main/images/app%20running.png)

2. **Fetch Endpoint Response**
   ![Fetch Response](https://github.com/Deepak8260/fetch-data-from-sql-using-api/blob/main/images/fetching.png)

> Replace `path/to/your/image.png` with actual paths to your screenshots.

---

## Error Handling

Ensure that:
- MySQL is running locally and accessible.
- The `name` field in the POST request matches an existing table name in `db1`.

---

## License

This project is open source and available under the [MIT License](LICENSE).
