import tensorflow as tf

tf.compat.v1.disable_eager_execution()

_session = None


def get_session():
    global _session

    # Build/retrieve the session if it doesn't exist
    if _session is None:
        if tf.compat.v1.get_default_session() is not None:
            _session = tf.compat.v1.get_default_session()
        else:
            _session = tf.compat.v1.Session()

    return _session


def set_session(session):
    global _session
    _session = session
