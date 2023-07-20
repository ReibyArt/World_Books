from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(),
        name='book-detail'),
    url(r'^author/$', views.AuthorListView.as_view(),
        name='authors'),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my_borrowed')
]
