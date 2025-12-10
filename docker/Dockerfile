FROM python:3.13

WORKDIR /project
COPY backend/requirements.txt /tmp/req.txt
RUN pip install --no-cache-dir -r /tmp/req.txt \
  && rm -rf \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/* \
    /var/lib/apt/lists/* \
    /var/tmp/*
ENV TZ=Asia/Shanghai PYTHONUNBUFFERED=x
CMD ["python", "-m http.server"]
