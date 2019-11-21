
class LazyProperty:
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance,self.func.__name__,value)
        return value


class Singleton(type):
    instance_dic = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instance_dic:
            cls.instance_dic[cls] = super().__call__(*args, **kwargs)
        return cls.instance_dic[cls]

