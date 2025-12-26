import time
import json


def timeit(func):
  def wrapper(*args, **kwargs):
    t0 = time.time()
    r = func(*args, **kwargs)
    t1 = time.time()
    return r, t1 - t0
  return wrapper


def save_json(path, obj):
  with open(path, 'w', encoding='utf-8') as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)