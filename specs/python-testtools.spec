# To build this package in a new environment (i.e. a new EPEL branch), you'll
# need to build in a particular order.  Duplicate numbered steps can happen at
# the same time.
#
# 1. bootstrap python-testtools
# 2. python-fixtures
# 2. python-testscenarios
# 3. python-testresources
# 4. python-testtools
%bcond bootstrap 0

# Twisted support is optional, but introduces twisted as a build requirement,
# and that has it's own pile of dependencies.  Let's avoid that during EPEL
# bringup.
%bcond twisted %{undefined rhel}

Name:           python-testtools
Version:        2.7.2
Release:        %autorelease
Summary:        Extensions to the Python standard library unit testing framework
License:        MIT
URL:            https://github.com/testing-cabal/testtools
Source:         %{pypi_source testtools}
# https://github.com/testing-cabal/testtools/pull/387
Patch:          0001-Prepare-tests-for-upcoming-twisted-version.patch
BuildArch:      noarch

%global common_description %{expand:
testtools is a set of extensions to the Python standard library's unit testing
framework.}


%description %{common_description}


%package -n python3-testtools
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-testtools %{common_description}


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
%autosetup -p 1 -n testtools-%{version}

%if %{without twisted}
sed -e '/twistedsupport,/d' -i testtools/tests/__init__.py
%endif


%generate_buildrequires
%pyproject_buildrequires %{!?with_bootstrap:-x test %{?with_twisted:-x twisted}}


%build
%pyproject_wheel

%if %{without bootstrap}
make -C doc html
%endif


%install
%pyproject_install
%pyproject_save_files -l testtools


%check
%if %{with bootstrap}
# Exclude modules that import things that are not available during bootstrap.
%pyproject_check_import -e 'testtools.tests*' -e testtools.twistedsupport
%else
%{py3_test_envvars} %{python3} -m testtools.run testtools.tests.test_suite
%endif


%files -n python3-testtools -f %{pyproject_files}
%doc NEWS README.rst


%if %{without bootstrap}
%files doc
%doc doc/_build/html/*
%endif


%changelog
%autochangelog
