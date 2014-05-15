r"""
Parse biological sequences (:mod:`skbio.parse.sequences`)
=========================================================

.. currentmodule:: skbio.parse.sequences

This module provides functions for parsing sequence files in a variety of
different formats, the available parsers are listed below.

Functions
---------

.. autosummary::
   :toctree: generated/

    parse_clustal
    parse_fasta
    parse_fastq
    parse_qual

"""

# ----------------------------------------------------------------------------
# Copyright (c) 2013, The scikit-bio Developers.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------


from .clustal import parse_clustal
from .fasta import parse_fasta, parse_qual
from .fastq import parse_fastq
from .iterator import FastaIterator, FastqIterator, SequenceIterator
from .factory import load


__all__ = ['parse_clustal', 'parse_fasta', 'parse_fastq', 'parse_qual',
           'FastqIterator', 'FastaIterator', 'SequenceIterator', 'load']
