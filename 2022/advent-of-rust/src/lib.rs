use std::{path::Path, fs::File, io::BufRead, collections::HashMap};

fn get_shape_score(shape: &str) -> u32 {
    match shape {
        "A" | "X" => 1,
        "B" | "Y" => 2,
        _ => 3,
    }
}

fn get_outcome_score(outcome: &str) -> u32 {
    match outcome {
        "W" => 6,
        "D" => 3,
        _ => 0,
    }
}

fn get_outcome_from_str(outcome: &str) -> &str {
    match outcome {
        "X" => "W",
        "Y" => "D",
        _ => "L",
    }
}

fn get_shape_from_out(outcome: &str, opp: &u32) -> u32 {
    match outcome {
        "D" => opp.clone(),
        "W" => {if opp < &3 {opp + 1} else {1}},
        _ => {if opp > &1 {opp - 1} else {3}},
    }
}

fn calculate_score(opp: &u32, me: &u32) -> u32 {
    let beaters: [u32; 3] = [2,3,1];
    if opp == me { 3 } // draw
    else if beaters[(opp-1) as usize] == *me { 6 } // win
    else { 0 } // loss
}

pub fn day_one<P: AsRef<Path>>(path: P) -> (u32, u32) {
    let file = File::open(path).unwrap();
    let reader = std::io::BufReader::new(file);

    let mut vec = vec![];
    let mut sum = 0 as u32;

    for res in reader.lines() {
        let Ok(line) = res else { vec.push(sum); break; };
        
        match line.parse::<u32>() {
            Ok(num) => sum += num,
            Err(_) => {
                vec.push(sum);
                sum = 0;
            },
        }
    }

    vec.sort_by(|a, b| b.cmp(a));

    (vec[0], vec[0..3].iter().sum())
    
}

pub fn day_two<P: AsRef<Path>>(path: P) -> (u32, u32) {

    let file = File::open(path).unwrap();
    let reader = std::io::BufReader::new(file);

    let mut score_1 = 0 as u32;
    let mut score_2 = 0 as u32;

    for res in reader.lines() {
        let Ok(line) = res else { break; };
        let (opponent, shape) = line.split_at(1);

        let opp = get_shape_score(opponent);
        let my = get_shape_score(shape);

        score_1 += my + calculate_score(&opp, &my);

        let desired = get_outcome_from_str(shape);
        score_2 += get_outcome_score(desired) + calculate_score(&opp, &get_shape_from_out(desired, &opp));
    }

    (score_1, score_2)


}