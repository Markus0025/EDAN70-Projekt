Classification and Cross-edition Matching and Linking for Nordisk
Familjebok
---
Authors: Emil Jönsson and Markus Möller

Nordisk Familjebok is a Swedish encyclopedia written by subject experts between 1876
and 1995. It spans four editions and as one of
the most influential encyclopedias in Sweden,
it offers a valuable lens through which to see
how Swedish perspective and knowledge have
shifted over time.
This paper analyzes entities from the second
and third editions using a digitized version from
Project Runeberg. We first extract headwords
from each edition by using machine learning
and sequence annotation. Each headword is
then classified, using the BERT architecture,
into one of the following three categories: other,
location and person.
This paper focuses on entities classified as persons, by matching persons across the two editions we can see whether the encyclopedia focuses more on people over time. Further, by
linking these entities to Wikidata, we can obtain
additional information about the persons, such
as gender and birth year. This enables further
examination of how representations of people
in Sweden changed over time. Entity matching and linking were realized using SentenceBERT to compare entity descriptions to each
other.
Our results indicate that the proportion of entities devoted to individuals increased from the
second to the third edition. The gender distribution remained similar, with a slight increase
in entities describing men in the third edition.
