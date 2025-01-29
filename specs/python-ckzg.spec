%global pypi_name ckzg

Name:          python-%{pypi_name}
Version:       2.0.1
Release:       %autorelease
Summary:       An implementation of the Polynomial Commitments API for EIP-4844/7594
License:       Apache-2.0
URL:           https://github.com/ethereum/c-kzg-4844
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# Fedora-specific
Patch1:        python-ckzg-0001-Let-override-CC.patch
# Fedora-specific
Patch2:        python-ckzg-0002-Disable-Werror.patch
# https://github.com/supranational/blst/pull/109
Patch3:        blst-0001-Support-64-bit-limbs-on-no-asm-platforms.patch
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-pytest
# https://github.com/supranational/blst
Provides:      bundled(blst)

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
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
cd src
make test

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
