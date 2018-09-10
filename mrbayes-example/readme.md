# example of running a "long" analysis

was used [here](http://cecileane.github.io/computingtools/pages/notes0915.html)
to show how to
- redirect the output and/or errors, and
- pause or kill or process.

This folder contain the sequence [data](alignedDNA.nex) and the
[option](mrBayes-run.nex) file to reproduce the analysis.
To run the analysis, the [MrBayes](http://mrbayes.sourceforge.net/index.php)
program also needs to be installed, and its executable `md` needs to be located in a
directory in the PATH variable.
Run the analysis from the command line like this:

```shell
mb mrBayes-run.nex
```
