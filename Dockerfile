FROM python:3.10-slim

# 环境变量
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    TZ=Asia/Shanghai

# 创建工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

# 复制项目源代码
COPY . .

# 暴露端口
EXPOSE 5002

# 默认启动命令
CMD ["gunicorn", "-b", "0.0.0.0:5002", "run:app"] 