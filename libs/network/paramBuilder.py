import uuid
import base64
import hashlib

from libs.network import url
from urllib.parse import quote_plus
from libs.utils import mytime

class ParameterBuilder:
    def __init__(self, uid: str, auth_key: str, secret_key: str):
        self.uid_ = uid
        self.auth_key_ = auth_key
        self.secret_key_ = secret_key
        self.content_ = ''

        self.parameter_list_ = [
            ('appVer', url.app_ver_),
            ('authKey', self.auth_key_),
            ('dataVer', str(url.data_ver_)),
            ('dateVer', str(url.date_ver_)),
            ('idempotencyKey', str(uuid.uuid4())),
            ('lastAccessTime', str(mytime.GetTimeStamp())),
            ('userId', self.uid_),
            ('verCode', url.ver_code_),
        ]

    def AddParameter(self, key: str, value: str):
        self.parameter_list_.append((key, value))

    def Build(self) -> str:
        self.parameter_list_.sort(key=lambda tup: tup[0])

        temp = ''
        for first, second in self.parameter_list_:
            if temp:
                temp += '&'
                self.content_ += '&'
            
            escaped_key = quote_plus(first)
            
            if not second:
                temp += first + '='
                self.content_ += escaped_key + '='
            else:
                escaped_value = quote_plus(second)
                temp += first + '=' + second
                self.content_ += escaped_key + '=' + escaped_value

        temp += ':' + self.secret_key_


        self.content_ += '&authCode=' + \
            quote_plus(base64.b64encode(hashlib.sha1(temp.encode('utf-8')).digest()))

        return self.content_

    def Clean(self):
        self.content_ = ''
        self.parameter_list_ = [
            ('appVer', url.app_ver_),
            ('authKey', self.auth_key_),
            ('dataVer', str(url.data_ver_)),
            ('dateVer', str(url.date_ver_)),
            ('idempotencyKey', str(uuid.uuid4())),
            ('lastAccessTime', str(mytime.GetTimeStamp())),
            ('userId', self.uid_),
            ('verCode', url.ver_code_),
        ]