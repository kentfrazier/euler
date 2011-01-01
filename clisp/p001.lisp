;If we list all the natural numbers below 10 that are multiples of 3 
;or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
;
;Find the sum of all the multiples of 3 or 5 below 1000.

(defun is-multiple-p (num divisor)
  (zerop (mod num divisor)))

(defun is-multiple-many-p (num divisors)
  (flet ((test-p (divisor) (is-multiple-p num divisor)))
    (some #'test-p divisors)))

(defun filter-multiples (divisors limit)
  (flet ((test-p (num) (is-multiple-many-p num divisors)))
    (loop for i from 1 to limit
          when (test-p i)
          collect i)))

(defun main ()
  (reduce #'+ (filter-multiples '(3 5) 999)))
