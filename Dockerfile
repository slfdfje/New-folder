# SIMPLIFIED BUILD v3 - NO PYTHON, NO AI - December 17 2025
# Using pure Node.js for maximum stability
FROM node:20-alpine

WORKDIR /app

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

CMD ["node", "server.mjs"]
