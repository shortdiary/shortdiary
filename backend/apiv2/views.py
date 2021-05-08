from rest_framework.response import Response
from rest_framework import viewsets
from diary.models import Post
from django.core.cache import cache
from django.db.models import Q
from rest_framework.permissions import BasePermission, AllowAny

from rest_framework.generics import (
	RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView,
	get_object_or_404
)

from .serializers import (
	UserSerializer, PostSerializer, PublicPostSerializer,
	LeaderboardSerializer
)


class CurrentUserView(RetrieveUpdateAPIView):
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user


class AuthenticatedOnlyExceptRetrieve(BasePermission):
	def has_permission(self, request, view):
		if request.user.is_authenticated:
			return True

		if view.action == 'retrieve':
			return True

		return False


class PostViewSet(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	permission_classes = [AuthenticatedOnlyExceptRetrieve]

	def get_queryset(self):
		return self.request.user.posts

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

	def retrieve(self, request, *args, **kwargs):
		"""
		Custom retrieve function that allows retrieval of other users posts if
		they are public, but switches to PublicPostSerializer then
		"""

		filters = Q(public=True)
		if self.request.user.is_authenticated:
			filters |= Q(author=self.request.user)

		post = get_object_or_404(Post, filters, pk=kwargs['pk'])

		serializer_class = self.get_serializer_class()
		if post.author != self.request.user:
			serializer_class = PublicPostSerializer

		serializer = serializer_class(post, context=self.get_serializer_context())
		return Response(serializer.data)


class RandomPublicPostView(ListAPIView):
	serializer_class = PublicPostSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		return Post.objects.filter(public=True).order_by('?')[:25]


class LeaderboardView(RetrieveAPIView):
	serializer_class = LeaderboardSerializer

	def get_object(self):
		return cache.get('leaderboard')
