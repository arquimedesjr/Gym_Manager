from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    #Login 
    url(r'^$', RedirectView.as_view(url='/logar/')),
    url('logar/$', logar, name='logar'),
    url('deslogar/$', deslogar, name='deslogar'),
    url('esqueci-minha-senha/$', esqueci_minha_senha, name="esqueci_minha_senha"),
    
    # Index Dashboard
    url('index/$', index, name='index'),

    # aluno
    url('cadastrar-aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    url(r'^listar-aluno/', listar_aluno, name='aluno_list'),
    url(r'^editar-aluno/(?P<pk>[0-9]+)', editar_aluno, name='editar_aluno'),
    url(r'^remover-aluno/(?P<pk>[0-9]+)', remover_aluno, name='remover_aluno'),
    url(r'^detalhes-do-aluno/(?P<pk>[0-9]+)', details_aluno, name='details_aluno'),

    # não definido
    url('registrar_usuario/$', registrar_usuario, name='registrar_usuario'),
    url('listar_usuario/$', listar_usuario, name='listar_usuario'),
    url('remover_usuario/(?P<pk>[0-9]+)', remover_usuario, name='remover_usuario'),

    # Password Reset
    # url('^', include('django.contrib.auth.urls')),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Password Reset
    # url('^', include('django.contrib.auth.urls')),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
