.. title: The Bigger Analogy Test Set (BATS)
.. slug: BATS
.. tags: mathjax
.. hidetitle: True
.. pretty_url: True
.. template: base3.tmpl


==================================
The Bigger Analogy Test Set (BATS)
==================================

.. raw:: html

   <div style = "padding-top: 15px; padding-bottom: 25px; margin-left: 40px">
   <br/>
   <p>The English dataset: <a href="https://my.pcloud.com/publink/show?code=XZOn0J7Z8fzFMt7Tw1mGS6uI1SYfCfTyJQTV">direct download</a></p>
   <p>The testing scripts for 6 different analogy solving methods are <a href="http://vecto.readthedocs.io/en/docs/tutorial/evaluating.html#word-analogy-task">available in Vecto library</a>.</p>
   <p>BATS in other languages:  <a href="http://vecto.space/projects/jBATS">Japanese</a>.</p>
   </div>

.. contents:: In this page:

-----------------
Word analogy task
-----------------

Analogies have been one of the standard intrinsic benchmarks for word embeddings since the striking demonstration of “linguistic regularities” by Mikolov et al. (2013) [#f1]_. The big finding of that study was that simple vector offset between one pair of words with a given relation can be used to identify the missing member of a different word pair with the same relation.

.. figure:: /assets/img/queen.png
   :height: 200 px
   :align: center

   Figure 1. "Linguistic regularitities": linear vector offsets as model of linguistic relations (Mikolov et al., 2013) [#f1]_


For example, consider a pair of words $a : a' :: b : b$ such as *man:
woman :: king : queen*. Mikolov et al. proposed that the $b'$ word could be found with the help of the offset between the words $b$ and $a$:

$$b'=argmax_{~d\in{V}}(cos(b',b-a+a'))$$

In other words, the word analogy task was interpreted as follows: given the words *a, a' and b'*, to choose the word vector that is the closest to the result of calculation *b-a+a'*, and that vector should be the *b'* vector.

---------------------
Why BATS is different
---------------------

The "linguistic regularity" phenomenon was demonstrated by Mikolov et al. on
 a new dataset of 9 morphological and 5 semantic categories, with 20-70 unique word pairs per category which are combined in all possible ways to yield 8,869 semantic and 10,675 syntactic questions. This set is still a popular benchmark for word embeddings, commonly referred to as the Google analogy dataset. These numbers look convincingly large. When word embedding models started claiming over 80% accuracy on this dataset [#f2]_, that could be interpreted as suggesting that identifying different linguistic relations is a solved task, and we already have extremely accurate, context-independent distributional semantic representations.

It has since become clear that this is not the case. Language has thousands of relations of various kinds, and human analogical reasoning, while fundamental to our learning, clearly `does not operate on one-rule-for-all-cases base <http://www.aclweb.org/anthology/S17-1017>`_. The Google test set had only 15 relations, and it was also highly unbalanced. 56.72\% of all semantic questions are from the same famous *country:capital* category, and "syntactic" questions were mostly on inflectional rather than derivational morphology.

BATS [#f3]_ was created to address these issues and detect what kinds of relations *are* currently detectable with analogical reasoning. BATS includes 4 types of linguistic relations: inflectional and derivational morphology, and lexicographic and encyclopedic semantics. Each relation is represented with 10 categories, and each category contains 50 unique word pairs. For a test in the vector offset paradigm it yields 2480 questions (99,200 [#f4]_ in total).

In addition to the goals of representativeness and balance, BATS has two new important features:

 * the morphological categories are morphological categories are sampled to reduce homonymy. For example, for verb present tense the Google set includes pairs like *walk:walks*, which could be both verbs and nouns. BATS only includes words that have no more than one part-of-speech in WordNet.
 * where applicable, BATS contains several acceptable answers (sourced from WordNet). For example, both *mammal* and *canine* are hypernyms of dog. In some cases alternative spellings are also listed (e.g. *organize: reorganize/reorganise*).

-----------------
Structure of BATS
-----------------

.. include:: ./files/assets/files/bats-table.html

-------------------
Performance on BATS
-------------------

The initial results with BATS were striking: GloVe, the model that claimed over 80% accuracy on the Google syntactic analogies, achieved under 30% on BATS. Furthermore, only inflectional morphology categories can be reliably detected, and the famous *country:capital* category is a clear outlier among the semantic categories, most of which have very low accuracy.

.. figure:: /assets/img/bats_stats.png

   Figure 2. Performance on BATS: GloVe word embeddings vs count-based vectors condensed with SVD

Interestingly, the above figure also shows that GloVe is generally not that
different from a traditional count-based SVD: although it performs 5-10%
better in many cases, the overall pattern of categories that are
easy/difficult is clearly the same for both models. The same pattern was
confirmed in a subsequent study [#f5].

-----------------------------------------------------
What subsequent studies with BATS helped to establish
-----------------------------------------------------

Subsequent projects used the balanced structure of BATS to show the following:

 * the vector offset method is not the best way to solve word analogies, with `LRCos method achieving up to 35% improvement <http://www.aclweb.org/anthology/C16-1332>`_ in some categories [#f5]_ ;
 * all the current methods are heavily biased by cosine similarity between the source words, which means that `the results on word analogy task indicate which relations a given model favors in vector neighborhoods <http://www.aclweb.org/anthology/S17-1017>`_ (and *not* some general "goodness" of the model) [#f6]_ .
 * `subword-level models such as Fasttext achieve much higher accuracy on derivational morphology <http://www.aclweb.org/anthology/W18-1205>`_, as compared to the word-level models such as SkipGram [#f7]_ .


 A comparable dataset for Japanese is now also `available <http://vecto.space/projects/jBATS>`_. It was used to show the effectiveness of leveraging subcharacter information to produce more meaningful representations for Japanese characters.

  .. (which turned out to be `domain-dependent, and not as high as that claimed for Chinese <https://sites.google.com/view/relsnnlp/home/accepted-papers>`_).

.. rubric:: Footnotes

.. [#f1] Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic Regularities in Continuous Space Word Representations. In Proceedings of NAACL-HLT 2013 (pp. 746–751). Atlanta, Georgia, 9–14 June 2013. Retrieved from https://www.aclweb.org/anthology/N13-1090

.. [#f2] Pennington, J., Socher, R., & Manning, C. D. (2014). Glove: Global vectors for word representation. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) (Vol. 12, pp. 1532–1543). https://www.aclweb.org/anthology/D14-1162

.. [#f3] Gladkova, A., Drozd, A., & Matsuoka, S. (2016). Analogy-based detection of morphological and semantic relations with word embeddings: what works and what doesn’t. In Proceedings of the NAACL-HLT SRW (pp. 47–54). San Diego, California, June 12-17, 2016: ACL. https://www.aclweb.org/anthology/N/N16/N16-2002.pdf

.. [#f4] The abstract of the original paper has a mistake: the total number of questions in BATS is 99,200.

.. [#f5] Drozd, A., Gladkova, A., & Matsuoka, S. (2016). Word embeddings, analogies, and machine learning: beyond king - man + woman = queen. In Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical Papers (pp. 3519–3530). Osaka, Japan, December 11-17. https://www.aclweb.org/anthology/C/C16/C16-1332.pdf

.. [#f6] Rogers, A., Drozd, A., & Li, B. (2017). The (Too Many) Problems of Analogical Reasoning with Word Vectors. In Proceedings of the 6th Joint Conference on Lexical and Computational Semantics (* SEM 2017) (pp. 135–148). http://www.aclweb.org/anthology/S17-1017

.. [#f7] Li, B., Drozd, A., Liu, T., & Du, X. (n.d.). Subword-level Composition Functions for Learning Word Embeddings. In Proceedings of the Second Workshop on Subword/Character LEvel Models (pp. 38–48). New Orleans, Louisiana, June 6, 2018. http://www.aclweb.org/anthology/W18-1205


