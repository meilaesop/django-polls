#!/data/data/com.termux/files/usr/bin/bash

echo "🔧 Git推送问题诊断与修复"
echo "========================"

cd /data/data/com.termux/files/home/django-polls

# 1. 检查当前状态
echo "1. 📊 当前状态:"
echo "   目录: $(pwd)"
echo "   Git用户: $(git config user.name)"
echo "   远程仓库: $(git remote -v)"

# 2. 检查文件
echo -e "\n2. 📁 项目文件:"
ls -la | grep -E "\.(py|toml|cfg|rst|md)$" | head -10

# 3. 创建新的GitHub仓库（如果需要）
echo -e "\n3. 🌐 确保GitHub仓库存在..."
echo "   请确认已在GitHub创建仓库:"
echo "   网址: https://github.com/meilaesop/django-polls"
echo "   如果没有，请先创建（不要初始化文件）"
read -p "   已创建？(y/n): " -n 1 created
echo ""

if [ "$created" != "y" ] && [ "$created" != "Y" ]; then
    echo "⚠️  请先创建GitHub仓库"
    echo "   访问: https://github.com/new"
    echo "   名称: django-polls"
    echo "   不要初始化README/.gitignore/license"
    read -p "   创建后按回车继续..." dummy
fi

# 4. 获取新Token
echo -e "\n4. 🔑 获取新GitHub Token:"
echo "   访问: https://github.com/settings/tokens"
echo "   点击 'Generate new token (classic)'"
echo "   权限必须包括: repo (全部)"
echo "   有效期: 建议90天"
echo ""
read -sp "   输入新Token: " github_token
echo ""
echo "   Token长度: ${#github_token} 字符"

if [ ${#github_token} -lt 40 ]; then
    echo "   ❌ Token可能不完整或错误"
    exit 1
fi

# 5. 重新配置
echo -e "\n5. ⚙️  重新配置Git..."
git remote remove origin 2>/dev/null
git remote add origin "https://${github_token}@github.com/meilaesop/django-polls.git"

# 6. 测试连接
echo -e "\n6. 🔌 测试连接..."
curl -s -H "Authorization: token ${github_token}" \
  https://api.github.com/user | grep -o '"login":"[^"]*"' || echo "连接测试失败"

# 7. 推送
echo -e "\n7. 🚀 开始推送..."
if git push -u origin main 2>&1; then
    echo -e "\n🎉 推送成功！"
    echo -e "\n🔗 仓库: https://github.com/meilaesop/django-polls"
    echo -e "\n下一步:"
    echo "   1. 设置PyPI API Token:"
    echo "      访问: https://github.com/meilaesop/django-polls/settings/secrets/actions"
    echo "      添加: PYPI_API_TOKEN = 您的PyPI Token"
    echo "   2. 创建Release自动发布"
else
    echo -e "\n❌ 推送失败"
    echo "可能原因:"
    echo "   - Token权限不足 (需要repo全部权限)"
    echo "   - Token过期"
    echo "   - 网络问题"
    echo "   - 仓库不存在"
fi
