# 1. Install Ollama
!curl -fsSL https://ollama.com/install.sh | sh

# 2. Run Ollama server in the background using nohup
# 'nohup' ensures the process keeps running, and '&' puts it in the background.
print("Starting Ollama server in the background...")
!nohup ollama serve &

# 3. Give the server a moment to start up.
# This is crucial to ensure the server is ready before we send commands to it.
!sleep 5

# 4. Pull the required models
print("\nPulling 'nomic-embed-text' for embeddings...")
!ollama pull nomic-embed-text

print("\nPulling 'deepseek-r1:1.5b' for chat...")
!ollama pull deepseek-r1:1.5b

# 5. Verify that the models are running by listing them
print("\nVerifying installed models...")
!ollama list

print("\n✅ Ollama setup complete.")
