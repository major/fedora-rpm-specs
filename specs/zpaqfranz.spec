# JIT is supported on x86 and x86_64 only. 60.09 brought an autodetection, but
# in case of a misdetection, it could annoy a user by requiring -nojit
# run-time option. bug #1309772
%ifarch %{ix86} x86_64
%bcond_without jit
%else
%bcond_with jit
%endif

# Prefer GCC compiler
%global toolchain gcc
%bcond_with toolchain_clang
%bcond_with toolchain_gcc

Name:           zpaqfranz
Epoch:          1
Version:        62.5
Release:        2%{?dist}
Summary:        Advanced multiversioned archiver with hardware acceleration
# LICENSE:  MIT text
# man/LICENSE:  Unlicense text
# man/zpaqfranz.pod:    LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp:    MIT
# zpaqfranz.cpp parts from zpaq:    LicenseRef-Fedora-Public-Domain
#               <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/306>
#               <https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/728>
# zpaqfranz.cpp parts from libtom/libtomcrypt:  LicenseRef-Fedora-Public-Domain OR WTFPL
#                                               (this bundle)
#                                   (relicensed to Unlicense later
#                                   <https://github.com/libtom/libtomcrypt/commit/3630bee6fc0f73dd9c7923fd43f8ae15a2c0fb70>)
# zpaqfranz.cpp parts from salsa20: LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp parts from 7-zip:   LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp parts from libdivsufsort-lite:  MIT
# zpaqfranz.cpp parts from Embedded Artistry:   MIT
# zpaqfranz.cpp parts from Nilsimsa:    MIT
# zpaqfranz.cpp parts from fcorbelli/zsfx:  MIT
# zpaqfranz.cpp parts from crc32:   Zlib
# zpaqfranz.cpp parts from stbrumme/hash-library:   Zlib
# zpaqfranz.cpp parts from madler/brotli:   Zlib
# zpaqfranz.cpp parts from wangyi-fudan/wyhash: Unlicense
# zpaqfranz.cpp parts from memcached: BSD-2-Clause
# zpaqfranz.cpp parts from BLAKE3-team/BLAKE3:  CC0-1.0 OR Apache-2.0
# zpaqfranz.cpp parts from Whirlpool:   LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp parts from wernerd/ZRTPCPP Twofish: Ferguson-Twofish
# zpaqfranz.cpp parts from google/highwayhash:  Apache-2.0
# zpaqfranz.cpp parts from Bill-Gray/PDCursesMod: LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp parts from noloader/SHA-Intrinsics: LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp parts from Stephan Brumme's SHA3 and MD5:   Zlib
# zpaqfranz.cpp parts from Iliade translated by Vincenzo Monti in 1825
#       in extract_test[1-4] Base64-encoded variables:   LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp parts from zpaqd v7.15: LicenseRef-Fedora-Public-Domain
# zpaqfranz.cpp parts from LZ4: BSD-2-Clause
# zpaqfranz.cpp parts from codewithnick/ascii-art:  MIT
## Used at build time, but not packaged in any binary package
# zpaqfranz.cpp part with zsfx_mime64[] Base64-encoded variable:
#       ZPAQ-compressed Win executable built from ZSFX/zsfx.cpp and
#       ZSFX/libzpaq.cpp using mingw
## Not used at build time and not in any binary package
# man/zpaqfranz.1:      LicenseRef-Fedora-Public-Domain (built from man/zpaqfranz.pod)
# zpaqfranz.cpp parts from cURL: curl
# ZSFX/libzpaq.cpp: MIT AND Unlicense AND LicenseRef-Fedora-Public-Domain
#       (a subset and an old version of zpaqfranz.cpp)
# ZSFX/LICENSE:     MIT text
# ZSFX/zsfx.cpp:    MIT
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND Ferguson-Twofish AND (LicenseRef-Fedora-Public-Domain OR WTFPL) AND Unlicense AND Zlib AND LicenseRef-Fedora-Public-Domain
SourceLicense:  %{license} AND curl
URL:            https://github.com/fcorbelli/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Unbundle curl.h and fix loading curl libary, probably not suitable for
# the upstream.
Patch0:         zpaqfranz-62.5-Unbundle-curl.h-and-load-curl-DSO-by-a-bare-file-nam.patch
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  perl-podlators
# rpm-build for elfdeps tool
BuildRequires:  rpm-build
BuildRequires:  sed
# libdivsufsort-lite-2.00 is bundled to libzpaq.cpp from
# <https://libdivsufsort.googlecode.com/files/libdivsufsort-lite.zip> that
# is simplified version of
# <http://libdivsufsort.googlecode.com/files/libdivsufsort-2.0.0.tar.bz2>.
# New libdivsufsort upstream is <https://github.com/y-256/libdivsufsort>.
Provides:       bundled(libdivsufsort-lite) = 2.00
# Unknown version of lz4 is bundeld to libzpaq.cpp from
# <https://github.com/lz4/lz4>.
Provides:       bundled(lz4)
# For cURL library with SFTP support. It's dlopened at run-time as an optional
# feature.
Recommends:     libcurl-full
%if 0%(/usr/lib/rpm/elfdeps --provides %{_libdir}/libcurl.so.4 >/dev/null 2>&1 && echo 1)
Recommends:     %(/usr/lib/rpm/elfdeps --provides %{_libdir}/libcurl.so.4)
%endif
# For "zpaq mysqldump" subcommand
Recommends:     (mariadb or mysql)

%description
This is a Swiss army knife for backup and disaster recovery with deduplicated
snapshots. It efficiently keeps backups, without a need to ever prune. Handles
millions of files and terabytes of data. Non-Latin support. Backups with full
encryption. Data integrity check with CRC32 and XXHASH or SHA-1, SHA-2, SHA-3,
MD5, XXH3, or BLAKE3. Multithread support. Specific ZFS handling functions.

%prep
%autosetup -p1 -n %{name}-%{version}
# Remove pregenerated files
rm man/zpaqfranz.1
# Remove precompiled code
sed -i -e '/zsfx_mime64\[\]={/d' zpaqfranz.cpp
# Normalize EOLs
for F in CHANGELOG.md; do
    tr -d "\r" < "${F}" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done
# Extract license texts
sed -n -e '/^Credits and copyrights and licenses/,/^   _____ _____/ p' \
    < zpaqfranz.cpp > LICENSES

%build
# Don't use Makefile: It installs to /usr/local.
%{build_cxx} %{optflags} \
    -DIPV6 \
    -Dunix \
%if %{without jit}
    -DNOJIT \
%endif
%ifarch x86_64
    -DHWSHA2 \
%endif
%ifarch s390x
    -DBIG \
%endif
    -DSFTP \
    zpaqfranz.cpp %{?__global_ldflags} -pthread -o zpaqfranz
pod2man --utf8 man/zpaqfranz.pod man/zpaqfranz.1

%check
# Run a selftest
./zpaqfranz autotest
# Test compress-decopress idemptotency
./zpaqfranz a test.zpaq LICENSE
./zpaqfranz v test.zpaq

%install
install -m 0755 -D -t %{buildroot}%{_bindir} zpaqfranz
install -m 0644 -D -t %{buildroot}%{_mandir}/man1 man/zpaqfranz.1

%files
%license COPYING LICENSE LICENSES
%doc CHANGELOG.md README.md TODO.md
%{_bindir}/zpaqfranz
%{_mandir}/man1/zpaqfranz.1*

%changelog
* Thu Jul 31 2025 Petr Pisar <ppisar@redhat.com> - 1:62.5-2
- Disable pipefail in the TMT test

* Wed Jul 30 2025 Petr Pisar <ppisar@redhat.com> - 1:62.5-1
- 62.5 bump

* Thu Jul 24 2025 Petr Pisar <ppisar@redhat.com> - 1:62.4-1
- 62.4 bump

* Mon Jul 21 2025 Petr Pisar <ppisar@redhat.com> - 1:62.3-1
- 62.3 bump

* Mon Jun 16 2025 Petr Pisar <ppisar@redhat.com> - 1:61.4-1
- 61.4 bump (upstream mistyped previous 61.2 version as 62.2)

* Thu Apr 03 2025 Petr Pisar <ppisar@redhat.com> - 62.2-1
- 62.2 bump

* Mon Feb 17 2025 Petr Pisar <ppisar@redhat.com> - 61.1-1
- 61.1 bump

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 60.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Petr Pisar <ppisar@redhat.com> - 60.10-1
- 60.10 bump

* Fri Oct 25 2024 Petr Pisar <ppisar@redhat.com> - 60.8-2
- Replace deprecated gethostbyname() with getaddrinfo() (upstream issue #141)

* Wed Oct 23 2024 Petr Pisar <ppisar@redhat.com> - 60.8-1
- 60.8 version packaged

