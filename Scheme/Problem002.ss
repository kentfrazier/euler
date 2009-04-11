(define (even-fib-sum limit)
  (define (even? x)
    (if (= (remainder x 2) 0)
        #t
        #f))
  (define (fib-iter 1st 2nd sum)
    (define fib (+ 1st 2nd))
    (if (> fib limit)
        sum
       (fib-iter 2nd
                 fib 
                 (if (even? fib)
                     (+ sum fib)
                     sum))))
  (fib-iter 1 1 0))
(even-fib-sum 4000000)