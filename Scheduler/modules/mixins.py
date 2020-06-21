from django.contrib.auth.mixins import UserPassesTestMixin

class MyselfOnlyMixin(UserPassesTestMixin):
    railse_esception = True
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']
