%global pypi_name bashate

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        %autorelease
Summary:        A pep8 equivalent for bash scripts

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.org/project/%{pypi_name}/
Source0:        %{pypi_source}
# https://review.opendev.org/c/openstack/bashate/+/985796
Patch0:         remove_reno_br.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  git-core

%description
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.

%package -n python3-%{pypi_name}
Summary:        A pep8 equivalent for bash scripts


%description -n python3-%{pypi_name}
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.


%package -n python-%{pypi_name}-doc
Summary: Documentation for bashate module


%description -n python-%{pypi_name}-doc
Documentation for the bashate module


%prep
%autosetup -S git -n %{pypi_name}-%{version}

sed -i \
    -e "/^coverage[[:space:]]*[!><=]/d" \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    -e "/^reno[[:space:]]*[!><=]/d" \
    -e "/^discover$/d" \
    test-requirements.txt doc/requirements.txt


%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv},docs


%build
#remove shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' bashate/bashate.py
# doc
%tox -e docs
rm -rf doc/build/html/.{doctrees,buildinfo}

%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l bashate


%check
%tox -e %{default_toxenv}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_bindir}/%{pypi_name}


%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE


%changelog
%autochangelog
