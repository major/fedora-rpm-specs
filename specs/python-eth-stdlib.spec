%global pypi_name eth-stdlib

Name:          python-%{pypi_name}
Version:       0.2.7
Release:       %autorelease
BuildArch:     noarch
Summary:       A collection of libraries for developers building on the EVM
License:       LGPL-3.0-or-later
URL:           https://github.com/skellet0r/eth-stdlib
VCS:           git:%{url}.git
Source0:       %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Fedora-specific. We're using cryptodomex.
Patch1:        python-eth-stdlib-0001-Switch-to-cryptodomex.patch
# https://github.com/skellet0r/eth-stdlib/pull/21
Patch2:        python-eth-stdlib-0002-Clarify-licensing-terms.patch
# Fedora-specific. We do not do code coverage during builds.
Patch3:        python-eth-stdlib-0003-Disable-pytest-coverage.patch
BuildRequires: python3-devel
BuildRequires: python3-dotenv
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L eth

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license COPYING.LESSER
%doc README.md

%changelog
%autochangelog
