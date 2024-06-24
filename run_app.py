# run_app.py

import os
import subprocess
from pyngrok import ngrok

# Menjalankan aplikasi Streamlit
streamlit_command = "streamlit run app.py"
process = subprocess.Popen(streamlit_command.split())

# Menjalankan ngrok untuk membuat URL publik
public_url = ngrok.connect(8501)
print(f"Public URL: {public_url}")

# Menjaga script berjalan untuk menjaga ngrok aktif
try:
    process.wait()
except KeyboardInterrupt:
    print("Terminating Streamlit process...")
    process.terminate()
