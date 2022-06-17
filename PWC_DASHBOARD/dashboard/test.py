
from project.models import *

project = Project.objects.filter(manager=2)
print(project)
