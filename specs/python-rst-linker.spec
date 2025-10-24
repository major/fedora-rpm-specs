# Created by pyp2rpm-3.2.2
%global pypi_name rst.linker
%global pkg_name rst-linker
# This package is interdependant on jaraco-packaging to build docs
# will build both with out docs and add docs in later
%bcond_with docs

Name:           python-%{pkg_name}
Version:        2.4.0
Release:        %autorelease
Summary:        Can add links and perform other custom replacements to rst

License:        MIT
URL:            https://github.com/jaraco/rst.linker
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
rst.linker provides a routine for adding links and performing other custom
replacements to reStructuredText files as a Sphinx extension.

%package -n python3-%{pkg_name}
Summary:        %{summary}

Requires:       python3dist(six)

BuildRequires:  python3-devel
BuildRequires:  python3dist(path) >= 13
BuildRequires:  python3dist(pytest)

%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
rst.linker provides a routine for adding links and performing other custom
replacements to reStructuredText files as a Sphinx extension.

%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        rst.linker documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco-packaging)

%description -n python-%{pkg_name}-doc
Documentation for rst.linker
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with docs}
# generate html docs
# this package requires itself to build docs :/
PYTHONPATH=./ sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files rst

%check
%pytest

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%if %{with docs}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog
