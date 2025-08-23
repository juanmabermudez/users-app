import bcrypt
import uuid
from datetime import datetime, timedelta

def get_salt() -> bytes:
    """Genera una nueva sal."""
    return bcrypt.gensalt()

def hash_password(password: str, salt: bytes) -> str:
    """Hashea una contraseña usando una sal proporcionada."""
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pw.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str, salt: bytes) -> bool:
    """Verifica una contraseña contra su hash y sal."""
    # bcrypt.checkpw requiere que el hash sea bytes, no str.
    # La sal ya está incluida en el hash que checkpw espera, pero como la tenemos separada,
    # debemos reconstruir el hash esperado o usar el hash directo.
    # La forma correcta es usar el hash almacenado directamente.
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_token() -> (str, datetime):
    """Genera un token de sesión único y su fecha de expiración."""
    token = str(uuid.uuid4())
    expire_at = datetime.utcnow() + timedelta(hours=1) # Token válido por 1 hora
    return token, expire_at
