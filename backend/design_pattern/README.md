# How to run client code of design pattern
```
docker-compose run --rm backend sh -c "python manage.py migrate"
docker-compose run --rm backend sh -c "python manage.py shell"
from design_pattern.patterns.creational import factory_method
factory_method.main()
```
