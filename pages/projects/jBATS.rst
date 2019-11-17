.. title: The Japanese Bigger Analogy Test Set (jBATS)
.. slug: jbats
.. tags: mathjax
.. use_math: true
.. hidetitle: True
.. pretty_url: True
.. template: jBATS.tmpl

.. role:: emph

============================================
The Japanese Bigger Analogy Test Set (jBATS)
============================================

Word analogy task has been one of the standard benchmarks for word embeddings since the striking demonstration of “linguistic regularities” by Mikolov et al. (2013) [#f1]_. Their big finding was that linear vector offsets seem to mirror linguistic relations, and can be used to perform analogical reasoning.

.. figure:: /assets/img/queen.png
   :height: 100 px
   :align: center

   Figure 1. Linear vector offsets as model of linguistic relations (Mikolov et al., 2013) [#f1]_

For example, consider a pair of words *a : a' :: b : b* such as *man:
woman :: king : queen*. Mikolov et al. proposed that the *b'* word could be found with the help of the offset between the word vectors *b* and *a*. In this case, the word vector *queen* should be the vector that is the closest to the result of calculation *king - man + woman*.

 .. $$b'=argmax_{~d\in{V}}(cos(b',b-a+a'))$$


Mikolov et al. demonstrated their findings on the Google analogy dataset, which consists of 9 morphological and 5 semantic categories, with 20-70 unique word pairs per category: 8,869 semantic and 10,675 syntactic questions in total. However, this set was unbalanced, and some categories were overrepresented (particularly the country:capital relation constituted over 50% of all word pairs in the semantic category).
Gladkova et al. (2016) proposed `BATS <http://vecto.space/projects/BATS/>`_ (The Better Analogy Test Set), which covers eaqually derivational and inflectional morphology, as well as lexicographic and encyclopedic semantics. Each of these relations consists of 10 categories and each of the categories is being represented by 50 unique word pairs giving a total of 99,200 questions [#f3]_ for the vector offset method.

---------------
What is jBATS?
---------------

jBATS was designed based on `BATS <http://vecto.space/projects/BATS/>`_ and is, to our best knowledge, the first analogy test set for Japanese. Similarly to BATS it features 4 linguistcs relations: (1) derivational morphology, (2) inflectional morphology, (3) lexicographic semantics, and (4) encyclopedic semantics.

jBATS was structured to be:

* **balanced and representative** - similarly to BATS, jBATS also offers 4 linguistics relations, each of which consists of 10 categories featuring 50 distinguish pairs (with an exception of the *city*:*prefecture* pairing, which contains 47 pairs since there are only 47 prefectures). This gives a total of 97,712 questions for the vector offset method.
* **tokenization friendly** - all the pairs were desinged so that they can be used with a MeCab-like tokenization. Pairs, in which tokenization could introduce ambiguity, were avoided.
* **frequency balanced** - the mean of frequencies from the `Balance Corpus of Conterprorary Written Japanese <http://pj.ninjal.ac.jp/corpus_center/bccwj/en/>`_ and the `Mainichi Newspaper <http://www.nichigai.co.jp/sales/mainichi/mainichi-data.html>`_ corpus were computed and only items with mean frequencies between 1,000 and 10,000 were chosen, whenever possible.
* **alternative spelling** - the correct answers are provided in both *kanji* and *hiragana*/*katakana* forms. For example, 出す is being represented as 出す and だす.
* **multiple correct answers** - similarly to BATS, jBATS is not penalizing the model for the complicity of human language. For example, 服, アパレル and お召し物  will all be listed among others as hypernyms of スカート.


.. include:: ./files/assets/files/jbats-table.html


--------------------
Performance on jBATS
--------------------

jBATS was initially used to evaluate the performance of the subcharacter and character level models in Japanese [#f7]_. These models take advantage of the information in Chinese characters - *kanji* (SG + *kanji*) and their components, called *bushu* (SG + *kanji* + *bushu*). The overall performance of both models was compared with the traditional Skip-Gram model (SG) and FastText.

.. figure:: /assets/img/jbats.png

   Figure 2. Performance on jBATS: SG, SG + *kanji*, and SG + *kanji* + *bushu* as measure by the 3CosAdd (upper figure) and LRCos (lower figure) methods.


Including the *bushu* information has proven to be beneficial especially for the inflectional and derivational relations, where most tokens were written using a single *kanji* or a *kanji* affix, related to the word meaning. The smallest improvement was observed for the lexicographic semantics categories, where traditional Skip-Gram model performed better in most cases. Semantic relations were also the most difficult to capture, which is consistent with the finidings for English in Gladkova et al. (2016) [#f2]_ and Drozd et al. (2016) [#f5]_. Moreover, the LRCos method [#f5]_ yielded overall better results than 3CosAdd achieving up to **over 36% better accuracy**, which was also shown for English in Drozd et al. (2016) [#f5]_. The overall accuracy on word analogy task (LRCos method) of all the models (including FastText) for different corpus size can be found in Karpinska et al. (2018) [#f7]_


.. rubric:: Footnotes

.. [#f1] Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic Regularities in Continuous Space Word Representations. In Proceedings of NAACL-HLT 2013 (pp. 746–751). Atlanta, Georgia, 9–14 June 2013. Retrieved from https://www.aclweb.org/anthology/N13-1090

.. [#f2] Gladkova, A., Drozd, A., & Matsuoka, S. (2016). Analogy-based detection of morphological and semantic relations with word embeddings: what works and what doesn’t. In Proceedings of the NAACL-HLT SRW (pp. 47–54). San Diego, California, June 12-17, 2016: ACL. https://www.aclweb.org/anthology/N/N16/N16-2002.pdf

.. [#f3] The abstract of the original paper has a mistake: the total number of questions in BATS is 99,200.

.. [#f5] Drozd, A., Gladkova, A., & Matsuoka, S. (2016). Word embeddings, analogies, and machine learning: beyond king - man + woman = queen. In Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical Papers (pp. 3519–3530). Osaka, Japan, December 11-17. https://www.aclweb.org/anthology/C/C16/C16-1332.pdf

.. [#f6] Rogers, A., Drozd, A., & Li, B. (2017). The (Too Many) Problems of Analogical Reasoning with Word Vectors. In Proceedings of the 6th Joint Conference on Lexical and Computational Semantics (* SEM 2017) (pp. 135–148). http://www.aclweb.org/anthology/S17-1017

.. [#f7] Karpinska, M., Li, B., Rogers, A., & Drozd, A. (2018) Subcharacter information in Japanese embeddings: when is it worth it? In In Proceedings of the Workshop on Relevance of Linguistic Structure in Neural Architectures for NLP (RELNLP) 2018, to appear. ACL, 2018.
