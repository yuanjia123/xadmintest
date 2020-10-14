import xadmin
from .models import Question, Choice

xadmin.site.register(Question)
xadmin.site.register(Choice)