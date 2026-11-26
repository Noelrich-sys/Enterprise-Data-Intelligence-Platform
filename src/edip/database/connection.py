from sqlalchemy import create_engine

from edip.config.settings import settings



def get_engine():

    db=settings.database


    connection_string=(

        f"postgresql://"
        f"{db['host']}:{db['port']}/"
        f"{db['name']}"

    )


    return create_engine(
        connection_string
    )