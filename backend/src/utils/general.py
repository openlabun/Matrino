
def response_wrapper(msg: str, success: bool = True, **keys) -> dict:
    return {
            'success': success,
            'message': msg,
            **keys
        }
