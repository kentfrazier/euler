(define (max-prime-factor num)
  (define primes '(2))
  (define (is-prime? x prime-list)
    (if (null? prime-list)
        #t
        (if (and (= 0 (remainder x (car prime-list)))
                 (is-prime? x (cdr prime-list)))
                 #f
                 #t)))
  (define (is-factor? x)
    (if (= 0 (remainder num x))
        #t
        #f))
  (define (accumulate-primes n max)
    (cond ((> n num) max)
          (else (if (is-prime? n primes)
                    (cons primes n))
                (accumulate-primes (+ n 2)
                                   (if (is-factor? n)
                                       n
                                       max)))))
  (accumulate-primes 3 1))
               