from django.db import models

class Post(models.Model):
    
    u_id = models.TextField()
    name = models.TextField()
    symbol = models.TextField()
    rank = models.TextField()
    price_usd = models.TextField()
    price_btc = models.TextField()
    volume_usd_24h = models.TextField()
    market_cap_usd = models.TextField()
    available_supply = models.TextField()
    total_supply = models.TextField()
    max_supply = models.TextField()
    percent_change_1h = models.TextField()
    percent_change_24h = models.TextField()
    percent_change_7d = models.TextField()
    images = models.TextField()
    last_updated = models.TextField()
    history = models.TextField()
 

    def __str__(self):
        return self.name

