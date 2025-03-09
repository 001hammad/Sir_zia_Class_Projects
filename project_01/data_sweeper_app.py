import streamlit as st
import pandas as pd
import os
from io import BytesIO

# App Configuratii
st.set_page_config(page_title="📀 Data Sweeper", layout="wide")

# App Title
st.title("📀 Data Sweeper")
st.write("### Convert, clean, and visualize your CSV & Excel files with ease!")

# File Upload
uploaded_files = st.file_uploader("📂 Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[-1].lower()
        try:
            if file_extension == ".csv":
                df = pd.read_csv(file, header=0)  # Ensure first row is treated as headers
            else:
                df = pd.read_excel(file, header=0)
            
            st.subheader(f"📄 {file.name}")
            st.write(f"**Size:** {file.size / 1024:.2f} KB")
            st.dataframe(df.head())

            # Remove 'Unnamed' columns if they exist
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            # Data Cleaning Options
            with st.expander("🛠️ Data Cleaning Options"):
                if st.button("🧹 Remove Duplicates", key=f"dup_{file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed!")
                if st.button("🛠️ Fill Missing Values", key=f"fill_{file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("✅ Missing Values Filled!")

            # Data Visualization
            numeric_columns = df.select_dtypes(include='number').columns.tolist()
            if numeric_columns:
                st.subheader("📊 Data Visualization")
                selected_columns = st.multiselect("Select columns to visualize:", numeric_columns, default=numeric_columns[:2] if len(numeric_columns) >= 2 else numeric_columns)
                if selected_columns:
                    st.bar_chart(df[selected_columns])
                else:
                    st.warning("⚠️ Please select at least one numeric column for visualization.")
            else:
                st.warning("⚠️ No numeric columns found in the uploaded file. Charts cannot be generated.")

            # File Conversion & Download
            st.subheader("🔄 Convert & Download")
            conversion_type = st.radio("Convert To:", ["CSV", "Excel"], key=file.name)
            if st.button("📥 Convert & Download", key=f"download_{file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_extension, ".csv")
                    mime_type = "text/csv"
                else:
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_extension, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)
                st.download_button("⬇️ Download File", data=buffer, file_name=file_name, mime=mime_type)
        except Exception as e:
            st.error(f"❌ Error processing file {file.name}: {e}")

if uploaded_files:
    st.success("🎉 All files processed successfully!")
