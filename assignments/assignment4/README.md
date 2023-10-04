## Assignment 4: BWT and Modmers
Assignment Date: Wednesday, October 4, 2023 <br>
Due Date: Wednesday, October 11, 2023 @ 11:59pm <br>

### Assignment Overview

In this assignment you will implement the BWT and modmers. These exercises can be computed in any programming language, although we recommend python (or C++, Java, or Rust).

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


### Question 3. Randomers and modimizers [25 pts]

- 4a. Extract the 1Mbp sequence in chr22 from position 20,000,000 to 21,000,000 [Hint use `samtools faidx` with [https://schatz-lab.org/appliedgenomics2023/assignments/assignment1/chr22.fa.gz](https://schatz-lab.org/appliedgenomics2023/assignments/assignment1/chr22.fa.gz)]. From this sequence pick 1000 kmers (k=21) with uniform random probability (without replacement). Make sure to record their position (just record the left most position). Note there are 1M-21+1 possible kmers to pick from. Make a plot of the location of these selected kmers: x-axis = genomic position, y-axis = vertical line from (x,0) to (x,1)

- 4b. Compute the distances between the selected kmers: Sort the starting positions of the kmers selected in 4a, and then substract consecutive positions in the sorted list. Compute the mean and standard deviation of the distances between kmers. Plot a histogram of the distances (x-axis=distance, y-axis=density). 

- 4c. Recall that a modimizer is a kmer such that `hash(kmer) % M == 0`. For this question you should use the default `hash()` function in your programming language. Scan the 1Mbp sequence from 4a, and output the modimizers and their postions using `M=1000`. How many modimizers are reported? Use the code from 4a and 4b to plot the locations of the modimizers and a histogram of the distance between them. What is the mean and standard deviation of the distance between the modimizers? How does the distribution in the space between modimizers compare to the randomized selections from 4a and 4b.

- 4d. Recall the Jaccard coefficient between sets A and B is `|A intersect B| / |A union B|` Extract the 1Mbp sequence in chr22 starting at position 21,000,000 to 22,000,000. Use the code from 4d to compute the modimizers using `M=1000`. Now compute the Jaccard coefficient between these sets. To compute the set union and set intersect, we recommend storing the kmers from A in a dictionary, and then scanning through the kmers in B to check whether they are already in the dictionary.

- 4e. Compute the Jaccard coefficient between chr22:20M-21M and chr22:21M-22M using modimizers using `M=100` and `M=10`. In a few sentences, reflect on how the values compare


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
