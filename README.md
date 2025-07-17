# Streamlit JSON Schema UI

一个基于Vue.js和Vuetify的Streamlit组件，用于创建美观的JSON Schema用户界面。

## 功能特性

- 🎨 基于Vuetify的现代化UI设计
- 📝 完整的JSON Schema支持
- 🔄 实时数据验证
- 📱 响应式设计
- 🎯 易于集成到Streamlit应用中

## 安装

```bash
pip install streamlit-jsonschema-ui
```

## 快速开始

```python
import streamlit as st
from streamlit_jsonschema_ui import JsonSchemaUI

# 定义JSON Schema
schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "姓名",
            "description": "请输入您的姓名"
        },
        "age": {
            "type": "integer",
            "title": "年龄",
            "minimum": 0,
            "maximum": 150
        },
        "email": {
            "type": "string",
            "format": "email",
            "title": "邮箱"
        }
    },
    "required": ["name", "email"]
}

# 初始数据
initial_data = {
    "name": "",
    "age": 25,
    "email": ""
}

```

## 高级用法

### 自定义主题

```python
import streamlit as st
from streamlit_jsonschema_ui import streamlit_jsonschema_ui

# 自定义主题配置
theme_config = {
    "primary": "#1976D2",
    "secondary": "#424242",
    "accent": "#82B1FF"
}

result = streamlit_jsonschema_ui(
    schema=schema,
    streamlit_jsonschema_ui=streamlit_jsonschema_ui,
    key="custom_theme_form"
)
```

### 复杂Schema示例

```python
complex_schema = {
    "type": "object",
    "properties": {
        "personal_info": {
            "type": "object",
            "title": "个人信息",
            "properties": {
                "name": {"type": "string", "title": "姓名"},
                "birth_date": {"type": "string", "format": "date", "title": "出生日期"}
            }
        },
        "preferences": {
            "type": "array",
            "title": "偏好设置",
            "items": {
                "type": "object",
                "properties": {
                    "category": {"type": "string", "title": "类别"},
                    "value": {"type": "string", "title": "值"}
                }
            }
        }
    }
}
```

## 开发

### 环境设置

1. 克隆仓库：
```bash
git clone https://github.com/find-partner/streamlit_jsonschema_ui.git
cd streamlit_jsonschema_ui
```

2. 安装开发依赖：
```bash
uv sync --dev
```

3. 安装前端依赖：
```bash
cd src/streamlit_jsonschema_ui/frontend
npm install
```

### 构建前端

```bash
cd src/streamlit_jsonschema_ui/frontend
npm run build
```

## 贡献

欢迎提交Issue和Pull Request！

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开Pull Request

## 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 相关链接

- [Streamlit文档](https://docs.streamlit.io/)
- [JSON Schema规范](https://json-schema.org/)
- [Vuetify文档](https://vuetifyjs.com/)
- [Vue.js文档](https://vuejs.org/)
