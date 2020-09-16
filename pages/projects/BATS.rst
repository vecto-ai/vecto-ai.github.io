.. title: The Bigger Analogy Test Set (BATS)
.. slug: BATS
.. tags: mathjax
.. use_math: true
.. hidetitle: True
.. pretty_url: True
.. template: BATS.tmpl

.. role:: emph

==================================
The Bigger Analogy Test Set (BATS)
==================================

Word analogy task has been one of the standard benchmarks for word embeddings since the striking demonstration of “linguistic regularities” by Mikolov et al. (2013) [#f1]_. Their big finding was that linear vector offsets seem to mirror linguistic relations, and can be used to perform analogical reasoning.

.. figure:: /assets/img/queen.png
   :height: 100 px
   :align: center

   Figure 1. Linear vector offsets as model of linguistic relations (Mikolov et al., 2013) [#f1]_

For example, consider a pair of words *a : a' :: b : b* such as *man:
woman :: king : queen*. Mikolov et al. proposed that the *b'* word could be found with the help of the offset between the word vectors *b* and *a*. In this case, the word vector *queen* should be the vector that is the closest to the result of calculation *king - man + woman*.

 .. $$b'=argmax_{~d\in{V}}(cos(b',b-a+a'))$$

---------------------
Why BATS is different
---------------------

Mikolov et al. demonstrated their findings on a dataset of the Google analogy dataset that had 9 morphological and 5 semantic categories, with 20-70 unique word pairs per category: 8,869 semantic and 10,675 syntactic questions in total.

These numbers look convincingly large, but language has thousands of relations of various kinds, and human analogical reasoning `does not just use one rule for all cases <http://www.aclweb.org/anthology/S17-1017>`_. The Google test set had only 15 relations, and was also highly unbalanced. 56.72\% of all semantic questions are from the same famous *country:capital* category, and "syntactic" questions were mostly on inflectional rather than derivational morphology.

 .. When word embedding models started claiming over 80% accuracy on this dataset [#f2]_, that could be interpreted as suggesting that identifying different linguistic relations is a solved task, and we already have extremely accurate, context-independent distributional semantic representations.

 .. It has since become clear that this is not the case.

BATS [#f2]_ is an improvement over this dataset in several aspects:

 * :emph:`balanced and representative`: BATS covers inflectional and derivational morphology, and lexicographic and encyclopedic semantics. Each relation is represented with 10 categories, and each category contains 50 unique word pairs. This makes for 98,000 [#f3]_ questions for the vector offset method.
 * :emph:`reduced homonymy`: the morphological categories were sampled to reduce homonymy. For example, for verb present tense the Google set includes pairs like *walk:walks*, which could be both verbs and nouns.
 * :emph:`multiple correct answers` where applicable. For example, both *mammal* and *canine* are hypernyms of dog. In some cases alternative spellings are listed (e.g. *organize: reorganize/reorganise*).

.. include:: ./files/assets/files/bats-table.html

-------------------
Performance on BATS
-------------------

The initial results with BATS were striking: GloVe [#f4]_, the model that claimed over 80% accuracy on the Google syntactic analogies, achieved under 30% on BATS. Furthermore, only inflectional morphology categories can be reliably detected, and the famous *country:capital* category is a clear outlier among the semantic categories, most of which have very low accuracy.

.. figure:: /assets/img/bats_stats.png

   Figure 2. Performance on BATS: GloVe word embeddings vs count-based vectors condensed with SVD

Interestingly, the above figure also shows that GloVe is generally not that different from a traditional count-based SVD: although it performs slightly better in many cases, the overall pattern of categories that are easy/difficult is clearly the same for both models. The same pattern was confirmed in a subsequent study [#f5]_.

BATS thus presents more of a challenge to the modern systems that make use of word embeddings for verbal reasoning tasks. To the best of our knowledge, no system has yet achieved over 50% accuracy on the whole BATS, although there were several significant improvements:

 * `subword-level models such as Fasttext achieve much higher accuracy on derivational morphology <http://www.aclweb.org/anthology/W18-1205>`_, as compared to the word-level models such as SkipGram [#f6]_ .
 * the vector offset method is not the best way to solve word analogies, with `LRCos method achieving up to 35% improvement <http://www.aclweb.org/anthology/C16-1332>`_ in some categories [#f5]_ ;

Future work should take into account that all the current methods are heavily biased by cosine similarity between the source words, which means that `the results on word analogy task indicate which relations a given model favors in vector neighborhoods <http://www.aclweb.org/anthology/S17-1017>`_ (and *not* some general "goodness" of the model) [#f7]_ .

A comparable dataset for Japanese is now also `available <http://vecto.space/projects/jBATS>`_. It was used to show the effectiveness of leveraging subcharacter information to produce more meaningful representations for Japanese characters.

.. rubric:: Footnotes

.. [#f1] Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic Regularities in Continuous Space Word Representations. In Proceedings of NAACL-HLT 2013 (pp. 746–751). Atlanta, Georgia, 9–14 June 2013. Retrieved from https://www.aclweb.org/anthology/N13-1090

.. [#f2] Gladkova, A., Drozd, A., & Matsuoka, S. (2016). Analogy-based detection of morphological and semantic relations with word embeddings: what works and what doesn’t. In Proceedings of the NAACL-HLT SRW (pp. 47–54). San Diego, California, June 12-17, 2016: ACL. https://www.aclweb.org/anthology/N/N16/N16-2002.pdf

.. [#f3] The original paper has a typo: the total number of questions in BATS is 98,000, not 99,200.

.. [#f4] Pennington, J., Socher, R., & Manning, C. D. (2014). Glove: Global vectors for word representation. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) (Vol. 12, pp. 1532–1543). https://www.aclweb.org/anthology/D14-1162

.. [#f5] Drozd, A., Gladkova, A., & Matsuoka, S. (2016). Word embeddings, analogies, and machine learning: beyond king - man + woman = queen. In Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical Papers (pp. 3519–3530). Osaka, Japan, December 11-17. https://www.aclweb.org/anthology/C/C16/C16-1332.pdf

.. [#f6] Li, B., Drozd, A., Liu, T., & Du, X. (n.d.). Subword-level Composition Functions for Learning Word Embeddings. In Proceedings of the Second Workshop on Subword/Character LEvel Models (pp. 38–48). New Orleans, Louisiana, June 6, 2018. http://www.aclweb.org/anthology/W18-1205

.. [#f7] Rogers, A., Drozd, A., & Li, B. (2017). The (Too Many) Problems of Analogical Reasoning with Word Vectors. In Proceedings of the 6th Joint Conference on Lexical and Computational Semantics (* SEM 2017) (pp. 135–148). http://www.aclweb.org/anthology/S17-1017

