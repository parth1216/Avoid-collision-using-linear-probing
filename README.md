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
