from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Blog, Category 
from .forms import BlogForm, CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def all_blogs(request):
    blogs = Blog.objects.all().order_by('-date_added')
    context = {
        "blogs":blogs
    }
    return render(request, 'blog/blogs.html', context )


@login_required
def your_blogs(request):
    publications = Blog.objects.filter(author=request.user)
    context = {
        "publications":publications
    }
    
    return render(request, 'blog/dashboard.html', context)

def single_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    print(blog)
    context = {
        "blog": blog
    }
    return render(request, "blog/blog.html", context)



class BlogCreateView(LoginRequiredMixin, CreateView):
        model = Blog
        fields = ['title', 'article', 'topic', 'image']
        
        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['topics'] = Category.objects.all()
            return context



@login_required
def CategoryView(request):
    if request.method != 'POST':
       form = CategoryForm()
    else:
        form =  CategoryForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/new-blog')
     
       
    return render(request, 'blog/category_form.html', {
           'form':form
            })

# class CategoryView(LoginRequiredMixin, CreateView):
#     model = Category
#     fields = ['name']

    # def form_valid(self, form):
    #     return super().form_valid(form)
    
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model= Blog
    fields = ['title', 'article', 'topic', 'image']
    template_name_suffix = "_update_form"

@login_required
def edit_blog( request, pk):
    blog = Blog.objects.get(id=pk)
    update = BlogForm(instance=blog)

    if request.method == 'POST':
        update = BlogForm(request.POST, instance=blog )
         
        if update.is_valid():
            update.save()
            return redirect("/blogs/")
    context = {
            "update": update
        }
    
    return render(request, "blog/blog_update_form.html", context)

@login_required
def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk, )
    blog.delete()
    return redirect('/dashboard/')
    


# @login_required
# def new_blog(request):
#     if request.method != 'POST':
#         form = BlogForm()
#     else:
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             return redirect('/dashboard/')
    
#     context = {
#         'form': form
#     }
#     return render(request, "blog/newBlog.html", context)


