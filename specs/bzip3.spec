Name:           bzip3
Version:        1.5.1
Release:        2%{?dist}
Summary:        Tools for compressing and decompressing bzip3 files
# 3rdparty/libsais-LICENSE: Apache-2.0 text
# bz3grep:                  BSD-2-Clause
# include/common.h:         LGPL-3.0-or-later
# include/libsais.h:        Apache-2.0
# include/libbz3.h:         LGPL-3.0-or-later
# include/yarg.h:           (unspecified, defaults to global LGPL-3.0-or-later)
# LICENSE:                  LGPL-3.0 text
# src/libbz3.c:             LGPL-3.0-or-later
# src/main.c:               LGPL-3.0-or-later
## Unbundled and not in any binary package
# aclocal.m4:               FSFULLR AND GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/ax_build_date_epoch.m4: GPL-3.0-or-later WITH Autoconf-exception-macro
# build-aux/ax_pthread.m4:  GPL-3.0-or-later WITH Autoconf-exception-macro
# build-aux/ax_check_compile_flag.m4:   FSFAP
# build-aux/compile:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/config.guess:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/config.sub:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/depcomp:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/git-version-gen:    GPL-3.0-or-later
# build-aux/install-sh:     X11 AND "FSF changes to this file are in the public domain"
# build-aux/libtool.m4:     FSFULLR AND GPL-2.0-or-later WITH Libtool-exception
#                           AND FSFUL
# build-aux/ltmain.sh:      GPL-2.0-or-later WITH Libtool-exception AND
#                           (GPL-2.0-or-later OR MIT)
# build-aux/lt~obsolete.m4  FSFULLR
# build-aux/ltoptions.m4:   FSFULLR
# build-aux/ltsugar.m4:     FSFULLR
# build-aux/missing:        GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:                FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# Makefile.in:              FSFULLR
License:        LGPL-3.0-or-later AND BSD-2-Clause
SourceLicense:  GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-macro AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND (GPL-2.0-or-later OR MIT) AND LGPL-3.0-or-later AND BSD-2-Clause AND Apache-2.0 AND X11 AND FSFULLR AND FSFUL AND FSFAP
URL:            https://github.com/kspalaiologos/%{name} 
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz 
# Do not use /usr/bin/env in shell bangs, not suitable for upstream,
# <https://github.com/kspalaiologos/bzip3/pull/75>.
Patch0:         bzip3-1.5.0-Do-not-use-usr-bin-env-in-shell-bangs.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bash
# coreutils for cat, tr in build-aux/git-version-gen
BuildRequires:  coreutils
BuildRequires:  findutils
# awk in configure.ac, configure, Makefile.in
BuildRequires:  gawk
BuildRequires:  gcc
# For git-version-gen script executed from autoconf.ac
BuildRequires:  gnulib-devel
BuildRequires:  libtool
BuildRequires:  make
# PKG_PROG_PKG_CONFIG in configure.ac
BuildRequires:  pkgconf-pkg-config
# sed in build-aux/git-version-gen
BuildRequires:  sed
# Tests:
# md5sum is not helpful
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Executed by bz3grep
Requires:       grep
# Executed by bz3less
Requires:       less
# Executed by bz3more
Requires:       util-linux-core
# Executed by bz3most
Requires:       most

%description
These are tools for compressing, decompressing, printing, and searching bzip3
files. bzip3 features higher compression ratios and better performance than
bzip2 thanks to an order-0 context mixing entropy coder, a fast
Burrows-Wheeler transform code making use of suffix arrays and a run-length
encoding with Lempel-Ziv prediction pass based on LZ77-style string matching
and PPM-style context modeling.

%package libs
Summary:        Shared libraries for bzip3 compression and decompression
License:        LGPL-3.0-or-later AND Apache-2.0 
# Forked, fixed, and pruned libasais <https://github.com/IlyaGrebnov/libsais>
# because of rejected fix <https://github.com/IlyaGrebnov/libsais/issues/10>.
Provides:       bundled(libsais) = 2.7.0

%description libs
This is a library for compressing and decompressing bzip3 compression format.
bzip3 features higher compression ratios and better performance than bzip2
thanks to an order-0 context mixing entropy coder, a fast Burrows-Wheeler
transform code making use of suffix arrays and a run-length encoding with
Lempel-Ziv prediction pass based on LZ77-style string matching and PPM-style
context modeling.

%package devel
Summary:        Files for developing with bzip3 library
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Header files, a pkg-config module and link objects for building applications
which use a bzip3 library.

%prep
%autosetup -p1
# Remove generated autoconf files
rm aclocal.m4 configure Makefile.in
# Remove generated manual pages
for F in *.1.in; do
    rm "${F%%.in}"
done
# Unbundle autoconf macros and scripts, except those not yet packaged in
# autoconf-archive
find build-aux -type f \! \( \
    -name ax_progvar.m4 -o \
    -name ax_subst_man_date.m4 -o \
    -name ax_subst_transformed_package_name.m4 \
    \) -delete
# Execute git-version-gen from a system location
ln -s %{_datadir}/gnulib/build-aux/git-version-gen build-aux/git-version-gen

%build
autoreconf -vfi
%configure \
    --disable-arch-native \
    --with-pic \
    --with-pthread \
    --enable-shared \
    --disable-static \
    --disable-static-exe
%{make_build}

%check
make check roundtrip %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -name '*.la' -delete
# Deduplicate identical files
if cmp %{buildroot}%{_mandir}/man1/{bz3cat,bunzip3}.1; then
    rm %{buildroot}%{_mandir}/man1/bunzip3.1
    ln -s bz3cat.1 %{buildroot}%{_mandir}/man1/bunzip3.1
fi

%files
%define programs \{bunzip3,bz3cat,bz3grep,bz3less,bz3more,bz3most,bzip3\}
%{_bindir}/%{programs}
%{_mandir}/man1/%{programs}.1*

%files libs
%license 3rdparty/libsais-LICENSE LICENSE
%doc NEWS README.md
%{_libdir}/libbzip3.so.1{,.*}

%files devel
%{_includedir}/libbz3.h
%{_libdir}/libbzip3.so
%{_libdir}/pkgconfig/bzip3.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Petr Pisar <ppisar@redhat.com> - 1.5.1-1
- 1.5.1 bump

* Mon Dec 16 2024 Petr Pisar <ppisar@redhat.com> - 1.5.0-1
- 1.5.0 bump

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Petr Pisar <ppisar@redhat.com> - 1.4.0-1
- 1.4.0 bump

* Mon Aug 07 2023 Petr Pisar <ppisar@redhat.com> - 1.3.2-1
- 1.3.2 bump

* Tue Jul 25 2023 Petr Pisar <ppisar@redhat.com> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Petr Pisar <ppisar@redhat.com> - 1.3.1-1
- 1.3.1 bump

* Wed Apr 05 2023 Petr Pisar <ppisar@redhat.com> - 1.3.0-1
- 1.3.0 bump (CVE-2023-29415, CVE-2023-29416, CVE-2023-29417, CVE-2023-29418,
  CVE-2023-29419, CVE-2023-29420, CVE-2023-29421)

* Mon Mar 27 2023 Petr Pisar <ppisar@redhat.com> - 1.2.3-1
- 1.2.3 bump

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Petr Pisar <ppisar@redhat.com> - 1.2.2-1
- 1.2.2 bump

* Fri Nov 11 2022 Petr Pisar <ppisar@redhat.com> - 1.2.1-1
- 1.2.1 bump

* Wed Nov 02 2022 Petr Pisar <ppisar@redhat.com> - 1.2.0-3
- Do not own pkg-config directory

* Wed Nov 02 2022 Petr Pisar <ppisar@redhat.com> - 1.2.0-2
- Less globs and and more verbose output in a spec file

* Tue Nov 01 2022 Petr Pisar <ppisar@redhat.com> - 1.2.0-1
- 1.2.0 bump

* Wed Oct 26 2022 Petr Pisar <ppisar@redhat.com> - 1.1.8-1
- 1.1.8 packaged

