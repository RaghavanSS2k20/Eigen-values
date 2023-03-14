# Eigen maps hackathon

### concepts used
**->** Python
**->** Flask
**->** Pytest
**->** Pytest-cov

## APIs

### ENDPOINT :- /getip
```
  {
    "ip": "192.168.80.1"
  }
```

### ENDPOINT :- /cnn/metrics
```
 {
  "metrics": {
    "accuracy": 0.991100013256073,
    "loss": 0.04238595440983772,
    "val_accuracy": 0.991100013256073,
    "val_loss": 0.04238595440983772
  },
  "model": "CNN"
}
```


### ENDPOINT :- /classifier/metrics
```
{
  "metrics": {
    "Accuracy": 0.9,
    "Confusion Matrix": [
      [
        9,
        0,
        0
      ],
      [
        0,
        11,
        1
      ],
      [
        0,
        2,
        7
      ]
    ],
    "F1-score": 0.9011764705882354,
    "Precision": 0.907051282051282,
    "Recall": 0.898148148148148
  },
  "model": "Decision tree"
}
```

### COVERAGE REPORT
![image](https://user-images.githubusercontent.com/76263002/225035989-8e13f03b-d53f-443e-9eed-69c9fdf406f0.png)





