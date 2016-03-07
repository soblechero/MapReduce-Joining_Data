# MapReduce-Joining_Data

·En unix:
cat test_files/join2_gen*.txt | ./join2_mapper.py | sort | ./join2_reducer.py

·En windows:
type test_files/join2_gen*.txt | python join2_mapper.py | sort | python join2_reducer.py
