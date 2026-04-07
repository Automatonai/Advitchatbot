# Use a lightweight Python base image
FROM python:3.10.6

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose Streamlit port
EXPOSE 8501

CMD ["streamlit", "run", "ui.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.headless=True", \
     "--server.enableCORS=False"]