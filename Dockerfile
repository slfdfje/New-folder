FROM python:3.11-slim

# Install Node.js
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install ONLY basic Python dependencies (NO transformers/torch - causes corruption)
RUN pip install --no-cache-dir pillow boto3

# Copy and install Node dependencies
COPY backend/package.json backend/package-lock.json ./
RUN npm install

# Copy backend code
COPY backend/ ./

# Create directories
RUN mkdir -p uploads reference_images

EXPOSE 5000

ENV PORT=5000
ENV NODE_ENV=production
ENV PYTHONUNBUFFERED=1

CMD ["node", "server.mjs"]
