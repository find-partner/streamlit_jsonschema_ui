import streamlit as st
from streamlit_jsonschema_ui import streamlit_jsonschema_ui
import psutil
import os
import time

st.write("""
# Streamlit jsonschema example
""")

true = True
false = False

res = streamlit_jsonschema_ui(
    {
    "type": "object",
    "title": "组织配置",
    "properties": {
        "ORG_CODE": {
            "type": "string",
            "title": "组织代码",
            "x-from": "project",
            "minLength": 2
        },
        "module_groups": {
            "type": "array",
            "title": "模块分组列表",
            "items": {
                "type": "object",
                "properties": {
                    "group_name": {
                        "type": "string",
                        "title": "分组名",
                        "minLength": 1
                    },
                    "module_types": {
                        "type": "array",
                        "title": "模块类型列表",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type_name": {
                                    "type": "string",
                                    "title": "类型名",
                                    "enum": [
                                        "domains",
                                        "interfaces"
                                    ]
                                },
                                "modules": {
                                    "type": "array",
                                    "title": "模块列表",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "module_name": {
                                                "type": "string",
                                                "title": "模块名",
                                                "minLength": 1
                                            },
                                            "model_name": {
                                                "type": "string",
                                                "title": "业务模型名",
                                                "minLength": 1
                                            },
                                            "domains_config": {
                                                "type": "object",
                                                "title": "domains 配置",
                                                "properties": {
                                                    "admin": {
                                                        "type": "boolean",
                                                        "title": "是否生成 admin",
                                                        "default": true
                                                    },
                                                    "migrations": {
                                                        "type": "boolean",
                                                        "title": "是否生成 migrations",
                                                        "default": true
                                                    }
                                                },
                                                "required": []
                                            },
                                            "interfaces_config": {
                                                "type": "object",
                                                "title": "interfaces 配置",
                                                "properties": {
                                                    "api_version": {
                                                        "type": "string",
                                                        "title": "API 版本",
                                                        "default": "v1"
                                                    },
                                                    "serializer": {
                                                        "type": "boolean",
                                                        "title": "是否生成 serializer",
                                                        "default": true
                                                    }
                                                },
                                                "required": []
                                            }
                                        },
                                        "required": [
                                            "module_name",
                                            "model_name"
                                        ]
                                    }
                                }
                            },
                            "required": [
                                "type_name",
                                "modules"
                            ]
                        }
                    }
                },
                "required": [
                    "group_name",
                    "module_types"
                ]
            }
        }
    },
    "required": [
        "ORG_CODE",
        "module_groups"
    ]
},
    {'module_groups': [], 'ORG_CODE': 'asdfasdf'},
    key='222'
)
print(res)

exit_app = st.sidebar.button("Shut Down")
if exit_app:
    # Give a bit of delay for user experience
    time.sleep(5)
    # Terminate streamlit python process
    pid = os.getpid()
    p = psutil.Process(pid)
    p.terminate()
