#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

import json
from ast import literal_eval


class Ticket:
    def __init__(self, source, destination):
        self.order = None
        self.source = source
        self.destination = destination
        self.next = None

    def __repr__(self):
        ticket = {
            'source': self.source,
            'destination': self.destination,
        }
        return str(ticket)
    
def reconstruct_trip(tickets, length):
    route = [None]*length

    # ht = HashTable(length)
    # for t in tickets:
    #     hash_table_insert(ht,t.source,t.destination)

    for i,t in enumerate(tickets):
        if route[0] is None:
            start = [t for t in tickets if t.source == 'NONE'][0]
            route[0] = start
            continue
        next_source = route[i-1].destination
        next_trip = [t for t in tickets if t.source == next_source][0]
        route[i] = next_trip
        
    trip = [r.destination for r in route]
    return trip[:-1]


tickets = [
  Ticket("PIT","ORD"),
  Ticket("XNA","CID"),
  Ticket("SFO","BHM"),
  Ticket("FLG","XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX","SFO"),
  Ticket("CID","SLC"),
  Ticket("ORD","NONE"),
  Ticket("SLC","PIT"),
  Ticket("BHM","FLG")
]

'''
retrieve, get the value.  next will be where val = next_key
'''

new_route = reconstruct_trip(tickets,len(tickets))
print(new_route)
