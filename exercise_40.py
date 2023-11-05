#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:26:51 2020

@author: henry
"""

class MyStuff(object):
    
    def __init__(self):
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I AM CLASSY APPLES")
        
        
thing = MyStuff()
thing.apple()
print(thing.tangerine)

class Song(int):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["happy birthday to you",
                   "I don't want to get sued",
                   "so I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

new_lyrics = ["here we come", "we're fifty strong", "and fifty frenchmen", "can't be wrong"]

mob_song = Song(new_lyrics)

mob_song.sing_me_a_song()
messed_up = '\n'.join(mob_song.lyrics)
print('try this:', messed_up)

