from fake_useragent import FakeUserAgent
UA = FakeUserAgent()
headers = {
    'User-Agent':UA.random
}