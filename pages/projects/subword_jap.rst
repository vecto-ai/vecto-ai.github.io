.. title: Japanese Subword-level word embeddings
.. slug: subword_jap
.. tags: mathjax
.. use_math: true
.. hidetitle: True
.. pretty_url: True
.. template: BATS.tmpl

.. role:: emph



======================================
Japanese Subword-level word embeddings
======================================

Languages with logographic writing systems present a difficulty for traditional character-level models.
Leveraging the subcharacter information was recently shown to be beneficial for a number of intrinsic and extrinsic tasks in Chinese.
We examine whether the same strategies could be applied for Japanese, and contribute a new analogy dataset (jBATS_) for this language.


----------------------------------------------
Three levels of Japanese word embedding models
----------------------------------------------


.. figure:: /assets/img/subword/jap/models.png
   :width: 600 px
   :align: center

   Figure 1. Model architecture of SG, SG+kanji, and SG+kanji+bushu [#f3]_ .
   Example sentence: いつも~~忙しい~~仲間~~と~~やっと~~会え~~た (I have finally met with my busy colleague.), window size 2.


..
   .. figure:: /assets/img/subword/jap/bushu_example.png
      :width: 400 px
      :align: center

      Figure 1. Example sentence with shallow decomposition.


The overall achitecture of Japanese embedding models are shown in Figure 1.
We investigate the effect of explicit inclusion of kanjis and kanji components (bushu).

In Figure 1-a, we use only word-level information. The model is the same as Skip-Gram (SG) [#f1]_.

In Figure 1-b, to take individual kanji into account,
we modified SG by summing the target word vector with vectors of its constituent characters.
This can be regarded as a special case of FastText [#f2]_, where the minimal n-gram size and maximum n-gram size are both set to $1$.
We refer to this model as SG+kanji

In Figure 1-c, Similarly to characters, we sum the vector of the target word, its constituent characters,
and their constituent bushu to incorporate the bushu information.
For example, the vector of the word 仲間, the vectors of characters 仲 and 間, and the vectors of bushu 亻, 中, 門, 日 are summed to predict the contextual words.
We refer to this model as SG+kanji+bushu.

.. Those kanji components often contain semantically meaningful components.
.. As shown in Figure 2, in pre-processing step, we prepend each kanji a list of bushu.


-----
Usage
-----

We implement all the subword-level models using Chainer deep learning framework.

Sample script for training Japanese word-level word embeddings (SG):

:code:`python3 -m vecto.embeddings.train_word2vec --path_corpus $path_corpus --path_out $path_out --subword none --language jap`


Sample script for training Japanese subword-level word embeddings (SG+kanji):

:code:`python3 -m vecto.embeddings.train_word2vec --path_corpus $path_corpus --path_out $path_out --subword sum --language jap`

Sample script for training Japanese subword-level word embeddings (SG+kanji+bushu):

:code:`python3 -m vecto.embeddings.train_word2vec --path_corpus $path_corpus --path_out $path_out --subword sum --language jap --path_word2chars path_word2chars`



-----------
Experiments
-----------


.. figure:: /assets/img/subword/jap/similarity.png
   :width: 600 px
   :align: center

   Table 1. Spearman's correlation with human similarity judgements.


Table 1 shows the results on word similarity task (jSIM_). Models are trained on the full Mainichi corpus, a half Mainichi corpus, and Wikipedia.
The strongest effect for inclusion of bushu is observed in the OOV condition: in all datasets the Spearman's correlations are higher for SG+kanji+bushu
than for other SG models, which suggests that this information is indeed meaningful and helpful.

.. _jSIM: /projects/jSIM

.. figure:: /assets/img/subword/jap/analogy.png
   :width: 300 px
   :align: center

   Table 2. Word analogy task accuracy (LRCos).


Table 2 shows the results on 4 categories of word analogy task (jBATS_).
The morphology categories behave similarly to adjectives in the similarity task:
the SG+kanji beats the original SG by a large margin on inflectional and derivational morphology categories,
and bushu improve accuracy even further.

.. _jBATS: /projects/jBATS

----------
Conclusion
----------

We show that Japanese subword-level word embeddings do improve the performance of Skip-Gram model in kanji-rich domains
and for tasks relying on mostly single-kanji vocabulary or morphological patterns.

.. rubric:: Footnotes

.. [#f1] Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic Regularities in Continuous Space Word Representations. In Proceedings of NAACL-HLT 2013 (pp. 746–751). Atlanta, Georgia, 9–14 June 2013. Retrieved from https://www.aclweb.org/anthology/N13-1090
.. [#f2] Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). Enriching Word Vectors with Subword Information. Transactions of the Association for Computational Linguistics, 5, 135-146. http://www.aclweb.org/anthology/Q17-1010
.. [#f3] Karpinska, M., Li, B., Rogers, A., & Drozd, A. (2018) Subcharacter information in japanese embeddings: when is it worth it? In Proceedings of the Workshop on Relevance of Linguistic Structure in Neural Architectures for NLP (RELNLP) 2018, to appear. ACL, 2018.


