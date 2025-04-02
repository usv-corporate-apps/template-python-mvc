import os
import urllib

class Config:
    TESTING = True

class DevConfig:
    TESTING = True
    SECRET_KEY='dev'

class TestConfig:
    TESTING = True
    SECRET_KEY='test'

class ProdConfig:
    TESTING = False
    SECRET_KEY='production'