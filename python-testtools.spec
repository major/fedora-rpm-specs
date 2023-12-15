%global srcname testtools
%global common_description %{expand:
testtools is a set of extensions to the Python standard library's unit testing
framework.}

# To build this package in a new environment (i.e. a new EPEL branch), you'll
# need to build in a particular order.  Duplicate numbered steps can happen at
# the same time.
#
# 1. bootstrap python-extras
# 1. bootstrap python-fixtures
# 2. bootstrap python-testtools
# 3. python-extras
# 3. python-fixtures
# 3. python-testscenarios
# 4. python-testresources
# 5. python-testtools
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        2.7.1
Release:        %autorelease
Summary:        Extensions to the Python standard library unit testing framework
License:        MIT
URL:            https://github.com/testing-cabal/testtools

Source:         %pypi_source
# When rebasing patches, be aware that setup.cfg uses spaces in the git source,
# but tabs in the PyPI tarball.

BuildArch:      noarch

%description %{common_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{common_description}

%if %{without bootstrap}
%package        doc
BuildRequires:  make
BuildRequires:  python3-sphinx
Summary:        Documentation for %{name}

# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_temporary_exceptions
Provides:       bundled(jquery)

%description doc
This package contains HTML documentation for %{name}.
%endif


%prep
%autosetup -p 1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires %{!?with_bootstrap:-x test -x twisted}


%build
%pyproject_wheel

%if %{without bootstrap}
make -C doc html
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%if %{without bootstrap}
PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m testtools.run testtools.tests.test_suite
# Typically we would want an %%else condition to run an import check, but it
# will fail during the bootstrap phase, so leave it out.
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc NEWS README.rst

%if %{without bootstrap}
%files doc
%doc doc/_build/html/*
%endif


%changelog
%autochangelog
