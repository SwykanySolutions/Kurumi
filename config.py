from dotenv import *
import os
load_dotenv()
venv_vars = { 'api_gs_key':os.getenv('api_gs_key'),
              'cx_gs':os.getenv('cx_gs'),
              'api_owm_key':os.getenv('api_owm_key')
            }