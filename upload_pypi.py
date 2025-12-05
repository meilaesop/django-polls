#!/usr/bin/env python3
"""
简单的 PyPI 上传脚本，无需 twine
"""
import requests
import os
import sys
from pathlib import Path
import getpass

def upload_file(file_path, token):
    """上传单个文件到 PyPI"""
    url = "https://upload.pypi.org/legacy/"
    
    with open(file_path, 'rb') as f:
        files = {
            ':action': (None, 'file_upload'),
            'name': (None, 'django-polls'),
            'version': (None, '1.0.0'),
            'file': (os.path.basename(file_path), f, 'application/octet-stream')
        }
        
        headers = {
            'Authorization': f'token {token}'
        }
        
        print(f"上传 {os.path.basename(file_path)}...")
        response = requests.post(url, files=files, headers=headers)
        
        return response

def main():
    # 检查 dist 目录
    dist_dir = Path("dist")
    if not dist_dir.exists():
        print("错误: dist 目录不存在")
        print("请先运行: python -m build")
        print("或者: python setup.py sdist bdist_wheel")
        sys.exit(1)
    
    # 获取文件列表
    files = list(dist_dir.glob("*"))
    if not files:
        print("错误: dist 目录中没有文件")
        sys.exit(1)
    
    print("找到的文件:")
    for i, f in enumerate(files, 1):
        size = f.stat().st_size / 1024
        print(f"  [{i}] {f.name} ({size:.1f} KB)")
    
    # 获取 token
    print("\n需要 PyPI API token")
    print("获取地址: https://pypi.org/manage/account/#api-tokens")
    token = getpass.getpass("请输入 token (以 pypi- 开头): ").strip()
    
    if not token:
        print("错误: token 不能为空")
        sys.exit(1)
    
    # 上传文件
    success = True
    for file_path in files:
        print(f"\n上传 {file_path.name}...")
        try:
            response = upload_file(file_path, token)
            
            if response.status_code == 200:
                print(f"✓ {file_path.name} 上传成功")
            else:
                print(f"✗ {file_path.name} 上传失败 (状态码: {response.status_code})")
                print("响应:", response.text[:500])
                success = False
        except Exception as e:
            print(f"✗ {file_path.name} 上传出错: {e}")
            success = False
    
    if success:
        print("\n✓ 所有文件上传成功！")
        print("检查: https://pypi.org/project/django-polls/")
    else:
        print("\n⚠ 部分文件上传失败")
        sys.exit(1)

if __name__ == "__main__":
    main()
