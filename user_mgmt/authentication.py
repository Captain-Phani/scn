from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailBackend(ModelBackend):

    '''
    A class to overwrite the default features provided by django
    Normally Django use username for verification purpose
    Now we are overwritng the method to change it to username for verificaiton process
    '''

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tries to fetch the user object if
            # provided email matches with username(which is email in this conttext)
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        # chech_password takes provided password as param and converts into hashed code by using
        # same algorith which is used for hashing password while registering
        # if both hashed passwords are same it returns user
        if user.check_password(password):
            return user

        return None

