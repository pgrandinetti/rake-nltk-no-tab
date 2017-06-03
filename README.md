# rake-nltk-no-tab

The *Rapid Automatic Keyword Extraction* (**RAKE**) algorithm, is widely known and used techique for **keyword extraction** from a single document. Its main features are:

- non supervision (no learning phase),
- language independency,
- domain independency.

## Background

The RAKE is part of the Natural Language Processing (**NLP**) theory, and it is often chosen for its simplicity and efficiency. The algorithm itself is formally described in the paper *Automatic keyword extraction from individual documents*, by Stuart Rose,
Dave Engel, Nick Cramer and Wendy Cowley, which can also be found in the book [*Text mining applications and theory*](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-0470749822.html), by M.W. Berry.

## Motivation and related works

Several implementation of the RAKE can be found in the internet, also using the [NLTK](http://www.nltk.org/) python package. However in our opinion, such implementations hide details and overcomplexify the algorithm, which is instead to be intended as very simple. We show here that it can implemented in just 15 lines of python code, without even indenting one (''no-tab'')! Variables are named as in the above mentioned paper, thus the implementation should be easy to follow.

### Comments

This simple implementation proved to give the same result of others available in the internet. Of course, efficency was not targeted, in favour of clarity of the implementation.

### Requirements
Python3 and NLTK.

## Usage and output
Run it as:

```
python3 rake-nltk-no-tab/rake.py
```

Output

|**Keyword**                    |**Score**|
|-------------------------------|:-------:|
|minimal generating sets        |8.7      |
|linear diophantine equations   |8.5      |
|minimal supporting set'        |7.7      |
|minimal set                    |4.7      |
|linear constraints             |4.5      |
|natural numbers                |4.0      |
|strict inequations             |4.0      |
|nonstrict inequations          |4.0      |
|upper bounds                   |4.0      |
|mixed types                    |3.7      |
|corresponding algorithms       |3.5      |
|considered types               |3.2      |
|set                            |2.0      |
|types                          |1.7      |
|considered                     |1.5      |
|algorithms                     |1.5      |
|compatibility                  |1.0      |
|systems                        |1.0      |
|criteria                       |1.0      |
|system                         |1.0      |
|components                     |1.0      |
|solutions                      |1.0      |
|construction                   |1.0      |
|given                          |1.0      |
|constructing                   |1.0      |
|used                           |1.0      |
|solving                        |1.0      |

## Contributors

The code has been entirely written by Pietro Grandinetti.
