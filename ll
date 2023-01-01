<div id="dataGoal">Top Goal Scorers<br>
    <span id="daterange">{{start}}---{{end}}</span>
    <hr>
    <div class="flex-containerScore">
    <table class="w3-table-all">
        <thead>
        <tr class="w3-gray" style="color: black; text-align: center; background-color:rgb(170, 150, 150);">
            <th>#</th>
            <th>Player Name</th>
            <th>Goals</th>
        </tr>
        </thead>
            {% for top in topper %}
            {% if forloop.counter <= 5 %}
                <tr>
                <td>
                    <a href="{{top.team.website}}" target="_blank">
                    <img src="{{top.team.crest}}" id="crest">
                    </a>
                </td>
                <td>
                    <span id="playerDetail">{{top.player.name}}</span>
                </td>
                <td>
                    <ion-icon name="football"></ion-icon>{{top.goals}}
                </td>
                </tr>
            {% endif %}
            {% endfor %}
        </table>
    </div>
</div>

#data2{
	width: 700px;
	margin: 2px;
	text-align: center;
	height: fit-content;
	padding-left: 10px;
	font-size: 25px;
}
#daterange{
	font-family: 'Poppins', sans-serif;
	text-align: center;
	font-size: 13px;
	color: grey;
}

.flex-Todaymatch {
	display: flex;
	flex-direction: column;
	font-family: 'Poppins', sans-serif;
}
.flex-Todaymatch > div{
	text-align: left;
	font-size: 20px;

}
#crest{
	width:30px;
}