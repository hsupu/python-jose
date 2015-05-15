

class JOSEError(Exception):
    pass


class JWSError(JOSEError):
    pass


class JWSAlgorithmError(JWSError):
    pass


class JWTError(JOSEError):
    pass


class JWTClaimsError(JWTError):
    pass


class JWTSignatureError(JWTError):
    pass


class ExpiredSignatureError(JWTError):
    pass
