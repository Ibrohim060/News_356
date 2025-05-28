from django.db.models import manager

class CategoryManager(manager.Manager):
    def get_category(self, category_name):
        try:
            return self.get(name__icontains=category_name)
        except Exception as e:
            print(e)
            return None
        
        
        


