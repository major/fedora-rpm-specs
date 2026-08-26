%global pypi_name eth_pydantic_types

Name:          python-eth-pydantic-types
Version:       0.2.6
Release:       %autorelease
BuildArch:     noarch
Summary:       ETH Pydantic types
License:       Apache-2.0
URL:           https://github.com/ApeWorX/eth-pydantic-types
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch:         python-eth-pydantic-types-0001-Go-back-to-a-pure-python-to_checksum_address.patch
BuildRequires: python3-eth-typing
BuildRequires: python3-eth-utils
BuildRequires: python3-hypothesis
BuildRequires: python3-pydantic
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-typing-extensions
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-eth-pydantic-types
Summary: %{summary}

%description -n python3-eth-pydantic-types
%{summary}.

%prep -a
# Upstream caps these three at the next major purely as a precaution, not in
# response to any known incompatibility.
%pyproject_patch_dependency hexbytes:drop_upper
%pyproject_patch_dependency eth-utils:drop_upper
%pyproject_patch_dependency eth-typing:drop_upper

%check -a
%pytest

%files -n python3-eth-pydantic-types -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
