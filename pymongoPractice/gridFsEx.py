import gridfs
from dbConnection import client

db = client.gridfs_example
fs = gridfs.GridFS(db)
a = fs.put(b"hello world")
print(fs.get(a).read())