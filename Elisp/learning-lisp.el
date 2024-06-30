(setq my-list '(1 2 3 4))

(dolist (element my-list)
  (when (= (mod element 2) 0)
    (print element)))


;; local variables

(let (some-var)
  (when (null some-var)
    (message "var is null")))


;; if statement

(let ((some-var 0)
      (some-var-2 1))
  (if (null some-var)
      (message "impossibile")
    (message  "yes")))

;; mustu se progn for multiple true function

(let ((some-var 0)
      (some-var-2 1))
  (if (null some-var)
      (message "impossibile")
    (message  "yes")
    (message "no")
    ))


;; sums even in the list

(defun sum-evens (list)
  (let ((sum 0))
    (dolist (element list)
      (when (= (mod element 2) 0)
        (setq sum (+ sum element))))
    sum))

(sum-evens my-list)


;; interactive function

(defun cheap-count-words ()
  (interactive)
  (let ((words 0))
    (save-excursion (goto-char (point-min))
                    (while (forward-word)
                      (setq words (+ 1 words))))
    (message (format "words in buffer: %s" words))
    words))

;; Minor mode

(defvar boolcase-mode-words '("true" "false")
  "Words to capitalize")

(defun boolcase-mode-fix ()
  (save-excursion
    (copy-region-as-kill (point)
                         (progn (backward-sexp) (point)))
    (when (member (current-kill 0) boolcase-mode-words)
      (capitalize-word 1))
    ;; remove element from this killring
    (setq kill-ring (cdr kill-ring))
    ))

(defun boolcase-mode-check ()
  "check if capitalize or not"
  (if (= last-command-event ?e)
      (boolcase-mode-fix)
    ))

(define-minor-mode boolcase-mode
  "Automatically capitalize booleans"
  :lighter " BC"
  (if boolcase-mode
      (add-hook 'post-self-insert-hook
                'boolcase-mode-check nil t)
    (remove-hook 'post-self-insert-hook
                 'boolcase-mode-check)
    ))


;; other lists CON CELS

(setq list '(pizza pineapple shrek))

(car list)
(cdr list)

(cdr (cdr list))

;; dotted notations

(setq another '(pizza . (pineapple . (shrek))))

(cdr another)

(setq another '(pizza . (pineapple . (shrek))))

;; alist and org-combine-plists

(setq test-list '(
                  (prova1 . 1)
                  (prova2 . 2)
                  ))

;; must be reverse

(setq test-list-without-dot '(
                              (1 prova1)
                              (2 prova2)
                              ))

;; check association
(cdr (assoc 'prova1 test-list))

;; return nil if missing
(cdr (assoc 'prova3 test-list))

;; difference equal and eq (need to be the exact same object)

(equal "hey" "hey")
(eq "hey" "hey")

(let ((test "prova"))
  (eq test test))


;; plist

(setq test-plist '(shrek fiona blue red sky floor))

(plist-get test-plist 'shrek)

(plist-get test-plist 'red) ; return nil, no association

(plist-get test-plist 'blue)

(plist-get '(foo 1 bar) 'bar) ;; return nil

(plist-get '(foo 1 bar (1 2 3)) 'bar) ;; return (1 2 3)

;; why?
;; equal to association in a sense, importance of costintency
;; they are used in text-properties-at to list text properties


;; weird , in list with ` (backquote)

(equal `(1 2 3) '(1 2 3)) ; return True


;; they are equal
(setq numbers '(1 2 3))

(setq numbers `(1 2 3))

(setq other-number '(4 5 6))

(setq number `(1 2 3 ,other-number))

`(one plus two is ,(+ 1 2))

;; remove () for listt using @ for splice
`(lets count 1 2 3 ,@numbers)

;; ' instead of ` securety problem
