# MapReduce-Joining_Data

..*Lo que queremos:

```
select sum( viewer count) from File A, File B where FileA.TVshow = FileB.TVshow and FileB.Channel='ABC' grouped by TVshow
```

..*Probar en unix:

```
$ cat test_files/join2_gen*.txt | ./join2_mapper.py | sort | ./join2_reducer.py
```
..*Probar en windows:

```
> type test_files/join2_gen*.txt | python join2_mapper.py | sort | python join2_reducer.py
```
