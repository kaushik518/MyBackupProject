section .data
    array db 5, 3, 8, 1, 4       ; array of 5 elements
    arr_len equ 5
    newline db 10

section .bss
    temp resb 1

section .text
    global _start

_start:
    ; Outer loop (i from 0 to n-1)
    xor r8, r8                  ; r8 = i

outer_loop:
    cmp r8, arr_len
    jge done

    xor r9, r9                  ; r9 = j

inner_loop:
    movzx r10, byte [array + r9]
    movzx r11, byte [array + r9 + 1]
    cmp r9, arr_len - 1
    jge end_inner

    cmp r10, r11
    jle no_swap

    ; swap array[j] and array[j+1]
    mov [temp], r10b
    mov [array + r9], r11b
    mov r10b, [temp]
    mov [array + r9 + 1], r10b

no_swap:
    inc r9
    jmp inner_loop

end_inner:
    inc r8
    jmp outer_loop

done:
    ; Print the sorted array
    xor rsi, rsi               ; index = 0

print_loop:
    cmp rsi, arr_len
    jge exit

    movzx rax, byte [array + rsi]
    add al, '0'                ; convert to ASCII
    mov [temp], al

    ; write(1, temp, 1)
    mov rax, 1                 ; syscall: write
    mov rdi, 1                 ; stdout
    mov rsi, temp              ; address of char
    mov rdx, 1                 ; length
    syscall

    ; write(1, newline, 1)
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall

    inc rsi
    jmp print_loop

exit:
    ; exit(0)
    mov rax, 60
    xor rdi, rdi
    syscall
