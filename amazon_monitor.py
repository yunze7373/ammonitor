def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')

    # 邮件相关参数
    email_host = config['Email']['host']
    email_port = config['Email']['port']
    email_username = config['Email']['username']
    email_password = config['Email']['password']
    email_recipient = config['Email']['recipient']

    # Twitter 相关参数
    twitter_api_key = config['Twitter']['api_key']
    twitter_api_secret_key = config['Twitter']['api_secret_key']
    twitter_access_token = config['Twitter']['access_token']
    twitter_access_token_secret = config['Twitter']['access_token_secret']

    # 通用参数
    interval = int(config['General']['interval'])
    asin_list = config['General']['asin_list'].split(',')

    # 创建邮件和推特客户端
    email_client = EmailClient(host=email_host, port=email_port, username=email_username, password=email_password)
    twitter_client = TwitterClient(api_key=twitter_api_key, api_secret_key=twitter_api_secret_key,
                                   access_token=twitter_access_token, access_token_secret=twitter_access_token_secret)

    while True:
        # 检查邮件，更新asin_list列表
        # ...

        # 循环监控asin_list列表中的商品
        for asin in asin_list:
            try:
                # 解析页面获取商品信息
                product_title, product_url, availability = parse_page(asin)

                # 判断是否有库存
                if 'In stock' in availability:
                    # 发送邮件和推特消息
                    subject = f'{product_title} 可以购买了！'
                    body = f'现在可以购买了！商品链接：{product_url}'
                    email_client.send_email(subject=subject, body=body, recipient=email_recipient)
                    twitter_client.send_tweet(status=f'{product_title} 可以购买了！ {product_url}')

                    # 将该商品从 asin_list 中移除
                    asin_list.remove(asin)

            except Exception as e:
                print(f'出现异常：{e}')

        # 等待指定时间
        time.sleep(interval)
