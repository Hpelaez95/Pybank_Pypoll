
import os
import csv
# importing the modules i will need

election_data=os.path.join("election_data.csv")
election_data
# creating variable for opening the file and making sure it works
# created variables that will look for keywords and some empty lists for tracking
# created empty counters to tally the times each candidate appeared.
First_candidate = "Charles Casper Stockham"
Second_candidate = "Diana DeGette"
Third_candidate="Raymon Anthony Doane"
voter_count=[]
Charles_candidate=0
Diane_candidate=0
Raymon_candidate=0
candidate_votes={}
# creating the loops for the file nested inside of it while it is open
with open(election_data) as csvfile:
    election_reader = csv.reader(csvfile, delimiter=',') 
    voter_count=[]
    Charles_candidate=0
    Diane_candidate=0
    Raymon_candidate=0
    candidate_votes={}
    header=next(election_reader)
    for row in election_reader:
       voter_count.append(row[0])
       vote_total=len(voter_count)
       print(vote_total)
       for indvidual in election_reader:
           if any((First_candidate) in name for name in map(str,indvidual)):
            Charles_candidate +=1 
            Finalfirstcount = Charles_candidate +1
           elif any((Second_candidate) in name for name in map(str,indvidual)):
            Diane_candidate +=1
            Finalsecondcount=Diane_candidate
           else:
            any((Third_candidate)in name for name in map (str, indvidual))
            Raymon_candidate +=1
            Finalthirdcount= Raymon_candidate 
            # counting the times that each candidate appeared in the file

         
       
# total count of votes sums all of the votes for the candidates
total_voter_count=Finalfirstcount+Finalsecondcount+Finalthirdcount
# finding the percent for each of the candidate and how much of the vote they won
percent_charles = (Finalfirstcount/total_voter_count)*100
percent_diane = (Finalsecondcount/total_voter_count)*100
percent_Raymon = (Finalthirdcount/total_voter_count)*100
print(round(percent_charles,3),round(percent_diane,3),round(percent_Raymon,3))

# creating my output for writing the results 
output_path=os.path.join( "Poll Results.txt")
#  creating a variable to call out all of the results at once in a print out and write it.
output=(

    f"Election Results\n"
    f"------------------\n"
    f"Total votes: {total_voter_count}\n"
    f"{First_candidate}: {round(percent_charles,3)}% ({Finalfirstcount})\n"
    f"{Second_candidate}: {round(percent_diane,3)}% ({Finalsecondcount})\n"
    f"{Third_candidate}: {round(percent_Raymon,3)}% ({Finalthirdcount})\n"
    f"------------------\n"
    f" Winner: {Second_candidate}\n"
    f"------------------\n"
)
# showing the results on the terminal
print(output)
# writing the results to a new file as Poll Results.txt
with open(output_path, 'w') as txtfile:
    txtfile.write(output)
   





