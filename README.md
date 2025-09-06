<h1 style="text-align:center;color:#4CAF50;">Python Player Ranking System</h1>

<p style="text-align:center;font-size:16px;color:#555;">
A player ranking management system developed in Python, allowing you to add players, update scores, list rankings, search for players, and save/load data persistently through an interactive terminal menu.
</p>

<hr style="border:1px solid #eee;">

<h2 style="color:#4CAF50;">Features</h2>
<ul style="font-size:15px;color:#333;">
    <li><strong>Add players:</strong> Register new players with name and score.</li>
    <li><strong>Remove players:</strong> Delete a player from the ranking.</li>
    <li><strong>Update scores:</strong> Add points to an existing player's score.</li>
    <li><strong>List ranking:</strong> Display all players sorted by score (highest to lowest).</li>
    <li><strong>Top players:</strong> Show players with scores above a certain threshold (40 points).</li>
    <li><strong>Search players:</strong> Find a player by name.</li>
    <li><strong>Persistent storage:</strong> Save and load players automatically using JSON files.</li>
    <li><strong>Interactive interface:</strong> Terminal menu for easy use.</li>
</ul>

<hr style="border:1px solid #eee;">

<h2 style="color:#4CAF50;">How to Use</h2>
<ol style="font-size:15px;color:#333;">
    <li><strong>Clone the repository:</strong>
        <pre style="background-color:#f6f8fa;padding:10px;border-radius:5px;">git clone https://github.com/your-username/python-player-ranking.git</pre>
    </li>
    <li><strong>Navigate to the project folder:</strong>
        <pre style="background-color:#f6f8fa;padding:10px;border-radius:5px;">cd python-player-ranking</pre>
    </li>
    <li><strong>Run the program:</strong>
        <pre style="background-color:#f6f8fa;padding:10px;border-radius:5px;">python main.py</pre>
    </li>
    <li><strong>Use the interactive menu to manage players:</strong>
        <pre style="background-color:#f6f8fa;padding:10px;border-radius:5px;">
[1] Add player
[2] Remove player
[3] Update score
[4] List ranking
[5] Top players
[6] Search player
[0] Exit
        </pre>
        <p>Data is saved automatically when you exit (<strong>0</strong>).</p>
        <p>Players are stored in <strong>ranking.json</strong> for persistent storage.</p>
    </li>
</ol>

<hr style="border:1px solid #eee;">

<h2 style="color:#4CAF50;">Example</h2>
<pre style="background-color:#f6f8fa;padding:10px;border-radius:5px;font-size:14px;">
ranking = Ranking()
ranking.adicionar_jogador("Alice", 50)
ranking.adicionar_jogador("Bob", 30)
ranking.atualizar_pontuacao("Bob", 15)
ranking.listar_ranking()
print(ranking.top_jogadores())
</pre>

<h3 style="color:#4CAF50;">Output:</h3>
<pre style="background-color:#f6f8fa;padding:10px;border-radius:5px;font-size:14px;">
Alice: 50 pontos
Bob: 45 pontos
['Alice', 'Bob']
</pre>
