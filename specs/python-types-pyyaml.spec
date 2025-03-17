%global srcname types-pyyaml
%global modname types_PyYAML
%global pypi_name types-PyYAML

Name:           python-%{srcname}
Version:        6.0.1
Release:        %autorelease
Summary:        Typing stubs for PyYAML
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%global _description %{expand:
This is a PEP 561 type stub package for the PyYAML package. It can be used by
type-checking tools like mypy, PyCharm, pytype etc. to check code that uses
PyYAML. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/PyYAML. All fixes for types
and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files yaml-stubs


%if 0%{?fedora}
%check
%py3_check_import yaml-stubs
%endif


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md


%changelog
%autochangelog
