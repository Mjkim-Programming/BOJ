use std::io::{self, BufRead, BufWriter, Write};

const MOD: i64 = 1_000_000_007;

struct SegmentTree {
    tree: Vec<i64>,
    lazy: Vec<(i64, i64)>, // (mul, add)
}

impl SegmentTree {
    fn new(arr: &Vec<i64>) -> Self {
        let n = arr.len() - 1;
        let size = 4 * n;
        let mut st = SegmentTree {
            tree: vec![0; size],
            lazy: vec![(1, 0); size],
        };
        st.init(1, 1, n, arr);
        st
    }

    fn init(&mut self, node: usize, s: usize, e: usize, arr: &Vec<i64>) -> i64 {
        if s == e {
            self.tree[node] = arr[s] % MOD;
            return self.tree[node];
        }
        let m = (s + e) / 2;
        self.tree[node] = (self.init(node*2, s, m, arr) + self.init(node*2+1, m+1, e, arr)) % MOD;
        self.tree[node]
    }

    fn push(&mut self, node: usize, s: usize, e: usize) {
        let (a, b) = self.lazy[node];
        if a == 1 && b == 0 { return; }
        if s != e {
            for &child in &[node*2, node*2+1] {
                let (a2, b2) = self.lazy[child];
                self.lazy[child] = (a * a2 % MOD, (a * b2 + b) % MOD);
            }
        }
        self.tree[node] = (a * self.tree[node] + (e - s + 1) as i64 * b) % MOD;
        self.lazy[node] = (1, 0);
    }

    fn update(&mut self, node: usize, s: usize, e: usize, l: usize, r: usize, mul: i64, add: i64) {
        self.push(node, s, e);
        if r < s || e < l { return; }
        if l <= s && e <= r {
            let (a, b) = self.lazy[node];
            self.lazy[node] = (a * mul % MOD, (b * mul + add) % MOD);
            self.push(node, s, e);
            return;
        }
        let m = (s + e) / 2;
        self.update(node*2, s, m, l, r, mul, add);
        self.update(node*2+1, m+1, e, l, r, mul, add);
        self.tree[node] = (self.tree[node*2] + self.tree[node*2+1]) % MOD;
    }

    fn query(&mut self, node: usize, s: usize, e: usize, l: usize, r: usize) -> i64 {
        self.push(node, s, e);
        if r < s || e < l { return 0; }
        if l <= s && e <= r { return self.tree[node]; }
        let m = (s + e) / 2;
        (self.query(node*2, s, m, l, r) + self.query(node*2+1, m+1, e, l, r)) % MOD
    }
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let mut arr: Vec<i64> = vec![0];
    arr.extend(
        lines.next().unwrap().unwrap()
            .trim().split_whitespace()
            .map(|x| x.parse::<i64>().unwrap())
    );

    let mut st = SegmentTree::new(&arr);

    let m: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let stdout = io::stdout();
    let mut out = BufWriter::new(stdout.lock());

    for _ in 0..m {
        let line = lines.next().unwrap().unwrap();
        let mut iter = line.trim().split_whitespace();
        let op: usize = iter.next().unwrap().parse().unwrap();
        let x: usize = iter.next().unwrap().parse().unwrap();
        let y: usize = iter.next().unwrap().parse().unwrap();

        if op != 4 {
            let v: i64 = iter.next().unwrap().parse().unwrap();
            match op {
                1 => st.update(1, 1, n, x, y, 1, v),
                2 => st.update(1, 1, n, x, y, v, 0),
                3 => st.update(1, 1, n, x, y, 0, v),
                _ => {}
            }
        } else {
            writeln!(out, "{}", st.query(1, 1, n, x, y)).unwrap();
        }
    }
}
