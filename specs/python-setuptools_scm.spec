%bcond tests 1

Name:           python-setuptools_scm
Version:        8.3.1
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
%pyproject_extras_subpkg -n python%{python3_pkgversion}-setuptools_scm toml%{!?rhel:,rich}


%prep
%autosetup -p1 -n setuptools_scm-%{version}
%if %{defined rhel}
# Remove unnecessary test dependencies:
# rich is listed in both [rich] and [test] extras, so we need to be more careful
sed -Ei '/^test = \[/,/^\]/ { /"(rich|build)",/d }' pyproject.toml
# Don't blow up all of the tests by failing to report the installed version of build
sed -i '0,/VERSION_PKGS/{s/, "build"//}' testing/conftest.py
%endif


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test} %{!?rhel:-x rich}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files setuptools_scm


%if %{with tests}
%check
# test_pip_download tries to download from the internet
# test_pyproject_missing_setup_hook_works requires build
%pytest -v -k 'not test_pip_download%{?rhel: and not test_pyproject_missing_setup_hook_works}'
%endif


%files -n python%{python3_pkgversion}-setuptools_scm -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
