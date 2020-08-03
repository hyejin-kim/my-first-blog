from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
# import requests as req
# import json

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(dir(post))
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




#
#
# def searchIms(hostname):
#     #IMS url
#     url = "http://api.ims.daumkakao.io/v1/serverViews"
#     query = "?hostname="+hostname
#     url_query = url + query
#     headers = {'Content-type': 'application/json;charset=UTF-8', 'Accept': '*'}
#
#     #Open API 검색 요청 개체 설정
#     res = req.get(url_query, headers=headers)
#
#     res.raise_for_status()
#     if res.ok:
#         return res.text
#     else:
#         return None
#
# #검색 결과 항목 정보 출력하기
# def showIms(result):
#
#     hosts = []
#     results = result['results']
#     str = '01'
#
#     for ims in result['results']:
#         if ims['server_type'] == 'DEFAULT':
#            host = ims['hostname']
#            if str in "host01":
#              hosts.append(host)
#     return json.dumps({'all': {'hosts': hosts}})
#
# #프로그램 진입점
# def main():
#     #검색 질의 요청
#     return_res = searchIms('grace')
#
#     print(return_res)
#     if(return_res == None):
#         print("검색 실패!!!")
#         exit()
#     #검색 결과를 json개체로 로딩
#     jres = json.loads(return_res)
#     if(jres == None):
#          print("json.loads 실패!!!")
#          exit()
#
#     #검색 결과의 results 목록의 각 항목을 출력
#     print(showIms(jres))
#
#
#
# #진입점 함수를 main으로 지정
# if __name__ == '__main__':
#     main()
