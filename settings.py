from envparse import Env


env = Env()

REAL_DATABASE_URL = env.str("REAL_DATABASE_URL",
                            default="postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres")
# --! Connect to database !-

