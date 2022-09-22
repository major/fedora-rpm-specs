%global srcname subprocess-tee
%global pkgname python-subprocess-tee
%global forgeurl https://github.com/pycontribs/subprocess-tee

%bcond_with tests

Name:    %{pkgname}
Version: 0.3.5
%forgemeta
Release: %autorelease
Summary: A subprocess.run that works like tee, being able to display output in real time while still capturing it

URL:     %{forgeurl}
Source:  %{pypi_source}
License: MIT

Patch0: 0002_ignoring_molecule_test.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%if %{with tests}
BuildRequires: python3dist(rich)
BuildRequires: python3dist(enrich)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytest-xdist)
%endif

%global common_description %{expand:
This package provides an drop-in alternative to subprocess.run that captures
the output while still printing it in real time, just the way tee does.}

%description %{common_description}

%package -n python3-%{srcname}
Summary: %summary

Requires: python3dist(rich)
Requires: python3dist(enrich)

%py_provides python3-%{srcname}
%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x testing}

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with tests}
%check
PYTHONPATH=src %{python3} -m pytest -vv src/subprocess_tee/test
%endif

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/subprocess_tee/
%{python3_sitelib}/subprocess_tee-*.dist-info/

%changelog
%autochangelog