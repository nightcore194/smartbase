import inspect
import pkgutil
import sys
import re

from server.migrator import Migrator


def get_migration_modules(packages=[]):
    """
    Get python modules with migrations
    :param packages: iterable - list or tuple with packages names for the searching
    :return: list - ('module.path', 'module_name')
    """
    # List of the modules to migrate
    migration_modules = list()
    for pack in packages:
        migration_module = __import__(pack, globals(), locals(), fromlist=[str('migrations')])
        try:
            # Check, that imported object is module
            if inspect.ismodule(migration_module.migrations):
                # Find submodules inside the module
                for importer, modname, ispkg in pkgutil.iter_modules(migration_module.migrations.__path__):
                    if re.match(r'^\d{3,}_migration_[\d\w_]+$', modname) and not ispkg:
                        migration_modules.append((migration_module.migrations.__name__, modname))
            # Unregister module
            sys.modules.pop(migration_module.__name__)
        except AttributeError:
            pass
    return migration_modules

def get_migration_classes(migration_modules):
    """
    Get list of the migration classes
    :type migration_modules: iterable
    :param migration_modules: array with a migration modules
    :return: list
    """
    migration_classes = list()
    for mig_mod, m in migration_modules:
        mig = __import__(mig_mod, globals(), locals(), fromlist=[m])
        try:
            target_module = mig.__getattribute__(m)
            # Check, that imported object is module
            if inspect.ismodule(target_module):
                for name, obj in inspect.getmembers(target_module):
                    # Get all containing elements
                    if inspect.isclass(obj) and issubclass(obj, Migrator) and obj != Migrator:
                        # Save this elements
                        migration_classes.append(obj)
            # Remove imported module from the stack
            sys.modules.pop(mig.__name__)
        except AttributeError:
            pass
    return migration_classes