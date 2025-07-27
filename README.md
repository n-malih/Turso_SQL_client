# Turso SQL Client

A simple Python command-line tool for querying [Turso](https://turso.tech/) SQLite databases over HTTP using the pipeline API.

## 🔧 Features

- Send raw SQL queries to your Turso database directly from the terminal
- Works with Turso's HTTP API
- Lightweight and easy to configure

---

## 📦 Requirements

- Python 3.7+
- `requests`

---

Replace TOKEN and URL values with yours:
```python
TOKEN = 'your_turso_auth_token_here'
URL = 'https://your-database-name.turso.io/v2/pipeline'
```
Replace **'your_turso_auth_token_here'** with your actual Turso API token.

Replace **'https://your-database-name.turso.io/v2/pipeline'** with your database URL.

If your Turso URL starts with **libsql://**, you must replace **libsql://** with **https://**

Append **/v2/pipeline** to the end

Example:
**libsql://my-db-name.turso.io**  -> becomes: **https://my-db-name.turso.io/v2/pipeline**

Refer to [Turso HTTP SDK Quickstart](https://docs.turso.tech/sdk/http/quickstart) for more details.

---

## Run the tool

```bash
python turso_sql_client.py
```
You'll see a prompt like this:
```bash
sql: >
```
Enter your SQL queries interactively.

🔎 Example Query
```bash
SELECT * FROM users;
```
