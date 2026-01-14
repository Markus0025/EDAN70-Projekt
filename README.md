Categorization and Cross-edition Matching and Linking for Nordisk
Familjebok
---
Authors: Emil Jönsson and Markus Möller

The Nordisk Familjebok is a Swedish encyclo-
pedia written by subject experts between 1876
and 1995. It spans four editions and as one of
the most influential encyclopedias in Sweden, it
offer a valuable lens through which to see how
swedish perspectives have shifted over time.
This paper analyzes entries from the second and
third editions using a digitized version from
Projekt Runeberg. We first extract headwords
from each edition by using machine learning
and sequence annotation. Each headword is
then classified using a BERT model into one of
three categories location, person and other.
This paper focuses on entries classified as per-
sons, by matching persons across the two edi-
tions we can see whether the encyclopedia fo-
cuses more on people over time. Further by
linking these entries to Wikidata, we can obtain
additional information about our persons, such
as gender and occupation. This enables further
possibilities of examination of how represen-
tations of people changed in Sweden across
time. The entity matching and linking were
done by using Sentence-BERT to compare the
descriptions with each other.
Our results indicate that the proportion of en-
tries devoted to individuals remained relatively
stable, as did the gender distribution.
