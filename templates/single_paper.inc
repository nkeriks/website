
<div class="grid_2 alpha">
  <img class="thumbnail" src="img/{{paper.thumbnail}}">
</div>

<div class="grid_9 omega">
  <p class="title">{{paper.title}}</p>
  <p class="authors"> {% if "math" in paper.category %}{{paper.authors}}
  {% else %} {{paper.authors|boldnke}}
  {% endif %}</p>
  <p class="citation">{{paper.citation}}</p>
  {% if paper.summary %}<p class="summary"><b>Summary:</b> {{paper.summary}}</p>{% endif %}
    
  <p class="links"> <b>Links:</b>
  {% if paper.pubmed %}
    <a href="http://www.ncbi.nlm.nih.gov/pubmed/{{paper.pubmed}}">Pubmed</a>
  {% endif %}
  {% for link in paper.links %} 
      <a href={{link.url}}>{{link.name}}</a>
  {% endfor %}</p>

    {% if paper.press %}
    <p class="press"> <b>Press:</b> {% for link in paper.press %} 
        <a href={{link.url}}>{{link.name}}</a>
      {% endfor %} </p>
    {% endif %}
    {% if paper.blogs %}
    <p class="press"> <b>Blogs:</b> {% for link in paper.blogs %} 
        <a href={{link.url}}>{{link.name}}</a>
      {% endfor %} </p>
    {% endif %}
  <!--<a href="#" id="toggle_details_{{paper.name}}">Read more &raquo;</a>-->
  <div class="hidden" id="details_{{paper.name}}">
    {% if paper.abstract %}
        <p class="abstract"><b>Abstract:</b> {{paper.abstract}}</p>
    {% endif %}
  </div>
</div>

<div class="clear"></div>

