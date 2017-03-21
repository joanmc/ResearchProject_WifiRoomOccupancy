# Reference: Franklin, Simeon,'Tutorial: Using Django's Multiple Database Support',(2012) [Web] https://newcircle.com/s/post/1242/django_multiple_database_support
class OccupantsRouter(object):  
    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'occupants':
            return 'occupantsdb'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'occupants':
            return 'occupantsdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'occupants' and obj2._meta.app_label == 'occupants':
            return True
        elif 'occupants' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'occupantsdb' or model._meta.app_label == "occupants":
            return False 
        else: 
            return True
