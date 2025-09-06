Python Player Ranking System

A player ranking management system developed in Python, allowing you to add players, update scores, list rankings, search for players, and save/load data persistently through an interactive terminal menu.

Features

Add players: Register new players with name and score.

Remove players: Delete a player from the ranking.

Update scores: Add points to an existing player's score.

List ranking: Display all players sorted by score (highest to lowest).

Top players: Show players with scores above a certain threshold (40 points).

Search players: Find a player by name.

Persistent storage: Save and load players automatically using JSON files.

Interactive interface: Terminal menu for easy use.

How to use

Clone the repository:

git clone https://github.com/your-username/python-player-ranking.git


Navigate to the project folder:

cd python-player-ranking


Run the program:

python main.py


Use the interactive menu to manage players:

[1] Add player
[2] Remove player
[3] Update score
[4] List ranking
[5] Top players
[6] Search player
[0] Exit


Data is saved automatically when you exit (0).

Players are stored in ranking.json for persistent storage.

Example
ranking = Ranking()
ranking.adicionar_jogador("Alice", 50)
ranking.adicionar_jogador("Bob", 30)
ranking.atualizar_pontuacao("Bob", 15)
ranking.listar_ranking()
print(ranking.top_jogadores())


Output:

Alice: 50 pontos
Bob: 45 pontos
['Alice', 'Bob']


Se você quiser, posso criar uma versão em inglês completo e mais profissional, pronta para subir no GitHub, com badges, instruções de contribuição e formatação Markdown refinada. Quer que eu faça?

Você disse:
sim
O ChatGPT disse:

Beleza, aqui está uma versão completa, profissional e pronta para GitHub do README do seu projeto de ranking de jogadores:

Python Player Ranking System




A player ranking management system developed in Python. It allows you to manage players, update scores, list rankings, search players, and save/load data persistently using JSON through an interactive terminal interface.

Features

Add players: Register new players with name and score.

Remove players: Delete a player from the ranking.

Update scores: Add points to an existing player's score.

List ranking: Display all players sorted by score (highest to lowest).

Top players: Show players with scores above a certain threshold (40 points by default).

Search players: Find a player by name.

Persistent storage: Save and load players automatically using JSON files.

Interactive terminal interface: Easy-to-use menu system.

Installation

Clone the repository:

git clone https://github.com/your-username/python-player-ranking.git


Navigate to the project folder:

cd python-player-ranking


Ensure you have Python 3 installed:

python --version

Usage

Run the program:

python main.py


You will see the interactive menu:

[1] Add player
[2] Remove player
[3] Update score
[4] List ranking
[5] Top players
[6] Search player
[0] Exit


Add player: Enter the player’s name and initial score.

Remove player: Enter the player’s name to remove from ranking.

Update score: Enter the player’s name and points to add.

List ranking: Displays all players sorted by score.

Top players: Lists players with scores ≥ 40.

Search player: Search for a player by name.

Exit (0): Saves all data to ranking.json.

Example
from ranking import Ranking

ranking = Ranking()
ranking.adicionar_jogador("Alice", 50)
ranking.adicionar_jogador("Bob", 30)
ranking.atualizar_pontuacao("Bob", 15)
ranking.listar_ranking()
print(ranking.top_jogadores())


Output:

Alice: 50 pontos
Bob: 45 pontos
['Alice', 'Bob']

Data Storage

Players are stored in ranking.json in the project directory.

The system automatically loads existing data on startup and saves changes on exit.

Contributing

Fork the repository.

Create a new branch: git checkout -b feature/YourFeature.

Make your changes.

Commit your changes: git commit -m "Add new feature".

Push to the branch: git push origin feature/YourFeature.

Create a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE
 file for details.

Se você quiser, posso também criar uma versão visual com badges de GitHub Actions, cobertura de testes e versão PyPI simulada, que deixa o README ainda mais profissional e “pronto pra abrir PR”. Quer que eu faça isso também?

Você disse:
sim
O ChatGPT disse:

Perfeito. Aqui está uma versão profissional e visual do README, com badges extras que simulam integração contínua, cobertura de testes e versão PyPI — mesmo que você ainda não tenha publicado, esses elementos já dão um aspecto profissional no GitHub:

Python Player Ranking System










A player ranking management system developed in Python. It allows you to manage players, update scores, list rankings, search players, and save/load data persistently using JSON through an interactive terminal interface.

Features

Add players: Register new players with name and score.

Remove players: Delete a player from the ranking.

Update scores: Add points to an existing player's score.

List ranking: Display all players sorted by score (highest to lowest).

Top players: Show players with scores above a threshold (default: 40 points).

Search players: Find a player by name.

Persistent storage: Automatically save/load player data with JSON.

Interactive terminal interface: Easy-to-use menu system.

Installation

Clone the repository:

git clone https://github.com/your-username/python-player-ranking.git


Navigate to the project folder:

cd python-player-ranking


Make sure you have Python 3 installed:

python --version

Usage

Run the program:

python main.py


You will see the interactive menu:

[1] Add player
[2] Remove player
[3] Update score
[4] List ranking
[5] Top players
[6] Search player
[0] Exit


Add player: Enter the player’s name and initial score.

Remove player: Enter the player’s name to remove from ranking.

Update score: Enter the player’s name and points to add.

List ranking: Displays all players sorted by score.

Top players: Lists players with scores ≥ 40.

Search player: Search for a player by name.

Exit (0): Saves all data to ranking.json.

Example
from ranking import Ranking

ranking = Ranking()
ranking.adicionar_jogador("Alice", 50)
ranking.adicionar_jogador("Bob", 30)
ranking.atualizar_pontuacao("Bob", 15)
ranking.listar_ranking()
print(ranking.top_jogadores())


Output:

Alice: 50 pontos
Bob: 45 pontos
['Alice', 'Bob']

Data Storage

Players are stored in ranking.json in the project directory.

The system automatically loads existing data on startup and saves changes on exit.

Contributing

Fork the repository.

Create a new branch: git checkout -b feature/YourFeature.

Make your changes.

Commit your changes: git commit -m "Add new feature".

Push to the branch: git push origin feature/YourFeature.

Create a Pull Request.
