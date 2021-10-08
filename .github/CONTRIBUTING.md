# Contributing to the curriculum

Parts of this document were adapted from the [Tidyverse](https://tidyverse.tidyverse.org/CONTRIBUTING.html)
and the [Software Carpentry](https://github.com/swcarpentry/python-novice-inflammation/blob/gh-pages/CONTRIBUTING.md)
contributing guides.

## Code of Conduct

Please note that this curriculum is released with a
[Contributor Code of Conduct](CODE_OF_CONDUCT.md).
By contributing, you agree to abide by its terms and
you agree that we may redistribute your work under [our license](../LICENSE.md).

## How to Contribute

You can fix typos, spelling mistakes, or grammatical errors directly using the GitHub web interface.
If you want to make a bigger change, it's a good idea to first file an issue and make sure someone from the team agrees that it’s needed.
If you’ve found a bug, please file an issue that illustrates the bug with a minimal reproducible example.

### Pull request process

You may first want to look at
[How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github).
We follow [GitHub flow](https://guides.github.com/introduction/flow/) to make
changes to the curriculum.
To contribute:

1.  Fork this repository to your GitHub profile. You may wish to clone your
fork to make changes locally, or you can use the GitHub web interface if you
are not planning to edit any of the Jupyter notebooks.
1.  Within your version of the forked repository, move to the `main` branch and
create a new branch for each significant change being made.
1.  Navigate to the file(s) you wish to change within the new branches and make
revisions as required. Take a look at the [Style Guidelines](#style-guidelines)
below to ensure your changes meet our standards.
1.  If you made changes to a Jupyter notebook, make sure that
the notebook renders and runs correctly in [JupyterLab](https://jupyter.org/).
1.  Commit all changed files within the appropriate branches.
1.  Create individual pull requests from each of your changed branches
to the `main` branch within the originating repository.
1.  If you receive feedback, make changes using your issue-specific branches of
the forked repository and the pull requests will update automatically.
1.  Repeat as needed until all feedback has been addressed.

When starting work, please make sure your clone of the originating `main` branch
is up-to-date before creating your own revision-specific branch(es) from there.
Additionally, please only work from your newly-created branch(es) and *not*
your clone of the originating `main` branch.

## Style Guidelines

### Commit messages

We recommend this [style guide](https://chris.beams.io/posts/git-commit/) for
writing good commit messages.
The highlights:
- Capitalize the first word of the message.
- The first word should be a verb in the imperative tense.
- Keep the message short but descriptive of the changes.

### File naming scheme

Every lesson module has 4 corresponding files; the lesson, practice, and keys for each.
If you edit one file, you'll likely need to edit the other files too.
Our directory structure is as follows:
```
.
├── Lessons
│   ├── Lesson99_Topic-Description.ipynb
│   └── _Keys
│       └── KEY_Lesson99_Topic-Description.ipynb
└── Practices
    ├── Practice99_Topic-Description.ipynb
    └── _Keys
        └── KEY_Practice99_Topic-Description.ipynb
```
Be sure the filenames follow this pattern!

### File paths

If you need to read in a dataset, Pandas can read https links to raw github files. Example:

```
path = 'https://raw.githubusercontent.com/GWC-DCMB/curriculum-notebooks/main/'
tips = pd.read_csv(path + 'SampleData/tips.csv')
```

Don't use local filepaths (e.g. `pd.read_csv('../SampleData/tips.csv')`), because we live-code in Google Colab.

The same applies to including images in markdown cells, e.g.:

```
Here's a diagram:
![](https://raw.githubusercontent.com/GWC-DCMB/curriculum-notebooks/main/Figures/IfElifElseDiagram.png)
```

### Cell output

**Keys**:
Every Key (filename starts with `KEY_`) should show the output of all cells.  
Make sure Keys work by running all cells in JupyterLab by clicking `Run` > `Run All Cells`.

**Lessons & Practices**:
The output cells of every Lesson and Practice notebook should be empty.
To remove the output cells from a notebook, click `Edit` > `Clear All Outputs`.

### JupyterLab

**TLDR**: When editing notebooks, be sure to use JupyterLab on your local machine.
If you open a notebook with Google Colab, please don't commit the changes.

Jupyter notebooks are text files in [JSON format](https://www.json.org/),
which can be conveniently parsed as Python dictionaries.
JupyterLab formats them nicely with tab indentation & individual fields on different lines
(i.e. [pretty-print](https://docs.python.org/3.4/library/pprint.html)), like this:

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "KSChitqaVpii"
   },
   "source": [
    "# Subsetting Pandas DataFrames I\n",
    "\n",
    "You now know how to read external datasets into `pandas`. Let's put those skills to use and read in the `tips` dataset again:"
   ]
  },
...
```

However, when you open a Jupyter notebook with Google Colab, it squishes all of the content onto one line, like this:
```
{ "cells": [  {   "cell_type": "markdown",   "metadata": {    "colab_type": "text",    "id": "KSChitqaVpii"   },   "source": [    "# Subsetting Pandas DataFrames I\n",    "\n",    "You now know how to read external datasets into `pandas`. Let's put those skills to use and read in the `tips` dataset again:"   ]  },
```

This makes it difficult to compare & merge Jupyter notebooks written in JupyterLab vs Colab via `git diff`.
To keep our notebooks easy to compare & merge, we strongly prefer JupyterLab for editing.
