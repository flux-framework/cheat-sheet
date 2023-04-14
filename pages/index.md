---
layout: default
permalink: /
---

<div class="logo"><a href="https://flux-framework.readthedocs.org" target="_blank">
  <img src="{{ site.baseurl }}/assets/images/logo.png" style="width:80px"></a>
</div>

<div class="breadcrumbs">
<a href="#top">top</a> | {% for group in site.data.flux-commands.commands %} <a href="#{{ group.name | replace: ' ', '-' }}">{{ group.name }}</a> |{% endfor %} <a href="{{ site.repo }}" target="_blank">GitHub</a> | <a href="{{ site.baseurl }}/api" target="_blank">API</a> 
</div>

<a style="padding-bottom:30px" id="top"></a>
{% for group in site.data.flux-commands.commands %}

<a style="padding-bottom:30px" id="{{ group.name | replace: ' ', '-' }}"></a>
<h2 style="padding-top:20px">{{ group.name }}</h2>

{% for subgroup in group.groups %}

<blockquote>
{{ subgroup.name }}
</blockquote>

<pre><code class="language-bash">{% for item in subgroup.items %}
<span class="comment"># {{ item.title }}</span>
<span class="fluxcode">{{ item.command }}</span>
{% endfor %}
</code></pre>

{% endfor %}
{% endfor %}

<script src='//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
<script>
$(".fluxcode").click(function(){
  element = $(this)
  text = element.text()
  console.log(text)
  try {
      navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
      toastr.success(text, 'Code copied to clipboard')
  } catch (err) {
      console.error('Failed to copy: ', err);
      toastr.success('Error', 'Code failed to copy, see console')
  }  
})

/*  copyContent = function(e) => {
    console.log(e);
    console.log(e.innerHTML);
    text = e.innerHTML;
    //let text = document.getElementsByClassName("fluxcode").innerHTML;
    try {
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }
  }*/
</script>
