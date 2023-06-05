# Project Name

Brief description of the project.

## Overview

Provide a high-level overview of the project, including its purpose and main features.

## Installation

1. Make sure you have Python installed on your machine.
2. Clone this repository or download the `generate_top50_by_country.py` file.
3. Place your streaming data in a CSV file named `data.csv`.
4. Install the required dependencies by running the following command:`pip install pandas`
5. Run the script using the following command:`python generate_top50_by_country.py`

### Automated Execution with Jenkins

1. Install and set up Jenkins on your machine or server.
2. Create a new Jenkins job.
3. Configure the job to execute a shell command or execute a Python script build step.
4. Specify the path to the Python interpreter and the script in the job's configuration.
5. Save the configuration and schedule the job to run daily at the specified time.

### Task Scheduling on Google Cloud Platform

1. Set up a virtual machine instance on Google Cloud Platform.
2. Install Python and the necessary dependencies on the virtual machine.
3. Clone this repository or copy the `generate_top50_by_country.py` file to the virtual machine.
4. Place your streaming data in a CSV file named `data.csv` on the virtual machine.
5. Set up a cron job or use Google Cloud Scheduler to schedule the execution of the script daily at the specified time.
