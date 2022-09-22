%global srcname types-boto
%global modname types_boto

Name:           python-%{srcname}
Version:        2.49.2
Release:        %autorelease
Summary:        Typing stubs for boto
License:        ASL 2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
This is a PEP 561 type stub package for the boto package. It can be used by
type-checking tools like mypy, PyCharm, pytype etc. to check code that uses
boto. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/boto. All fixes for types
and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install


%if 0%{?fedora}
# py_check_import on EL9 need valid Python module names
%check
%py3_check_import boto-stubs
%endif


%files -n  python%{python3_pkgversion}-%{srcname}
%doc CHANGELOG.md
%{python3_sitelib}/boto-stubs
%{python3_sitelib}/%{modname}-%{version}.dist-info/


%changelog
%autochangelog
