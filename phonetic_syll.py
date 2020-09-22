#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:05:57 2019

@author: Cécile Macaire et Ludivine Robert
"""
#from syllabipy.sonoripy import SonoriPy
#import re

ortho_c = ["p", "t", "k", "b", "d", "g", "f", "s", "c", "v", "z", "g", "j", "m", "n", "r", "l", "h"]
ortho_v = ["a", "e", "i", "o", "u", "y", "é", "ê", "ë", "ï", "à", "ù"]
stop_V = ["b", "d", "g"]
stop_U = ["p", "t", "k"]
fric_V = ["v", "z", "Z"]
fric_U = ["f", "s", "S"]
liquids = ["R", "l"]
nasals = ["m", "n", "N", "G"]
semi_vowels = ["w", "j", "8"]
vowels_O = ["a", "e", "i", "u", "o", "y", "E", "9", "2", "O", "*"]
vowels_N = ["@", "1", "5"]

v = ['aa', 'ee', 'ii', 'oo', 'uu', 'yy', 'EE', '99', '22', 'OO', '**', '@@', '11', '55']

syl_cons = stop_V + stop_U + fric_V + fric_U + nasals
syl_vow = vowels_N + vowels_O


def open_input(path):
    input_file = open(path, "r", encoding='utf-8-sig')
    words = []
    transcriptions = []
    for lines in input_file:
        tmp = lines.split()
        words.append(tmp[0])
        transcriptions.append(tmp[1])
    return words, transcriptions


def ortho_VC(l):
    words_VC = []
    for word in l:
        word_VC = ''
        for letter in word:
            if letter in ortho_c:
                word_VC += 'C'
            else:
                word_VC += 'V'
        words_VC.append(word_VC)
    return words_VC


def phon_VC(l):
    trans_VC = []
    for word in l:
        word_VC = ''
        for letter in word:
            if letter in vowels_O:
                word_VC += 'V'
            elif letter in vowels_N:
                word_VC += 'V'
            else:
                word_VC += 'C'
        trans_VC.append(word_VC)
    return trans_VC


def syll_VC(l):
    syll_VC = []
    for word in l:
        word_VC = ''
        for letter in word:
            if letter in vowels_O:
                word_VC += 'V'
            elif letter in vowels_N:
                word_VC += 'V'
            elif letter == '-':
                word_VC += '-'
            else:
                word_VC += 'C'
        syll_VC.append(word_VC)
    return syll_VC


def syllabification(l):
    syllab = []
    for word in l:
        string = ''
        i = 0
        is_add2 = False
        is_add3 = False
        cpt = 0
        for p in word:
            if p in syl_vow:
                cpt += 1
        if cpt == 1:
            string += word
            is_add2 = True
        if not is_add2 and all(a in (syl_cons + liquids + semi_vowels) for a in word[:-1]):
            if word[-1] in syl_vow:
                string += word
                is_add3 = True
        if not is_add3 and not is_add2:
            while i < len(word):
                is_add = False
                if i == 0 and word[i] in (syl_cons + liquids + semi_vowels):
                    if word[i + 1] in (syl_cons + liquids + semi_vowels):
                        string += word[i] + word[i + 1]
                        is_add = True
                        i += 2
                    else:
                        string += word[i]
                        is_add = True
                        i += 1
                if not is_add and i + 5 < len(word):
                    if (word[i] and word[i + 5]) in syl_vow and word[i + 1] not in (syl_vow + liquids + semi_vowels) and \
                            word[i + 2] not in (syl_vow + liquids + semi_vowels) and word[i + 3] not in (
                            syl_vow + liquids + semi_vowels) and word[i + 4] not in (syl_vow + liquids + semi_vowels):
                        string += word[i] + word[i + 1] + '-' + word[i + 2] + word[i + 3] + word[i + 4] + word[i + 5]
                        is_add = True
                        i += 4
                if not is_add and i + 4 < len(word):
                    if (word[i] and word[i + 4]) in syl_vow:
                        if word[i + 1] not in (syl_vow + liquids + semi_vowels) and word[i + 2] not in (
                                syl_vow + liquids + semi_vowels) and word[i + 3] not in (
                                syl_vow + liquids + semi_vowels):
                            string += word[i] + word[i + 1] + '-' + word[i + 2] + word[i + 3] + word[i + 4]
                            is_add = True
                            i += 3
                        elif word[i + 1] not in (syl_vow + liquids + semi_vowels) and word[
                            i + 2] in liquids and word[i + 3] in semi_vowels:
                            string += word[i] + word[i + 1] + '-' + word[i + 2] + word[i + 3] + word[i + 4]
                            is_add = True
                            i += 3
                if not is_add and i + 3 < len(word):
                    if (word[i] and word[i + 3]) in syl_vow:
                        if word[i + 1] not in (syl_vow + liquids + semi_vowels) and word[i + 2] in (
                                liquids + semi_vowels):
                            string += word[i] + '-' + word[i + 1] + word[i + 2] + word[i + 3]
                            is_add = True
                            i += 3
                        elif (word[i + 1] and word[i + 2]) in liquids or (
                                word[i + 1] in liquids and word[i + 2] not in (
                                syl_vow + liquids + semi_vowels)) or (
                                word[i + 1] in semi_vowels and word[i + 1] not in syl_vow) or (
                                (word[i + 1] and word[i + 2]) not in (syl_vow + liquids + semi_vowels)):
                            string += word[i] + word[i + 1] + '-' + word[i + 2] + word[i + 3]
                            is_add = True
                            i += 3
                if not is_add and i + 2 < len(word):
                    if word[i] in syl_vow and word[i + 1] not in syl_vow and word[i + 2] in syl_vow:
                        string += word[i] + '-' + word[i + 1] + word[i + 2]
                        is_add = True
                        i += 2
                if not is_add and i + 1 < len(word):
                    if word[i] in syl_vow and word[i + 1] in syl_vow:
                        string += word[i] + '-' + word[i + 1]
                        is_add = True
                        i += 1
                if not is_add and len(word) - (i + 1) == 0 and word[i - 1] in syl_vow:
                    string += word[i - 1] + word[i]
                    i += 1
                    is_add = True
                if not is_add and len(word) - (i + 1) == 0 and word[i] in (syl_cons+liquids+nasals) and word[i-1] in (syl_cons+liquids+nasals) and word[i-2] in syl_vow:
                    string += word[i - 1] + word[i]
                    i += 1
                    is_add = True
                if not is_add:
                    i += 1
            for i in v:
                if i in string:
                    string = string.replace(i, i[0])
        syllab.append(string)
    return syllab


if __name__ == "__main__":
    words, transcriptions = open_input("Input_File.txt")
    words_VC = ortho_VC(words)
    trans_VC = phon_VC(transcriptions)
    trans_syll= syllabification(transcriptions)
    trans_syll_VC = syll_VC(trans_syll)
    #print(words)
    #print(transcriptions)
    #print(words_VC)
    #print(trans_VC)
    print(syllabification(['apst*nE'] ))
    #print(trans_syll)
    #print(trans_syll_VC)