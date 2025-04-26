

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


![Screenshot 2025-04-26 111249](https://github.com/user-attachments/assets/2b2155fc-0651-45b7-8da1-1f2ea3b1ee8e)
![Screenshot 2025-04-26 111443](https://github.com/user-attachments/assets/45ccff26-0c69-457b-9b9c-3f4cb78c8439)
![Screenshot 2025-04-26 111706](https://github.com/user-attachments/assets/f75cc20d-7033-4632-b3c1-3871a46a18f0)
![Screenshot 2025-04-26 111841](https://github.com/user-attachments/assets/f2627f39-0100-47de-8eb5-afb98d40ded1)




