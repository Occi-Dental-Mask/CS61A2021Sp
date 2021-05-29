(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
 (car (cdr s))
 )

(define (caddr s) 
 (car (cddr s))
 )

(define (sign val) 'YOUR-CODE-HERE
    (cond
      ((= 0 val) 0)
      ((> val  0) 1)
      (else -1))
)
(define (square x) (* x x))

(define (pow base exp)'YOUR-CODE-HERE
 (cond
  ((= exp 1) base)
  ((= exp 0) 1)
  ((even? exp) (pow (square base) (quotient exp 2)))
  (else  (* (pow (square base) (quotient exp 2)) base))
))
