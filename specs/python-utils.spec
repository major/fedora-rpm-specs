Name:           python-utils
Version:        3.9.1
Release:        %autorelease
Summary:        Python Utils is a module with some convenient utilities

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/WoLpH/python-utils
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# tox.ini uses _python_utils_tests/requirements.txt and that uses coverage and linting
# so we cherry-pick what we need instead
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-sphinx


%description
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.

%package -n     python3-utils
Summary:        %{summary}

%description -n python3-utils
Python Utils is a collection of small Python functions and classes which
make common patterns shorter and easier. This module makes it easy to
execute common tasks in Python scripts such as converting text to numbers
and making sure a string is in unicode or bytes format.

%package        docs
Summary:        Documentation for python-utils

%description docs
Documentation for python-utils.


%prep
%autosetup -p1 -n %{name}-%{version}

# Stop linting code in %%check and measuring coverage, this is upstream's business
sed -Ei '/--(cov|mypy)/d' pytest.ini

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/{.doctrees,.buildinfo,*.inv}


%install
%pyproject_install
%pyproject_save_files python_utils


%check
# Ignoring test_logger.py and python_utils/loguru.py - we don't have loguru
# in Fedora yet, hence we don't package the loguru extra for python-utils.
%pytest --ignore _python_utils_tests/test_logger.py --ignore python_utils/loguru.py


%files -n python3-utils -f %{pyproject_files}
%doc README.rst

%files docs
%doc html


%changelog
%autochangelog
