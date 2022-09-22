# Build doc by default
%bcond_without doc

%global srcname django-extensions
%global modname django_extensions

Name:           python-%{srcname}
Version:        3.2.0
Release:        %autorelease
Summary:        Extensions for Django

License:        GPLv3+
URL:            https://github.com/django-extensions/django-extensions
# PyPI tarball doesn't contain some requirements files
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
#Patch0:         %%{srcname}-localdeps.patch

BuildArch:      noarch

BuildRequires:	make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{with doc}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%global _description %{expand:
Django Extensions is a collection of custom extensions for the Django
Framework.}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%package -n python%{python3_pkgversion}-%{srcname}-doc
Summary:        Documentation for %{srcname}
Suggests:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}-doc %{_description}
This package contains the documentation for %{srcname}.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel

%if %{with doc}
(cd docs && make html)
%endif


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
# tox.ini invokes make invokes pytest
# call directly so we can disable tests that require network
%pytest django_extensions tests \
  -k "not PipCheckerTests"


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md CONTRIBUTING.md README.rst

%if %{with doc}
%files -n python%{python3_pkgversion}-%{srcname}-doc
%license LICENSE
%doc docs/_build/html/*
%endif


%changelog
%autochangelog
