%global pypi_name packaging

# Specify --with bootstrap to build in bootstrap mode
# This mode is needed, because python3-rpm-generators need packaging
%bcond_with bootstrap

# When bootstrapping, the tests and docs are disabled because the dependencies are not yet available.
# We don't want python-pretend in future RHEL, so we disable tests on RHEL as well.
# No reason to ship the documentation in RHEL either, so it is also disabled by default.
%if %{without bootstrap} && %{undefined rhel}
# Specify --without docs to prevent the dependency loop on python-sphinx
# Doc subpackage is disabled because it requires sphinx-toolbox since packaging 24.1
# and that package is not available in Fedora yet.
%bcond_with docs

# Specify --without tests to prevent the dependency loop on python-pytest
%bcond_without tests
%else
%bcond_with docs
%bcond_with tests
%endif

Name:           python-%{pypi_name}
Version:        25.0
Release:        %autorelease
Summary:        Core utilities for Python packages

License:        BSD-2-Clause OR Apache-2.0
URL:            https://github.com/pypa/packaging
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  unzip

%if %{with bootstrap}
BuildRequires:  python%{python3_pkgversion}-flit-core
%endif

# Upstream uses nox for testing, we specify the test deps manually as well.
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pretend
%endif
%if %{with docs}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-furo
%endif


%global _description %{expand:
python-packaging provides core utilities for Python packages like utilities for
dealing with versions, specifiers, markers etc.}

%description %_description


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%if %{with bootstrap}
Provides:       python%{python3_pkgversion}dist(packaging) = %{version}
Provides:       python%{python3_version}dist(packaging) = %{version}
Requires:       python(abi) = %{python3_version}
%endif

%description -n python%{python3_pkgversion}-%{pypi_name}  %_description


%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        python-packaging documentation

%description -n python-%{pypi_name}-doc
Documentation for python-packaging
%endif


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires -r
%endif


%build
%if %{with bootstrap}
%{python3} -m flit_core.wheel
%else
%pyproject_wheel
%endif

%if %{with docs}
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Do not bundle fonts
rm -rf html/_static/fonts/
%endif


%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
unzip dist/packaging-%{version}-py3-none-any.whl -d %{buildroot}%{python3_sitelib} -x packaging-%{version}.dist-info/RECORD
echo '%{python3_sitelib}/packaging*' > %{pyproject_files}
%else
%pyproject_install
%pyproject_save_files %{pypi_name}
%endif


%check
%{!?with_bootstrap:%pyproject_check_import}
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst CHANGELOG.rst CONTRIBUTING.rst


%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE LICENSE.APACHE LICENSE.BSD
%endif


%changelog
%autochangelog
