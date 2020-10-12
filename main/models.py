from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.db.models import Q, QuerySet, Max, F, Count, Case, When, Exists, OuterRef
from django.utils import timezone
from django.forms.models import model_to_dict
from django.utils.dateformat import format
from django.core.validators import RegexValidator, URLValidator
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime, date, time

# Create your models here.
