%global _description %{expand:
Writing a setup.py typically involves lots of boilerplate and copy-pasting from
project to project.

This package aims to simplify that and bring some DRY principle to python
packaging.}

Name:           python-setupmeta
Version:        3.8.0
Release:        %{autorelease}
Summary:        Simplify your setup.py

License:        MIT
URL:            https://pypi.org/pypi/setupmeta
Source:         %{pypi_source setupmeta}

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
# required to make it not try to self-refer
# this is deliberately in this section instead of %%prep
# as we need to remove it over and over again
# with repeated %%generate_buildrequires rounds
rm -rf setupmeta.egg-info
%pyproject_buildrequires


%build
# to avoid a self dependency bootstrap loop, we build the wheel twice
# 1) this generates a wheel with version 0.0.0
%pyproject_wheel
# 2) we use it to generate the versioned wheel
export PYTHONPATH=%{_pyproject_wheeldir}/setupmeta-0.0.0-py3-none-any.whl
%pyproject_wheel
rm %{_pyproject_wheeldir}/setupmeta-0.0.0-py3-none-any.whl

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
