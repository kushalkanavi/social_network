from django.shortcuts import render, redirect
from django.views import View

from myApp.models import UserProfile, UserFriends
from .forms import UserProfileForm
from django.contrib.auth.models import User
import random

from django.db.models import Q, F
from django.contrib import messages
import crypt


class Main(View):
    def get(self, request, *args, **kwargs):
        userform = UserProfile.objects.filter(User=request.user.id)
        if userform.count() >= 1:
            form = UserProfileForm(instance=UserProfile.objects.get(User=request.user.id))
        else:
            form = UserProfileForm()

        recommendation_list = recommendation(request.user.id)

        data = UserFriends.objects.filter(user=request.user.id).values(id=F('user__user_profile_id'),
                                                                       firstname=F('friend_user__firstname'),
                                                                       lastname=F('friend_user__lastname'),
                                                                       age=F('friend_user__age'),
                                                                       location=F('friend_user__location'),
                                                                       interests=F('friend_user__interests'),
                                                                       photo=F('friend_user__photo'))

        context = {
            'form': form,
            'data': data,
            'recommendation': recommendation_list
        }

        return render(request, 'myApp/main.html', context)


class Create_User(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        for user in users:

            UserProfile.objects.create(
                firstname=user.first_name,
                lastname=user.last_name,
                age=random.randrange(20, 80),
                gender='Others',
                location='US',
                photo='basic_profile_photo/others.png',
                interests=['Walking', 'Listening', 'Volunteer Work', 'Painting', 'Reading'],
                User=user
            )

        random_first_name_girl = ['OLIVIA', 'RUBY', 'EMILY', 'GRACE', 'JESSICA', 'CHLOE', 'SOPHIE', 'LILY', 'AMELIA',
                                  'EVIE', 'MIA', 'ELLA', 'CHARLOTTE', 'LUCY', 'MEGAN', 'ELLIE', 'ISABELLE', 'ISABELLA',
                                  'HANNAH', 'KATIE', 'AVA', 'HOLLY', 'SUMMER', 'MILLIE', 'DAISY', 'PHOEBE', 'FREYA',
                                  'ABIGAIL', 'EVA',
                                  'POPPY', 'ERIN', 'EMMA', 'MOLLY', 'IMOGEN', 'AMY', 'JASMINE', 'ISLA', 'SCARLETT',
                                  'LEAH',
                                  'SOPHIA', 'ELIZABETH', 'BROOKE', 'MATILDA', 'CAITLIN', 'KEIRA', 'ALICE', 'LOLA',
                                  'LILLY',
                                  'AMBER', 'ISABEL']

        random_first_name_boy = ['JACK', 'OLIVER', 'THOMAS', 'HARRY', 'JOSHUA', 'ALFIE', 'CHARLIE', 'DANIEL', 'JAMES',
                                 'WILLIAM', 'SAMUEL', 'GEORGE', 'JOSEPH', 'LEWIS', 'ETHAN', 'MOHAMMED', 'DYLAN',
                                 'BENJAMIN',
                                 'ALEXANDER', 'JACOB', 'RYAN', 'LIAM', 'JAKE', 'MAX', 'LUKE', 'TYLER', 'CALLUM',
                                 'MATTHEW',
                                 'JAYDEN', 'OSCAR', 'ARCHIE', 'ADAM', 'RILEY', 'HARVEY', 'HARRISON', 'LUCAS',
                                 'MUHAMMAD',
                                 'HENRY', 'ISAAC', 'LEO', 'CONNOR', 'EDWARD', 'FINLEY', 'LOGAN', 'NOAH', 'CAMERON',
                                 'ALEX',
                                 'OWEN', 'RHYS', 'NATHAN']

        random_last_name = ['Mills', 'Wiggins', 'Lewis', 'Bowers', 'Drake', 'Ritter', 'Robinson', 'Combs', 'Romero',
                            'Pearson', 'Fisher', 'Humphrey', 'Walters', 'Clayton', 'Reynolds', 'Leon', 'Maddox',
                            'Davila', 'Mcdowell', 'Christian', 'Morse', 'Hart', 'Fitzgerald', 'Green', 'Clark', 'Lowe',
                            'Shaw', 'Reese', 'Yang', 'Collins', 'Decker', 'Cobb', 'Atkins', 'Cisneros', 'Braun',
                            'Giles',
                            'Weiss', 'Henry', 'Riddle', 'Davidson', 'Vaughan', 'Bowman', 'Oneal', 'Estes', 'Lane',
                            'Roman',
                            'Gillespie', 'Stewart', 'Bryant', 'Melton', 'Mckinney', 'Cervantes', 'Estrada', 'Mcpherson',
                            'Lindsey', 'Krause', 'Fritz', 'Mayer', 'Mcdaniel', 'Ho', 'Beck', 'Rojas', 'Velasquez',
                            'Smith',
                            'Harrison', 'Stout', 'Randall', 'Davies', 'Phelps', 'Shannon', 'Liu', 'Archer', 'Padilla',
                            'Camacho', 'Clay', 'Simon', 'Wise', 'Little', 'Ashley', 'Love', 'Wiley', 'Reyes', 'Manning',
                            'Zimmerman', 'Cummings', 'Cantu', 'Rubio', 'Wells', 'Serrano', 'Mann', 'West', 'Daugherty',
                            'Beard', 'Hanson', 'Paul', 'Adams', 'Ball', 'Landry', 'Hickman', 'Stone']

        random_location = ['Washington, US', 'Springfield, US', 'Franklin, US', 'Greenville, US', 'Bristol, US',
                           'Clinton, US', 'Fairview, US', 'Salem, US', 'Madison, US', 'Georgetown, US']

        random_interest = ['Walking', 'Exercise', 'Running', 'Tennis', 'Bicycling', 'Swimming', 'Skiing', 'Golf',
                           'Team Sports', 'Playing Music', 'Listening Music', 'Traveling', 'Fishing', 'hunting',
                           'Community work', 'Church Activities', 'Volunteer Work', 'Painting', 'Dancing', 'Reading',
                           'Writing', 'Gardening', 'Animal Care']

        count = 1
        while count <= 10000:
            if count % 3 == 0:
                firstname = random.choice(random_first_name_girl)
                gender = 'Female'
                photo = 'basic_profile_photo/girl.jpg'
            elif count % 3 == 1:
                firstname = random.choice(random_first_name_boy)
                gender = 'Male'
                photo = 'basic_profile_photo/boy.jpg'
            elif count % 3 == 2:
                firstname = random.choice(random_first_name_boy) + ' ' + random.choice(random_first_name_girl)
                gender = 'Others'
                photo = 'basic_profile_photo/others.png'

            lastname = random.choice(random_last_name)
            location = random.choice(random_location)
            interest = list()
            interest_count = 1

            while interest_count <= 5:
                interest.append(random.choice(random_interest))
                interest_count = interest_count + 1

            user = User.objects.create_user(
                username=firstname + lastname+str(count),
                email=firstname + lastname + '@demo.com',
                password=crypt.crypt(firstname + lastname)
            )

            UserProfile.objects.create(
                firstname=firstname,
                lastname=lastname,
                age=random.randrange(20, 80),
                gender=gender,
                location=location,
                photo=photo,
                interests=interest,
                User=user
            )
            count = count + 1
        return redirect('social:main')


class Create_Connection(View):
    def get(self, request, *args, **kwargs):
        users = UserProfile.objects.all()
        for user in users:
            count = 1
            while count <= 3:

                UserFriends.objects.create(
                                    user=user,
                                    friend_user=random.choice(users)
                )
                count = count + 1

        return redirect('social:main')


class saveProfile(View):
    def post(self, request, *args, **kwargs):
        form = UserProfileForm(self.request.POST, self.request.FILES,
                               instance=UserProfile.objects.get(user_profile_id=kwargs['id']))
        if form.is_valid():
            form.save()

        return redirect('social:main')


def friendSearch(request):
    if request.method == 'POST':
        srch = request.POST['search']

        if srch:
            match = UserProfile.objects.filter(Q(firstname__icontains=srch) | Q(lastname__icontains=srch))

            if match:
                userform = UserProfile.objects.filter(User=request.user.id)
                if userform.count() >= 1:
                    form = UserProfileForm(instance=UserProfile.objects.get(User=request.user.id))
                else:
                    form = UserProfileForm()

                recommendation_list = recommendation(request.user.id)

                data = UserFriends.objects.filter(user=request.user.id).values(id=F('user__user_profile_id'),
                                                                               firstname=F('friend_user__firstname'),
                                                                               lastname=F('friend_user__lastname'),
                                                                               age=F('friend_user__age'),
                                                                               location=F('friend_user__location'),
                                                                               interests=F('friend_user__interests'),
                                                                               photo=F('friend_user__photo'))

                context = {
                    'srch': match,
                    'form': form,
                    'data': data,
                    'recommendation': recommendation_list
                }
                return render(request, 'myApp/main.html', context)
            else:
                messages.error(request, 'No Result Found.')

        else:
            return redirect('social:main')

    return redirect('social:main')


def recommendation(user):
    users = UserFriends.objects.filter(user__User=user)
    recommendation_list = list()
    for user in users:
        friends = UserFriends.objects.filter(user=user.friend_user)
        for friend in friends:
            recommendation_list.append({
                'name': friend.friend_user.firstname+' '+friend.friend_user.lastname,
                'age': friend.friend_user.age,
                'location': friend.friend_user.location,
                'interests': friend.friend_user.interests
            })
        age_friends = UserFriends.objects.filter(user__age=user.user.age)
        for friend in age_friends:
            recommendation_list.append({
                'name': friend.friend_user.firstname+' '+friend.friend_user.lastname,
                'age': friend.friend_user.age,
                'location': friend.friend_user.location,
                'interests': friend.friend_user.interests
            })

    # print(recommendation_list)

    return recommendation_list
