# Hotel-Reviews-Classification
<br>How genuine are the reviews? Are they positive or negative?
<br>Find out with this classifier.
<br>It's a Naive Bayes classifier that classifies hotel reviews in class Fake/True and Positive/Negative.

Training file format:
File train-labeled.txt containing labeled training data with a single training instance (hotel review) per line. The first 3 tokens in each line are:
<ol>
<li>a unique 7-character alphanumeric identifier
<li>a label True or Fake
<li>a label Pos or Neg
</ol>
These are followed by the text of the review.
<br>
<br>
<table style="width:50%">
<caption>Results</caption>
<tr>
  <td>Reference Mean F1</td><td>My Mean F1</td>
</tr>
<tr>
<td>0.8937280481685901</td><td>0.9047</td>
</tr>

</table>
<br> Future scope :  It can be extended to classify any types of reviews.
<br>
<br>
For more details refer : http://ron.artstein.org/csci544-2018/coding-2.html and https://github.com/visrahane/Hotel-Reviews-Classification/blob/master/Description.pdf
