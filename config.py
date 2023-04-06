class Config:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://usman:MfoTvJXbYJnN4vHBEdWDocwGWObnaWRN@dpg-cgn6mpfdvk4k0104a04g-a.singapore-postgres.render.com/fsnd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://usman:MfoTvJXbYJnN4vHBEdWDocwGWObnaWRN@dpg-cgn6mpfdvk4k0104a04g-a.singapore-postgres.render.com/fsnd'
