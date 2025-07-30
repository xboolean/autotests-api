from enum import Enum


class AllureTag(str, Enum):
    SMOKE = "SMOKE"
    USERS = "USERS"
    REGRESSION = "REGRESSION"
    AUTHENTICATION = "AUTHENTICATION"
    GET_ENTITIES = "GET ENTITIES"
