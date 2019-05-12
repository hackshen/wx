import re
from wxpy import *

# 开启缓存
bot = Bot(cache_path=True)

# 登录成功发送消息
bot.file_helper.send('Hello Hackshen')

# bot缓存历史消息条数
bot.messages.max_history = 10000;

# 机器人账号自身
myself = bot.self

@bot.register()
def system_msg(msg):
    # 打印全部接收到的消息
    print(msg)
    raw = msg.raw
    # 4表示消息状态为撤回
    if raw['Status'] == 4:
        # 转发撤回的消息
        forward_revoke_msg(msg)

def forward_revoke_msg(msg):
    # 获取被撤回消息的ID
    revoke_msg_id = re.search('<msgid>(.*?)</msgid>', msg.raw['Content']).group(1)
    # bot中有缓存之前的消息，默认200条
    for old_msg_item in msg.bot.messages[::-1]:
        # 查找撤回的那条
        if revoke_msg_id == str(old_msg_item.id):
            # 判断是群消息撤回还是好友消息撤回
            if old_msg_item.member:
                sender_name = '群「{0}」中的「{1}」'.format(old_msg_item.chat.name, old_msg_item.member.name)
            else:
                sender_name = '「{}」'.format(old_msg_item.chat.name)
            # 名片无法转发
            if old_msg_item.type == 'Card':
                sex = '男' if old_msg_item.card.sex == 1 else '女' or '未知'
                msg.bot.file_helper.send('「{0}」撤回了一张名片：\n名称：{1}，性别：{2}'.format(sender_name, old_msg_item.card.name, sex))
            else:
                # 转发消息给文件助手
                old_msg_item.forward(msg.bot.file_helper,
                                     prefix='{}撤回了一条消息：'.format(sender_name, get_msg_chinese_type(old_msg_item.type)))
            return None

def get_msg_chinese_type(msg_type):
    """转中文类型名"""
    if msg_type == 'Text':
        return '文本'
    if msg_type == 'Map':
        return '位置'
    if msg_type == 'Card':
        return '名片'
    if msg_type == 'Note':
        return '提示'
    if msg_type == 'Sharing':
        return '分享'
    if msg_type == 'Picture':
        return '图片'
    if msg_type == 'Recording':
        return '语音'
    if msg_type == 'Attachment':
        return '文件'
    if msg_type == 'Video':
        return '视频'
    if msg_type == 'Friends':
        return '好友请求'
    if msg_type == 'System':
        return '系统'

# 堵塞线程
embed()

# API --> https://wxpy.readthedocs.io
