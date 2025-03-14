import os

# Definir rutas en EFS para dependencias grandes
EFS_PATH = '/mnt/efs1/dependencies/'
os.environ['TRANSFORMERS_CACHE'] = os.path.join(EFS_PATH, 'transformers')
os.environ['TORCH_HOME'] = os.path.join(EFS_PATH, 'torch')
os.environ['XGBOOST_CACHE'] = os.path.join(EFS_PATH, 'xgboost')

# Crear directorios en EFS si no existen
for path in [os.environ['TRANSFORMERS_CACHE'], os.environ['TORCH_HOME'], os.environ['XGBOOST_CACHE']]:
    os.makedirs(path, exist_ok=True)
