import requests
import json

url = "http://127.0.0.1:8000/evaluate_answer"

test_cases = [
    {
        "question": "Explain the process of nuclear fission.",
        "answer": "Nuclear fission is the process in which the nucleus of an atom splits into two or more smaller nuclei, along with the release of a large amount of energy. This energy is produced due to the conversion of some mass into energy, according to Einstein's mass-energy equivalence principle."
    },
    {
        "question": "What is the significance of the Turing test?",
        "answer": "The Turing test, proposed by Alan Turing, is a test to determine whether a machine can exhibit intelligent behavior indistinguishable from that of a human. If a machine can successfully pass the Turing test, it is considered to have demonstrated artificial intelligence."
    },
    {
        "question": "How do black holes form?",
        "answer": "Black holes form when a massive star exhausts its nuclear fuel and collapses under the force of gravity. The star's core contracts, and the outer layers are expelled, leaving behind an extremely dense object called a black hole, which has such a strong gravitational pull that even light cannot escape it."
    },
    {
        "question": "Explain the difference between classical and operant conditioning.",
        "answer": "Classical conditioning is a learning process in which a neutral stimulus becomes associated with a significant stimulus, eliciting a response similar to the original response. In contrast, operant conditioning involves learning through the consequences of behavior, where actions that are followed by desirable consequences are reinforced, and those followed by undesirable consequences are discouraged."
    },
    {
        "question": "What are the main functions of the circulatory system?",
        "answer": "The main functions of the circulatory system are to transport oxygen and nutrients to cells, remove waste products, and help regulate body temperature. It achieves these functions through the continuous circulation of blood, driven by the pumping action of the heart."
    },
    {
        "question": "Describe the process of DNA replication.",
        "answer": "DNA replication is the process by which the DNA molecule duplicates itself to produce two identical copies. It begins with the unwinding of the DNA double helix, followed by the separation of the two strands. Each strand then serves as a template for the synthesis of a new complementary strand, resulting in two identical DNA molecules."
    },
    {
        "question": "Explain the concept of plate tectonics.",
        "answer": "Plate tectonics is the theory that the Earth's lithosphere is divided into several large plates that float on the semi-fluid asthenosphere. These plates move in response to the convection currents in the mantle, causing them to interact at their boundaries. The interactions between plates result in geological phenomena such as earthquakes, volcanic eruptions, and the formation of mountain ranges."
    },
    {
        "question": "What is the role of the mitochondria in a cell?",
        "answer": "Mitochondria are organelles found in the cells of eukaryotic organisms. They are often referred to as the 'powerhouses' of the cell because they generate most of the cell's supply of adenosine triphosphate (ATP), the primary source of chemical energy. Mitochondria are also involved in various other cellular processes, including the regulation of the cell cycle, cell growth, and cell death."
    },
    {
        "question": "What are the four fundamental forces of nature?",
        "answer": "The four fundamental forces of nature are gravity, electromagnetism, the strong nuclear force, and the weak nuclear force. Gravity is the force responsible for the attraction between objects with mass; electromagnetism governs the interactions between charged particles; the strong nuclear force holds atomic nuclei together; and the weak nuclear force is responsible for radioactive decay and neutrino interactions."
    },
    {
        "question": "Explain the difference between a eukaryotic cell and a prokaryotic cell.",
        "answer": "Eukaryotic cells are more complex and larger than prokaryotic cells. They contain membrane-bound organelles, such as the nucleus, which houses the cell's DNA, and other specialized structures like mitochondria and the endoplasmic reticulum. Prokaryotic cells, on the other hand, do not have a nucleus or membrane-bound organelles. Their DNA is found in a single circular chromosome in the cytoplasm, and they generally have fewer structures and simpler organization."
    }
]

for i, test_case in enumerate(test_cases, 1):
    response = requests.post(url, json=test_case)

    print(f"Test case {i}:")
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, indent=2))
    else:
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

    print("\n" + "=" * 80 + "\n")
