安装打包工具 `pip install pyinstaller`

执行打包命令(根据实际位置替换路径) `pyinstaller -F -w -i C:\Users\CJ\PycharmProjects\ToolForPP\ppicon\favicon.ico --add-data C:\Users\CJ\PycharmProjects\ToolForPP\ppicon;ppicon --hidden-import=_cffi_backend C:\Users\CJ\PycharmProjects\ToolForPP\main.py`

默认打包位置为 用户文件夹下的dist文件夹中。
