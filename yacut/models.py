from datetime import datetime

from yacut import db
from .constants import SITE_URL


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(254), nullable=False)
    short = db.Column(db.String(63))
    timestamp = db.Column(db.DateTime, default=datetime.now())

    @classmethod
    def is_short_exists(cls, short_url):
        return cls.query.filter_by(short=short_url).first() is not None

    def to_dict(self):
        return dict(url=self.original,
                    short_link=f'{SITE_URL}/{self.short}')

    def from_dict(self, data):
        url_dict = {'url': 'original', 'custom_id': 'short'}
        for field in url_dict:
            if field in data:
                setattr(self, url_dict[field], data[field])
