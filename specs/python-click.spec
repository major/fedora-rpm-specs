%bcond tests 1

Name:           python-click
Version:        8.2.2
Release:        %autorelease
Summary:        Simple wrapper around optparse for powerful command line utilities

License:        BSD-3-Clause
URL:            https://github.com/pallets/click
Source0:        %{url}/archive/%{version}/click-%{version}.tar.gz
# Fix regressions introduced with 8.2.2
# https://github.com/pallets/click/pull/3030 minus changes to CHANGES.rst due to conflicts
Patch:          python-click-8.2.2-fix-none-defaults.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

%global _description \
click is a Python package for creating beautiful command line\
interfaces in a composable way with as little amount of code as necessary.\
It's the "Command Line Interface Creation Kit".  It's highly configurable but\
comes with good defaults out of the box.

%description %{_description}


%package -n     python%{python3_pkgversion}-click
Summary:        %{summary}

%description -n python%{python3_pkgversion}-click %{_description}


%prep
%autosetup -n click-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-g tests}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files click


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-click -f %pyproject_files
%license LICENSE.txt
%doc README.md CHANGES.rst


%changelog
%autochangelog
