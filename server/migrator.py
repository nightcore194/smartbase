import abc
from playhouse.migrate import (migrate, PostgresqlMigrator)
from server.databaseSetup import setup_connection

db = setup_connection()

class Migrator(object):
    """
    Migration interface
    """

    __metaclass__ = abc.ABCMeta

    connection = db.connection()           # db_connection is a Borg instance
    migrator = PostgresqlMigrator(db.connection)

    @abc.abstractproperty
    def migrations(self):
        """
        List of the migrations dictionaries
        :param self: class instance
        :return: list
        """
        return [
            {'statement': 1 != 2, 'migration': ['list', 'of', 'migration', 'options'],
             'migration_kwargs': {}, 'pre_migrations': list(), 'post_migrations': list()}
        ]          # Just an example

    def migrate(self):
        """
        Run migrations
        """
        for migration in self.migrations:
            if migration['statement']:
                # Run scripts before the migration
                pre_migrations = migration.get('pre_migrations', list())
                for pre_m in pre_migrations:
                    pre_m()
                # Migrate
                with db.connection.transaction():
                    migration_kwargs = migration.get('migration_kwargs', {})
                    migrate(*migration['migration'], **migration_kwargs)
                # Run scripts after the migration
                post_migrations = migration.get('post_migrations', list())
                for post_m in post_migrations:
                    post_m()