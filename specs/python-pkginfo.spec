%global pypi_name pkginfo

%global common_description %{expand:
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distribution (an sdist) or a binary distribution
(e.g., created by running bdist_egg). It can also query the EGG-INFO directory
of an installed distribution, and the *.egg-info stored in a "development
checkout" (e.g, created by running setup.py develop).}

Name:           python-%{pypi_name}
Summary:        Query metadata from sdists / bdists / installed packages
Version:        1.13
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

# These all appear to be due to metadata version discrepancies from PyPI, the
# same root cause as “test_installed_ctor_w_dist_info fails against wheel built
# with flit > 3.10.0,” https://bugs.launchpad.net/pkginfo/+bug/2090840, and
# “Different core metadata version in recent setuptools,”
# https://bugs.launchpad.net/pkginfo/+bug/2103804.
k="${k-}${k+ and }not test_installed_ctor_w_package"
k="${k-}${k+ and }not test_installed_ctor_w_name"
k="${k-}${k+ and }not test_get_metadata_w_module"
k="${k-}${k+ and }not test_get_metadata_w_package_name"

%pytest -k "${k-}"


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt CHANGES.txt

%{_bindir}/pkginfo


%files -n python-%{pypi_name}-doc
%license LICENSE.txt
%doc html


%changelog
%autochangelog
