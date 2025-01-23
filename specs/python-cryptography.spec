%bcond_without tests

%{!?python3_pkgversion:%global python3_pkgversion 3}

%global srcname cryptography

Name:           python-%{srcname}
Version:        44.0.0
Release:        %autorelease
Summary:        PyCA's cryptography library

# cryptography is dual licensed under the Apache-2.0 and BSD-3-Clause,
# as well as the Python Software Foundation license for the OS random
# engine derived by CPython.
License:        (Apache-2.0 OR BSD-3-Clause) AND PSF-2.0
URL:            https://cryptography.io/en/latest/
Source0:        https://github.com/pyca/cryptography/archive/%{version}/%{srcname}-%{version}.tar.gz
                # created by ./vendor_rust.py helper script
Source1:        cryptography-%{version}-vendor.tar.bz2
Source2:        conftest-skipper.py

# Merged for 45.0.0+
# https://github.com/pyca/cryptography/pull/12091
Patch: 12091.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
%if 0%{?fedora}
BuildRequires:  rust-packaging
%else
BuildRequires:  rust-toolset
%endif

BuildRequires:  python%{python3_pkgversion}-cffi >= 1.12
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-rust >= 0.11.4

%if %{with tests}
%if 0%{?fedora}
BuildRequires:  python%{python3_pkgversion}-certifi
BuildRequires:  python%{python3_pkgversion}-hypothesis >= 1.11.4
BuildRequires:  python%{python3_pkgversion}-iso8601
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-pytest-benchmark
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
BuildRequires:  python%{python3_pkgversion}-pytz
%endif
BuildRequires:  python%{python3_pkgversion}-pytest >= 6.2.0
%endif

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%package -n  python%{python3_pkgversion}-%{srcname}
Summary:        PyCA's cryptography library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

Requires:       openssl-libs
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9
# Can be safely removed in Fedora 37
Obsoletes: python%{python3_pkgversion}-cryptography-vectors < 3.4.7
%endif

%description -n python%{python3_pkgversion}-%{srcname}
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%prep
%autosetup -p1 -n %{srcname}-%{version}
%if 0%{?fedora}
%cargo_prep
sed -i 's/locked = true//g' pyproject.toml
%else
# RHEL: use vendored Rust crates
%cargo_prep -V 1
%endif

%if ! 0%{?fedora}
sed -i 's,--benchmark-disable,,' pyproject.toml
%endif


%generate_buildrequires
%pyproject_buildrequires
%if 0%{?fedora}
# Fedora: use RPMified crates
cd src/rust
%cargo_generate_buildrequires
cd ../..
%endif


%build
export RUSTFLAGS="%build_rustflags"
export OPENSSL_NO_VENDOR=1
export CFLAGS="${CFLAGS} -DOPENSSL_NO_ENGINE=1 "
%pyproject_wheel


%install
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete
find . -name Cargo.toml -print -delete
%pyproject_install
%pyproject_save_files %{srcname}


%check
%if %{with tests}
%if 0%{?rhel}
# skip benchmark, hypothesis, and pytz tests on RHEL
rm -rf tests/bench tests/hypothesis tests/x509
# append skipper to skip iso8601 and pretend tests
cat < %{SOURCE2} >> tests/conftest.py
%endif

# enable SHA-1 signatures for RSA tests
# also see https://github.com/pyca/cryptography/pull/6931 and rhbz#2060343
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes

# see https://github.com/pyca/cryptography/issues/4885 and
# see https://bugzilla.redhat.com/show_bug.cgi?id=1761194 for deselected tests
# see rhbz#2042413 for memleak. It's unstable under Python 3.11 and makes
# not much sense for downstream testing.
# see rhbz#2171661 for test_load_invalid_ec_key_from_pem: error:030000CD:digital envelope routines::keymgmt export failure
PYTHONPATH=${PWD}/vectors:%{buildroot}%{python3_sitearch} \
    %{__python3} -m pytest \
    --ignore vendor \
    -k "not (test_buffer_protocol_alternate_modes or test_dh_parameters_supported or test_load_ecdsa_no_named_curve or test_decrypt_invalid_decrypt or test_openssl_memleak or test_load_invalid_ec_key_from_pem)"
%endif


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst docs
%license LICENSE LICENSE.APACHE LICENSE.BSD


%changelog
%autochangelog
