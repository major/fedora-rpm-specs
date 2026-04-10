# Bootstrap mode is needed to break circular dependency with setuptools-scm:
# - vcs-versioning tests require setuptools_scm
# - setuptools_scm >= 10 requires vcs-versioning
# - pytest itself also requires setuptools_scm
# When bootstrapping, we cannot run tests at all.
%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-vcs-versioning
Version:        1.1.1
Release:        %autorelease
Summary:        The blessed package to manage your versions by vcs metadata
License:        MIT
URL:            https://github.com/pypa/setuptools-scm
Source:         %{pypi_source vcs_versioning}

BuildArch:      noarch

BuildSystem:    pyproject
BuildOption(install): -l vcs_versioning

%if %{with tests}
BuildOption(generate_buildrequires): -g test
# some tests need setuptools-scm for file finder entry points
# the package is missing from the test dependency group:
# https://github.com/pypa/setuptools-scm/issues/1353
BuildRequires:  python3-setuptools_scm >= 10
BuildRequires:  /usr/bin/git
%if %{undefined rhel}
BuildRequires:  /usr/bin/hg
%endif
%else
# this imports pytest, so we cannot import check it without it
BuildOption(check): -e '*.test_api'
%endif

%global _description %{expand:
This package extracts project version information from version control system
(VCS) metadata, eliminating the need to manually maintain version numbers in
multiple places. It automatically derives versions from VCS tags and commit
history.}

%description %_description


%prep -a
# Remove unwanted test dependencies (coverage not needed, pytest-xdist not in RHEL)
sed -i -e '/pytest-cov/d' %{?rhel:-e '/pytest-xdist/d'} pyproject.toml

%package -n python3-vcs-versioning
Summary:        %{summary}

%description -n python3-vcs-versioning %_description


%if %{with tests}
%check -a
%pytest -v %{!?rhel:-n auto}
%endif


%files -n python3-vcs-versioning -f %{pyproject_files}
%doc README.md
%{_bindir}/vcs-versioning


%changelog
%autochangelog
