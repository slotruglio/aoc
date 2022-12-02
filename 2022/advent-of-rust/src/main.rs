mod lib;

fn main() {
    let inputs_dir = std::env::current_dir().unwrap()
    .parent().unwrap().join("inputs");

    let (part_one, part_two) = lib::day_two(inputs_dir.join("day2/input.txt"));
    println!("Part one: {}\nPart two: {}", part_one, part_two);
    
}
