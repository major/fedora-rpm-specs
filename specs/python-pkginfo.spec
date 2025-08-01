%global pypi_name pkginfo

%global common_description %{expand:
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distribution (an sdist) or a binary distribution
(e.g., created by running bdist_egg). It can also query the EGG-INFO directory
of an installed distribution, and the *.egg-info stored in a "development
checkout" (e.g, created by running setup.py develop).}

Name:           python-%{pypi_name}
Summary:        Query metadata from sdists / bdists / installed packages
Version:        1.12.1.2
Release:        %autorelease
License:        MIT

URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(wheel)

%description %{common_description}


%package -n python3-%{pypi_name}
Summary:        Query metadata from sdists / bdists / installed packages
Requires:       python3-setuptools

%description -n python3-%{pypi_name} %{common_description}


%package        doc
Summary:        Documentation for python-%{pypi_name}

%description    doc %{common_description}
This package contains the documentation.


%prep
%autosetup -n %{pypi_name}-%{version} -p1

# don't ship internal test subpackage
sed -i "s/, 'pkginfo.tests'//g" setup.py
# work around the wheel metadata version (Fedora already produces 2.4 while upstream it's still 2.3)
sed -i "s/assert(installed.metadata_version == '2.3')/assert(installed.metadata_version == '2.4')/" pkginfo/tests/test_installed.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import

%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt CHANGES.txt

%{_bindir}/pkginfo


%files -n python-%{pypi_name}-doc
%license LICENSE.txt
%doc html


%changelog
%autochangelog
