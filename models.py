from sqlalchemy import Column, Integer, DateTime
from database import Base
from datetime import datetime


class Downloads(Base):
    __tablename__ = "Downloads"
    id = Column(Integer, primary_key=True)
    total_num_of_downloads = Column(Integer, nullable=False, default=0)
    windows_no_of_downloads = Column(Integer, nullable=False, default=0)
    linux_no_of_downloads = Column(Integer, nullable=False, default=0)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, total_num_of_downloads=0, windows_no_of_downloads=0, linux_no_of_downloads=0):
        self.total_num_of_downloads = total_num_of_downloads
        self.windows_no_of_downloads = windows_no_of_downloads
        self.linux_no_of_downloads = linux_no_of_downloads
    
    def __repr__(self):
        return f'<Downloads {self.num_of_downloads}>'
    

class Visits(Base):
    __tablename__ = "Traffic"
    id = Column(Integer, primary_key=True)
    num_of_visits = Column(Integer, nullable=False, default=0)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, num_of_visits=0):
        self.num_of_visits = num_of_visits

    def __repr__(self):
        return f'<Visits {self.num_of_visits}>'
    
