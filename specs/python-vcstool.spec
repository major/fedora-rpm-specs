%global srcname vcstool

Name:           python-%{srcname}
Version:        0.3.0
Release:        %autorelease
Summary:        Tool to invoke vcs commands on multiple repositories

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/dirk-thomas/%{srcname}
Source0:        https://github.com/dirk-thomas/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-pkg_resources
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description
Vcstool is a version control system (VCS) tool, designed to make working with
multiple repositories easier.

Note: This tool should not be confused with vcstools (with a trailing s) which
provides a Python API for interacting with different version control systems.
The biggest differences between the two are:

- vcstool doesn't use any state beside the repository working copies available
  in the filesystem.
- The file format of vcstool export uses the relative paths of the repositories
  as keys in YAML which avoids collisions by design.
- vcstool has significantly less lines of code than vcstools including the
  command line tools built on top.


%package -n python3-%{srcname}
Summary:        %{summary}

Recommends:     git

%description -n python3-%{srcname}
Vcstool is a version control system (VCS) tool, designed to make working with
multiple repositories easier.

Note: This tool should not be confused with vcstools (with a trailing s) which
provides a Python API for interacting with different version control systems.
The biggest differences between the two are:

- vcstool doesn't use any state beside the repository working copies available
  in the filesystem.
- The file format of vcstool export uses the relative paths of the repositories
  as keys in YAML which avoids collisions by design.
- vcstool has significantly less lines of code than vcstools including the
  command line tools built on top.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

# Integrate bash completion with the bash-completion package
install -d %{buildroot}%{_datadir}/bash-completion/completions
cp -af %{buildroot}%{_datadir}/%{srcname}-completion/vcs.bash %{buildroot}%{_datadir}/bash-completion/completions/vcs


%check
# We skip two classes of test:
# 1. Code style
# 2. Tests which require network access
PYTHONWARNINGS=ignore %pytest --ignore=test/test_flake8.py --ignore=test/test_commands.py


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CONTRIBUTING.md README.rst
%{_bindir}/vcs*
%{_datadir}/%{srcname}-completion/
%{_datadir}/bash-completion/completions/vcs


%changelog
%autochangelog

