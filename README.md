# Django Rest Framework App to fetch bank details
##### This app uses data from https://github.com/snarayanank2/indian_banks and builds REST api to fetch the details. For authentication it uses JWT.
##### 1. Hosting URL - 
>> https://pacific-scrubland-56756.herokuapp.com
>> Deployed the app using Heroku.
##### 2. Understanding the project
First step is to understand the building blocks of the project. There are two apps in the project - 
>a. banks - it is all realed to bank branches!
>>1. Models - There are two models namely, BankName which includes the bank names and its id as a primary key and BankData in which resides the details of every single bank branch present acorss the country, importantly here the field bank is a foreign key to BankData table.
>>2. Serializer - Two serializers are present, one is BankSerializer which inherits ModelSerializer and renders BankName model. Second one is BankBranchSerailizer whic also inherits ModelSerializer an renders BankData model, foreign key in the model is mapped using PrimaryKeyRelatedField.
>>3. Views - First view, which is BankUsingIFSC, helps in fetching the bank branch with the given ifsc code. It uses generic view ListAPIView. Second one also uses the same generic view, which is BankListUsingNameCity, and returns bank branches list filtered by banks name & city name.
>>4. Urls - Contains two APIs, one which uses BankUsingIFSC view and the other one BankListUsingNameCity. Details of which we'll dicuss later.

>b. user - all related to creating a user!
>>1. Serializer - Uses django User model to create a user. Uses only three fields - username, email, password with unique values in each.
>>2. Views - UserCreate view uses generic CreateAPIView to generate a user.
>>3. Urls - API for signup!
##### 3. JWT Authentication
Authentication is performed using https://github.com/davesque/django-rest-framework-simplejwt. First installed django-rest-framework-simplejwt, then included in settings.py - 
```
  'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
```
Also, included the views, provided by the package, in root urls.py - TokenObtainPairView, TokenRefreshView, TokenVerifyView. TokenObtainPairView also works as a login which provides with access and refresh tokens.
```
  urlpatterns = [
    ...
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
```
##### 4. Steps to reproduce APIs
> a. Create user and token!
```
  # Let's ask Tom Hanks to join
  curl -X POST \
  https://pacific-scrubland-56756.herokuapp.com/api/users/ \
  -H 'content-type: application/json' \
  -d '{
	"username": "Tom_Hanks",
  	"email": "tom@example.com",
	"password": "abcd1234"
}'
```
>> Let's create a token for him
```
  curl -X POST \
  https://pacific-scrubland-56756.herokuapp.com/api/login/ \
  -H 'content-type: application/json' \
  -d '{
	"username": "Tom_Hanks",
	"password": "abcd1234"
}'

# response
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU2NzgwMTQ0NCwianRpIjoiNGEzODFjYjM2ZjRjNDBkMGFjOTkzYmEyNjIxMTBkNTYiLCJ1c2VyX2lkIjozfQ.PMEHnnkjtSL2-X9HihO1Btjg2R5r9u4c-hwFvjnXcxA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3ODAxNDQ0LCJqdGkiOiI1NDlmOTRjMDNhOTc0Njg5OTcyMGNiZTllZjM1NTQ1YSIsInVzZXJfaWQiOjN9.OLOgcRGOtK035u1liVyqC-gRDthy5MEwNzeSWiDe-mA"
}

```
> b. Fetch bank branch given branch IFSC code
>> The api which makes it work  - /api/banks/ifsc/
```
  #curl
  curl -X GET \
  https://pacific-scrubland-56756.herokuapp.com/api/banks/ALLA0210513/ \
  -H 'authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3ODAxNDQ0LCJqdGkiOiI1NDlmOTRjMDNhOTc0Njg5OTcyMGNiZTllZjM1NTQ1YSIsInVzZXJfaWQiOjN9.OLOgcRGOtK035u1liVyqC-gRDthy5MEwNzeSWiDe-mA'
```
> c. Fetch bank branches given bank name and city name
>> Api mentioned in the project - /api/banks/bank_name/city/
```
  curl -X GET \
  https://pacific-scrubland-56756.herokuapp.com/api/banks/ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED/MUMBAI/ \
  -H 'authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3ODAxNDQ0LCJqdGkiOiI1NDlmOTRjMDNhOTc0Njg5OTcyMGNiZTllZjM1NTQ1YSIsInVzZXJfaWQiOjN9.OLOgcRGOtK035u1liVyqC-gRDthy5MEwNzeSWiDe-mA'
```
With limit and offset
```
  curl -X GET \
  'https://pacific-scrubland-56756.herokuapp.com/api/banks/ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED/MUMBAI/?limit=2&offset=5' \
  -H 'authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3ODAxNDQ0LCJqdGkiOiI1NDlmOTRjMDNhOTc0Njg5OTcyMGNiZTllZjM1NTQ1YSIsInVzZXJfaWQiOjN9.OLOgcRGOtK035u1liVyqC-gRDthy5MEwNzeSWiDe-mA'
```

