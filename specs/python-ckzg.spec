%global pypi_name ckzg

Name:          python-%{pypi_name}
Version:       2.1.1
Release:       %autorelease
Summary:       An implementation of the Polynomial Commitments API for EIP-4844/7594
License:       Apache-2.0
URL:           https://github.com/ethereum/c-kzg-4844
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# Fedora-specific
Patch:         python-ckzg-0001-Let-override-CC.patch
# Fedora-specific
Patch:         python-ckzg-0002-Disable-Werror.patch
# https://github.com/supranational/blst/pull/109
Patch:         blst-0001-Support-64-bit-limbs-on-no-asm-platforms.patch
BuildRequires: gcc
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(prep):    -n %{pypi_name}-%{version}
BuildOption(install): -l %{pypi_name}
# https://github.com/supranational/blst
Provides:      bundled(blst)

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
cd src
make test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
