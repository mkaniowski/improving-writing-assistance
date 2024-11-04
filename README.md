
# Improving writing assistance

This project aims to compare the performance of two spell checkers: `py_spellchecker` and `Bhuvana/t5-base-spellchecker`. The comparison is based on various evaluation metrics such as accuracy, precision, recall, and F1 score. The goal is to determine which spell checker is more effective in identifying and correcting misspelled words.


## Dataset

The datasets used in this project include multiple text files containing misspelled words and their correct forms. These files are combined and sampled to create a representative dataset for evaluation. The datasets used are

- `spell-testset1.txt`
- `spell-testset2.txt`

[Link to dataset on kaggle](https://www.kaggle.com/datasets/bittlingmayer/spelling)
## Comparing Results

In this project, we compared the performance of two spell checkers: `py_spellchecker` and `base_spellchecker`. The evaluation metrics used for comparison were accuracy, precision, recall, and F1 score. The results were as follows:

**Accuracy**: `py_spellchecker` achieved an accuracy of `0.73`, significantly higher than `base_spellchecker's` accuracy of `0.09`.

**Precision**: `py_spellchecker` had a precision of `0.5856`, compared to `base_spellchecker's` precision of `0.05`.

**Recall**: `py_spellchecker's` recall was `0.5781`, while `base_spellchecker's` recall was `0.0435`.

**F1 Score**: `py_spellchecker` achieved an F1 score of `0.5808`, whereas `base_spellchecker` had an F1 score of `0.0454`.

From these results, it is evident that `py_spellchecker` outperforms `base_spellchecker` across all metrics. This suggests that `py_spellchecker` is more effective in identifying and correcting misspelled words, making it a more reliable choice for spell checking tasks in this context.
## Findings

The evaluation results show that `py_spellchecker` significantly outperforms `Bhuvana/t5-base-spellchecker` across all metrics. Specifically, `py_spellchecker` achieved an accuracy of 0.73, a precision of 0.5856, a recall of 0.5781, and an F1 score of 0.5808. In contrast, `Bhuvana/t5-base-spellchecker` had an accuracy of 0.09, a precision of 0.05, a recall of 0.0435, and an F1 score of 0.0454. These findings suggest that `py_spellchecker` is a more reliable choice for spell checking tasks in this context.