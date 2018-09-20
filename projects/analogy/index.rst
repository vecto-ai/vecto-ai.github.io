.. title: Analogical reasoning with word embeddings
.. slug: analogy
.. hidetitle: True
.. pretty_url: True
.. tags: mathjax
.. use_math: true

=======================================================
The latest in analogical reasoning with word embeddings
=======================================================

.. |nbsp| unicode:: 0xA0
.. |nn| unicode:: &#xd;

|

|

Analogical reasoning has been a "poster child" task for word embeddings ever since the introduction of word2vec. Even at this  point, most papers introducing new word embedding models use the Google test set as intrinsic  evaluation benchmark. The big finding by `Mikolov et al. (2013) <https://www.aclweb.org/anthology/N13-1090>`_ was that linear vector offsets seem to mirror linguistic relations, and can be used to perform analogical reasoning.

.. figure:: /assets/img/queen.png
   :height: 100 px
   :align: center

   Linear vector offsets as model of linguistic relations (Mikolov et al., 2013)

For example, consider a pair of words *a : a' :: b : b* such as *man: woman :: king : queen*. Mikolov et al. proposed that the *b'* word could be found with the help of the offset between the word vectors *b* and *a*. In this case, the word vector *queen* should be the vector that is the closest to the result of calculation *king - man + woman*.

 .. $$b'=argmax_{~d\in{V}}(cos(b',b-a+a'))$$

However, multiple studies have since highlighted considerable problems with this approach, including 5 studies by `the Vecto team <http://vecto.space/team>`_. This page summarizes the main takeaways from these studies:

|

|

.. container:: row

   .. class:: row

     .. class:: col-4

        .. figure:: /assets/img/bats_stats.png
           :height: 200 px
           :class: margin-right

     .. class:: col

        The Google test set is heavily unbalanced (roughly 50% of all the semantic questions are targeting the same country:capital relation). We have developed the Bigger Analogy Test Set (BATS) that covers 40 relations, balanced across inflectional  morphology, derivational morphology, encyclopedic and lexicographic semantics. This dataset shows that most relations not in the original Google test set are not well detected with GloVe (and the overall pattern of performance of the latter is not dissimilar from simple SVD-based representations). Lexicographic semantics and derivational morphology were particularly difficult, with GloVe accuracy not reaching even 10%.
        `Project page <http://vecto.space/projects/BATS/>`_, |nbsp| `pdf <http://www.aclweb.org/anthology/N16-2002>`_

|

|

.. container:: row

   .. class:: row

     .. class:: col-4

        .. figure:: /assets/img/lrcos.png
           :height: 160 px
           :class: margin-right

     .. class:: col

        The analogy task as originally formulated by Mikolov ("king - man + woman = queen") underestimates the amount of information about linguistic relations that can be retrieved from a given representation. We proposed an alternative LRCos method that reformulates the task in a way that allows leveraging machine learning. This method gained a significant boost in performance on BATS (up to 30% gain for some relations and embeddings).
        `pdf <http://www.aclweb.org/anthology/C16-1332>`__

|

|

.. container:: row

   .. class:: row

     .. class:: col-4

        .. figure:: /assets/img/honest.png
           :height: 150 px
           :class: margin-right

     .. class:: col

        At least a part of the problem with the original word analogy task stems from the linear offset model of linguistic relations. This model is not only linguistically/cognitively improbable, but it also biases the results by the cosine similarity between pairs of input words. We show that the linear offset (and, to a lesser degree, LRCos) has much higher chances of finding the correct answer when the source words are close in the vector space, and that the accuracy of the vector offset method depends dramatically on the exclusion of the input words from the pool of candidate.
        `pdf <http://www.aclweb.org/anthology/S17-1017>`__

|

|

.. container:: row

   .. class:: row

     .. class:: col-4

        .. figure:: /assets/img/crnn.png
           :height: 160 px
           :class: margin-right

     .. class:: col

        Derivational morphology problems in BATS get a significant boost in subword-level models such as FastText.
        `Project page <http://vecto.space/projects/subword/>`__, |nbsp| `pdf <http://www.aclweb.org/anthology/W18-1205>`__


|

|

.. container:: row

   .. class:: row

     .. class:: col-4

        .. figure:: /assets/img/jbats.png
           :height: 200 px
           :class: margin-right

     .. class:: col

        The overall pattern of performance observed for BATS in English conforms to the findings for the Japanese version of BATS. Incoroporation of subcharacter-level information for this language was clearly helpful only for morphological questions
        `Project page <http://vecto.space/projects/jBATS/>`__, |nbsp| `pdf <http://aclweb.org/anthology/W18-2905>`__

|

|
