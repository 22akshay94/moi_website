from django.db import models

class Personal(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(null=True, blank=True)
    email = models.EmailField(blank=False)
    linked_in = models.CharField(blank=False, max_length=200)
    profile_statement = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HomeItem(models.Model):

    class ItemObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(display_item=True)

    id = models.AutoField(primary_key=True)
    type_choices = (
        (0, 'Education'),
        (1, 'Work')
    )
    type = models.CharField(choices=type_choices, default=0, max_length=9)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    display_item = models.BooleanField(default=True)

    objects = models.Manager() # default manager
    item_objs = ItemObjects() # custom manager

    class Meta:
        abstract = True
        ordering = ['id']

class Education(HomeItem):

    type = 0
    level = models.CharField(max_length=50)
    final_percentage = models.PositiveIntegerField()
    key_modules = models.CharField(max_length=500)

    personal = models.ForeignKey(Personal, null=True, blank=True, on_delete=models.CASCADE, related_name='education')

    def __str__(self):
        return self.institution

class Work(HomeItem):

    type = 1
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    work_description = models.CharField(max_length=500)
    is_current = models.BooleanField(default=False)

    personal = models.ForeignKey(Personal, null=True, blank=True, on_delete=models.CASCADE, related_name='work')

    def __str__(self):
        return self.institution

class Project(models.Model):

    class ProjectObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(display_project=True)

    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    display_project = models.BooleanField(default=True)

    education = models.ForeignKey(Education, null=True, blank=True, on_delete=models.CASCADE, related_name='projects')
    work = models.ForeignKey(Work, null=True, blank=True, on_delete=models.CASCADE, related_name='projects')

    objects = models.Manager()  # default manager
    project_objs = ProjectObjects()  # custom manager

    def __str__(self):
        return self.name