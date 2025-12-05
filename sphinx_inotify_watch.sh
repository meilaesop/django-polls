#!/data/data/com.termux/files/usr/bin/bash
cd /data/data/com.termux/files/home/django-polls

echo "使用 inotifywait 监控"
echo "这是最可靠的监控方式"
echo "按 Ctrl+C 停止"

# 初始构建
echo "$(date '+%H:%M:%S') 初始构建..."
sphinx-build -b html docs/source docs/livehtml

echo "开始监控 docs/source/ 目录..."

while true; do
    # 等待文件变化
    inotifywait -q -r -e modify,create,delete,move docs/source 2>/dev/null
    
    echo ""
    echo "========================================"
    echo "$(date '+%H:%M:%S') 检测到文件变化！"
    echo "开始构建..."
    
    # 执行构建
    sphinx-build -b html docs/source docs/livehtml
    
    if [ $? -eq 0 ]; then
        echo "$(date '+%H:%M:%S') ✅ 构建成功！"
    else
        echo "$(date '+%H:%M:%S') ❌ 构建失败"
    fi
    
    echo "继续监控..."
    echo "========================================"
    echo ""
done
