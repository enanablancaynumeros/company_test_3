# Current architecture     
To update the graph got to `http://asciiflow.com/` copy this graph and load it there.


```
                                            +-----------------+
                                            |   Graphic UI    |
                                            |                 |
                                            +--------+--------+
                                                     |
                                                     |
                                                     |
                                                     |
                                                     |
                                                     |
                                                     |
                                             +-------+---------
                                             |                |
                                             |                |
                                             |    REST API    |
                                             |                |
                                             |                |
                                             +-------+--------+
                                             |       |
                                             |       |
+------------+      +--------------+         |       |
|            +------+   RabbitMQ   +---------+  +----+---+
|   Celery   |      +-------+------+            |        |
|    Beat    |              |                   |        |
|            |              |                   |        |
+------------+              |                   |        |
                       +----+----+              |Postgres|
                       |         |              |        |
                       | Celery  |              |        |
        +--------------+ Worker  |              |        |
        |              |         |              |        |
        |              +---------+              +--------+
        |
        |
    +---+------+
    | Minio    |
    | (Models  |
    | storage) |
    |          |
    +----------+

```
