from pyngrok import ngrok
import os

# Terminate any existing ngrok tunnels
ngrok.kill()

# Get your ngrok authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
NGROK_AUTH_TOKEN = "32OIzXWdRpHfPhXZWWpP4UPSYBw_7enQUgvMy5xc7o9mUdEYG"  # <--- ⚠️ PASTE YOUR NGROK TOKEN HERE ⚠️
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Run streamlit app in the background
os.system("streamlit run app.py &")

# Open a tunnel to the streamlit port (8501)
public_url = ngrok.connect(8501)
print("Click the URL to access your Streamlit app:")
print(public_url)
