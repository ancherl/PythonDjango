# Urls -- 路由系统
- 创建一个app
    - 一个app负责一个具体业务或者一类具体业务
- 路由
    - 根据具体请求的url, 导入到相应业务处理模块的功能
    - django的信息控制中枢
    - 本质上是接收请求的URL, 然后映射到相应的处理模块
    
- 数据库的迁移
    - 生成数据库迁移语句
    ```
    python manage.py makemigrations
    ```
    - 执行数据迁移指令
    ```
    python manage.py migrate
    ```
    - 强制迁移命令
    ```
    python manage.py makemigrations 应用名
    python manage.py migrate 应用名
    ```
- 查看数据库中的数据
    - python manage.py shell命令行