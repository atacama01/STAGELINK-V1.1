from .models import Internship
from .roles import Role


def visible_internships_for(actor):
    """
    Returns only the internships this caller is allowed to see.
    Every read goes through this function, so the rules live in one place.
    """
    if actor.role == Role.STUDENT:
        return Internship.objects.filter(student_user_id=actor.user_id)

    if actor.role == Role.COMPANY:
        return Internship.objects.filter(company_user_id=actor.user_id)

    if actor.role == Role.UNIVERSITY:
        return Internship.objects.all()

    # ADMIN (platform administration) has no access to internship data in this version.
    # Default-deny: any role not listed above sees nothing.
    return Internship.objects.none()
