Name:    python-slip10
Version: 1.0.1
Release: 6%{?dist}
Summary: Reference implementation of SLIP-0039: Shamir’s Secret-Sharing for Mnemonic Codes

# MIT: slip10/ripemd160.py
# Rest of the project is BSD-3-Clause
License: BSD-3-Clause and MIT
URL:     https://github.com/trezor/python-slip10
Source0: %{pypi_source slip10}

# master have changed build system where LICENSE is included
Source1: https://raw.githubusercontent.com/trezor/python-slip10/e1a9972598574dc491fb4bc7b1679de21324e265/LICENCE

BuildArch:     noarch
BuildRequires: python3-devel


%global _description %{expand:
A reference implementation of the SLIP-0010 specification,
which generalizes the BIP-0032 derivation scheme for
private and public key pairs in hierarchical deterministic wallets
for the curves secp256k1, NIST P-256, ed25519 and curve25519.}

%description %_description

%package -n python3-slip10
Summary: %{summary}

%description -n python3-slip10 %_description


%prep
%autosetup -n slip10-%{version}
cp -v %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files slip10


%check
%pyproject_check_import


%files -n python3-slip10 -f %{pyproject_files}
%license LICENCE
%doc README.md
%doc CHANGELOG.md


%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.14

* Sat Apr 05 2025 Jonny Heggheim <hegjon@gmail.com> - 1.0.1-1
- Inital packaging
