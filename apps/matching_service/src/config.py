import glob
import os

_FIXTURES_GLOB_PATTERN = os.path.join(os.environ['FIXTURES_DIR'], '*.csv')
FIXTURES = glob.glob(_FIXTURES_GLOB_PATTERN)
MATCHING_MIN_SCORE = float(os.environ['MATCHING_MIN_SCORE'])
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
