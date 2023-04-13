---
layout: default
permalink: /
---

<div class="logo"><a href="https://flux-framework.readthedocs.org" target="_blank">
  <img src="{{ site.baseurl }}/assets/images/logo.png" style="width:80px"></a>
</div>

<div class="breadcrumbs">
{% for group in site.data.flux-commands.commands %} <a href="#{{ group.name | replace: ' ', '-' }}">{{ group.name }}</a> {% if forloop.last %}{% else %}|{% endif %}{% endfor %}
</div>

{% for group in site.data.flux-commands.commands %}

<h2 id="{{ group.name | replace: ' ', '-' }}">{{ group.name }}</h2>

{% for subgroup in group.groups %}

<blockquote>
{{ subgroup.name }}
</blockquote>

<pre><code class="language-bash">{% for item in subgroup.items %}
<span class="comment"># {{ item.title }}</span>
{{ item.command }}
{% endfor %}
</code></pre>

{% endfor %}
{% endfor %}
