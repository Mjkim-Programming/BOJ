let () =
    let a = ref 0 in
    let b = ref 0 in
    let set_values () =
        match String.split_on_char ' ' (read_line ()) with
        | [x; y] -> a := int_of_string x; b := int_of_string y
        | _ -> failwith "Invalid input"
    in
    set_values();
    while !a <> 0 && !b <> 0 do
        Printf.printf "%d\n" (!a + !b);
        set_values();
    done