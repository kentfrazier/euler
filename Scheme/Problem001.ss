(define (multiples limit)
  (define (is-multiple? x)
    (if (or (= (remainder x 3) 0)
            (= (remainder x 5) 0))
           #t
           #f))
  (define (mult-iter number sum)
    (if (>= number limit)
        sum
        (mult-iter (+ number 1)
                   (if (is-multiple? number)
                       (+ sum number)
                       sum))))
  (mult-iter 1 0))
(multiples 1000)