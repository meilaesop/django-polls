==========================
meilaesop-django-polls 投票系统
==========================

一个可重用的Django应用，用于创建基于Web的投票系统。包含完整的用户认证功能。

.. image:: https://img.shields.io/pypi/v/meilaesop-django-polls.svg
    :target: https://pypi.org/project/meilaesop-django-polls/
    :alt: PyPI 版本

.. image:: https://img.shields.io/pypi/pyversions/meilaesop-django-polls.svg
    :target: https://pypi.org/project/meilaesop-django-polls/
    :alt: Python 版本支持

.. image:: https://img.shields.io/pypi/djversions/meilaesop-django-polls.svg
    :target: https://pypi.org/project/meilaesop-django-polls/
    :alt: Django 版本支持

.. image:: https://github.com/meilaesop/django-polls/actions/workflows/test.yml/badge.svg
    :target: https://github.com/meilaesop/django-polls/actions
    :alt: 测试状态

安装
----

从PyPI安装：

.. code-block:: bash

    pip install meilaesop-django-polls

或安装开发版本：

.. code-block:: bash

    pip install git+https://github.com/meilaesop/django-polls.git

快速开始
--------

1. 将 ``django_polls`` 添加到 ``INSTALLED_APPS``：

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'django_polls',
    ]

2. 在项目的 ``urls.py`` 中包含投票URL配置：

.. code-block:: python

    from django.urls import include, path

    urlpatterns = [
        # ...
        path('polls/', include('django_polls.urls')),
        # ...
    ]

3. 运行数据库迁移：

.. code-block:: bash

    python manage.py migrate

4. 启动开发服务器并访问管理后台创建投票。

5. 访问 ``/polls/`` 参与投票。

功能特性
--------

用户认证功能
~~~~~~~~~~~~
- ✅ 用户注册（含邮箱验证）
- ✅ 登录/注销功能
- ✅ 用户个人资料管理
- ✅ 认证用户创建投票
- ✅ 投票历史记录

投票功能
~~~~~~~~
- ✅ 创建和管理投票
- ✅ 参与投票
- ✅ 实时结果显示
- ✅ 投票结果图表
- ✅ 响应式设计（Bootstrap 5）

管理功能
~~~~~~~~
- ✅ Django管理后台集成
- ✅ 投票数据管理
- ✅ 用户管理
- ✅ 数据导出

开发功能
~~~~~~~~
- ✅ RESTful API 接口
- ✅ 完整的测试覆盖
- ✅ 生产环境配置
- ✅ 可定制的模板

系统要求
--------

- Django >= 3.2, < 5.0
- Python >= 3.8

文档
----

详细文档位于 "docs" 目录。

开发环境设置
------------

1. 克隆仓库：

.. code-block:: bash

    git clone https://github.com/meilaesop/django-polls.git
    cd django-polls

2. 创建虚拟环境：

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # venv\Scripts\activate   # Windows

3. 安装开发依赖：

.. code-block:: bash

    pip install -e .[dev]

4. 运行数据库迁移：

.. code-block:: bash

    python manage.py migrate

5. 创建超级用户：

.. code-block:: bash

    python manage.py createsuperuser

6. 启动开发服务器：

.. code-block:: bash

    python manage.py runserver

运行测试
--------

.. code-block:: bash

    pip install pytest pytest-django
    pytest django_polls/

API 使用示例
-----------

获取所有投票：

.. code-block:: bash

    GET /api/polls/

创建新投票：

.. code-block:: bash

    POST /api/polls/
    {
        "question_text": "你最喜欢的编程语言是什么？",
        "choices": ["Python", "JavaScript", "Java", "Go"]
    }

参与投票：

.. code-block:: bash

    POST /api/polls/1/vote/
    {
        "choice_id": 2
    }

部署指南
--------

生产环境部署建议：

1. 使用PostgreSQL数据库
2. 配置环境变量
3. 使用Gunicorn或uWSGI
4. 配置Nginx反向代理
5. 启用HTTPS

详细部署说明请查看 ``docs/deployment.rst``。

常见问题
--------

Q: 如何自定义模板？
A: 在项目的templates目录中创建同名模板文件即可覆盖。

Q: 如何限制投票次数？
A: 默认每个用户只能投票一次，可在设置中配置。

Q: 支持多语言吗？
A: 支持Django的国际化和本地化功能。

贡献指南
--------

欢迎贡献代码！请阅读 ``CONTRIBUTING.rst`` 了解贡献流程和代码规范。

问题反馈
--------

遇到问题时，请：

1. 查看文档
2. 搜索已有的问题
3. 提交新问题并提供详细信息

更新日志
--------

查看 ``CHANGELOG.rst`` 了解版本更新历史。

版本 0.1.0
~~~~~~~~~~

**发布日期**: 2025-12-20

新增功能：
- 完整的用户认证系统
- 投票创建和管理
- REST API接口
- 响应式设计模板
- 完整的测试覆盖

许可证
-------

BSD 3-Clause License

相关链接
--------

- GitHub: https://github.com/meilaesop/django-polls
- PyPI: https://pypi.org/project/meilaesop-django-polls/
- 问题反馈: https://github.com/meilaesop/django-polls/issues
- 文档: https://github.com/meilaesop/django-polls/tree/main/docs

致谢
----

- Django 软件基金会
- Bootstrap 团队
- 所有贡献者和用户

联系方式
--------

如有问题或建议，请通过GitHub Issues联系我们。

------------

**meilaesop-django-polls** - 一个功能完整的Django投票系统
