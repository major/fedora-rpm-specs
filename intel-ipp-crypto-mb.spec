%global debug_package %{nil}
%global srctag ippcp_2021.7.1
%global mbx_int_major 11
%global mbx_int_minor 6
%global desc %{expand: \
Crypto multi-buffer library provides optimized version of RSA, ECDSA, SM3 and
x25519 multi-buffer algorithms based on Intel Advanced Vector Extensions 512
(Intel AVX-512) integer fused multiply-add (IFMA) operations.}

Name:		intel-ipp-crypto-mb
Version:	1.0.8
Release:	1%{?dist}
Summary:	Intel IPP Cryptography multi-buffer library

License:	Apache-2.0
URL:		https://github.com/intel/ipp-crypto
Source0:	%{url}/archive/%{srctag}/%{name}-%{srctag}.tar.gz

# Upstream exclusively uses x86_64-specific intrinsics
ExclusiveArch:	x86_64

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	openssl-devel >= 1.1.0

%description
%{desc}

%package devel
Summary: Development files for %{name}
Provides:	%{name}-static = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel %{desc}

Development files.

%package static
Summary: Static libraries for %{name} development
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description static %{desc}

Static library.

%prep
%autosetup -n ipp-crypto-%{srctag}
# library path fix
sed -i 's/"lib\"/"lib64"/g' sources/ippcp/crypto_mb/src/CMakeLists.txt

%build
pushd sources/ippcp/crypto_mb
%cmake \
	-DARCH=intel64 \
	-DMERGED_BLD:BOOL=off
%cmake_build
popd

%install
pushd sources/ippcp/crypto_mb
%cmake_install
popd

%ldconfig_scriptlets

%files
%license LICENSE
%doc sources/ippcp/crypto_mb/Readme.md
%{_libdir}/libcrypto_mb.so.%{mbx_int_major}
%{_libdir}/libcrypto_mb.so.%{mbx_int_major}.%{mbx_int_minor}

%files devel
%{_includedir}/crypto_mb
%{_libdir}/libcrypto_mb.so

%files static
%license LICENSE
%{_libdir}/libcrypto_mb.a

%changelog
* Wed Jun 28 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Wed Feb 15 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Andrey Matyukov <andrey.matyukov@intel.com> - 1.0.4-2
- Fixed a symbolic link in intel-ipp-crypto-mb-devel package.

* Wed Dec 22 2021 Andrey Matyukov <andrey.matyukov@intel.com> - 1.0.4-1
- Added ECDSA/ECDHE for the NIST P-521 curve;
- Added ECC over SM2 curve: Public Key Generation, ECDSA Signature / Verification, ECDHE;
- Added SM3 algorithm;
- Added SM4 algorithm (ECB, CBC, CTR, OFB and CFB modes of operation);
- Added ed25519 Signature / Verification schemes;
- Added x25519 key agreement functionality: public key generation, shared key computation;
- Added modular exponentiation for fixed sizes: 1k, 2k, 3k, 4k.

 * Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.1-3
 - Rebuilt with OpenSSL 3.0.0

 * Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
 - Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Oct 21 2020 Intel - 1.0.1-1
- Refactoring of crypto_mb library (API naming, directory structure changes, etc);
- Added ECDSA/ECDHE for the NIST P-256 curve;
- Added ECDSA/ECDHE for the NIST P-384 curve.
