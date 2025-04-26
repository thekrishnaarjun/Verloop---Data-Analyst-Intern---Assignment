![Screenshot 2025-04-26 111443](https://github.com/user-attachments/assets/2bef05db-c1eb-4282-bc20-832e2918a6ad)# Chat Metrics Report Generator

This project is a Streamlit-based web application that allows users to upload a Data Dump file (in CSV or Excel format) and automatically generates an Excel report containing chat metrics. The metrics are grouped into an Overall summary and a weekly breakdown (for February in this example).


## Overview

The Chat Metrics Report Generator processes a Data Dump file that includes columns such as `RoomCode`, `UserId`, `ClosedBy`, `ChatStartTime`, and `ChatEndTime`. The application computes the following metrics:
- **Incoming Chats:** Total number of chats.
- **Unique Users:** Number of distinct users.
- **Closed By Bot:** Count of chats closed by the system (where `ClosedBy` equals `'System'`).
- **Bot Deflection %:** Percentage of chats closed by the system relative to total chats.
- **Closed By Agents:** Count of chats closed by agents (excluding system/bot).

Results are grouped overall and by weekly intervals (e.g., "01 Feb - 07 Feb", "08 Feb - 14 Feb", etc.) and are exported in an Excel file using the `xlsxwriter` engine.

## Features

- **File Upload:**  
  Users can upload either CSV or Excel files containing chat data.

- **Automated Processing:**  
  The web app processes the uploaded file to compute overall and weekly chat metrics.

- **Excel Report Generation:**  
  An Excel report is generated with the following columns:
  - Week
  - Incoming Chats
  - Unique Users
  - Closed By Bot
  - Bot Deflection %
  - Closed By Agents

- **Web App Interface:**  
  Built with Streamlit, the app displays the computed metrics and allows users to download the report.


![Screenshot 2025-04-26 111841](https://github.com/user-attachments/assets/94044f20-7f79-4d12-b033-90ecc3c5e29b)
![Screenshot 2025-04-26 111706](https://github.com/user-attachments/assets/eab2d680-0702-427c-8e6b-49e0a8a5ee06)
![Screenshot 2025-04-26 111443](https://github.com/user-attachments/assets/b9bcf826-fddf-4566-ae62-b67e9985e540)
![Screenshot 2025-04-26 111249](https://github.com/user-attachments/assets/e42df399-712d-44cf-b864-83a0b6b3ee2b)



