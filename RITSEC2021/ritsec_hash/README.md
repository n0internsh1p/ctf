# RITSEC Hash

![Category](https://img.shields.io/badge/Category-Crypto-red.svg?style=for-the-badge)   
![score](https://img.shields.io/badge/Score-250-blue.svg?style=for-the-badge)

*Hmmm.. we found this hash along with a white paper explaining this custom hashing algorithm.*\
*Can you break it for us?*\
*hash : 435818055906*\
*Flag should be submitted as RS{<cracked hash>}*\
*Author: 1nv8rZim*

## Detailed solution

We are asked to crack a hash digest made with a hashing function detailed in the given white paper.
This paper also contains a valid pair (message:digest) mapped by this function.
First we need to implement the hashing algorithm, test it with the valid pair and finally find a message associated with the target digest.

The implementation is pretty straightforward, the major diffculty for me was to understand the meaning of the red squares in the graph, I originally thought they were either bitwise OR or AND operations, so I adjusted the program to test all the possibilities.
Nothing worked so I asked the author if I was going in the right direction and he told me that those red square are in fact addition operations.
With that out of the way I completed the hash function and the test message gave the right value on the first try.

In order to find a valid message I initially created a basic bruteforce loop on messages of lenght 3 and 4, it yiedled quite a lot of message candidate so I figured none of them was the good one.
I remarked that all the valid messages ended with the 'm' character, just like the author's name, so I tested RS{1nv8rZim}, without success.
I proceeded to craft a basic bruteforcing function to test all possible message of an arbitrary length.
This turned out useless as there were lots of candidates and began to take a long time to compute.

However, after giving it some thought, I tried a dictionary attack with the famous "rockyou" wordlist "just in case".
The flag was waiting for me there, not so far from the hunch I had at the beginning.

NB: The hints about the squares being additions and the use of "rockyou" were released the next day.

# Flag

RS{invaderzim}
