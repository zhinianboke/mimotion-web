# 小米运动助手 (MiMotion Assistant)

一个基于 Flask 的小米运动（Zepp Life）自动刷步数工具，提供友好的 Web 界面和丰富的功能。

![小米运动助手](https://img.shields.io/badge/小米运动助手-v1.0-blue)
![Flask](https://img.shields.io/badge/Flask-v2.2.5-green)
![Python](https://img.shields.io/badge/Python-v3.8+-orange)

## 功能特点

- 🌟 **美观的 Web 界面**：基于现代化设计的简洁界面
- 👥 **多账号管理**：支持添加多个小米运动账号，统一管理和监控
- ⏰ **智能时间控制**：设置同步时间范围，根据时间自动计算合理的步数
- 📊 **数据可视化**：提供步数趋势图表和同步成功率统计分析
- 🔄 **自动定时同步**：按计划自动同步步数，无需手动操作
- 📱 **响应式设计**：在各种设备上都能良好显示
- 🔐 **用户系统**：支持多用户注册登录，数据隔离

## 安装步骤

### 方法一：使用 Docker (推荐)

1. **克隆仓库**

```bash
git clone https://github.com/yourusername/mimotion-web.git
cd mimotion-web
```

2. **使用 Docker Compose 启动**

```bash
docker-compose up -d
```

访问 http://localhost:5002 即可使用。

### 方法二：手动安装

1. **克隆仓库**

```bash
git clone https://github.com/yourusername/mimotion-web.git
cd mimotion-web
```

2. **创建虚拟环境**

```bash
# 使用 conda 创建虚拟环境
conda create -n mimotion python=3.8
conda activate mimotion

# 或使用 venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **初始化数据库**

```bash
python update_db.py
```

5. **启动应用**

```bash
python run.py
```

访问 http://127.0.0.1:5002 即可使用。

## 环境变量配置

你可以通过环境变量或创建 `.env` 文件来配置以下参数：

- `SECRET_KEY`: Flask 应用密钥（默认：'dev-key-mimotion'）
- `DATABASE_URL`: 数据库连接 URI（默认：'sqlite:///mimotion.db'）

## 使用方法

### 1. 注册与登录

- 首次使用需要注册账号
- 已有账号直接登录

### 2. 添加小米运动账号

1. 在"账号管理"页面点击"添加账号"
2. 输入小米运动/Zepp Life 的账号和密码
3. 设置步数范围（最小步数和最大步数）
4. 设置同步时间范围（开始时间和结束时间）

### 3. 管理账号

- **查看账号列表**：所有已添加的账号会显示在账号管理页面
- **编辑账号**：修改步数范围和同步时间
- **启用/禁用账号**：控制是否参与自动同步
- **删除账号**：移除不再使用的账号

### 4. 同步步数

- **自动同步**：系统会在设定的时间范围内每小时自动同步步数
- **手动同步**：点击账号列表中的"同步"按钮可立即执行同步

### 5. 查看统计数据

- **同步记录**：查看每个账号的同步历史记录
- **步数趋势图**：可视化查看步数变化趋势
- **成功率统计**：查看同步成功率分析

## 工作原理

小米运动助手通过模拟小米运动/Zepp Life 应用的 API 请求来修改步数数据：

1. **智能步数计算**：根据当天的时间比例计算合理的步数
2. **定时同步任务**：使用 Flask-APScheduler 实现定时任务
3. **IP 保护机制**：每次请求使用随机 IP，降低封号风险

## 项目结构

```
mimotion-web/
├── app/                    # 应用主目录
│   ├── controllers/        # 控制器
│   │   ├── account.py      # 账号管理相关
│   │   ├── auth.py         # 用户认证相关
│   │   └── main.py         # 主页及仪表盘
│   ├── models/             # 数据模型
│   │   ├── mi_account.py   # 小米账号模型
│   │   ├── step_record.py  # 步数记录模型
│   │   └── user.py         # 用户模型
│   ├── scheduler/          # 定时任务
│   │   └── tasks.py        # 定时同步步数任务
│   ├── templates/          # 页面模板
│   ├── utils/              # 工具函数
│   │   └── mi_motion.py    # 小米运动API工具类
│   └── __init__.py         # 应用初始化
├── instance/               # 实例配置及数据库
├── config/                 # 配置文件
├── Dockerfile              # Docker配置
├── docker-compose.yml      # Docker Compose配置
├── run.py                  # 启动脚本
├── update_db.py            # 数据库更新脚本
└── requirements.txt        # 依赖列表
```

## 技术栈

- **后端**：Flask、SQLAlchemy、APScheduler
- **前端**：HTML、CSS、JavaScript
- **数据库**：SQLite
- **部署**：Docker、Gunicorn

## 常见问题

1. **账号验证失败**
   - 确认小米账号/密码正确
   - 确认账号未开启二次验证
   - 尝试在官方应用中重新登录

2. **同步步数失败**
   - 查看日志了解具体错误信息
   - 检查网络连接
   - 可能是小米服务器问题，稍后重试

3. **步数不更新**
   - 小米服务器同步可能有延迟
   - 检查应用是否已正确关联手环/手表

## 注意事项

1. 本项目仅供学习交流使用，请勿用于商业用途
2. 请合理设置步数范围，避免设置不合理的步数
3. 请遵守小米运动的使用条款
4. 账号密码等敏感信息存储在本地数据库，请确保安全

## 未来计划

- [ ] 增加数据导出功能
- [ ] 支持自定义步数算法
- [ ] 支持邮件/推送通知

## 开源许可

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 致谢

本项目基于以下开源项目开发：

- [Flask](https://flask.palletsprojects.com/) - Python Web 框架
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - ORM 框架
- [Flask-APScheduler](https://github.com/viniciuschiele/flask-apscheduler) - 任务调度框架

---

如有问题或建议，欢迎提交 Issue 或 Pull Request。
