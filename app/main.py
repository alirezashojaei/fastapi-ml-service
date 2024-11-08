from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db_control import models
from app.db_control.session import engine

from app.api import endpoints

# Not for production, only for development. For production, a migration tool should be used.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the user router
app.include_router(endpoints.router, prefix="/api/users", tags=["Users"])


@app.get("/api/healthcheck")
async def health_check():
    return {"status": "API is running"}


if __name__ == "__main__":
    import uvicorn
    # Configure server settings
    uvicorn_config = uvicorn.Config(app=app,
                                    host="0.0.0.0",
                                    port=5001,
                                    loop="asyncio",
                                    reload=True,
                                    )
    uvicorn_server = uvicorn.Server(uvicorn_config)
    uvicorn_server.run()
