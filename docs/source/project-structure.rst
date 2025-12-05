项目结构
========

主要目录和文件：

::

    django-polls/
    ├── manage.py          # Django 管理命令入口
    ├── django-polls/      # 项目主目录
    │   ├── __init__.py
    │   ├── settings.py    # 项目设置
    │   ├── urls.py        # URL 路由
    │   └── wsgi.py
    ├── polls/             # Polls 应用
    │   ├── migrations/    # 数据库迁移文件
    │   ├── __init__.py
    │   ├── admin.py       # 管理后台配置
    │   ├── apps.py        # 应用配置
    │   ├── models.py      # 数据模型
    │   ├── tests.py       # 测试文件
    │   ├── urls.py        # 应用 URL
    │   └── views.py       # 视图函数
    └── docs/              # 本文档目录
        ├── source/        # 文档源文件
        └── build/         # 生成的文档
