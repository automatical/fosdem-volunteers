# Minor hack to allow Userena to work with LDAP
from django_auth_ldap.backend import LDAPBackend as Orig

class workaround(Orig):
    def authenticate(self, username=None, password=None, identification=None):
        if identification and not username:
            username = identification
        return super(workaround, self).authenticate(username, password)