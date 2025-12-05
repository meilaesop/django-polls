使用指南
========

基本操作
--------

运行开发服务器：

.. code-block:: bash

   python manage.py runserver 8080

创建管理员：

.. code-block:: bash

   python manage.py createsuperuser

数据库迁移：

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

访问管理后台
------------

1. 启动服务器：``python manage.py runserver 8080``
2. 打开浏览器访问：``http://localhost:8080/admin``
3. 使用创建的管理员账号登录

创建投票
--------

1. 登录管理后台
2. 点击 "Questions"
3. 点击 "ADD QUESTION"
4. 填写问题文本和发布日期
5. 保存后可以添加选项 (Choices)
