from contextlib import contextmanager


@contextmanager
def get_db_session_scope(sql_db_session):
    """Provide a transactional scope around a series of operations.
    :param sql_db_session: With specific environment information defined outside
    """
    session = sql_db_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
