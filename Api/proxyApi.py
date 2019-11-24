import platform
from flask import Flask, Response, jsonify
from Manager import ProxyManager


class JsonResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        print("JsonResponse---->:", response)
        if isinstance(response, (dict, list)):

            response = jsonify(response)

        return super(JsonResponse, cls).force_type(response, environ)


app = Flask(__name__)
app.response_class = JsonResponse
api_list = {
    'get': '从DB获取一个proxy',
    'get_all': '从DB获取所有proxy',
    'delete': '从DB中删除一个proxy',
    'get_useful_number': '获取现在DB中可用proxy数量',
    'get_http_proxy': '获取所有的http代理',
    'get_https_proxy': '获取所有的https代理',
}

proxy_manager = ProxyManager.ProxyManager()
@app.route('/get/')
def get_proxy():
    # TODO

    proxy = proxy_manager.get_proxy()
    return proxy


@app.route('/get_all/')
def get_all_proxy():
    proxy_list = proxy_manager.get_all_proxy()
    return proxy_list


@app.route('/delete/<string:ip_port>/')
def delete_proxy(ip_port):
    proxy_manager.delete_proxy(ip_port)
    return True


@app.route('/proxy_number/')
def get_all_number():
    return proxy_manager.get_proxy_number()


@app.route('/get_http_proxy/')
def get_http_proxy():
    return proxy_manager.get_http_proxy()


@app.route('/get_https_proxy')
def get_https_proxy():
    return proxy_manager.get_https_proxy()


# if __name__ == '__main__':
#     from Config.settings import SERVER_API
#     if platform.system() == 'Windows':
#         app.run(
#             host=SERVER_API['HOST'],
#             port=SERVER_API['PORT'],
#             debug=SERVER_API['DEBUG'])

if __name__ == '__main__':
    print(proxy_manager.get_proxy())
    print(proxy_manager.get_all_proxy())
    print(proxy_manager.get_http_proxy())
    print(proxy_manager.get_proxy_number())
    print(proxy_manager.get_https_proxy())
    # print(proxy_list)