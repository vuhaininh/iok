# Run the application
```
docker-compose up
```
# Destroy the application
```
docker-compose down
```
# Test
```
docker-compose run --rm backend sh -c "python manage.py test && flake8"
```
# Create Django super user
```
docker-compose run --rm backend sh -c "python manage.py createsuperuser"
```
