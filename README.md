ECL2 - Windows ACL Management CLI Tool
ECL2 (Enhanced Control List CLI Tool) is a Python-based command-line utility designed to manage access control permissions on Windows systems. Built for cybersecurity enthusiasts and professionals, ECL2 helps automate the process of granting or revoking file and folder access rights using Windows ACLs.

🔐 About
Access control is a cornerstone of cybersecurity. ECL2 provides a lightweight and powerful way to enforce file-level security by controlling user and group access on Windows NTFS systems.

Whether you're a system administrator, cybersecurity student, or Python developer exploring OS-level automation, ECL2 gives you a hands-on tool to manage permissions directly from your terminal.

⚙️ Features
✅ Grant or revoke access to specific users or groups

📁 Batch permission management for multiple targets

🧾 Auto-generated log files for every command run

🖥️ Pure Windows-compatible — built using native Windows ACL support

🐍 Lightweight CLI built with Python

🛡️ Designed with cybersecurity automation in mind

🛠️ Installation
Make sure you have Python 3.8+ installed on your Windows machine.

bash
Copy
Edit
git clone https://github.com/yourusername/ecl2.git
cd ecl2
(Replace yourusername with your actual GitHub handle.)

🚀 Usage
The CLI tool is run using the following pattern:

bash
Copy
Edit
python ecl2.py <command> [options]
📌 Commands
grant
Grants access permissions to a user or group.

bash
Copy
Edit
python ecl2.py grant <path_to_file_or_folder> <username> <permission_type>
Example:

bash
Copy
Edit
python ecl2.py grant "C:\SensitiveData" Alice FullControl
remove
Removes access permissions from a user or group.

bash
Copy
Edit
python ecl2.py remove <path_to_file_or_folder> <username>
Example:

bash
Copy
Edit
python ecl2.py remove "C:\SensitiveData" Alice
batch
Batch grants or revokes access from multiple users.

bash
Copy
Edit
python ecl2.py batch grant <path> users.txt
python ecl2.py batch remove <path> users.txt
Where users.txt is a file with usernames listed line by line.

📝 Logging
Every command execution is automatically logged.

Logs are stored in a dedicated folder in the current user’s directory:

makefile
Copy
Edit
C:\Users\<YourUsername>\ECL2Logs
Each log file contains timestamps, commands run, and the result of the operation.

This ensures auditability and helps track changes made to system permissions — a critical part of access control in cybersecurity environments.

🧠 Why This Matters (Cybersecurity Context)
Access control is one of the core principles of cybersecurity. Unauthorized access to sensitive files is one of the most common vectors for data breaches and internal threats.

ECL2 helps enforce the principle of least privilege by making it easy to control who can access what. This tool is also a great example of how Python — a go-to language in cybersecurity — can be used to build security automation tools that integrate with operating systems.

Whether used to automate administrative tasks or to support red/blue team activities, ECL2 is a practical application of Python for system hardening and security policy enforcement.

📚 Prerequisites
Python 3.8 or later

Windows OS (with NTFS file system)

Administrator privileges (for certain access changes)

👩‍💻 Author
Chineme
Cybersecurity & Python enthusiast
GitHub Profile


