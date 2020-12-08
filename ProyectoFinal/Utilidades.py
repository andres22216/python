def esNumerico(texto):
    try:
        int(texto)
        return True
    except ValueError:
        return False