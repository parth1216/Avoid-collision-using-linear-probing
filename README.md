# Avoid-collision-using-linear-probing

Collision
While hashing, two or more key points to the same hash index under some modulo M is called as collision.




Linear Probing
Calculate the hash key. key = data % size;

If hashTable[key] is empty, store the value directly. hashTable[key] = data.

If the hash index already has some value, check for next index.

key = (key+1) % size;

If the next index is available hashTable[key], store the value. Otherwise try for next index.

Do the above process till find the space.
=====================================================================================================
INPUT :: input.txt
13
1
6
11
10
15

OUTPUT ::  

(venv) bisag@bisag-Precision-T1700:~/PycharmProjects/test$ python test2.py
input:  ['13', '1', '6', '11', '10', '15']

data 13

data 1

data 6

i= 0
key= 1
!! colision !!

i= 1
key= 2
!! get place !!

data 11

i= 0
key= 1
!! colision !!

i= 1
key= 2
!! colision !!

i= 2
key= 3
!! colision !!

i= 3
key= 4
!! get place !!

data 10

data 15

i= 0
key= 0
!! colision !!

i= 1
key= 1
!! colision !!

i= 2
key= 2
!! colision !!

i= 3
key= 3
!! colision !!

i= 4
key= 4
!! colision !!
output:  [10, 1, 6, 13, 11]
Total collision:  9
