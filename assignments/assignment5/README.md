## Assignment 5: Bedtools and RNA-seq
Assignment Date: Wednesday October 18, 2023 <br>
Due Date: Wednesday October 25 2023 @ 11:59pm <br>

### Assignment Overview

In this assignment you will explore the capabiltiies of bedtools, plus a key couple of aspects of RNA-seq (with a small introduction to clustering). For this assignment, you will have to generate some visualizations - we recommend R or Python, but use a language you are comfortable with! 

 **Make sure to show your work/code in your writeup!**

As a reminder, any questions about the assignment should be posted to [Piazza](https://piazza.com/jhu/fall2023/600449600649).

#### Question 1. De novo mutation analysis [20 pts]

For this question, we will be focusing on the de novo variants identified in this paper:<br>
[http://www.nature.com/articles/npjgenmed201627](http://www.nature.com/articles/npjgenmed201627)

Download the de novo variant positions from here (Supplementary Table S4):<br>
[https://github.com/schatzlab/appliedgenomics2023/blob/main/assignments/assignment4/41525_2016_BFnpjgenmed201627_MOESM431_ESM.xlsx?raw=true](https://github.com/schatzlab/appliedgenomics2022/blob/main/assignments/assignment4/41525_2016_BFnpjgenmed201627_MOESM431_ESM.xlsx?raw=true)

Download the gene annotation of the human genome here: <br>
[https://ftp.ensembl.org/pub/release-87/gff3/homo_sapiens/Homo_sapiens.GRCh38.87.gff3.gz](https://ftp.ensembl.org/pub/release-87/gff3/homo_sapiens/Homo_sapiens.GRCh38.87.gff3.gz)

Download the annotation of regulatory variants from here:<br>
[https://ftp.ensembl.org/pub/release-87/regulation/homo_sapiens/homo_sapiens.GRCh38.Regulatory_Build.regulatory_features.20161111.gff.gz](https://ftp.ensembl.org/pub/release-87/regulation/homo_sapiens/homo_sapiens.GRCh38.Regulatory_Build.regulatory_features.20161111.gff.gz)

**NOTE** The variants are reported using version 37 of the reference genome, but the annotation is for version 38. Fortunately, you can 'lift-over' the variants to the coordinates on the new reference genome using several avaible tools. I recommmend the [UCSC liftover tool](https://genome.ucsc.edu/cgi-bin/hgLiftOver) that can do this in batch by converting the variants into BED format. Note, some variants may not successfully lift over, especially if they become repetitive and/or missing in the new reference, so please make a note of how many variants fail liftover.

- 1a. How much of the genome is annotated as a gene? (as a percentage)

- 1b. What is the sequence of the shortest gene on chromosome 22? [Hint: `bedtools getfasta`]

- 1c. How much of the genome is an annotated regulatory sequence (any type)? (as a percentage) [Hint `bedtools merge`]

- 1d. How much of the genome is neither gene nor regulatory sequences? (as a percentage) [Hint: `bedtools merge` + `bedtools subtract`]

- 1e. Using the [UCSC liftover tool](https://genome.ucsc.edu/cgi-bin/hgLiftOver), how many of the variants can be successfully lifted over to hg38?

- 1f. How many variants are in genes? [Hint: convert xlsx to BED, then `bedtools`]

- 1g. How many variants are in *any* annotated regulatory regions? [Hint: `bedtools`]

- 1h. What type of annotated regulatory region has the most variants? [Hint: `bedtools`]

- 1i. Is the number of variants in the regulatory type with the most variants a statistically significant number of variants (P-value < 0.05)? [Hint: If you don't want to calculate this analytically, you can do an experiment. Try simulating the same number of variants as the original file 100 times, and see how many fall into this regulatory type. If at least this many variants fall into this feature type more than 5% of the trials, this is not statistically significant]



#### Question 2. Time Series [20 pts]

[This file](http://schatz-lab.org/teaching/exercises/rnaseq/rnaseq.1.expression/expression.txt) contains normalized expression values for 100 genes over 10 time points. Most genes have a stable background expression level, but some special genes show increased
expression over the timecourse and some show decreased expression.

- Question 2a. Cluster the genes using hierarchical clustering. Which genes show increasing expression and which genes show decreasing expression, and how did you determine this? What is the background expression level (numerical value) and how did you determine this?

- Question 2b. Calculate the first two principal components of the expression matrix. Show the plot and color the points based on their cluster from part (a). Does the PC1 axis, PC2 axis, neither, or both correspond to the clustering?

- Question 2c. Create a heatmap of the expression matrix. Order the genes by cluster, but keep the time points in numerical order.

- Question 2d. Visualize the expression data using t-SNE.

- Question 2e. Using the same data, visualize the expression data using UMAP.

- Question 2f. In a few sentences, compare and contrast the (1) heatmap, (2) PCA, (3) t-SNE and (4) UMAP results. Be sure to comment on understandability, relative positioning of clusters, runtime, and any other significant factors that you see.


#### Question 3. Sampling Simulation [10 pts]

A typical human cell has ~250,000 transcripts, and a typical bulk RNA-seq experiment may involve millions of cells. Consequently in an RNAseq experiment you may start with trillions of RNA molecules, although your sequencer will only give a few tens of millions of reads. Therefore your RNAseq experiment will be a small sampling of the full composition. We hope the sequences will be a representative sample of the total population, but if your sample is very unlucky or biased it may not represent the true distribution. We will explore this concept by sampling a small subset of transcripts (500 to 50000) out of a much larger set (1M) so that you can evaluate this bias.

In [data1.txt](data1.txt) with 100,000 lines we provide an abstraction of RNA-seq data where normalization has been performed and the number of times a gene name occurs corresponds to the number of transcripts in the sample.

- Question 3a. Randomly sample 500 rows. Do this simulation 10 times and record the relative abundance of each of the 15 genes. Make a scatterplot the mean vs. variance of each gene (x-axis=mean of gene_i, y-axis=variance of gene_i)

- Question 3b. Do the same sampling experiment but sample 5000 rows each time. Again plot the mean vs. variance.

- Question 3c. Do the same sampling experiment but sample 50000 rows each time. Again plot the mean vs. variance.

- Question 3d. Is the variance greater in (a), (b) or (c)? What is the relationship between mean abundance and variance? Why?


#### Question 4. Differential Expression [20 pts]

- Question 4a. Using the file from question 3 (data1.txt) along with [data2.txt](data2.txt), randomly sample 5000 rows from each file. Sample 3 times for each file (this emulates making experimental replicates) and conduct a paired t-test for differential expression of each of the 15 genes. Which genes are significantly differentially expressed at the 0.05 level and what is their mean fold change?

- Question 4b. Make a volano plot of the data from part a: x-axis=log2(fold change of the mean expression of gene_i); y-axis=-log_10(p_value comparing the expression of gene_i). Label all of the genes that show a statistically siginificant change

- Question 4c. Now sample 5000 rows 10 times from each file, equivalent to making more replicates. Which genes are now significant at the 0.05 level and what is their mean fold change?

- Question 4d. Make a volcano plot using the results from part c (label any statistically significant genes)

- Question 4e. Perform the simulations from parts a/c but sample 50000 rows each time from each file. Which genes are significant and what is their mean fold change? 

- Question 4f. Make a volcano plot from 5e (label any statistically significant genes)

- Question 4g. Now examine the complete files: compare the fold change in the complete files vs the different subsamples making sure to address replicates and the size of the random sample. 


#### Question 5. Motif clustering and classifications [BONUS: 20 points]

In this question you will need to cluster and classify transcription factor sequence motifs from the [JASPAR database](https://jaspar.genereg.net/). The sequences were generated from the position weight matrices using the script [printsequence.py](printsequence.py) which loads the position frequency matrix (pfm) file and randomly generates a sequence according to the nucleotide probabilities in the matrix. We have provided three files to evaluate: [training.txt](training.txt) which contains 2500 training examples (500 examples from 5 different transcription factors; [validation.txt](validation.txt) which contains 500 examples from these 5 TFs that can be used for validating your model; and [secret.txt](secret.txt) which contains 100 unlabeled examples to run your code against. Note, you may find it helpful to generate additional examples using the provided printsequence.py script. We have provided the matrix for [TP53.pfm](TP53.pfm) as an example.

- Question 5a. The file [training.txt](training.txt) contains 2500 labeled examples. Generate a PCA plot of the examples. For this, you will need to convert the sequences into numerical data that can be used for PCA by "one-hot encoding" the DNA sequences as binary vectors:

```
def one_hot_encode_sequence(seq):
    mapping = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1]}
    return np.array([mapping[base] for base in seq])

one_hot_encoded_sequences = np.array([one_hot_encode_sequence(seq) for seq in dna_sequences])
```

You will then need to flatten the one-hot encoded arrays (which are each 4x18) into a long vector of length 72. In this encoding, each sequence is a point in 72-dimensional space where each dimension is either 0 or 1. You will also need to scale the matrix so that PCA will work correctly. Finally color each point with the transcription factor that generates it.


```
    # Flatten the one-hot encoded data
    flattened_data = one_hot_encoded_sequences.reshape(one_hot_encoded_sequences.shape[0], -1)

    # Standardize the flattened data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(flattened_data)
```




- Question 5b. Implement a neural network classifier that predicts the transcription factor that will bind to the given sequences. For training data, it should use the labeled examples in training.txt and hold out 20% of the data for model validation. In a few sentences describe the model architecture you decided to use and why. Also report the accuracy of the model on the validation data. [Hint: You will need to use a multilayer neural network for this to reach high accuracy]

- Question 5c. Use the labeled data in validation.txt to evaluate the accuracy of your model. Make sure to comment on the accuracy for each transcription factor separately. Also comment on why certain transcription factors are harder than others (hint: how do the hardest ones appear in the PCA plot in Question 5a.)

- Question 5d. Create a PCA plot that has both the labeled examples from training.txt and the unlabeled examples from secret.txt. Color each point with the transcription factor it is associated with (or ???? if it is unlabeled). In a few sentences comment on how the secret data relates to the training data provided, and how you expect this will impact classification accuracy.

- Question 5e. Run your final model on secret.txt to predict which transcription factor best binds to each sequence. Save this to a text file named LAST.FIRST.txt where LAST FIRST are your first and last names. Each row in the file should contain the sequence and the transcription factor predicted. Store the file in google drive and include a link to the file in your write up. Make sure to set permissions so that anyone can read the file. We will then compare your predictions to the truth and use your accuracy to evalute the points awarded.


### Packaging

The solutions to the above questions should be submitted as a single PDF document that includes your name, email address, and all relevant figures (as needed). If you use ChatGPT for any of the code, also record the prompts used. Submit your solutions by uploading the PDF to [GradeScope](https://www.gradescope.com/courses/587880), and remember to select where in your submission each question/subquestion is. The Entry Code is: JK5VB4. 

If you submit after this time, you will use your late days. Remember, you are only allowed 4 late days for the entire semester!


### Resources

#### Bedtools

Bedtools has really nice documentation available at: [https://bedtools.readthedocs.io/en/latest/](https://bedtools.readthedocs.io/en/latest/)

##### Installation

If you were able to use mamba in assignment 2, then you can install bedtools with:

`$ mamba install -c bioconda bedtools`

If you had any issues installing/using mamba on your computer, you can use the Github compute environment from assignment 3.


#### PCA

In python, see [sklearn.decomposition.PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

#### Neural Networks

In python, see [Keras](https://www.tensorflow.org/guide/keras)