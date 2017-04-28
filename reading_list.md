sss- Articles
  - [How to improve your reading and understanding of code?](http://stackoverflow.com/questions/1307790/how-to-improve-your-reading-and-understanding-of-code)
    - Take a project (this can be a work project, personal project, open source project, whatever), and start refactoring.
    - ... testing and refactoring. You cannot say: "I understand this code" until you know how to break it with a test.
    - Don't just read open-source code, join one.
    - Other than simple experience leading to reading code better, I suggest attaching a **debugger** to the application, add some break points, and analyze data as it goes through the system. That way you KNOW what is going on, instead of presuming (by logic or any other means) what is going on.
  - [The Best Sources to Study Machine Learning and AI: Quora Session Highlight - Ben Hamner, Kaggle CTO](http://blog.kaggle.com/2017/04/17/the-best-sources-to-study-machine-learning-and-ai-with-ben-hamner-kaggle-cto/)
  - [Wiki - Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)
  - [Why Does Unsupervised Pre-training Help Deep Learning?](http://www.jmlr.org/papers/volume11/erhan10a/erhan10a.pdf)
  - [Effectively Using Matplotlib](http://pbpython.com/effective-matplotlib.html)
    - You can see which ones are available on your system using `plt.style.available`. Using a style is as simple as: `plt.style.use('ggplot')`.
    - I recommend getting in the habit of doing this ... `fig, ax = plt.subplots()` ...
    - `fig, (ax0, ax1) = plt.subplots(nrows=1,ncols=2, sharey=True, figsize=(7, 4))`
    - `fig.canvas.get_supported_filetypes()`
- Videos
  - [Deep Learning School](https://www.bayareadlschool.org/)
    - Nuts and Bolts of Applying Deep Learning - Andrew Ng
      - [video](https://www.youtube.com/watch?v=F1ka6a13S9I)
      - Read 20 papers and implement
    - Introduction to Feedforward Neural Networks - Hugo Larochelle
      - [Slides](https://dl.dropboxusercontent.com/u/19557502/hugo_dlss.pdf)
      - Universal approximation theorem - about single layer model
      - Empirical (structural) risk minimization
      - torch, theano, tensorflow
      - Initialization: can't-do's
      - Baysian Optimization for model selection is mentioned
      - Normalization - not to binary data
      - Decay of learning rate - manual way
      - How-to check gradient implementation
      - **Debugging on small dataset - make sure can overfit very small dataset (~50 samples)**
      - Dropout usually 0.5
      - Batch normalization: when used dropout is less useful.
    - Deep Learning for Computer Vision - Andrej Karpathy
      - [Slides](https://docs.google.com/presentation/d/1Q1CmVVnjVJM_9CDk3B8Y6MWCavZOtiKmOLQ0XB7s9Vg/edit?usp=sharing)
      - 
    - DL for NLP - Richard Socherf
      - [Slides](https://media.wix.com/ugd/142eb4_7581cfcf090e4e31a52599315f77c648.pdf)
      - Outline
        - Words: Word2vec, Glove
        - Sentences: RNN
        - Multiple sentences: Dynamic memory networks
      - Distributional similarity; Cooccurence matrix
      - 
      
   - [Hardcore data science in practice - Mikio Braun (Zalando SE) ](https://www.safaribooksonline.com/library/view/strata-hadoop/9781491944639/video249083.html)
      - Microservice as solution to data science v.s. engineering.

-----

[View Source](https://github.com/yang-zhang/yang-zhang.github.io)

[GitHub](https://github.com/yang-zhang)
