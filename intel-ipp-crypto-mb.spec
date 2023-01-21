############################################################################
# Copyright 2019-2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############################################################################

%undefine __cmake_in_source_build
%global _lto_cflags %{nil}
%global debug_package %{nil}

# Versions numbers
%global release_version_major    1
%global release_version_minor    0
%global release_version_rev      4

%global interface_version_major  11
%global interface_version_minor  3
%global interface_version_full  %{interface_version_major}.%{interface_version_minor}

%global github_source_archive_name   ippcp_2021.5

%global rpm_name         intel-ipp-crypto-mb
%global product_name     Intel(R) IPP Cryptography multi-buffer library

Summary:            %{product_name}
Name:               %{rpm_name}
Release:            5%{?dist}
Version:            %{release_version_major}.%{release_version_minor}.%{release_version_rev}
License:            ASL 2.0
# Upstream exclusively uses x86_64-specific intrinsics
ExclusiveArch:      x86_64
URL:                https://github.com/intel/ipp-crypto
Source0:            %{url}/archive/refs/tags/%{github_source_archive_name}.tar.gz#/%{rpm_name}-%{github_source_archive_name}.tar.gz
# Remove explicit -O3 compiler optimization flag
Patch0: 0001-remove-explicit-O3-flag.patch
# Fix of -Wmaybe-uninitialized warning
Patch1: 0002-fix-may-be-uninitialized-warning.patch
# Fix of -Werror=uninitialized warning (EPEL8 build)
Patch2: 0003-fix-uninitialized-warning.patch
BuildRequires:      coreutils
BuildRequires:      make
BuildRequires:      tar
BuildRequires:      cmake >= 3.10
BuildRequires:      openssl-devel >= 1.1.0
BuildRequires:      gcc-c++ >= 8.2

%global github_crypto_mb_page %{url}/tree/%{github_source_archive_name}/sources/ippcp/crypto_mb

%description
A software crypto library optimized for Intel architecture for packet
processing applications.

It contains universal and OpenSSL compatible APIs for cryptography operations.

For additional information please refer to:
%{github_crypto_mb_page}


%package devel
Summary:            %{product_name} (Development Files)
License:            ASL 2.0
Requires:           %{name}%{?_isa} = %{version}-%{release}
ExclusiveArch:      x86_64

%description devel
A software crypto library optimized for Intel architecture for packet
processing applications.

It contains development libraries and header files.

For additional information please refer to:
%{github_crypto_mb_page}


%prep
%autosetup -n ipp-crypto-%{github_source_archive_name} -p1

%build
cd sources/ippcp/crypto_mb
%cmake
%cmake_build
cd -

%install
cd sources/ippcp/crypto_mb
install -d %{buildroot}/%{_includedir}/crypto_mb
install -p -m 0644 -t %{buildroot}/%{_includedir}/crypto_mb include/crypto_mb/*.h
install -d %{buildroot}/%{_libdir}
install -p -s -m 0755 %{_vpath_builddir}/bin/libcrypto_mb.so.%{interface_version_full} %{buildroot}/%{_libdir}
cd %{buildroot}/%{_libdir}
ln -s libcrypto_mb.so.%{interface_version_full} libcrypto_mb.so.%{interface_version_major}
ln -s libcrypto_mb.so.%{interface_version_full} libcrypto_mb.so

%if 0%{?rhel} && 0%{?rhel} < 8
%ldconfig_scriptlets
%endif

%files
%license LICENSE
%doc sources/ippcp/crypto_mb/Readme.md
%{_libdir}/libcrypto_mb.so.%{interface_version_full}
%{_libdir}/libcrypto_mb.so.%{interface_version_major}

%files devel
%dir %{_includedir}/crypto_mb
%{_includedir}/crypto_mb/cpu_features.h
%{_includedir}/crypto_mb/defs.h
%{_includedir}/crypto_mb/ec_nistp256.h
%{_includedir}/crypto_mb/ec_nistp384.h
%{_includedir}/crypto_mb/ec_nistp521.h
%{_includedir}/crypto_mb/ec_sm2.h
%{_includedir}/crypto_mb/ed25519.h
%{_includedir}/crypto_mb/exp.h
%{_includedir}/crypto_mb/rsa.h
%{_includedir}/crypto_mb/sm3.h
%{_includedir}/crypto_mb/sm4.h
%{_includedir}/crypto_mb/status.h
%{_includedir}/crypto_mb/version.h
%{_includedir}/crypto_mb/x25519.h
%{_libdir}/libcrypto_mb.so

%changelog
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
