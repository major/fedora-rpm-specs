%global pypi_name eth_event

Name:          python-eth-event
Version:       1.2.6
Release:       %autorelease
BuildArch:     noarch
Summary:       Tools for Ethereum event decoding and topic generation
License:       MIT
URL:           https://github.com/iamdefinitelyahuman/eth-event
Source0:       %{pypi_source %pypi_name}
# https://github.com/iamdefinitelyahuman/eth-event/issues/32
Patch:         python-eth-event-0001-Readd-test-files-missing-in-PyPi.patch
Patch:         python-eth-event-0002-Update-to-hexbytes-1.0.0.patch
# Fedora-specific
Patch:         python-eth-event-0003-Relax-deps.patch
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-event
Summary: %{summary}

%description -n python3-eth-event
%{summary}.

%check -a
%pytest

%files -n python3-eth-event -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
