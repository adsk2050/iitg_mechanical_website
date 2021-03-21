from social_django.strategy import DjangoStrategy

class CustomDjangoStrategy(DjangoStrategy):
    def build_absolute_uri(self, path=None):
        if self.request:
            return self.request.build_absolute_uri(path)
        else:
            return path
"""
    def build_absolute_uri(self, path=None):
        if path:
            print(f"{path} -- in build_absolute_uri (custom)\n")
            return "https://intranet.iitg.ac.in"+path
        else:
            print("No path, running system defined build_absolute_uri\n")
            return "https://intranet.iitg.ac.in"
            # return self.build_absolute_uri2(path=path)
"""
