import logging
from collections import namedtuple

import config

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(config.LOG_LEVEL)

QARecord = namedtuple('QARecord', ('id', 'question', 'answer'))


class MemoryStore:
    def __init__(self):
        self._records_by_id = {}
        self._load_fixtures()

    def get_all_records(self):
        return self._records_by_id.values()

    def add_record(self, _id, question, answer):
        self._records_by_id[_id] = QARecord(_id, question, answer)

    def _load_fixtures(self):
        logger.info(f'Loading fixture from {len(config.FIXTURES)} into the data store.')
        for fixture_file in config.FIXTURES:
            with open(fixture_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    record_id, question, answer = line.strip().split(',')
                    self.add_record(int(record_id), question, answer)
                logger.info(f'Loaded {len(lines)} entries from fixture: {fixture_file}.')
