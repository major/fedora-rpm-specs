Name:           python-pysequoia
Version:        0.1.35
Release:        %autorelease
Summary:        OpenPGP in Python using Sequoia PGP
License:        Apache-2.0
URL:            https://github.com/wiktor-k/pysequoia
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  cargo-rpm-macros

%global desc %{expand:
This library provides OpenPGP facilities in Python through the Sequoia PGP
library. If you need to work with encryption and digital signatures using an
IETF standardized protocol, this package is for you!}

%description
%{desc}

%package -n python3-pysequoia
Summary:        %{summary}

# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# BSD-3-Clause
# BSL-1.0
# LGPL-2.0-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        %{shrink:
	Apache-2.0 AND
	(MIT OR Apache-2.0) AND
	Unicode-DFS-2016 AND
	(0BSD OR MIT OR Apache-2.0) AND
	BSD-3-Clause AND
	BSL-1.0 AND
	LGPL-2.0-or-later AND
	MIT AND
	(MIT OR Zlib OR Apache-2.0) AND
	Unicode-3.0 AND
	(Unlicense OR MIT)
}

%description -n python3-pysequoia
%{desc}

%prep
%autosetup -n pysequoia-%{version}
# crypto-rust is (currently) not available in Fedora
# crypto-nettle does not provide all required algorithms
sed -i '/^sequoia-openpgp / s/"crypto-rust", "allow-experimental-crypto", "allow-variable-time-crypto"/"crypto-openssl"/' Cargo.toml
%cargo_prep

%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires -a -t

%build
%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%pyproject_install
%pyproject_save_files -l pysequoia

%check
%pyproject_check_import
%pytest

%files -n python3-pysequoia -f %{pyproject_files}
%doc README.md
%license LICENSE.dependencies

%changelog
%autochangelog
