# SIMPLIFIED - No AI/CLIP - v3
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install Node dependencies only
RUN npm install --omit=dev

# Copy backend files
COPY . .

# Create directories
RUN mkdir -p uploads reference_images

ENV NODE_ENV=production
ENV PORT=8080

EXPOSE 8080

# Start server directly
CMD ["node", "server.mjs"]
