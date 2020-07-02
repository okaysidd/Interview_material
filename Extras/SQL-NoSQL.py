"""
NoSQL- the GOOD
- Insertions and deletions are very fast
- Schema can be changed for new records very quickly, without bothering the older ones
- Built for scale (scale horiontally)
- Good for aggregations
NoSQL - the BAD
- Not suited for update queries
- Consistency not there (availability over consistency)
- No ACID - so no transactions, not for Financial systems
- Not read optimised
- Relations are not implicit (FK)
- Joins are not easy

In distributed NoSQL database like Cassandra, Quorum is a value that is taken into consideration to decide
the truth. If the Replication factor is 3 and 2 nodes decide on a certain state of a record data availability,
that is taken as the truth, because of simple majority.

Cassandra-
- Made up of clusters, uses replication of data to improve availability
- Uses replication factor and quorum along with time stamps/version number to get latest data
- Uses log tables to store all data as it comes in, not sorted, just as they come in
- At certain intervals, the logs are aggregated as Sorted String Tables (SST), which are immutable and store data togther
- Since same record might be in different SST due to the write/update times, multiple copies can exist
- Time stamp is used to resolve the read queries, when multiple copies exist
- A batch job will merge the SST every certain amount of time, using merge sort, to combine the sorted tables
- On merging, since duplicates will be present, the versions apart from the latest time stamp/version can be maked as deleted,
	called as Tombstone, as a flag. Records with tombstone are considered destroyed and cannot be read or updated
"""

"""
Load balancing
- Hashing will help us with load balancing, for balancing/sending incoming requests between many servers
- Uniformly random hash function will help us balance the load properly
Load balancing using normal hashing - the BAD
- Adding new servers/databases will be destructive, because the target server/database is currently set using % with number of servers
- Deleting servers/databases will pose the same problem
Use CONSISTENT HASHING
# TODO: Read about Consistent Hashing
"""