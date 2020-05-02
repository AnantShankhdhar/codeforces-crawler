from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    sur_name = models.CharField(max_length=100, blank=True)
    
    email = models.CharField(max_length=200,blank=True)

@receiver(post_save,sender=User)

def update_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
class ContestDb(models.Model):
    contest_name=models.CharField(max_length=500)
    date=models.DateField()

class Question(models.Model):
    prob_link = models.CharField(max_length=500, default='')
    prob_level = models.CharField(max_length=1,default='')
    prob_rat = models.IntegerField(default=0)
    expression_parsing = models.BooleanField(default=False)
    fft = models.BooleanField(default=False)
    two_pointers = models.BooleanField(default=False)
    binary_search = models.BooleanField(default=False)
    dsu = models.BooleanField(default=False)
    strings = models.BooleanField(default=False)
    number_theory = models.BooleanField(default=False)
    data_structures = models.BooleanField(default=False)
    hashing = models.BooleanField(default=False)
    shortest_paths = models.BooleanField(default=False)
    matrices = models.BooleanField(default=False)
    string_suffix_structures = models.BooleanField(default=False)
    graph_matchings = models.BooleanField(default=False)
    dp = models.BooleanField(default=False)
    dfs_and_similar = models.BooleanField(default=False)
    meet_in_the_middle = models.BooleanField(default=False)
    games = models.BooleanField(default=False)
    schedules = models.BooleanField(default=False)
    constructive_algorithms = models.BooleanField(default=False)
    greedy = models.BooleanField(default=False)
    bitmasks = models.BooleanField(default=False)
    divide_and_conquer = models.BooleanField(default=False)
    flows = models.BooleanField(default=False)
    geometry = models.BooleanField(default=False)
    math = models.BooleanField(default=False)
    sortings = models.BooleanField(default=False)
    ternary_search = models.BooleanField(default=False)
    combinatorics = models.BooleanField(default=False)
    brute_force = models.BooleanField(default=False)
    implementation = models.BooleanField(default=False)
    sat_2 = models.BooleanField(default=False)
    trees = models.BooleanField(default=False)
    probabilities = models.BooleanField(default=False)
    graphs = models.BooleanField(default=False)
    chinese_remainder_theorem = models.BooleanField(default=False)
    interactive = models.BooleanField(default=False)
    other_tag = models.BooleanField(default=False)
    special_problem = models.BooleanField(default=False)

