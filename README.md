# pytodo
## 项目介绍
pytodo是一个基于Python的待办事项管理工具，允许用户以命令行界面管理他们的日常任务。通过这个工具，用户可以添加、编辑、删除以及查询他们的待办事项。

## 安装指南
下载本仓库，然后在包含main.py的目录下通过命令行运行以下命令来启动应用：
```shell
python main.py
```
## 使用方法
启动本应用后会进入主菜单界面，只需输入对应的指令进行对pytodo的操作
- 添加事件(add)：按照提示输入任务信息即可添加信息至本地history.json
- 帮助(help)：可查询事件类型的意义和指令的说明
- 删除事件(done)：按照提示删除指定的事件。可以选择删除指定序号对应的事项或删除所有事件
- 查询所有事件(show)：查询todo-list上的所有事件
- 查询今日可做或需要做的事件(today)
- 查询未来几日内要做的事件(future)：通过输入future，空格后加一个数字n可查询未来n天所要做的事件
- 退出程序(quit)

## 功能介绍
- Events.py：处理待办事项的事件逻辑，如添加、修改和删除事件。
- LoadSave.py：负责加载和保存待办事项到history.json，确保任务在会话之间保持。
- main.py：应用的入口，处理用户输入并调用相应的事件处理逻辑。
- history.json：存储用户待办事项的文件。
## 事件类型的介绍
- 周期事件：每隔一定时间要做的事
- 截止日期事件：要在指定日期前做的事
- 开始日期事件：要在指定日期之后做的事 
- 会议事件：要在指定日期当日做的事
- 原子事件：有起始日期和截止日期的事件