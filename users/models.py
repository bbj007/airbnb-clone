from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    
    """ Customer User Model """
    
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    
    GENDER_CHOICES = ( 
        ( GENDER_MALE,"Male" ),
        ( GENDER_MALE,"Female" ),                    
    )
    
    POSITION_SENIOR_DIRECTOR = "부장"
    POSITION_SENIOR_MANAGER = "차장"
    POSITION_MANAGER = "과장"
    POSITION_ASSOCIATE2 = "대리"
    POSITION_ASSOCIATE1 = "사원"
    
    POSITION_CHOICES = (
        ( POSITION_SENIOR_DIRECTOR, "부장"),
        ( POSITION_SENIOR_MANAGER, "차장"),
        ( POSITION_MANAGER, "과장"),
        ( POSITION_ASSOCIATE2, "대리"),
        ( POSITION_ASSOCIATE1, "사원"),
    )

    LANGUAGE_ENGLISH = "EN"
    LANGUAGE_KOREAN = "KR"
    LANGUAGE_CHOICES = ( (LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KRW"
    CURRENCY_CHOICES = ( (LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    photo = models.ImageField(upload_to="photos", null=True, blank=True)
    
    birthdate = models.DateField(null=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True 
    )
    
    """부서코드 테이블 연계"""
    department = models.CharField(max_length=50,null=True)
    
    position = models.CharField(
        choices = POSITION_CHOICES, max_length=10, null=True)
    
    """도로명 적용 어떻게"""
    Address = models.TextField(null=True) 
    jobdesc = models.TextField(default="",blank=True)
    bio = models.TextField(default="",blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True, default=LANGUAGE_KOREAN)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        pass
    
    
