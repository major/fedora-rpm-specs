# Default: when bootstrapping -> disable tests
%bcond bootstrap 0
%bcond tests %{without bootstrap}

# Similar to what we have in pythonX.Y.spec files.
# If enabled, provides unversioned executables and other stuff.
# Disable it if you build this package in an alternative stack.
%bcond main_python 1

Name:           python-wheel
Version:        0.45.1
Release:        %autorelease
Epoch:          1
Summary:        Built-package format for Python

# packaging is Apache-2.0 OR BSD-2-Clause
License:        MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://github.com/pypa/wheel
Source:         %{url}/archive/%{version}/wheel-%{version}.tar.gz
# Compatibility with the setuptools 75+
# https://github.com/pypa/wheel/issues/650
Patch:          https://github.com/pypa/wheel/commit/3028d3.patch
# Compatibility with the setuptools 78+ (PEP 639)
# Upstream has removed this code entirely instead
# https://github.com/pypa/wheel/pull/655
Patch:          adjusts-tests-for-setuptools-78.patch
# Security fix for CVE-2026-24049: Privilege Escalation or Arbitrary Code Execution via malicious wheel file unpacking
# https://github.com/pypa/wheel/commit/7a7d2d (from 0.46.2+)
Patch:          CVE-2026-24049.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
# several tests compile extensions
# those tests are skipped if gcc is not found
BuildRequires:  gcc
%endif

%global _description %{expand:
This is a command line tool for manipulating Python wheel files,
as defined in PEP 427. It contains the following functionality:

- Convert .egg archives into .whl.
- Unpack wheel archives.
- Repack wheel archives.
- Add or remove tags in existing wheel archives.}

%description %{_description}

# Virtual provides for the packages bundled by wheel.
# %%{_rpmconfigdir}/pythonbundles.py src/wheel/vendored/vendor.txt --namespace 'python%%{python3_pkgversion}dist'
%global bundled %{expand:
Provides: bundled(python%{python3_pkgversion}dist(packaging)) = 24
}


%package -n     python%{python3_pkgversion}-wheel
Summary:        %{summary}
%{bundled}

%description -n python%{python3_pkgversion}-wheel %{_description}


%prep
%autosetup -n wheel-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l wheel

mv %{buildroot}%{_bindir}/wheel{,-%{python3_version}}
%if %{with main_python}
ln -s wheel-%{python3_version} %{buildroot}%{_bindir}/wheel-3
ln -s wheel-3 %{buildroot}%{_bindir}/wheel
%endif


%check
%{_rpmconfigdir}/pythonbundles.py src/wheel/vendored/vendor.txt --namespace 'python%{python3_pkgversion}dist' --compare-with '%{bundled}'

# Smoke test
%{py3_test_envvars} wheel-%{python3_version} version
%py3_check_import wheel

%if %{with tests}
%pytest -v --ignore build
%endif


%files -n python%{python3_pkgversion}-wheel -f %{pyproject_files}
%doc README.rst
%{_bindir}/wheel-%{python3_version}
%if %{with main_python}
%{_bindir}/wheel
%{_bindir}/wheel-3
%endif


%changelog
%autochangelog
