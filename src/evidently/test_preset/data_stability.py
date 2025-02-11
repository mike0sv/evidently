from typing import List
from typing import Optional

from evidently.base_metric import InputData
from evidently.test_preset.test_preset import TestPreset
from evidently.tests import TestAllColumnsShareOfMissingValues
from evidently.tests import TestCatColumnsOutOfListValues
from evidently.tests import TestColumnsType
from evidently.tests import TestNumberOfColumns
from evidently.tests import TestNumberOfRows
from evidently.tests import TestNumColumnsMeanInNSigmas
from evidently.tests import TestNumColumnsOutOfRangeValues
from evidently.utils.data_operations import DatasetColumns


class DataStabilityTestPreset(TestPreset):
    """
    Data Stability tests.

    Contains tests:
    - `TestNumberOfRows`
    - `TestNumberOfColumns`
    - `TestColumnsType`
    - `TestAllColumnsShareOfMissingValues`
    - `TestNumColumnsOutOfRangeValues`
    - `TestCatColumnsOutOfListValues`
    - `TestNumColumnsMeanInNSigmas`
    """

    columns: Optional[List[str]]

    def __init__(
        self,
        columns: Optional[List[str]] = None,
    ):
        super().__init__()
        self.columns = columns

    def generate_tests(self, data: InputData, columns: DatasetColumns):
        return [
            TestNumberOfRows(),
            TestNumberOfColumns(),
            TestColumnsType(),
            TestAllColumnsShareOfMissingValues(columns=self.columns),
            TestNumColumnsOutOfRangeValues(columns=self.columns),
            TestCatColumnsOutOfListValues(columns=self.columns),
            TestNumColumnsMeanInNSigmas(columns=self.columns),
        ]
