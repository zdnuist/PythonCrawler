import configparser
import os
from qiniu import Auth,put_file,etag,urlsafe_base64_encode
import qiniu.config

cf = configparser.ConfigParser()

cf.read("qiniu_demo.conf")

secs = cf.sections()
print("secs:" + str(secs))
opts = cf.options("qiniu")
print("opts:" + str(opts))
access_key = cf.get("qiniu","access_key")
print("ak:" + access_key)
secret_key = cf.get("qiniu" , "secret_key")
print("sk:" + secret_key)

#构建鉴权对象
q = Auth(access_key,secret_key)

#要上传的空间
bucket_name = cf.get("qiniu","bucket_name")
print("bn:" + bucket_name)

#上传到七牛后保存的文件名
key = 'demo1'

#生成上传 Token 可以指定过期时间等
token = q.upload_token(bucket_name, key , 3600)

#要上传文件的本地路径
localfile = '../qsbk_2017-09-19'

info = put_file(token, key, localfile)
print(info)
