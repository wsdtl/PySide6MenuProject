from typing import Union
from .base import init_database

sessiom = init_database()

def INSERT(query: any) -> Union[bool, str]:
    try:
        sessiom.execute(query)
        sessiom.commit()
        return True
    except Exception as e:
        print(e)
        sessiom.rollback()
        return e
    
def SELECT(query: any, isdict: bool = False) -> any:
    try:
        reslut = sessiom.execute(query)
        if isdict:
            return reslut.mappings().all()
        else:
            return reslut
    except Exception as e:
        print(e)
        sessiom.rollback()
        return None
        
def UPDATE(query: any) ->  Union[bool, str]:
    try:
        sessiom.execute(query)
        sessiom.commit()
        return True
    except Exception as e:
        print(e)
        sessiom.rollback()
        return e