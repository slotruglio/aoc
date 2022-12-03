use std::{path::Path, fs::File, io::BufRead};

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
    fn get_shape_score(shape: &str) -> u32 {
        match shape.trim() {
            "A" | "X" => 1,
            "B" | "Y" => 2,
            _         => 3,
        }
    }
    
    fn get_outcome_from_str(outcome: &str) -> &str {
        match outcome.trim() {
            "X" => "L",
            "Y" => "D",
             _  => "W",
        }
    }
    
    fn get_shape_from_out(outcome: &str, opp: &u32) -> u32 {
        let beaters: [u32; 3] = [2,3,1];
        match outcome.trim() {
            "D" => opp.clone(),
            "W" => beaters[(opp-1) as usize],
            _ => beaters.iter().position(|x| x == opp).unwrap() as u32 + 1,
        }
    }
    
    fn calculate_score(opp: &u32, me: &u32) -> u32 {
        let beaters: [u32; 3] = [2,3,1];
        if opp == me { 3 } // draw
        else if me == beaters.get((opp-1) as usize).unwrap() { 6 } // win
        else { 0 } // loss
    }
    
    let file = File::open(path).unwrap();
    let reader = std::io::BufReader::new(file);

    let mut score_1 = 0 as u32;
    let mut score_2 = 0 as u32;

    for res in reader.lines() {
        let Ok(line) = res else { continue; };
        let (opponent, shape) = line.split_at(1);

        let opp = get_shape_score(opponent);
        let my = get_shape_score(shape);

        score_1 += my + calculate_score(&opp, &my);

        let desired = get_outcome_from_str(shape);
        score_2 += get_shape_from_out(desired, &opp);
        score_2 += calculate_score(&opp, &get_shape_from_out(desired, &opp));
    }

    (score_1, score_2)
}

pub fn day_three<P: AsRef<Path>>(path: P) -> (u16, u16) {
    let file = File::open(path).unwrap();
    let reader = std::io::BufReader::new(file);

    let mut sum_1 = 0;
    let mut sum_2 = 0;

    let mut group = Vec::new();
    for res in reader.lines() {
        let Ok(line) = res else { continue; };
        // first part
        let (first, second) = line.split_at(line.len()/2);
        for char in first.chars() {
            if !second.contains(char) { continue; }
            sum_1 += char as u16;
            sum_1 -= if char.is_lowercase() {96} else {38};
            break;
        }
        // second part
        group.push(line);
        if group.len() != 3 { continue; }
        for char in group[0].chars() {
            if group[1].contains(char) && group[2].contains(char) {
                sum_2 += char as u16;
                sum_2 -= if char.is_lowercase() {96} else {38};
                break;
            }
        }
        group.clear();
    }
    (sum_1,sum_2)
}