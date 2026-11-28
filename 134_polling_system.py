"""
Project 134: Simple Polling & Voting System
Concepts: dictionaries, voting counters, ASCII bar graphs, percentage calculation.
"""
def main():
    poll_question = "What is your favorite primary programming language?"
    options = ["Python", "JavaScript", "Rust", "C++", "Go"]
    votes = {opt: 0 for opt in options}

    print("=== LIVE POLLING & VOTING SYSTEM ===")
    print(f"Question: {poll_question}\n")

    while True:
        print("Options:")
        for idx, opt in enumerate(options, 1):
            print(f" {idx}. {opt}")
        print(" 0. Conclude Poll & View Results")

        choice = input("Cast your vote (0-5): ").strip()
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            selected = options[int(choice) - 1]
            votes[selected] += 1
            print(f"Voted for {selected}! Thank you.\n")
        else:
            print("Invalid selection.")

    total_votes = sum(votes.values())
    print("\n" + "=" * 45)
    print("                POLL RESULTS            ")
    print("=" * 45)
    print(f"Total votes cast: {total_votes}\n")
    for opt, count in votes.items():
        pct = (count / total_votes * 100) if total_votes > 0 else 0
        bar = "█" * int(pct // 4)
        print(f"{opt:<12} | {count:>3} votes ({pct:5.1f}%) | {bar}")
    print("=" * 45)

if __name__ == "__main__":
    main()
