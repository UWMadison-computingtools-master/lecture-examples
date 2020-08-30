# example of running a "long" analysis

illustration for [here](http://cecileane.github.io/computingtools/pages/notes0915.html)
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

Things to try:

```
mb mrBayes-run.nex
^z (sleep)
fg
^c (cancels / interrupts the process)
mb mrBayes-run.nex > alignedDNA.nex.screenlog
(error messages, if any, still go to the screen)
(forgot & : can't work)
^z (sleep)
ps
kill -9 ...
less alignedDNA.nex.screenlog
mb mrBayes-run.nex > alignedDNA.nex.screenlog &
ps (check the match in process ID)
top (q to quit)
tail -n 5 alignedDNA.nex.screenlog
kill -9 ...
mb mrBayes-run.nex > /dev/null 2> alignedDNA.nex.err
^z
ps
bg
```
