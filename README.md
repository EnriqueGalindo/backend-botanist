# The infamous EE challenge! xD

### Learning Objectives
- Familiarize using datetime library.
- Learn how to use table modules to beautify outputs.
- Get more practice reading information from JSON files.

### Assignment Goals
- The user receives a .txt file with a calendar of the watering
schedule
- The schedule covers the next 12 weeks starting on the next Monday.
- No plants are watered on Saturdays or Sundays.
- Each plant is watered on its desired schedule or as close as possible, taking into account weekends.

![LOGO](images/happy_flower.jpeg)

### Part A
Write a function, `parse_json` to obtain a list of dictionaries of plants and 
how often they need to be watered (Hint:You may want to reformat the `water_after` values in the dictionary for easier use later)

### Part B
Write a function `schedule_per_plant` using the [datetime](https://docs.python.org/3/library/datetime.html)library that adds a key value pair, with the key being `schedule`, to each plant's dictionary of the days that plant has to be watered, without being concerned with weekends quite yet. (Hint:using pprint might make the schedule easier to read)

### Part C
Write a function `final_schedule` to create a dictionary of all
the days in the 12 week period as the keys and a list of all the
plants that need to be watered on that day as the values.

### Part D
Write a function `weekend_filter` to implement in your
`schedule_per_plant` function. It should subtract a day if the
plant were to land on a Saturday, and add a day if it were to land
on a Sunday.

### Part E
Write a function `create_table` that outputs the schedule into a
table format using any Python table library.

### Part F
In the main function, write your now beautified schedule to plant_schedule.txt. Make sure that the file gets pushed to the repo as well.

### Example Output
```
+-------------------+------------+------------+-------------------+------------+------------+------------+
|     12-16-2019    | 12-17-2019 | 12-18-2019 |     12-19-2019    | 12-20-2019 | 12-21-2019 | 12-22-2019 |
+-------------------+------------+------------+-------------------+------------+------------+------------+
|  Fiddle Leaf Fig  |            | Wavy Fern  |  Bird's Nest Fern | Wavy Fern  |            |            |
|    Snake Plant    |            |            | Bell Pepper Plant |            |            |            |
|     Money Tree    |            |            |  Strawberry Plant |            |            |            |
|  Bird's Nest Fern |            |            |                   |            |            |            |
|       Croton      |            |            |                   |            |            |            |
| Bell Pepper Plant |            |            |                   |            |            |            |
```

![LOGO](images/eg_headshot.jpeg) ![LOGO](images/eh_headshot.jpeg)

## Background
This is a real world entry level application. This is based off a
real take home programming challenge given by a company in
Chicago in Dec 2019. The original challenge did not outline the
steps that needed to be taken to accomplish the challenge. The
steps are based off of the solution Enrique Galindo wrote and Eric
Hanson contributed to. 

### PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
4. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.

