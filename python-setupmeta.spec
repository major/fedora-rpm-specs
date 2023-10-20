%global _description %{expand:
Writing a setup.py typically involves lots of boilerplate and copy-pasting from
project to project.

This package aims to simplify that and bring some DRY principle to python
packaging.}

Name:           python-setupmeta
Version:        3.3.2
Release:        %{autorelease}
Summary:        Simplify your setup.py

License:        MIT
URL:            https://pypi.org/pypi/setupmeta
Source0:        %{pypi_source setupmeta}

BuildArch:      noarch

%description %_description

%package -n python3-setupmeta
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pep440
BuildRequires:  python3-setuptools_scm
BuildRequires:  git-core

%description -n python3-setupmeta %_description

%prep
%autosetup -n setupmeta-%{version}

%generate_buildrequires
# required to make it not try to self-refer
# this is deliberately in this section instead of %%prep to workaround
# https://github.com/rpm-software-management/mock/issues/1246
rm -rf setupmeta.egg-info
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files setupmeta

%check
# required for some tests
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# test_check_dependencies: requires a virtualenv
# test_version: requires a full git based project with their versioning scheme
# test_scenario: ditto
%{pytest} -k "not test_check_dependencies and not test_version and not test_scenario"

%files -n python3-setupmeta -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
