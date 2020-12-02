from social_django.strategy import DjangoStrategy

class CustomDjangoStrategy(DjangoStrategy):
    def build_absolute_uri2(self, path=None):
        if self.request:
            return self.request.build_absolute_uri(path)
        else:
            return path

    def build_absolute_uri(self, path=None):
        if path:
            return "https://intranet.iitg.ac.in"+path
        else:
            return self.build_absolute_uri2(path=path)
