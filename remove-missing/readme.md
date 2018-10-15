example for [awk](http://cecileane.github.io/computingtools/pages/notes1013.html)
for instance

## problem description

**task 1**: remove samples with missing genes from an alignment file,
and do so for all (hundreds) files in a given folder.

**file format**:

    number_of_samples number_of_sites_in_the_alignment
    sample_name sequence
    sample_name sequence
    ...

missing gene: when the sequence is made up entirely of the following symbols:
`?` or `-` or `N` or any combination of them.

example input:

    3 4
    sample1 AG-T
    sample2 ?--?
    sample3 A-CT

output file (in a new directory but with same file name as original file name):

    2 4
    sample1 AG-T
    sample3 A-CT

**task 2**:
second script to compare the input and output directory, to check what happened:
- csv-formatted output: `filename,n_before,n_after` where `n` is the number of samples
- number of files with no change
- max number of deletions
- total number of deletions
