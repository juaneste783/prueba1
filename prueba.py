import boto3
import pathlib

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('paulaphotography')
directorio_empresa = "paulaphotography/"
directorio_empresa_firmados = "paulaphotography/"

for object_summary in my_bucket.objects.filter(Prefix=directorio_empresa):
    print(object_summary.key)
    archivo_empresa_local = "/tmp/" + object_summary.key
    pos = archivo_empresa_local.rfind("/") + 1
    filename = archivo_empresa_local[pos:]
    archivo_empresa_local = archivo_empresa_local[:pos]

    pathlib.Path(archivo_empresa_local).mkdir(parents=True, exist_ok=True)
    if ".png" in filename:
        my_bucket.download_file(object_summary.key, archivo_empresa_local + filename)
