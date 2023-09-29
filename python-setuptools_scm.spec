%bcond tests 1

Name:           python-setuptools_scm
Version:        8.0.3
Release:        %autorelease
Summary:        Blessed package to manage your versions by SCM tags

# SPDX
License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source:         %{pypi_source setuptools-scm}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
%if %{with tests}
BuildRequires:  git-core
# Don't pull mercurial into RHEL just to test this work with it
%if %{undefined rhel}
BuildRequires:  mercurial
%endif
# Manually listed test dependencies from tox.ini, to avoid pulling tox into RHEL
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools) >= 45
# virtualenv omitted, see https://github.com/pypa/setuptools_scm/pull/940
# rich omitted, pulled in only with the [rich] extra
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
%autosetup -p1 -n setuptools-scm-%{version}
# Upstream bogusly declares rich as a build-system dependency,
# but the build works without it.
# We remove it here to simplify the bootstrap loop
# and to avoid the dependency in RHEL builds.
# Upstream issue: https://github.com/pypa/setuptools_scm/issues/941
# Upstream PR: https://github.com/pypa/setuptools_scm/pull/942
# The PR does not apply cleanly to 8.0.3, so we sed it out instead.
# The sed removes the first line with "rich" only:
sed -i '0,/"rich"/{/"rich"/d}' pyproject.toml



%generate_buildrequires
%pyproject_buildrequires %{?with_tests:%{!?rhel:-x rich}}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files setuptools_scm


%if %{with tests}
%check
# Skipped test tries to download from the internet
%pytest -v -k 'not test_pip_download'
%endif


%files -n python%{python3_pkgversion}-setuptools_scm -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
