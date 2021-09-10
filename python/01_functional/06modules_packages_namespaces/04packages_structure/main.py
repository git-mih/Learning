import common

for k in common.__dict__.keys():
    if not k.startswith('__'):
        print(f'{k}\t -> {common.__dict__[k]}')

# models   -> <module 'common.models' from '...common\\models\\__init__.py'>
# Posts    -> <class 'common.models.posts.posts.Posts'>
# Post     -> <class 'common.models.posts.post.Post'>
# User     -> <class 'common.models.users.users.User'>

p1 = common.models.users.User() # <common.models.users.users.User object at 0x01>
p2 = common.User()              # <common.models.users.users.User object at 0x02>
