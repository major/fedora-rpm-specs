# The network tests are not mocked at all
# Will fix later
%bcond_with tests

%global srcname django-gravatar2

Name:           python-%{srcname}
Version:        1.4.4
Release:        %autorelease
Summary:        Essential Gravatar support for Django
License:        MIT
URL:            https://gitlab.com/mailman/django-mailman3
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# Test dependencies:
BuildRequires:  python3dist(django)

%global _description %{expand:
A lightweight django-gravatar app. Includes helper methods for interacting with
gravatars outside of template code.

Features:
- Helper methods for constructing a gravatar url and checking an email for an
  existing gravatar
- Templatetags for generating a gravatar url or gravatar <img> tag.
- Full test suite}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django_gravatar


%if %{with tests}
%check
cd example_project
PYTHONPATH=${PYTHONPATH}:%{buildroot}%{python3_sitelib} \
  %{__python3} ./manage.py test django_gravatar
%endif


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
