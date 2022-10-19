class SingletonMeta(type):
    """
    Credits to https://refactoring.guru/es/design-patterns/singleton/python/example
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            instance = super().__call__(
                *args, **{**cls._instances[cls].__dict__, **kwargs}
            )
            cls._instances[cls] = instance
        return cls._instances[cls]
