# The function of bootstrap is that it builds the package with flit_core.wheel
# and installs it by unzipping it.
# A real build uses %%pyproject_wheel and %%pyproject_install.
%bcond bootstrap 0
# Default: when bootstrapping -> disable tests
%bcond tests %{without bootstrap}

# Similar to what we have in pythonX.Y.spec files.
# If enabled, provides unversioned executables and other stuff.
# Disable it if you build this package in an alternative stack.
%bcond main_python 1

%global pypi_name wheel
%global python_wheel_name %{pypi_name}-%{version}-py3-none-any.whl

Name:           python-%{pypi_name}
Version:        0.41.2
Release:        %autorelease
Epoch:          1
Summary:        Built-package format for Python

# packaging is Apache-2.0 OR BSD-2-Clause
License:        MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://github.com/pypa/wheel
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# This is used in bootstrap mode where we manually install the wheel and
# entrypoints
Source1:        wheel-entrypoint
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
# python3 bootstrap: this is rebuilt before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
BuildRequires:  python3-rpm-generators

# Needed to manually build and unpack the wheel
%if %{with bootstrap}
BuildRequires:  python%{python3_pkgversion}-flit-core
BuildRequires:  unzip
%endif

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
# several tests compile extensions
# those tests are skipped if gcc is not found
BuildRequires:  gcc
%endif

%global _description %{expand:
Wheel is the reference implementation of the Python wheel packaging standard,
as defined in PEP 427.

It has two different roles:

 1. A setuptools extension for building wheels that provides the bdist_wheel
    setuptools command.
 2. A command line tool for working with wheel files.}

%description %{_description}

# Virtual provides for the packages bundled by wheel.
# Actual version can be found in git history:
# https://github.com/pypa/wheel/commits/master/src/wheel/vendored/packaging/tags.py
%global bundled %{expand:
Provides:       bundled(python3dist(packaging)) = 23
}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{bundled}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}


%package -n     %{python_wheel_pkg_prefix}-%{pypi_name}-wheel
Summary:        The Python wheel module packaged as a wheel
%{bundled}

%description -n %{python_wheel_pkg_prefix}-%{pypi_name}-wheel
A Python wheel of wheel to use with virtualenv.


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
%if %{with bootstrap}
%global _pyproject_wheeldir dist
%python3 -m flit_core.wheel
%else
%pyproject_wheel
%endif


%install
# pip is not available when bootstrapping, so we need to unpack the wheel and
# create the entrypoints manually.
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
unzip %{_pyproject_wheeldir}/%{python_wheel_name} \
    -d %{buildroot}%{python3_sitelib} -x wheel-%{version}.dist-info/RECORD
install -Dpm 0755 %{SOURCE1} %{buildroot}%{_bindir}/wheel
%py3_shebang_fix %{buildroot}%{_bindir}/wheel
%else
%pyproject_install
%endif

mv %{buildroot}%{_bindir}/%{pypi_name}{,-%{python3_version}}
%if %{with main_python}
ln -s %{pypi_name}-%{python3_version} %{buildroot}%{_bindir}/%{pypi_name}-3
ln -s %{pypi_name}-3 %{buildroot}%{_bindir}/%{pypi_name}
%endif

mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}


%check
# Smoke test
%{py3_test_envvars} wheel-%{python3_version} version
%py3_check_import wheel

%if %{with tests}
%pytest -v --ignore build
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/%{pypi_name}-%{python3_version}
%if %{with main_python}
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-3
%endif
%{python3_sitelib}/%{pypi_name}*/

%files -n %{python_wheel_pkg_prefix}-%{pypi_name}-wheel
%license LICENSE.txt
# we own the dir for simplicity
%dir %{python_wheel_dir}/
%{python_wheel_dir}/%{python_wheel_name}

%changelog
%autochangelog
