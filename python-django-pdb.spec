# upstream test project is not in PyPI
# GitHub does not have the latest release tagged
# ... and importing fails because it expects some
# settings set
%bcond_with tests

%global srcname django-pdb

Name:           python-%{srcname}
Version:        0.6.2
Release:        %autorelease
Summary:        Easier pdb debugging for Django
License:        Public Domain
URL:            https://github.com/tomchristie/django-pdb
# PyPI tarball doesn't contain some requirements files
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
# Test dependencies:
BuildRequires:  python3dist(django)
%endif

%global _description %{expand:
Adding pdb.set_trace() to your source files every time you want to break into
pdb sucks.

Don’t do that.

Do this.}

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
%pyproject_save_files django_pdb


%if %{with tests}
%check
%pyproject_check_import
%endif


%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
