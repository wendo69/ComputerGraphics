
# COMPUTER GRAPHICS CAT 1
## Introduction
This undertaking revolves around fundamental manipulation of data stored in JSON files, concentrating on activities associated with handling and organizing data within the extensive dataset while managing files.

## Table of Contents

- [Tasks](#features)
   - [Question 1 - Python3 Development Environment](#question-1-python3-development-environment)
   - [Question 2 - Working with Files](#question-2-working-with-files)
- [Installation](#installation)
   - [Pre-requisites](#pre-requisites)
   - [Installation Instructions](#installation-instructions)

## Tasks<a name="features"></a>
### Question 1 - Python3 Development Environment<a name="question-1-python3-development-environment"></a>
In this section, you will set up the Python3 development environment and process the MASSIVE Dataset:

**Task 1**: Establish a Python3 development environment and configure essential dependencies.
**Task 2**: Construct a project layout akin to PyCharm and incorporate the dataset.
**Task 3**:  Produce "en-xx.xlxs" documents for all languages, utilizing the id, utt, and annot_utt attributes.
**Task 4**: Steer clear of employing recursive algorithms that exhibit elevated time complexity.
**Task 5**: Consult the Flags for executing the solution on generator.sh files.

### Question 2 - Working with Files<a name="question-2-working-with-files"></a>
In this section, you will work with JSON files and manage your project:

**Task 1**: Generate individual JSONL files for the English (en), Swahili (sw), and German (de) datasets, both for test, train, and dev sets.
**Task 2**:Assemble a sizable JSON file encompassing all English (en) to other languages (xx) translations for the training datasets, encompassing the id and utt fields.
**Task 3**: Ensure that the JSON file structure is formatted in a visually pleasing manner (pretty-printed).
**Task 4**: Upload all the created files to your designated Google Drive Backup Folder.

## Installation<a name="installation"></a>

### Pre-requisites<a name="pre-requisites"></a>

Before you begin, make sure you have the following pre-requisites installed on your system:

- [Python3 Development Environment](https://www.python.org/)

### Installation Instructions<a name="installation-instructions"></a>

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Wendo69/ComputerGraphics.git
   cd ComputerGraphics
   ```
2. Setup a virtual environment
   ```bash
   virtualenv venv
   ```
3. Import the MASSive dataset to the dataset folder
   The MASSive dataset can be found [here](https://github.com/alexa/massive/) together with the installation instructions.

3. Install all the required dependencies needed to run the project
   ```bash
   python -r pip install requirements.txt
   ```
