Name:           python-django-clacks
Version:        0.3.1
Release:        %autorelease
Summary:        Django Middleware for X-Clacks-Overhead
License:        MIT
URL:            https://github.com/ractf/django-clacks
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Django Middleware for X-Clacks-Overhead, a tribute to author Terry Pratchett.}


%description %_description


%package -n     python3-django-clacks
Summary:        %{summary}
%py_provides    python3-django-clacks


%description -n python3-django-clacks %_description


%prep
%autosetup -n django-clacks-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files clacks


%check
%pyproject_check_import


%files -n python3-django-clacks -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
