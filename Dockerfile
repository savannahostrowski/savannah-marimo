FROM nginx:alpine
COPY output_dir/ /usr/share/nginx/html
EXPOSE 80