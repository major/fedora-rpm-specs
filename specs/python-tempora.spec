# Created by pyp2rpm-3.3.2
%global pypi_name tempora
# Requires jaraco-tidelift
%bcond docs 0

Name:           python-%{pypi_name}
Version:        5.12.0
Release:        %autorelease
Summary:        Objects and routines pertaining to date and time (tempora)

License:        Apache-2.0
URL:            https://github.com/jaraco/tempora
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Objects and routines pertaining to date and time (tempora).

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
# The sdist's pyproject.toml drops the [project.optional-dependencies]
# table, so the "test" extra is not visible to the build backend. Supply
# the test dependencies explicitly.
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(pytest-freezer)

%description -n python3-%{pypi_name}
Objects and routines pertaining to date and time (tempora).

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        tempora documentation

%description -n python-%{pypi_name}-doc
Documentation for tempora
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_docs:-x doc}

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
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/calc-prorate

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
%autochangelog
