%bcond tests 1

Name:           python-setuptools_scm
Version:        9.2.2
Release:        %autorelease
Summary:        Blessed package to manage your versions by SCM tags

# SPDX
License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source:         %{pypi_source setuptools_scm}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  git-core
# Don't pull mercurial into RHEL just to test this work with it
%if %{undefined rhel}
BuildRequires:  mercurial
%endif
%endif

%description
Setuptools_scm handles managing your Python package versions in SCM metadata.
It also handles file finders for the supported SCMs.


%package -n python%{python3_pkgversion}-setuptools_scm
Summary:        %{summary}

%description -n python%{python3_pkgversion}-setuptools_scm
Setuptools_scm handles managing your Python package versions in SCM metadata.
It also handles file finders for the supported SCMs.


# We don't package the [rich] extra on RHELs, to avoid pulling rich into the buildroot
%pyproject_extras_subpkg -n python%{python3_pkgversion}-setuptools_scm simple,toml%{!?rhel:,rich}


%prep
%autosetup -p1 -n setuptools_scm-%{version}
# Remove flake8, mypy, ruff, … from the test dependencies
sed -Ei '/^test = \[/,/^\]/ { /"(griffe|mypy|ruff|flake8).*"/d }' pyproject.toml

%if %{defined rhel}
# Remove unnecessary test dependencies:
# rich is listed in both [rich] and [test] extras, so we need to be more careful
sed -Ei '/^test = \[/,/^\]/ { /"(rich|build|wheel|pytest-timeout)",/d }' pyproject.toml
sed -Ei '/^\[tool.pytest.ini_options\]/,/^\[/ { /^timeout/d }' pyproject.toml
# Don't blow up all of the tests by failing to report the installed version of build
sed -Ei '0,/VERSION_PKGS/{s/, "(build|wheel)"//g}' testing/conftest.py
%endif


%generate_buildrequires
# Note: We only pull in the [rich] extra when running tests.
# This is to make the new Python version bootstrapping simpler
# as setuptools_scm is an early package and rich is a late one.
%pyproject_buildrequires %{?with_tests:-g test %{!?rhel:-x rich}} -x simple,toml


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files setuptools_scm

# Allow parallel-installable executable for alternate Python stacks (e.g. in RHEL)
mv %{buildroot}%{_bindir}/setuptools-scm %{buildroot}%{_bindir}/setuptools-scm-%{python3_version}
%if "%{python3_pkgversion}" == "3"
ln -s ./setuptools-scm-%{python3_version} %{buildroot}%{_bindir}/setuptools-scm
%endif


%if %{with tests}
%check
# test_pip_download, test_xmlsec_download_regression try to download from the internet
# test_pyproject_missing_setup_hook_works requires build
%pytest -v -k 'not test_pip_download and not test_xmlsec_download_regression %{?rhel: and not test_pyproject_missing_setup_hook_works}'
%endif


%files -n python%{python3_pkgversion}-setuptools_scm -f %{pyproject_files}
%doc README.md
%{_bindir}/setuptools-scm-%{python3_version}
%if "%{python3_pkgversion}" == "3"
%{_bindir}/setuptools-scm
%endif


%changelog
%autochangelog
