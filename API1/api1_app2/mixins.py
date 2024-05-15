from rest_framework import permissions
from api1_app2.permissions import IsStaffEditorPermission
class StaffEditorPermissionsMixin():
     permissions_classes = [permissions.IsAdminUser, IsStaffEditorPermission]