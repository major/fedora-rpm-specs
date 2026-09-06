%global pypi_name electrum_ecc

Name:           python-electrum-ecc
Version:        0.0.7
Release:        1%{?dist}
Summary:        Pure python ctypes wrapper for libsecp256k1

License:        MIT
URL:            https://pypi.org/project/electrum-ecc/
Source0:        %pypi_source
BuildArch:      noarch

%global _description %{expand:
This package provides a pure python interface to libsecp256k1.

Unlike Coincurve, it uses ctypes, and has no dependency.}

%description %{_description}

%package -n python3-electrum-ecc
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libsecp256k1
Requires:       libsecp256k1%{?_isa}

%description -n python3-electrum-ecc %{_description}

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -fr src/electrum_ecc.egg-info
# Remove bundled libsecp256k1
rm -fr libsecp256k1

%generate_buildrequires
%pyproject_buildrequires

%build
export ELECTRUM_ECC_DONT_COMPILE=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-electrum-ecc -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
