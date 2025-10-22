# Created by pyp2rpm-3.3.2
%global pypi_name tempora
%bcond_with docs

Name:           python-%{pypi_name}
Version:        5.8.0
Release:        %autorelease
Summary:        Objects and routines pertaining to date and time (tempora)

License:        MIT
URL:            https://github.com/jaraco/tempora
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Objects and routines pertaining to date and time (tempora).

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(build)
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(jaraco-functools) >= 1.20
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(wheel)
# testing Reqs
BuildConflicts: python3dist(pytest) = 3.7.3
BuildRequires:  python3dist(pytest) >= 3.4
BuildRequires:  python3-more-itertools

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Objects and routines pertaining to date and time (tempora).

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        tempora documentation

BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco-packaging) >= 3.2
BuildRequires:  python3dist(rst-linker) >= 1.9


%description -n python-%{pypi_name}-doc
Documentation for tempora
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove tests that requires pytest-freezer.
# it is not packaged in Fedora
sed -i 221,229d tempora/__init__.py
sed -i 25,30d tempora/utc.py

%build
%pyproject_wheel
%if %{with docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
LANG=C.utf-8 %{__python3} -m pytest --ignore=build


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/calc-prorate
%{python3_sitelib}/%{pypi_name}*

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
