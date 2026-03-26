%global python3_pkgversion 3.13

# When bootstrapping new Python we need to build flit in bootstrap mode.
# The Python RPM dependency generators and pip are not yet available.
%bcond bootstrap 0

# Don't run tests in EPEL - they need unavailable dependencies.
%bcond tests 0

Name:           python%{python3_pkgversion}-flit-core
Version:        3.12.0
Release:        %autorelease
Summary:        PEP 517 build backend for packages using Flit

# flit-core is BSD-3-Clause
# flit_core/versionno.py contains a regex that is from packaging, BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause

URL:            https://flit.pypa.io/
Source:         %{pypi_source flit_core}

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
# Test deps that require flit-core to build:
BuildRequires:  python%{python3_pkgversion}-testpath
%endif

%description
This provides a PEP 517 build backend for packages using Flit.
The only public interface is the API specified by PEP 517,
at flit_core.buildapi.


%prep
%autosetup -p1 -n flit_core-%{version}

# Remove vendored tomli that flit_core includes to solve the circular dependency on older Pythons
# (flit_core requires tomli, but flit_core is needed to build tomli).
# We don't use this, as tomllib is a part of standard library since Python 3.11.
# Remove the bits looking for the license files of the vendored tomli.
rm -rf flit_core/vendor
sed -iE 's/, *"flit_core\/vendor\/\*\*\/LICENSE\*"//' pyproject.toml


%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
%if %{with bootstrap}
%{python3} -m flit_core.wheel
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
%{python3} bootstrap_install.py --install-root %{buildroot} dist/flit_core-%{version}-py3-none-any.whl
# for consistency with %%pyproject_install/brp-python-rpm-in-distinfo:
echo rpm > %{buildroot}%{python3_sitelib}/flit_core-%{version}.dist-info/INSTALLER
rm %{buildroot}%{python3_sitelib}/flit_core-%{version}.dist-info/RECORD
%else
%pyproject_install
%endif

%check
%py3_check_import flit_core flit_core.buildapi
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-flit-core
%doc README.rst
%{python3_sitelib}/flit_core-*.dist-info/
%license %{python3_sitelib}/flit_core-*.dist-info/licenses/LICENSE
%{python3_sitelib}/flit_core/


%changelog
%autochangelog
