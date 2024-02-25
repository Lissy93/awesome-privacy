###############################################################################
# A lightweight, non-root, multi-stage, cross-architecture Dockerfile         #
# That you can use in order to easily deploy Awesome Privacy to any server    #
# For docs visit the GitHub repo: https://github.com/lissy93/awesome-privacy  # 
# Licensed under MIT (C) Alicia Sykes <https://aliciasykes.com> 2024          #
###############################################################################
# Usage:                                                                      #
# Step 1: Build the Docker image                                              #
# docker build -t awesome-privacy .                                           #
#                                                                             #
# Step 2: Run the Docker container                                            #
# docker run -p 8080:80 awesome-privacy                                       #
#                                                                             #
# Step 3: Access the running app                                              #
# Open your browser and navigate to http://127.0.0.1:8080                     #
###############################################################################

# Stage 1: Build the app (Alpine + Node.js)
# Copies manifest and src files from host, installs deps, and builds the app
FROM node:16-alpine as build
WORKDIR /app
COPY package.json yarn.lock .env* ./
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn build

# Stage 2: Serve the app (Alpine + NGINX)
# Copies dist from the previous stage, exposes port 80, and starts web server
FROM nginx:alpine as runtime
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
