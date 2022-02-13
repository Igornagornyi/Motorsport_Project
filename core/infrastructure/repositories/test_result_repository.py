from datetime import datetime

from typing import List

from core.result import Result

from base_repository import BaseRepository

from core.infrastructure.models.test_result import TestResult


class TestResultRepository(BaseRepository):
    def save_all(self, test_results: List[Result]) -> None:
        report = []
        for test_result in test_results:
            report.append(TestResult(**test_result.to_dict()))
        self.session.add_all(report)
