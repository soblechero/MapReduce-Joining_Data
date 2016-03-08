# MapReduce-Joining_Data

* Objetivo:

Tenemos dos tipos de ficheros de pruebas con pares clave-valor, un tipo con \<TV show, viewer\> y otro con \<TV show, Channel\>

Y queremos hacer un inner join entre ambos tipos de datos:

```
select sum( viewer count) from FileA, FileB 
where FileA.TVshow = FileB.TVshow and FileB.Channel='ABC' 
group by TVshow
```

* Probar en unix:

```
$ cat test_files/join2_gen*.txt | ./join2_mapper.py | sort | ./join2_reducer.py
```
* Probar en windows:

```
> type test_files/join2_gen*.txt | python join2_mapper.py | sort | python join2_reducer.py
```
