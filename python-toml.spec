%global pypi_name toml
%global desc TOML aims to be a minimal configuration file format that's easy to read due to \
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML \
should be easy to parse into data structures in a wide variety of languages. \
This package loads toml file into python dictionary and dump dictionary into \
toml file. \
This package is deprecated, use tomllib from the Python standard library \
or tomli/tomli-w.

Name:           python-%{pypi_name}
Version:        0.10.2
Release:        %autorelease
Summary:        A deprecated Python Library for Tom's Obvious, Minimal Language

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
# python3 bootstrap: this is rebuilt before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
# Note that the package prefix is always python3-, even if we build for 3.X
BuildRequires:  python3-rpm-generators
BuildRequires:  pyproject-rpm-macros

%bcond_without tests
%if %{with tests}
BuildRequires:  /usr/bin/toml-test
%endif

%description
%desc


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
# https://fedoraproject.org/wiki/Changes/DeprecatePythonToml
Provides:       deprecated()

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# https://github.com/uiri/toml/pull/339
sed -i '/pytest-cov/d' tox.ini


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%if %{with tests}
%check
ln -s /usr/share/toml-test/ .  # python tests require test cases here
%tox
# Also using the language independent toml-test suite to launch tests
ln -s /usr/share/toml-test/tests/* tests/  # toml-test requires them here
toml-test $(pwd)/tests/decoding_test3.sh
%endif


%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
