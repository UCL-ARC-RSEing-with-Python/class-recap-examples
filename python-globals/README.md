# Problems with Python Globals

This folder contains code to demonstrate the following concepts:

- What a "global" or "module-level" variable is in Python.
- How to avoid using these where possible, but restructuring your functions.
- What the `if __name__ == "__main__"`: block does.

There are 2 data files containing some simple `.json` data about pets.
These two files exist to show that hard-coding the data path means that you'll need to repeat your code when you want to load different data sets, unless the function which is loading the data is converted to take the data path as an argument.

There are also two scripts.
`examine_dataset.py` is a simple data-loader script that has the following issues:

- The first is that the `DATA_FILE` is global, and used within the `load_pet_data` function.
  This means that, in it's current state, we cannot re-use it to examine the other data set without updating the global variable.
  This will mean that we either have to repeat the function, or commit a change every time we want to use a different dataset (which will cause conflicts with collaborators).
  - This can be fixed by making the `DATA_FILE` an argument to the `load_pet_data` function.
    Doing this means that we can `import` it into other files and make use of it.
  - Note that in our actual script commands, we still have to provide the file we want to load explicitly.
    However, this is an improvement since it means our function can be recycled into other scripts (so we don't have to repeat ourselves).
    Additionally, we could make further efforts to have our script accept the data file we want to examine from the command-line, which would further eliminate this problem.
- The second is that there is no main-protection block in the script, the commands are just loose.
  This means that, if the `examine_species.py` file is run after switching out the repeat code for an `import`, we should notice that our use of `import` actually runs the entire `examine_dataset.py` script too!
  Not super great if it's a long script that uses up a lot of compute time!
  - This can be fixed by wrapping the "script workflow" or the main-block as inside the `if __name__ == "__main__"` block.
  - Note that "hard-coded values" inside the main block are better than global variables, though you might still want to get rid of these by turning them into command-line arguments.

`examine_species.py` repeats the loading process that's in `load_pet_data`, again we can emphasise this is because of the hard-coded value preventing our function from being re-usable.
Once the `load_pet_data` function is correctly edited to take the data file as an argument, this repeat code can be eliminated and we can just re-use the function we trust.
Note that doing this will also uncover the problem with the lack of a main-block in `examine_dataset.py`.
