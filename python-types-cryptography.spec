%global srcname types-cryptography
%global modname types_cryptography

Name:           python-%{srcname}
Version:        3.3.23
Release:        %autorelease
Summary:        Typing stubs for cryptography
License:        ASL 2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
This is a PEP 561 type stub package for the cryptography package. It can be used
by type-checking tools like mypy, PyCharm, pytype etc. to check code that uses
cryptography. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/cryptography. All fixes for
types and metadata should be contributed there.

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
%check
%py3_check_import cryptography-stubs
%endif


%files -n  python%{python3_pkgversion}-%{srcname}
%doc CHANGELOG.md
%{python3_sitelib}/cryptography-stubs
%{python3_sitelib}/%{modname}-%{version}.dist-info/


%changelog
%autochangelog
