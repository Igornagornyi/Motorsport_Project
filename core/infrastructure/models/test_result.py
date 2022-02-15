from sqlalchemy import VARCHAR, DATETIME, FLOAT, TEXT, Column

from core.infrastructure.models.base_model import Base


class TestResult(Base):
    __tablename__ = 'test_result'
    __table_args__ = {'extend_existing': True}

    id = Column(VARCHAR(36), primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    result = Column(VARCHAR(30), nullable=False)
    date_created = Column(DATETIME, nullable=False)
    type = Column(VARCHAR(30), nullable=False)
    duration = Column(FLOAT)
    log = Column(TEXT)
    std_error = Column(TEXT)
    std_out = Column(TEXT)
