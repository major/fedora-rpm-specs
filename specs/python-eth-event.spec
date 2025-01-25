%global pypi_name eth-event

Name:          python-%{pypi_name}
Version:       1.2.5
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for Ethereum event decoding and topic generation
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/eth-event
Source0:       %{pypi_source %pypi_name}
# https://github.com/iamdefinitelyahuman/eth-event/issues/32
Patch1:        python-eth-event-0001-Readd-test-files-missing-in-PyPi.patch
Patch2:        python-eth-event-0002-Update-to-hexbytes-1.0.0.patch
# https://github.com/iamdefinitelyahuman/eth-event/pull/36
Patch3:        python-eth-event-0003-Update-to-eth-abi-5.0.1.patch
# Fedora-specific
Patch4:        python-eth-event-0004-Relax-deps.patch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov

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
%pyproject_save_files -l eth_event

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
