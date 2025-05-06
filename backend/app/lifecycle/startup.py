from app.db.bootstrap_db.bootstrap_db import BootstrapDb


class Startup:

    def run(self):
        """
        This method is called when the application starts.
        It can be used to perform any necessary initialization or setup tasks.
        """
        print("Application is starting...")
        # Perform any startup tasks here
        BootstrapDb.init_db()

