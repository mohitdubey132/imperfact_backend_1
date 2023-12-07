from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('users-list/', views.getUsers, name="users-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('signup/', views.user_create, name="user-create"),
    path('login/', views.custom_user_login, name="user-login"),

	path('task-update/', views.taskUpdate, name="task-update"),
	path('task-delete/', views.delete_all_custom_users, name="task-delete"),
	path('create-question/',views.create_question,name="create-question"),
	# ---------------------------question end points--------------------------------#
	path('question-list/',views.getQuestion,name="question-list"),
	path('answersForQuestion/',views.getAnswersForQuestion,name="answersForQuestion"),

	#--------------------------- Answer end points----------------------------------#
	path('write-answer/',views.answer_question,name="answer-a-question")
]
