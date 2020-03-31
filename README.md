# wx
> 微信防撤回

### 目前实现的功能

- 好友消息防撤回
- 打印好友发送消息
- 更多玩法请参考 [https://wxpy.readthedocs.io](https://wxpy.readthedocs.io)
### Docker版
```bash
# build镜像文件
docker build -t wx .

# 运行容器
docker run -itd --name wx -v ./robot.py:/robot/robot.py wx

# 查看日志(扫描二维码登录，会返回shell)
docker logs -f wx
```

###  常规版

```bash
pip install -U wxpy -i "https://pypi.doubanio.com/simple/
python robot.py
```
