================
部署指南
================

本文档介绍如何将 Django Polls 投票系统部署到生产环境。

📋 部署前准备
---------------

### 1. 服务器要求
- 操作系统：Ubuntu 20.04+ / CentOS 7+
- Python 3.8+
- 数据库：SQLite（小型项目）或 PostgreSQL（推荐）

### 2. 域名准备
- 已备案的域名（国内服务器需要）
- SSL证书（推荐使用 Let's Encrypt 免费证书）

🚀 快速部署步骤
----------------

### 步骤1：服务器初始化
```bash
# 更新系统
sudo apt update
sudo apt upgrade -y

# 安装基础软件
sudo apt install python3-pip python3-venv nginx git -y
```

步骤2：获取项目代码

```bash
# 克隆项目
cd /var/www
sudo git clone https://github.com/meilaesop/django-polls.git
sudo chown -R $USER:$USER django-polls
cd django-polls
```

步骤3：设置虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

步骤4：配置环境变量

```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑环境变量
nano .env
```

在 .env 文件中设置：

```ini
DEBUG=False
SECRET_KEY=你的安全密钥
ALLOWED_HOSTS=你的域名,localhost,127.0.0.1
```

步骤5：数据库设置

```bash
# 运行数据库迁移
python manage.py migrate

# 收集静态文件
python manage.py collectstatic --noinput

# 创建超级用户
python manage.py createsuperuser
```

步骤6：使用 Gunicorn

```bash
# 安装 Gunicorn
pip install gunicorn

# 测试运行
gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application
```

步骤7：配置 Systemd 服务

```bash
# 创建服务文件
sudo nano /etc/systemd/system/django-polls.service
```

服务文件内容：

```ini
[Unit]
Description=Django Polls Gunicorn Service
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/django-polls
Environment="PATH=/var/www/django-polls/venv/bin"
ExecStart=/var/www/django-polls/venv/bin/gunicorn \
    --workers 3 \
    --bind 127.0.0.1:8000 \
    mysite.wsgi:application

[Install]
WantedBy=multi-user.target
```

启动服务：

```bash
sudo systemctl start django-polls
sudo systemctl enable django-polls
sudo systemctl status django-polls
```

步骤8：配置 Nginx

```bash
# 创建 Nginx 配置
sudo nano /etc/nginx/sites-available/django-polls
```

Nginx 配置：

```nginx
server {
    listen 80;
    server_name 你的域名 www.你的域名;
    
    location /static/ {
        alias /var/www/django-polls/staticfiles/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

启用配置：

```bash
sudo ln -s /etc/nginx/sites-available/django-polls /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

步骤9：配置 SSL（可选但推荐）

```bash
# 安装 Certbot
sudo apt install certbot python3-certbot-nginx -y

# 获取证书
sudo certbot --nginx -d 你的域名 -d www.你的域名

# 自动续期测试
sudo certbot renew --dry-run
```

🔧 简单部署方式（适合初学者）

---

使用 PythonAnywhere（免费）

1. 注册 PythonAnywhere 账号
2. 创建新的 Web App
3. 上传项目代码
4. 配置虚拟环境和依赖
5. 运行数据库迁移
6. 部署完成

使用 Railway（有免费额度）

1. 注册 Railway 账号
2. 连接 GitHub 仓库
3. 自动部署
4. 配置环境变量
5. 访问生成的域名

⚡ 一键部署脚本

---

```bash
#!/bin/bash
# deploy.sh

echo "开始部署 Django Polls..."

# 1. 更新系统
sudo apt update && sudo apt upgrade -y

# 2. 安装依赖
sudo apt install python3-pip python3-venv nginx git -y

# 3. 获取代码
cd /var/www
sudo git clone https://github.com/meilaesop/django-polls.git
sudo chown -R $USER:$USER django-polls
cd django-polls

# 4. 设置虚拟环境
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. 基础配置
cp .env.example .env
# 请手动编辑 .env 文件

echo "请编辑 .env 文件，然后运行以下命令："
echo "1. python manage.py migrate"
echo "2. python manage.py collectstatic --noinput"
echo "3. python manage.py createsuperuser"
echo "4. 参考上面的步骤配置 Gunicorn 和 Nginx"
```

🐳 Docker 部署

---

```bash
# 使用 Docker Compose
docker-compose up -d

# 或直接使用 Docker
docker build -t django-polls .
docker run -p 8000:8000 django-polls
```

🚨 常见问题

---

1. 502 Bad Gateway

```bash
# 检查 Gunicorn 服务
sudo systemctl status django-polls
sudo journalctl -u django-polls -f
```

2. 静态文件 404

```bash
# 重新收集静态文件
python manage.py collectstatic --noinput

# 检查权限
sudo chown -R www-data:www-data /var/www/django-polls/staticfiles
```

3. 数据库连接问题

```bash
# 检查数据库服务
sudo systemctl status postgresql  # 如果是 PostgreSQL

# 检查迁移
python manage.py migrate
```

4. 域名无法访问

```bash
# 检查防火墙
sudo ufw status
sudo ufw allow 80
sudo ufw allow 443
```

📈 维护和监控

---

查看日志

```bash
# 应用日志
sudo journalctl -u django-polls -f

# Nginx 日志
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

备份数据

```bash
# 备份数据库（如果是 SQLite）
cp db.sqlite3 db.sqlite3.backup

# 或使用 cron 定时备份
0 2 * * * cp /var/www/django-polls/db.sqlite3 /backup/db.sqlite3.$(date +\%Y\%m\%d)
```

更新代码

```bash
cd /var/www/django-polls
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart django-polls
```

💡 最佳实践

---

1. 使用 PostgreSQL 替代 SQLite（生产环境）
2. 启用 HTTPS 保护用户数据
3. 定期备份 数据库
4. 监控日志 及时发现问题
5. 保持更新 安全补丁和功能更新

📞 获取帮助

---

遇到部署问题：

1. 查看本文档
2. 检查日志文件
3. 搜索 GitHub Issues
4. 创建新的 Issue

---

最后更新: 2025-12-20
