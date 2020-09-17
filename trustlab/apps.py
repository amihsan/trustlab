from django.apps import AppConfig


class TrustlabConfig(AppConfig):
    name = 'trustlab'

    # TODO: Handle corner cases i.e. restricting ready method running multiple times. (See AppConfig doc)
    def ready(self):
        Supervisor = self.get_model('Supervisor')
        Supervisor.objects.filter(agents_in_use=0).delete()
        print('Outdated supervisors handled')
