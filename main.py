from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','), allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
@app.get('/health')
async def health_check():
    return {'status': 'ok'}
