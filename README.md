# pjt05

### 1. Decorator의 역할 정확한 숙지 필요

- require_safe : GET 방식의 method일 때만!
- require_http_methods(['POST', 'GET']) : POST, GET 방식일 때만!
- require_POST : POST 방식일 때만!



### 2. UPDATE 부분

- 기존에 있던 정보를 불러오고 그 위에 새로운 요청을 받아서 덮어쓰는 것!!

  => 기존에 정보를 불러오는 방법 정확한 숙지!!!!!!!!

  ```python
  @require_http_methods(['POST', 'GET'])
  def update(request, pk):
      movie = get_object_or_404(Movie, pk=pk)
      if request.method == 'POST':
          # instance=movie!!!
          form = MovieForm(request.POST, instance=movie)
          if form.is_valid():
              form.save()
              return redirect('movies:detail', pk)
      else:
          form = MovieForm(instance=movie)
      context = {
          # form만 불러오면 안된다아아아아아아 제바아아알!!!!
          'form':form,
          'movie':movie
      }
      return render(request, 'movies/form.html', context)
  ```



### 3. form.html 만들 때

* 만약에 create에서 부르면 create를 보여주고 아니면 update를 보여줘라 => 당황하지 말고

  ```django
  <!-- 이거 쓰면된다~~ -->
  {% if request.resolver_match.url_name == 'create' %}
  ```

* form을 그대로 불러서 사용하는 방법에는 3가지가 있었지?

  ```django
  {{ form.as_p }}
  {{ form.as_ul }}
  {{ form.as_table }}
  ```

  