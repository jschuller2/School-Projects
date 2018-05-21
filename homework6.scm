; Problem 1, scheme macro (firstNon0 <expr1> <expr2> <expr3>)
(define-syntax firstNon0
  (syntax-rules ()
    ((_ expr1 expr2 expr3)
     (if (not (= expr1 0)) expr1
         (if (not (= expr2 0)) expr2
             (if (not (= expr3 0)) expr3 0))))))

(firstNon0 (+ 0 0) (- 1 1) (+ 3 (- 0 3)))

; Problem 2, scheme function (tribonacci n)
; regular recursive tribonacci
(define (tribonacci_ n)
  (cond ((= n 0) 0)
        ((= n 1) 0)
        ((= n 2) 1)
        (else (+ (tribonacci_ (- n 1)) (tribonacci_ (- n 2)) (tribonacci_ (- n 3))))))

(tribonacci_ 10)

; tail recursive tribonacci
(define (trib-iter a b c count)
  (if (= count 0) c
      (if (= (- count 1) 0) b
          (trib-iter (+ a b c) a b (- count 1)))))

(define (tribonacci n)
  (trib-iter 1 0 0 n))
