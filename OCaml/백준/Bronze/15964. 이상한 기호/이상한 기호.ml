let st_oper a b = 
    (a + b) * (a - b)
let () = 
    let a, b =
        match String.split_on_char ' ' (read_line()) with
        | [a; b] -> (int_of_string a, int_of_string b)
        | _ -> failwith "Invalid input"
    in
    let res = st_oper a b in
    print_int res