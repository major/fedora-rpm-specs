%global srcname  git-url-parse
%global pkgname  python-git-url-parse
%global slugname giturlparse
%global forgeurl https://github.com/coala/git-url-parse

%global common_description %{expand:
A simple GIT URL parser similar to giturlparse.py.
}

%bcond_without doc
%bcond_without tests

Name:           %{pkgname}
Version:        1.2.2
%forgemeta
Release:        %autorelease
Summary:        A simple GIT URL parser similar to giturlparse.py
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          0001_remove_pytest_coverage.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%if %{with doc}
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(alabaster)
%endif

%if %{with tests}
BuildRequires: python3dist(pytest)
%endif

%description %{common_description}

%package -n python-%{srcname}-doc
Summary: %summary

%description -n python-%{srcname}-doc
Documentation for python-git-url-parse

%package -n python3-%{srcname}
Summary: %summary

%description -n python3-%{srcname} %{common_description}

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel
%if %{with doc}
cd doc
PYTHONPATH=.. make html
rm -rf build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{slugname}

%check
%pyproject_check_import
%if %{with tests}
PYTHONWARNINGS=ignore %pytest -vv test
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files -n python-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc doc/build/html

%changelog
%autochangelog
