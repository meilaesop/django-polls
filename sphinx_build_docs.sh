#!/data/data/com.termux/files/usr/bin/bash
# 简化的文档构建脚本

echo "开始构建 Django Polls 文档..."

# 进入项目目录
cd /data/data/com.termux/files/home/django-polls

# 构建文档
cd docs
sphinx-build -b html source build/html

echo "文档构建完成！"
echo "文档位置：/data/data/com.termux/files/home/django-polls/docs/build/html/index.html"

# 提示如何查看
echo ""
echo "查看文档的方法："
echo "1. 在 Termux 中使用浏览器："
echo "   python -m http.server 8000 -d docs/build/html"
echo "   然后在浏览器访问 http://localhost:8000"
echo ""
echo "2. 直接查看 HTML 文件："
echo "   termux-open docs/build/html/index.html"
