from config import config, framework
from engine import registry, loader, log, timer
class index:
    def __init__(self):
        registry_ = registry.registry()
        config_ = config.config()
        framework.framework(config_)
        registry_.set("config", config_)
        registry_.set("loader", loader.loader(registry_))
        registry_.run()
        pass
index()