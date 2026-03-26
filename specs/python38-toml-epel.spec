%global pypi_name toml
%global desc TOML aims to be a minimal configuration file format that's easy to read due to \
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML \
should be easy to parse into data structures in a wide variety of languages. \
This package loads toml file into python dictionary and dump dictionary into \
toml file.
%bcond_without tests

%global python3_pkgversion 38
# Needed until https://bugzilla.redhat.com/show_bug.cgi?id=2091462 is fixed in RHEL 8.
%global __pytest /usr/bin/pytest%(test %{python3_pkgversion} == 3 || echo -%{python3_version})

%global toml_test_version 1.2.0
%bcond_with toml_test
%if %{with toml_test}
%define toml_test_path /usr/share/toml-test/tests
%else
%define toml_test_path %{_builddir}/toml-test-%{toml_test_version}/tests
%endif

Name:           python38-%{pypi_name}-epel
Version:        0.10.2
Release:        2%{?dist}
Summary:        Python Library for Tom's Obvious, Minimal Language

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}
Source1:        https://github.com/BurntSushi/toml-test/archive/v%{toml_test_version}/toml-test-%{toml_test_version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-numpy
# python3 bootstrap: this is rebuilt before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
# Note that the package prefix is always python3-, even if we build for 3.X
BuildRequires:  python3-rpm-generators

%if %{with tests} && %{with toml_test}
BuildRequires:  /usr/bin/toml-test
%endif

%description
%desc


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc


%prep
%autosetup -p1 %{!?with_toml_test:-b1} -n %{pypi_name}-%{version}
# https://github.com/uiri/toml/pull/339
sed -i '/pytest-cov/d' tox.ini


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
mkdir toml-test
ln -s %{toml_test_path} toml-test  # python tests require test cases here

%pytest

%if %{with toml_test}
# Also using the language independent toml-test suite to launch tests
ln -s %{toml_test_path}/* tests/  # toml-test requires them here
toml-test $(pwd)/tests/decoding_test3.sh
%endif
%endif


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info


%changelog
* Thu Jul 21 2022 Maxwell G <gotmax@e.email> - 0.10.2-2
- Rebuild to fix bug in epel-rpm-macros' Python dependency generator

* Wed Jun 08 2022 Maxwell G <gotmax@e.email> - 0.10.2-1
- Initial python38 package for EPEL 8.

