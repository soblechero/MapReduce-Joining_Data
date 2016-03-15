# MapReduce-Joining_Data

* Objetivo:

Tenemos dos tipos de ficheros de pruebas con pares clave-valor, un tipo con \<TV show, viewers\> y otro con \<TV show, Channel\>

Y queremos hacer un join entre ambos tipos de datos:

```
select sum( viewer count) from FileA, FileB 
where FileA.TVshow = FileB.TVshow and FileB.Channel='ABC' 
group by TVshow
```

* Se puede probar en unix así:

```
$ cat test_files/join2_gen*.txt | ./join2_mapper.py | sort | ./join2_reducer.py
```
* Y en windows así:

```
> type test_files\join2_gen*.txt | python join2_mapper.py | sort | python join2_reducer.py
```
