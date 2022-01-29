from rest_framework.authtoken.models import Token
from accounts.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, parsers, renderers, views, response, viewsets, authentication, permissions
from accounts.serializers import get_user_model, UserSerializer


class ObtainAuthToken(views.APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        context = {}
        email, password = serializer.validated_data['email'], serializer.validated_data['password']
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError({'msg': msg}, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError({'msg': msg}, code='authorization')
        context['user'], context['email'] = user, user.email
        token, created = Token.objects.get_or_create(user=user)
        return response.Response({'token': token.key})


class UserModeViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
