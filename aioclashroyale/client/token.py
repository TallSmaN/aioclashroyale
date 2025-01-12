from envparse import env

__all__ = (
    'Token',
)


class Token(str):

    @classmethod
    def from_env(cls, env_file: str, key: str = 'CLASH_ROYALE_TOKEN') -> 'Token':
        env.read_envfile(env_file)
        return cls(env.str(key))
