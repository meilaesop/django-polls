========
安装指南
========

本文档介绍如何安装和配置 Django Polls 投票系统。

📋 系统要求
------------

### 基本要求
- Python 3.8 或更高版本
- Django 3.2 或更高版本

### 推荐配置
- Python 3.10+
- Django 4.2+
- 1GB 以上内存

🚀 快速安装
------------

### 方法一：使用 pip 安装
```bash
# 安装最新版本
pip install meilaesop-django-polls
```

方法二：从源码安装

```bash
# 克隆仓库
git clone https://github.com/meilaesop/django-polls.git
cd django-polls

# 安装依赖
pip install -e .
```

🛠️ 项目配置

---

1. 添加到 Django 项目

在你的 Django 项目的 settings.py 文件中：

```python
INSTALLED_APPS = [
    # ... 其他应用
    'django_polls',  # 添加这一行
]
```

2. 配置 URL

在你的项目 urls.py 文件中：

```python
from django.urls import path, include

urlpatterns = [
    # ... 其他URL
    path('polls/', include('django_polls.urls')),
]
```

3. 数据库迁移

```bash
python manage.py migrate
```

4. 创建超级用户

```bash
python manage.py createsuperuser
```

5. 运行开发服务器

```bash
python manage.py runserver
```

现在可以访问：

· 网站：http://127.0.0.1:8000/polls/
· 管理后台：http://127.0.0.1:8000/admin/

🏗️ 开发环境设置

---

1. 克隆项目

```bash
git clone https://github.com/meilaesop/django-polls.git
cd django-polls
```

2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

3. 安装依赖

```bash
pip install -r requirements.txt
```

4. 运行测试

```bash
python manage.py test django_polls
```

⚙️ 配置选项

---

基本配置

```python
# 在 settings.py 中可以配置
# 静态文件配置
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
    }
]
```

🚨 故障排除

---

常见问题

1. 安装失败

```bash
# 升级 pip
pip install --upgrade pip
```

2. 数据库迁移失败

```bash
# 重新迁移
python manage.py migrate
```

3. 运行测试失败

```bash
# 详细输出测试信息
python manage.py test django_polls -v 2
```

📞 支持与反馈

---

技术支持

· 文档：https://github.com/meilaesop/django-polls/tree/main/docs
· Issues：https://github.com/meilaesop/django-polls/issues

---

最后更新: 2025-12-20
