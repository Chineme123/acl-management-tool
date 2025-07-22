# Windows ACL Management CLI Tool

This is a Python-based command-line utility for managing access control permissions on Windows systems.

Built with cybersecurity principles in mind, it enables users to automate the process of granting and revoking access to files and folders via Windows ACLs — all through a simple CLI interface powered by [Typer](https://typer.tiangolo.com/).

---

## 🔐 About

Access control is one of the most critical pillars of cybersecurity. With this project, you can:

- Enforce the principle of least privilege 🔒  
- Log every permission change for traceability 📜  
- Batch update permissions for multiple users 👥  
- Persist access control records in MongoDB 🧩  

Whether you're a security engineer, sysadmin, or Python learner, this tool brings Windows ACL automation into your terminal.

---

## ⚙️ Features

- ✅ Grant or revoke file/folder permissions for users  
- 📁 Batch processing of access control for multiple entries (JSON/CSV)  
- 🧾 Automatic logging of every command and change  
- 🧠 Access control data is stored and updated in a MongoDB database  
- 👁️ View current access control list (ACL) of a resource  
- 🐍 Clean and modern CLI interface using [Typer](https://typer.tiangolo.com/)  
- 🖥️ Fully Windows-compatible (NTFS access control)  
- 🔐 Inspired by cybersecurity best practices  

---

## 📦 Installation

> Requires **Python 3.8+** and **Windows OS**

Clone the repository:

```bash
git clone https://github.com/Chineme123/acl-management-tool.git
cd acl-management-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the tool using:

```bash
python acl_tool.py <command> [arguments]
```

---

## 📌 Available Commands

### `grant`

Grant permission to a user on a file or folder.

```bash
python acl_tool.py grant "<path_to_file_or_folder>" <username> <permission_type>
```

**Example:**

```bash
python acl_tool.py grant "C:\SensitiveData" Alice FullControl
```

---

### `remove`

Revoke permission from a user.

```bash
python acl_tool.py remove "<path_to_file_or_folder>" <username>
```

**Example:**

```bash
python acl_tool.py remove "C:\SensitiveData" Alice
```

---

### `batch`

Batch grant or remove access from multiple users using a `.json` or `.csv` file.

```bash
python acl_tool.py batch grant users.json
python acl_tool.py batch remove users.csv
```

---

### `view`

View the access control list (ACL) for a file or folder.  
If the resource already exists in the MongoDB database, its ACL will be updated; otherwise, a new record will be created.

```bash
python acl_tool.py view "<path_to_file_or_folder>"
```

**Example:**

```bash
python acl_tool.py view "C:\SensitiveData"
```

---

## 📄 Sample JSON File for `batch` Command

Here's an example of how your `users.json` file should look:

```json
[
    {
        "path": "C:\\test_acl\\test1.txt",
        "user": "testuser",
        "perm": "R"
    },
    {
        "path": "C:\\test_acl\\test2.txt",
        "user": "testuser",
        "perm": "W"
    },
    {
        "path": "C:\\test_acl\\test3.txt",
        "user": "testuser",
        "perm": "X"
    }
]
```

Where:
- `"R"` = Read  
- `"W"` = Write  
- `"X"` = Execute  

---

## 📝 Logging

All actions are automatically logged with timestamps and details.

Logs are saved in a dedicated folder:

```bash
C:\Users\<YourUsername>\acl_tool_logs
```

Each session appends to a log file for easy auditing and traceability.

---

## 🧠 Cybersecurity Context

Access control is a foundational cybersecurity practice. By tightly managing file and folder permissions, organizations can:

- Reduce attack surfaces  
- Minimize internal threat vectors  
- Maintain compliance and data integrity  

This project demonstrates how Python can be used for **security automation** and **system hardening** on Windows environments. It also integrates with **MongoDB** for centralized storage of access control metadata.

---

## 🧑‍💻 Author

**Chineme**  
Software Engineer & Cybersecurity Enthusiast  
[GitHub](https://github.com/chineme123)
