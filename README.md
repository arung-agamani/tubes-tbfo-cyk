# Tugas Besar 2 Teori Bahasa Formal dan Otomata - Python syntax checker using CYK Algorithm

## Description
Sebuah program syntax checker dan highlighting  bahasa python yang mengimplementasikan Context-Free Grammar.

Program ini menggunakan lexer untuk mengubah input teks menjadi bentuk token untuk parser, dan algoritma CYK untuk mengecek apakah teks tersebut berada dalam bahasa yang didefinisikan oleh Context-Free Grammar dalam bentuk Chomsky Normal Form.

## Bagian-bagian program

1. cyk_parser.py : Bentuk implementasi awal dari algoritma CYK. Hanya bisa memberi jawaban "accepted" atau "rejected".
2. lexer.py : Bentuk implementasi dari lexer, untuk mengubah input teks menjadi token-token yang berada dalam terminal dari CFG. Apabila teks tidak sesuai ketentuan, maka program hanya akan berhenti pada lexer, dan (niscaya) akan memberi informasi terkait letak kesalahan pada input.

## Implementasi

- Program menerima input berupa lexer.txt, grammar.txt, dan input.txt.
- Apabila input teks tidak ada kesalahan pada sintaks dan berada dalam grammar, maka program akan mengembalikan "Bahasa diterima". Apabila tidak, maka program akan menampilkan letak kesalahan.

## Referensi

https://tomassetti.me/guide-parsing-algorithms-terminology/
https://www.pythonmembers.club/2018/05/01/building-a-lexer-in-python-tutorial/
https://github.com/RobMcH/CYK-Parser