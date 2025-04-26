import streamlit as st
import pandas as pd
import io

# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------
def assign_week(date):
  
    day = date.day
    if 1 <= day <= 7:
        return "01 Feb - 07 Feb"
    elif 8 <= day <= 14:
        return "08 Feb - 14 Feb"
    elif 15 <= day <= 21:
        return "15 Feb - 21 Feb"
    elif 22 <= day <= 28:
        return "22 Feb - 28 Feb"
    else:
        return "29 Feb - ..."  # Adjust if needed

def compute_weekly_chat_metrics(df):
   
    # Overall metrics
    overall_incoming = df['RoomCode'].count()
    overall_unique = df['UserId'].nunique()
    overall_closed_bot = df[df['ClosedBy'] == 'System'].shape[0]
    overall_deflection = round((overall_closed_bot / overall_incoming * 100), 2) if overall_incoming > 0 else 0
    overall_closed_agent = df[df['ClosedBy'] != 'System'].shape[0]

    overall_row = {
        "Week": "Overall",
        "Incoming Chats": overall_incoming,
        "Unique Users": overall_unique,
        "Closed By Bot": overall_closed_bot,
        "Bot Deflection %": overall_deflection,
        "Closed By Agents": overall_closed_agent
    }
    
    # Assign week labels based on ChatStartTime column.
    df['Week'] = df['ChatStartTime'].apply(assign_week)
    
    # Group by week and compute metrics.
    weekly_rows = []
    for week, group in df.groupby("Week"):
        incoming = group['RoomCode'].count()
        unique = group['UserId'].nunique()
        closed_bot = group[group['ClosedBy'] == 'System'].shape[0]
        deflection = round((closed_bot / incoming * 100), 2) if incoming > 0 else 0
        closed_agent = group[group['ClosedBy'] != 'System'].shape[0]
        weekly_rows.append({
            "Week": week,
            "Incoming Chats": incoming,
            "Unique Users": unique,
            "Closed By Bot": closed_bot,
            "Bot Deflection %": deflection,
            "Closed By Agents": closed_agent
        })
    weekly_df = pd.DataFrame(weekly_rows)
    
    # Sort weekly data in desired order.
    desired_order = ["01 Feb - 07 Feb", "08 Feb - 14 Feb", "15 Feb - 21 Feb", "22 Feb - 28 Feb"]
    weekly_df['Week'] = pd.Categorical(weekly_df['Week'], categories=desired_order, ordered=True)
    weekly_df = weekly_df.sort_values("Week")
    
    # Combine overall metrics with weekly metrics.
    overall_df = pd.DataFrame([overall_row])
    final_df = pd.concat([overall_df, weekly_df], ignore_index=True)
    return final_df

def generate_excel_report(df):
    """
    Write the DataFrame to an Excel file in-memory and return the file bytes.
    """
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name="Chat Metrics", index=False)
    output.seek(0)
    return output.read()

# ---------------------------------------------------------------------------
# Streamlit Web App
# ---------------------------------------------------------------------------
st.title("Weekly Chat Metrics Report Generator")

st.markdown("""
Upload your Data Dump file (CSV or Excel). The file must include these columns:
- **RoomCode**
- **UserId**
- **ClosedBy**
- **ChatStartTime** (in "DD-MM-YYYY HH:MM:SS" format)
- **ChatEndTime** (in "DD-MM-YYYY HH:MM:SS" format)

An overall summary and a weekly breakdown (for February) will be computed.
""")

# File uploader widget
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("File loaded successfully!")
    except Exception as e:
        st.error(f"Error reading file: {e}")

    # Convert date columns (using dayfirst=True to match DD-MM-YYYY format)
    try:
        df["ChatStartTime"] = pd.to_datetime(df["ChatStartTime"], dayfirst=True)
        df["ChatEndTime"] = pd.to_datetime(df["ChatEndTime"], dayfirst=True)
    except Exception as e:
        st.error(f"Error converting date columns: {e}")
    
    # Optional: Convert AgentFirstResponseTime if it exists.
    if "AgentFirstResponseTime" in df.columns:
        df["AgentFirstResponseTime"] = pd.to_timedelta(df["AgentFirstResponseTime"], errors='coerce')
    
    # Compute metrics and display the report.
    metrics_df = compute_weekly_chat_metrics(df)
    st.write("### Chat Metrics Report")
    st.dataframe(metrics_df, height=300)
    
    # Generate Excel file in memory.
    excel_file = generate_excel_report(metrics_df)
    
    # Download button for Excel report.
    st.download_button(
        label="Download Excel Report",
        data=excel_file,
        file_name="weekly_chat_metrics.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
