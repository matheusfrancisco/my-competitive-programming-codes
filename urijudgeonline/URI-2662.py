# -*- coding: utf-8 -*-

PATTERN = {2, 4, 5, 7, 9, 11, 12}

notes = ['do','do#','re','re#','mi','fa','fa#','sol','sol#','la','la#','si', 'desafinado']

def majors():
    for tone in range(12):
        yield set(((tone + shift) % 12) for shift in PATTERN)


def song():
    n = int(input())
    while n > 0:
        yield (int(input()) - 1) % 12
        n -= 1


song_notes = set(song())


def is_valid_for(major):
    return all(notes in major for notes in song_notes)

res = 0
for major in majors():
  if is_valid_for(major):
    break
  res += 1

print(notes[res])
