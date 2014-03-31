#!/usr/bin/env python

class MinCDSLengthFilter:

    def __init__(self, min_length = 0):
        self.min_length = min_length
        return
        
    def apply(self, seq):
        for gene in seq.genes:
            for mrna in gene.mrnas:
                if mrna.cds != None and mrna.cds.length() < self.min_length:
                    mrna.cds = None # Destroy the cds