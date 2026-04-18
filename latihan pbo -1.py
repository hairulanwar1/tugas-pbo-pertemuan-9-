# SIMULASI USER

class User:
    def __init__(self, username, is_authenticated, permissions):
        self.username = username
        self.is_authenticated = is_authenticated
        self.permissions = permissions 

    def has_permission(self, permission):
        return permission in self.permissions


# BASE VIEW

class View:
    def dispatch(self, request):
        print("View: Halaman berhasil ditampilkan")


# MIXIN LOGIN

class LoginRequiredMixin:
    def dispatch(self, request):
        if not request.user.is_authenticated:
            print("LoginRequiredMixin: gagal anda belum login ")
            return
        print("LoginRequiredMixin: berhasil User sudah login ")
        return super().dispatch(request)


# MIXIN PERMISSION

class PermissionRequiredMixin:
    permission_required = None

    def dispatch(self, request):
        if not request.user.has_permission(self.permission_required):
            print("PermissionRequiredMixin: gagal anda Tidak punya izin ")
            return
        print("PermissionRequiredMixin: berhasil anda Punya izin ")
        return super().dispatch(request)


# REQUEST SIMULASI

class Request:
    def __init__(self, user):
        self.user = user


# VIEW UTAMA 

class MyView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "view_data"

    def dispatch(self, request):
        print("\n=== Mulai Akses MyView ===")
        return super().dispatch(request)


# TESTING

user1 = User("guest", False, [])
request1 = Request(user1)


user2 = User("user_biasa", True, [])
request2 = Request(user2)


user3 = User("admin", True, ["view_data"])
request3 = Request(user3)


view = MyView()


view.dispatch(request1)
view.dispatch(request2)
view.dispatch(request3)