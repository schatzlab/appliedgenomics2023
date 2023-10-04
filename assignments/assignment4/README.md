## Assignment 4: BWT and Modimizers
Assignment Date: Wednesday, October 4, 2023 <br>
Due Date: Wednesday, October 11, 2023 @ 11:59pm <br>

### Assignment Overview

In this assignment you will implement the BWT and modimizers. These exercises can be computed in any programming language, although we recommend python (or C++, Java, or Rust). R is generally inefficient at string processing unless you take great care.

As a reminder, any questions about the assignment should be posted to [Piazza](https://piazza.com/jhu/fall2023/600449600649).


### Question 1. BWT Encoding [25 pts]

In the language of your choice, implement a BWT encoder and encode the string below. Faster (Linear time) methods exist for computing the BWT, although for this assignment you can use the simple method based on standard sorting techniques. Your solution does *not* need to be an optimal algorithm and can use O(n^2) space and O(n^2 lg n) time. 

Here is the recommended pseudo code (make sure to submit your code as well as the encoded string):

```
computeBWT(string s)
  ## add the magic end-of-string character
  s = s + "$"
 
  ## build up the BWM from the cyclic permutations
  ## note the ith cyclic permutation is just "s[i..n] + s[0..i]"
  rows = []
  for (i = 0; i < length(s); i++)
    rows.append(cyclic_permutation(s, i))

  ## just use the builtin sort command to sort the cyclic permutations
  sort(rows)

  ## now extract the last column
  bwt = ""
  for (i = 0; i < length(s); i++)
    bwt += substr(rows[i], length(s), 1)
  return bwt
```

String to encode:
```
I_am_fully_convinced_that_species_are_not_immutable;_but_that_those_belonging_to_what_are_called_the_same_genera_are_lineal_descendants_of_some_other_and_generally_extinct_species,_in_the_same_manner_as_the_acknowledged_varieties_of_any_one_species_are_the_descendants_of_that_species._Furthermore,_I_am_convinced_that_natural_selection_has_been_the_most_important,_but_not_the_exclusive,_means_of_modification.
```


### Question 2. BWT Decoder [25 pts]

In the language of your choice, implement a BWT decoder and decode the string below. 

One of the essential properties of the BWT is that it can be decoded back into the source text without any other additional information. This is accomplished by iteratively applying the Last-First property starting with the first character of the BWT until reaching the end of string character `'$'`. The Last-First property states there is an equivalence between the ith occurrence of a character in the first column and the ith occurrence of that character in the last column. This equivalence can be evaluated by counting how many occurrences of a character are present in the BWT string (the last column of the BWM) or by counting characters in the first column (which you will have to determine from the BWT itself). Again, faster methods exist (the FM-index) to determine the rank of each character but you can just count it explicitly here.

The pseudocode for decoding the string is as follows:

```
decodeBWT(String bwt) 
  firstCol = makeFirstColumn(bwt)
  text = ""
  
  ## By construction, '$' always starts the zeroth row
  row = 0;
  while (bwt.charAt(row) != '$')
      text.append(bwt.charAt(row));
      row = applyLF(firstCol, bwt.charAt(row), rank(bwt, row));
  
  return reverse(text)
```

String to decode:
```
.uspe_gexr_______$..,e.orrs,sdddeedkdsuoden-tf,tyewtktttt,sewteb_ce__ww__h_PPsm_u_naseueeennnrrlmwwhWcrskkmHwhttv_no_nnwttzKt_l_ocoo_be___aaaooaAakiiooett_oooi_sslllfyyD__uouuueceetenagan___rru_aasanIiatt__c__saacooor_ootjeae______ir__a
```

Hint: use your sourcecode from Q1 to debug Q2. Also start with simple strings like GATTACA or your own name.


### Question 3. Randomers, modimizers, minimizers, and minhash [50 pts]

For these questions you will need to extract to segments of chr22 [Hint use `samtools faidx` with [https://schatz-lab.org/appliedgenomics2023/assignments/assignment1/chr22.fa.gz](https://schatz-lab.org/appliedgenomics2023/assignments/assignment1/chr22.fa.gz).

Recall the Jaccard coefficient between sets A and B is `|A intersect B| / |A union B|`. To compute the set union and set intersect, we recommend storing the kmers (modimizers, minhashes, minimizers) from A in a dictionary, and then scanning through the kmers in B to check whether they are already in the dictionary. As you process the kmers in A and B, just keep track of how many there are total and how many are shared between A and B.

- 3a. Extract the 1Mbp sequence in chr22 from position 20,000,000 to 21,000,000. Separately extract the 1Mbp sequence in chr22 from position 21,000,000 to 22,000,000 [Hint: just show the commands you ran]

#### Randomers

- 3b. From the chr22:20M-21M sequence, pick 1000 kmers (k=21) with uniform random probability (without replacement). Output both the position and the kmer starting at this position (just record the left most position). Note there are 1M-21+1=999,980 possible kmers to pick from. From the output file, make a plot of the locations of these selected kmers: x-axis = genomic position, y-axis = vertical line from (x,0) to (x,1)

- 3c. Compute the distances between the selected kmers: Sort the starting positions of the kmers selected in 3b, and then substract consecutive positions in the sorted list. Compute the mean and standard deviation of the distances between kmers. Plot a histogram of the distances (x-axis=distance, y-axis=density). 

#### Modimizers

Recall that a `modimizer` is a kmer such that `hash(kmer) % M == 0`. For this question you should use the default `hash()` function in your programming language (see below). 

- 3d. Scan the chr22:20M-21M sequence from 3b, and output the modimizers and their postions using `M=1000`. How many modimizers are reported? Use the code from 3c to plot a histogram of the distance between them and the mean & standard deviation between them. In a few sentences, reflect on how does the distribution in the space between modimizers compare to the randomized selections from 3c. [Hint you may want to use the code from 3b to inspect the positions]

- 3e. Use the code from 3d to compute the modimizers using `M=1000` for chr22:21M-22M. Compute the Jaccard coefficient between the modimizers in chr22:20M-21M and chr22:21M-22M. 

- 3f. Compute the Jaccard coefficient between chr22:20M-21M and chr22:21M-22M using modimizers using `M=100` and `M=10`. In a few sentences, reflect on how the values compare to `M=1000`

#### Minhash

Recall minhash is computed as the N smallest hash values computed from the kmers in the string. [Hint: compute the hash value of every kmer in the sequence, then sort those values to find smallest 1000 values for `N=1000`]

- 3g. Compute the minhash values for chr22:20M-21M using N=1000 and output the position and kmer sequence at those positions. Using your code from 3c, plot the histogram of the distances between the selected elements, and compute their mean and standard devaiation. How does this distribution compare to the the spacing of modimizers or randomers?

- 3h. Compute the Jaccard coefficient between chr22:20M-21M and chr22:21M-22M using minhash using `N=1000`, `N=100` and `N=10`. In a few sentences, reflect on how the values compare to each other

#### Minimizers [Bonus 10pts]

Recall `(w, k)-mimimizers` are the set of k-mers that have minimal value within each posible window of size `w` along a sequence. [Hint: use a nested for loop to consider every window, and then within each window, extract every possible kmer & sort]

- 3i. Compute the (1000,21)-minimizer values for chr22:20M-21M and output the position and kmer sequence at those positions.  Using your code from 3c, plot the histogram of the distances between the selected elements, and compute their mean and standard devaiation. How does this distribution compare to the the spacing of modimizers or randomers or minhash?

- 3j. Compute the Jaccard coefficient between chr22:20M-21M and chr22:21M-22M using (1000,21), (100,21), and (31,21) -minimizers. In a few sentences, reflect on how the values compare to each other


#### Comparison

- 3k. In a few sentences reflect on the properties of the different sketching approaches. Be sure to comment on the relative spacing of selected kmers, the Jaccard coefficients computed, and the relative ease/difficulty of implementing. [If you did not implement minimizers, you should still comment on randomers, modimizers, and minhash]



### Packaging

The solutions to the above questions should be submitted as a single PDF document that includes your name, email address, and all relevant figures (as needed). If you use ChatGPT for any of the code, also record the prompts used. Submit your solutions by uploading the PDF to [GradeScope](https://www.gradescope.com/courses/587880), and remember to select where in your submission each question/subquestion is. The Entry Code is: JK5VB4. 

If you submit after this time, you will use your late days. Remember, you are only allowed 4 late days for the entire semester!



### Resources


#### Python

Python `hash()` function: 

- [https://docs.python.org/3/library/functions.html?highlight=hash#hash](https://docs.python.org/3/library/functions.html?highlight=hash#hash)

- [https://www.w3resource.com/python/built-in-function/hash.php](https://www.w3resource.com/python/built-in-function/hash.php)

- Make sure to set the [PYTHONHASHSEED](https://docs.python.org/3/reference/datamodel.html#object.__hash__) so you will get the same results each time you run your code.


#### C++

C++ `hash<std:string>`:

- [https://stackoverflow.com/questions/8029121/how-to-hash-stdstring](https://stackoverflow.com/questions/8029121/how-to-hash-stdstring)


#### Java

`String.hashCode()`:

- [https://www.tutorialspoint.com/java/java_string_hashcode.htm](https://www.tutorialspoint.com/java/java_string_hashcode.htm)

#### R

`digest::digest2int()`

- [https://www.rdocumentation.org/packages/digest/versions/0.6.29/topics/digest2int](https://www.rdocumentation.org/packages/digest/versions/0.6.29/topics/digest2int)


#### Other languages

Post to piazza for recommendations
