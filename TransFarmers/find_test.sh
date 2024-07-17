#!/usr/bin/env zsh

TEST_DIRS=$(find . -path ./.venv -prune -o -type d -name 'tests' -print)

# mac이면 아래와 같이
source .venv/bin/activate
# window면 아래와 같이
# source .venv/Scripts/activate

for TEST_DIR in $TEST_DIRS; do
  APP_NAME=$(basename $(dirname $TEST_DIR))
  TEST_FILES=$(find $TEST_DIR -type f -name 'test*.py')

  if [ -z "$TEST_FILES" ]; then
    continue
  fi

  APP_TESTS+=("${APP_NAME}.tests")
done

echo "${APP_TESTS[@]}"