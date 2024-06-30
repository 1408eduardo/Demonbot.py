// main.rs
fn main() {
    let mut lyroncoin = Blockchain::new();
    lyroncoin.add_block("Block 1 Data".to_owned());
    lyroncoin.add_block("Block 2 Data".to_owned());
    println!("{:#?}", lyroncoin);

    let mut contract = SmartContract::new(
        PublicKey::new("owner".to_owned()),
        "payload".to_owned(),
        vec!["condition1".to_owned(), "condition2".to_owned()],
    );
    contract.execute(&["condition1".to_owned(), "condition2".to_owned()]);
}
