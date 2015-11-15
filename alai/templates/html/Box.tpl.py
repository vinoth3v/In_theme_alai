<section <%= attributes %>>
<py if _['title']: >
<h2><%= title %></h2><hr>
</py>
<%= value %> <%= children %></section>
