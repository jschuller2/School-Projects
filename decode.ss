; *********************************************
; *  314 Principles of Programming Languages  *
; *  Fall 2017                                *
; *  Author: Ulrich Kremer 
; * JARED SCHULLER                   *
; *********************************************
;; -----------------------------------------------------
;; ENVIRONMENT
;; contains "ltv", "vtl",and "reduce" definitions
(load "include.ss")

;; contains a test document consisting of three paragraphs. 
(load "document.ss")

;; contains a test-dictionary, which has a much smaller dictionary for testing
;; the dictionary is needed for spell checking
(load "test-dictionary.ss")

;; (load "dictionary.ss") ;; the real thing with 45,000 words


;; -----------------------------------------------------
;; HELPER FUNCTIONS

;; *** CODE FOR ANY HELPER FUNCTION GOES HERE ***
(define prime-list
    (lambda (w n)
      (cond ((null? w) '())
            (else (append (list n) (prime-list (cdr w) n))))))

 (define add0

     (encode-n 0))

   (define add1

     (encode-n 1)) 

   (define add2

     (encode-n 2)) 

   (define add3

     (encode-n 3)) 

   (define add4

     (encode-n 4)) 

   (define add5

     (encode-n 5)) 

   (define add6

     (encode-n 6)) 

   (define add7

     (encode-n 7)) 

   (define add8

     (encode-n 8)) 

   (define add9

     (encode-n 9))

   (define add10

     (encode-n 10)) 

   (define add11

     (encode-n 11))

    (define add12

      (encode-n 12)) 

     (define add13

       (encode-n 13)) 

     (define add14

       (encode-n 14)) 

     (define add15

       (encode-n 15)) 

     (define add16

       (encode-n 16)) 

     (define add17

       (encode-n 17)) 

     (define add18

       (encode-n 18)) 

     (define add19

       (encode-n 19)) 

     (define add20

       (encode-n 20)) 

     (define add21

       (encode-n 21)) 

     (define add22

       (encode-n 22)) 

     (define add23

       (encode-n 23)) 

     (define add24

       (encode-n 24)) 

     (define add25

       (encode-n 25))
     (define encode-p

       (lambda (p encoder)

         (map encoder p)))
 (define parachecker

       (lambda (p)

         (cond ((null? p) '())

               (else (and (parachecker (cdr p)) (spell-checker(car p)))))))
(define decode-count

   (lambda (l)

     (reduce + (map (lambda (x)

                      (if (eq? x #t) 1 0)) l) 0)))

(define index-max

    (lambda (l)

      (define index-max-aux

    (lambda (l i m)

      (cond ((null? l) (cdr m))

            ((> (car l) (car m)) (index-max-aux (cdr l) (+ 1 i) (list (car l) i)))

            (else (index-max-aux (cdr l) (+ 1 i) m)))))

      (cond ((null? l) 0)

            (else (index-max-aux (cdr l) 1 (list (car l) 0))))))
(define Max-Freq

   (lambda (sl) ;; sorted list

       (Max-Freq-Aux (car sl) (cdr sl) 1 (list '0 '0))))

 

(define Max-Freq-Aux

    (lambda (ltr sl cntr maxl)

            (cond ((null? sl) (cond ((> cntr (car(cdr maxl))) ltr) (else (car(cdr maxl))))  )

                      ((eq? ltr (car sl) )  (Max-Freq-Aux ltr (cdr sl) (+ 1 cntr) maxl))

                      ( (> cntr (car maxl)) (Max-Freq-Aux (car sl) (cdr sl) 1 (list cntr ltr) ) )

                      ( (Max-Freq-Aux (car sl) (cdr sl) 1 maxl) ) ) ) )

 

(define shift-E

   (lambda (n)

     (list(modulo (- 30 n) 26))))
 (define DecoderSP

     (lambda(p)

    (Gen-Decoder-A p)))
 (define DecoderFA

    (lambda (p)

      (Gen-Decoder-B p)))
;; -----------------------------------------------------
;; SPELL CHECKER FUNCTION

;;check a word's spell correctness
;;INPUT:a word(a global variable "dictionary" is included in the file "test-dictionary.ss", and can be used directly here)
;;OUTPUT:true(#t) or false(#f)
(define spell-checker

  (lambda (w)

    (define spell-checker-aux

  (lambda (w d)

 

    (cond ((null?  d) #f)

          ((equal? w (list (car d))) #t)

          (else (spell-checker-aux w (cdr d)) ))))

    (length dictionary)

    (spell-checker-aux (list w) dictionary)

    ))

;; -----------------------------------------------------
;; ENCODING FUNCTIONS

;;generate an Caesar Cipher single word encoders
;;INPUT:a number "n"
;;OUTPUT:a function, whose input is a word, and output is the encoded word
(define encode-n
  (lambda (n);;"n" is the distance, eg. n=3: a->d,b->e,...z->c
    (lambda (w);;"w" is the word to be encoded
     'SOME_CODE_GOES_HERE ;; *** FUNCTION BODY IS MISSING ***
      )))

;;encode a document
;;INPUT: a document "d" and a "encoder"
;;OUTPUT: an encoded document using a provided encoder
(define encode-d;;this encoder is supposed to be the output of "encode-n"
  (lambda (d encoder)
    'SOME_CODE_GOES_HERE ;; *** FUNCTION BODY IS MISSING ***
    ))
    
;; -----------------------------------------------------
;; DECODE FUNCTION GENERATORS
;; 2 generators should be implemented, and each of them returns a decoder

;;generate a decoder using brute-force-version spell-checker
;;INPUT:an encoded paragraph "p"
;;OUTPUT:a decoder, whose input=a word, output=decoded word
 (define Gen-Decoder-A

    (lambda (p)

      (index-max(map decode-count

           (list

            (map spell-checker (encode-p p add0))

            (map spell-checker (encode-p p add1))

            (map spell-checker (encode-p p add2))

            (map spell-checker (encode-p p add3))

            (map spell-checker (encode-p p add4))

            (map spell-checker (encode-p p add5))

            (map spell-checker (encode-p p add6))

            (map spell-checker (encode-p p add7))

            (map spell-checker (encode-p p add8))

            (map spell-checker (encode-p p add9))

            (map spell-checker (encode-p p add10))

            (map spell-checker (encode-p p add11))

            (map spell-checker (encode-p p add12))

            (map spell-checker (encode-p p add13))

            (map spell-checker (encode-p p add14))

            (map spell-checker (encode-p p add15))

            (map spell-checker (encode-p p add16))

           (map spell-checker (encode-p p add17))

            (map spell-checker (encode-p p add18))

            (map spell-checker (encode-p p add19))

            (map spell-checker (encode-p p add20))

            (map spell-checker (encode-p p add21))

            (map spell-checker (encode-p p add22))

            (map spell-checker (encode-p p add23))

            (map spell-checker (encode-p p add24))

            (map spell-checker (encode-p p add25))

            )))

      ))

;;generate a decoder using frequency analysis
;;INPUT:same as above
;;OUTPUT:same as above
(define Gen-Decoder-B

    (lambda (p)

      (shift-E (Max-Freq(sort (map ltv (flatten p)) <)))))

;; -----------------------------------------------------
;; CODE-BREAKER FUNCTION

;;a codebreaker
;;INPUT: an encoded document(of course by a Caesar's Cipher), a decoder(generated by functions above)
;;OUTPUT: a decoded document
 (define Code-Breaker

    (lambda (d decoder)

      (define decoder-fin

        (lambda (i)

          (cond ((equal? i '(0)) (encode-d d add0))

                ((equal? i '(1)) (encode-d d add1))

                ((equal? i '(2)) (encode-d d add2))

                ((equal? i '(3)) (encode-d d add3))

                ((equal? i '(4)) (encode-d d add4))

                ((equal? i '(5)) (encode-d d add5))

                ((equal? i '(6)) (encode-d d add6))

                ((equal? i '(7)) (encode-d d add7))

                ((equal? i '(8)) (encode-d d add8))

                ((equal? i '(9)) (encode-d d add9))

                ((equal? i '(10)) (encode-d d add10))

                ((equal? i '(11)) (encode-d d add11))

                ((equal? i '(12)) (encode-d d add12))

                ((equal? i '(13)) (encode-d d add13))

                ((equal? i '(14)) (encode-d d add14))

                ((equal? i '(15)) (encode-d d add15))

                ((equal? i '(16)) (encode-d d add16))

                ((equal? i '(17)) (encode-d d add17))

                ((equal? i '(18)) (encode-d d add18))

                ((equal? i '(19)) (encode-d d add19))

                ((equal? i '(20)) (encode-d d add20))

                ((equal? i '(21)) (encode-d d add21))

                ((equal? i '(22)) (encode-d d add22))

                ((equal? i '(23)) (encode-d d add23))

                ((equal? i '(24)) (encode-d d add24))

                ((equal? i '(25)) (encode-d d add25)))))

      (decoder-fin (decoder (car d)))))

;; -----------------------------------------------------
;; EXAMPLE APPLICATIONS OF FUNCTIONS
;;(spell-checker '(h e l l o))
;;(define add5 (encode-n 5))
;;(encode-d document add5)
;;(define decoderSP1 (Gen-Decoder-A paragraph))
;;(define decoderFA1 (Gen-Decoder-B paragraph))
;;(Code-Breaker document decoderSP1)
