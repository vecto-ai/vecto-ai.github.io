.. title: Subword-level word embeddings
.. slug: subword
.. tags: mathjax
.. use_math: true
.. hidetitle: True
.. pretty_url: True
.. template: BATS.tmpl

.. role:: emph

=============================
Subword-level word embeddings
=============================

Subword-level information is crucial for capturing the meaning and morphology of words, especially for out-of-vocabulary entries.
We investigate different subword-level composition functions,
and systematically compare them on a range of NLP tasks.

-----------------------------------------
Motivation for using subword-level models
-----------------------------------------
* Word-level models such as Word2Vec [#f1]_ consider word as smallest unit, and often ignores the morphology information.

* Most of them could not assign meaningful vectors to out-of-vocabulary (OOV) words.

-----------------------------------------
FastText (summation composition function)
-----------------------------------------
FastText [#f2]_ is probably the most influential and effective recent model. It represents each word as a
bag-of-character n-grams. Representations for character n-grams, once they are learned, can be combined (via
simple summation) to represent out-of-vocabulary (OOV) words.

More details about FastText can be found here https://fasttext.cc

------------------------------------------------------
CNN- and RNN-based subword-level composition functions
------------------------------------------------------

We contribute to the discussion of composition functions for constructing subword-level embeddings.
We propose CNN- and RNN-based subword-level word embedding models, which can embed
arbitrary character sequences into vectors.
The overall achitecture of the original Skip-Gram, FastText, and our subword-level models are shown in the figure below.

.. figure:: /assets/img/subword/models.png
   :width: 600 px
   :align: center

   Figure 1. llustration of original Skip-Gram and subword-level models. (Li et al., 2018) [#f3]_

We also propose a hybrid training scheme, which makes these neural networks directly integrated into Skip-Gram model.
We train two sets of word embeddings simultaneously:
one is from a lookup table as in traditional Skip-Gram,
and another is from convolutional or recurrent neural network.
The former is better at capturing semantic similarity.
The latter is more focused on morphology and can learn embeddings for OOV words.

-----
Usage
-----

We implement all the subword-level models (including FastText) using Chainer deep learning framework.

Sample script for training word-level word embeddings:

:code:`python3 -m vecto.embeddings.train_word2vec --path_corpus $path_corpus --path_out $path_out`


Sample script for training subword-level word embeddings (FastText, Summation):

:code:`python3 -m vecto.embeddings.train_word2vec --path_corpus $path_corpus --path_out $path_out --subword sum`

Sample script for training subword-level word embeddings (CNN):

:code:`python3 -m vecto.embeddings.train_word2vec --path_corpus $path_corpus --path_out $path_out --subword cnn1d``

Sample script for training subword-level word embeddings (Bi-directional LSTM):

:code:`python3 -m vecto.embeddings.train_word2vec --path_corpus $path_corpus --path_out $path_out --subword bilstm`


-----------
Experiments
-----------

For hybrid training scheme, we denote the embeddings that come from word vector lookup table as "Model\ :sub:`word`",
and the embeddings which come from the composition function as "Model\ :sub:`subword`".
We denote the vanilla (non-hybrid) models as "Model\ :sub:`vanilla`".
The "FastText\ :sub:`external`" is the public available FastText embeddings,
which are trained on the full Wikipedia corpus. We also test the version where OOV words are expanded,
and denote as "Model\ :sub:`+OOV`".

.. figure:: /assets/img/subword/similarity_analogy.png
   :width: 600 px
   :align: center

   Table 1. Results on word similarity and word analogy datasets.
   Model combinations are denoted as gray rows,
   and best results among them are marked Bold. Rare words dataset in blue column have 43.3% OOV rate,
   while other word similarity datasets have maximum 4.6% OOV rate. Morphology related categories are denoted as almond columns.


CNN\ :sub:`subword` and RNN\ :sub:`subword` are more focused on word morphology, and thus do not perform well on word similarity task.
However, compared to Skip-Gram, CNN\ :sub:`word` and RNN\ :sub:`word` (the versions with word vector lookup table) achieve comparable or even better results.

On word analogy datasets, the inflectional and derivational morphology categories demonstrate the effectiveness of subword-level word models.
It is especially obvious on derivation morphology category,
where Skip-Gram only achieves 9.6\% accuracy and subword-level models achieve minimal 57.8\% accuracy (excluding the lookup table versions)

.. figure:: /assets/img/subword/vis.png
   :width: 700 px
   :align: center

   Figure 2. Visualization of learned word embeddings, each dot represents a word,
   different colors represent different affixes.


We test the ability of subword-level embeddings to predict what affix is present in a morphologically complex word.
Figure 2 shows a t-SNE projection of the words with different affixes.
It is clear that both CNN and RNN are able to distinguish different derivation types, with the advantage of the former.

..
    .. figure:: /assets/img/subword/affix_sl.png
       :width: 400 px
       :align: center

       Table 2. Results on affix prediction (AP) and sequence labeling (SL) tasks. Sequence labeling tasks have 16.5%, 27.1%, 28.5% OOV rate respectively.


----------
Conclusion
----------

We implemented and evaluated several types of composition functions for subword-level elements (characters and character n-grams) in the context of training word embeddings in Skip-Gram-like model.

We show that morphological information can be captured efficiently.
The resulting embeddings also achieved high accuracy on a range of benchmarks and are particularly promising for datasets with high OOV rate.

.. rubric:: Footnotes

.. [#f1] Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic Regularities in Continuous Space Word Representations. In Proceedings of NAACL-HLT 2013 (pp. 746–751). Atlanta, Georgia, 9–14 June 2013. Retrieved from https://www.aclweb.org/anthology/N13-1090
.. [#f2] Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017). Enriching Word Vectors with Subword Information. Transactions of the Association for Computational Linguistics, 5, 135-146. http://www.aclweb.org/anthology/Q17-1010
.. [#f3] Li, B., Drozd, A., Liu, T., & Du, X. (n.d.). Subword-level Composition Functions for Learning Word Embeddings. In Proceedings of the Second Workshop on Subword/Character LEvel Models (pp. 38–48). New Orleans, Louisiana, June 6, 2018. http://www.aclweb.org/anthology/W18-1205
