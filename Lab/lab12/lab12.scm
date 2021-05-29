(define (tail-replicate x n) 
    (define (help-tail x lst1 n)
        (if (= n 0) 
            lst1
            (help-tail x (cons x lst1) (- n 1))
        )
     )
    (help-tail x nil n)
)

(define-macro (def func args body)
   ; `(define ,func (lambda ,args ,body))
    (list 'define func (list 'lambda args body))
)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let (
           (y (repeatedly-cube (- n 1) x))
           )
            (* y y y))
   )
)


    
    
    
