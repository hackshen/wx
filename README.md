# wx
微信防撤回

```bash
# build镜像文件
docker build -t wx .

# 运行容器
docker run -itd --name wx -v ./robot.py:/robot/robot.py wx

# 查看日志(扫描二维码登录，会返回shell)
docker logs -f wx
```
