from sklearn.metrics import (
    roc_auc_score, roc_curve, average_precision_score,
    accuracy_score, matthews_corrcoef, f1_score, precision_score, recall_score
)


def calc_metrics(y_true, y_score, threshold = 0.5):
    y_score = y_score > threshold
    accuracy = accuracy_score(y_true, y_score)
    f1 = f1_score(y_true, y_score)
    mcc = matthews_corrcoef(y_true, y_score)
    precision = precision_score(y_true, y_score)
    recall = recall_score(y_true, y_score)
    return accuracy, f1, mcc, precision, recall


def calc_f1_precision_recall(y_true, y_predict):
    """  """
    # accuracy = accuracy_score(y_true, y_predict)
    f1 = f1_score(y_true, y_predict)
    precision = precision_score(y_true, y_predict)
    recall = recall_score(y_true, y_predict)
    return f1, precision, recall


def find_threshold(y_true, y_score, alpha = 0.05):
    """ return threshold when fpr <= 0.05 """
    fpr, tpr, thresh = roc_curve(y_true, y_score)
    for i, _fpr in enumerate(fpr):
        if _fpr > alpha:
            return thresh[i-1]


def roc(y_true, y_score):
    fpr, tpr, thresh = roc_curve(y_true, y_score)
    roc = roc_auc_score(y_true, y_score)
    return roc, fpr, tpr


def auc_aupr(label, pred):
	label = label.reshape(-1)
	pred = pred.reshape(-1)
	return roc_auc_score(label, pred), average_precision_score(label, pred)