---
title: WebR in Quarto HTML Documents
format: html
engine: knitr
webr: 
  show-startup-message: false
  show-header-message: false
filters:
  - webr
---



## Webr
This is a webr-enabled code cell in a Quarto HTML document.

```{webr-r}
fit = lm(mpg ~ am, data = mtcars)
summary(fit)
```

## Comments
include-in-header: [webr-serviceworker.js, webr-worker.js]    
