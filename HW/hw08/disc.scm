(define (reverse lst)
    (reverse-helper lst nil)
)

(define (reverse-helper lst-change lst-sum)
    (if (eq? lst-change nil) lst-sum
        (reverse-helper (cdr lst-change) (cons (car lst-change) lst-sum ))
    )
)