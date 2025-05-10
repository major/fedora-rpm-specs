%global modname dateutil

Name:           python-%{modname}
Version:        2.9.0.post0
Release:        %autorelease
Epoch:          1
Summary:        Powerful extensions to the standard datetime module

# According to the LICENSE file:
# - Apache-2.0 applies to all contributions after 2017-12-01, as well as
#   all contributions that have been re-licensed.
# - BSD-3-Clause applies to all code, even that also covered by Apache-2.0
License:        (Apache-2.0 AND BSD-3-Clause) OR BSD-3-Clause

URL:            https://github.com/dateutil/dateutil
Source:         %{pypi_source python-dateutil}

# Allow setuptools-scm dependency greater than v8.0
Patch:          relax-setuptools_scm-requires.patch

# Fix dateutil module import in sphinx config file
Patch:          fix-sphinx-import.patch

# when bootstrapping dateutil-freezegun, we cannot run tests
# on RHEL, we do not have or want all test dependencies
%bcond tests %{undefined rhel}

BuildArch:      noarch
BuildRequires:  python3-devel

# For docs
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

# For tests
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(six)
%endif

%global _description \
The dateutil module provides powerful extensions to the standard datetime\
module available in Python.

%description %_description


%package -n python3-%{modname}
Summary:        %summary
Requires:       tzdata

%description -n python3-%{modname}  %_description


%package doc
Summary: API documentation for python-dateutil
%description doc
This package contains %{summary}.


%prep
%autosetup -p1 -n %{name}-%{version}

iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
make -C docs html


%install
%pyproject_install
%pyproject_save_files %{modname} -l


%check
%pyproject_check_import -e dateutil.tz.win -e dateutil.tzwin

%if %{with tests}
%pytest -W ignore::pytest.PytestUnknownMarkWarning
%endif


%files -n python3-%{modname} -f %{pyproject_files}
%doc NEWS README.rst


%files doc
%license LICENSE
%doc docs/_build/html


%changelog
%autochangelog
