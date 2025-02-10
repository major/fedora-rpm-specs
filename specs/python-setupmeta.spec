%global _description %{expand:
Writing a setup.py typically involves lots of boilerplate and copy-pasting from
project to project.

This package aims to simplify that and bring some DRY principle to python
packaging.}

Name:           python-setupmeta
Version:        3.6.1
Release:        %{autorelease}
Summary:        Simplify your setup.py

License:        MIT
URL:            https://pypi.org/pypi/setupmeta
Source:         %{pypi_source setupmeta}

# Allow for interpreters not named "python" in test_run_program
# https://github.com/codrsquad/setupmeta/pull/88
Patch:          https://github.com/codrsquad/setupmeta/pull/88.patch

BuildArch:      noarch

%description %_description

%package -n python3-setupmeta
Summary:        %{summary}
BuildRequires:  python3-devel
# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  git-core

%description -n python3-setupmeta %_description

%prep
%autosetup -n setupmeta-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l setupmeta

%check
# required for some tests
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# test_check_dependencies: requires a virtualenv
%pytest -k "not test_check_dependencies"

%files -n python3-setupmeta -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
