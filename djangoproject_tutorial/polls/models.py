import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)    # Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.
    pub_date = models.DateTimeField("date published")   # The name of each Field instance (e.g. question_text or pub_date) is the field's name, in machine-friendly format. You'll use this value in your Python code, and your database will use it as the column name.
    def __str__(self):                                  # You can give a Field a human-readable name. If a field has a name attribute, Django will use that name in the admin site.
        return self.question_text                       # Some Field classes have required arguments. CharField, for example, requires that you give it a max_length. That's used not only in the database schema, but in validation, as we'll soon see.
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):                   # Each Field instance has a name, which is used to reference it in Django code. This name is the machine-readable name, in lowercase, with underscores, and it's the same name you'll use to refer to the field in Python code.
        now = timezone.now()
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now   # Each Field instance has a name, which is used to reference it in Django code. This name is the machine-readable name, in lowercase, with underscores, and it's the same name you'll use to refer to the field in Python code.
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # Each ForeignKey represents a many-to-one relationship. The ForeignKey field requires a positional argument: the class to which the model is related.
    choice_text = models.CharField(max_length=200)                      # You can also create a recursive relationship – i.e., a relationship to itself. For example, a category can have a parent category that's also a category. In this case, use models.ForeignKey('self', on_delete=models.CASCADE).
    votes = models.IntegerField(default=0)                              # For every field that Django creates, it gives it a column type – e.g., an IntegerField, a CharField, etc. That's what the field.type in the table below represents. You can override the column type using the field's type attribute.
    def __str__(self):                                                  # Each field type, e.g. CharField, IntegerField, etc., has a corresponding Field class (e.g., Char
        return self.choice_text                                         # Field, IntegerField). Each Field class has a number of arguments, e.g., CharField has a max_length argument. That's how you define a database column's type, e.g., VARCHAR(200).