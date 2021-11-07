# coding: utf-8
class work:
    def __init__(self, fields):
        self.fields = {}
        for k, v in fields.items():
            self.fields[k] = v
    
    def set_def_val(self):
        require_fileds = {'bad_num':0, 'like_num':0, 'creator':'', 'explation':'', 'thumnail':'', 'title':''}
        for k, v in list(require_fileds.items()):
            self.fields.setdefault(k, v)
        return self.fields