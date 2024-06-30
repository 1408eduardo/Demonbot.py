// Block.rs
use sha2::{Sha256, Digest};
use std::fmt::Write;

#[derive(Debug)]
struct Block {
    timestamp: i64,
    data: String,
    previous_hash: String,
    hash: String,
}

impl Block {
    fn new(timestamp: i64, data: String, previous_hash: String) -> Self {
        let mut block = Block {
            timestamp,
            data,
            previous_hash,
            hash: String::new(),
        };
        block.hash = Block::calculate_hash(&block);
        block
    }

    fn calculate_hash(block: &Block) -> String {
        let mut hasher = Sha256::new();
        hasher.update(block.timestamp.to_string().as_bytes());
        hasher.update(&block.data.as_bytes());
        hasher.update(&block.previous_hash.as_bytes());
        let hash = hasher.finalize();
        let mut hash_str = String::new();
        for byte in hash {
            write!(&mut hash_str, "{:02x}", byte).expect("Unable to write");
        }
        hash_str
    }
}
