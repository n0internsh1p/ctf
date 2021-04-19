# Follow the Currents

![Category](https://img.shields.io/badge/Category-Crypto-red.svg?style=for-the-badge)

*go with the [flow](./enc)... [Source](source.py)*\
*Author: lamchcl*

## Detailed solution

The objective is to decrypt the "enc" file, encrypted by a stream cipher.
By reading the source file of the algorithm, we understand that the stream cipher is initialized by a two bytes seed from urandom(), that makes 16 bits of entropy, which is very weak.
We can bruteforce it by simulating the outcome of every possible seed and watch for the flag, which is guaranteed to be present by assert.

## Flag

actf{low_entropy_keystream}
