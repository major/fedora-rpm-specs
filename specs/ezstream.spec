Name:           ezstream
Version:        1.0.2
Release:        11%{?dist}
Summary:        Command line source client for Icecast media streaming servers
## Not installed files:
# aclocal.m4:               FSFULLR
# build-aux/compile:        GPLv2+ with Autoconf exception
# build-aux/config.guess:   GPLv3+ with Autoconf exception
# build-aux/config.rpath:   FSFULLR
# build-aux/config.sub:     GPLv3+ with Autoconf exception
# build-aux/depcomp:        GPLv2+ with Autoconf exception
# build-aux/install-sh:     MIT and Public Domain
# build-aux/ltmain.sh:      GPLv3+ and
#                           GPLv3+ with Libtool exception and
#                           GPLv2+ with Libtool exception
# build-aux/missing:        GPLv2+ with Autoconf exception
# build-aux/test-driver:    GPLv2+ with Autoconf exception
# compat/getopt.c:          MIT and BSD
# compat/reallocarray.c:    MIT
# configure:                GPLv2+ with Libtool exception and FSFUL
# doc/Makefile.in:          FSFULLR
# examples/Makefile.in:     FSFULLR
# INSTALL:                  FSFUL
# m4/attribute.m4:          MIT
# m4/ccflags.m4:            MIT
# m4/libshout.m4:           MIT
# m4/libtool.m4:            GPLv2+ with Libtool exception and FSFULLR and FSFUL
# m4/libxml2.m4:            MIT
# m4/ltoptions.m4:          FSFULLR
# m4/ltsugar.m4:            FSFULLR
# m4/ltversion.m4:          FSFULLR
# m4/Makefile.in:           FSFULLR
# m4/tree.m4:               MIT
# Makefile.in:              FSFULLR
# src/Makefile.in:          FSFULLR
# tests/Makefile.in:        FSFULLR
## Installed files:
# compat/strlcat.c:         MIT
# compat/strlcpy.c:         MIT
# compat/strtonum.c:        MIT
# COPYING:                  GPLv2
# doc/ezstream-cfgmigrate.1.in.in:  MIT
# doc/ezstream-file.sh.1*:  MIT
# doc/ezstream.1*:          GPLv2
# src/cfg.c:                MIT
# src/cfg.h:                MIT
# src/cfg_decoder.c:        MIT
# src/cfg_decoder.h:        MIT
# src/cfg_encoder.c:        MIT
# src/cfg_encoder.h:        MIT
# src/cfg_intake.c:         MIT
# src/cfg_intake.h:         MIT
# src/cfg_private.h:        MIT
# src/cfg_server.c:         MIT
# src/cfg_server.h:         MIT
# src/cfg_stream.c:         MIT
# src/cfg_stream.h:         MIT
# src/cfgfile_xml.c:        MIT
# src/cfgfile_xml.h:        MIT
# src/cmdline.c:            MIT
# src/cmdline.h:            MIT
# src/ezconfig0.c:          GPLv2
# src/ezconfig0.h:          GPLv2
# src/ezstream.c:           GPLv2
# src/ezstream.h:           MIT
# src/ezstream-cfgmigrate.c:    MIT
# src/ezstream-file.sh.in:  MIT
# src/log.c:                MIT
# src/log.h:                MIT
# src/mdata.c:              MIT
# src/mdata.h:              MIT
# src/playlist.c:           MIT
# src/playlist.h:           MIT
# src/stream.c:             MIT
# src/stream.h:             MIT
# src/util.c:               GPLv2
# src/util.h:               GPLv2
# src/xalloc.c:             MIT
# src/xalloc.h:             MIT
# Automatically converted from old format: GPLv2 and MIT - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:            https://www.icecast.org/%{name}/
Source0:        https://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
# Link to distribution-wide certificate store, not upsreamable
Patch0:         ezstream-1.0.1-doc-Link-to-distribution-OpenSSL-certificate-bundle.patch
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake >= 1.10
BuildRequires:  coreutils
BuildRequires:  gcc
# gettext-devel for AM_ICONV macro
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2
BuildRequires:  pkgconfig(shout) >= 2.2
BuildRequires:  pkgconfig(taglib_c) >= 1.4

%description
Ezstream is a command line source client for media streams, primarily for
streaming to Icecast servers.

It allows the creation of media streams based on input from files or standard
input that is piped through an optional external decoder and encoder. As every
part of this chain is highly configurable, ezstream can be useful in a large
number of streaming setups.

Supported media containers for streaming are MP3, Ogg, Theora, WebM, and
Matroska. Supported transport protocols are HTTP, ICY, and RoarAudio.
Metadata support is provided by TagLib library.

%prep
%setup -q
%patch -P0 -p1
# Regenerate a build script
autoreconf -fi
# Remove bundled code
rm compat/{getopt,reallocarray}.c
# Copy examples for a documention
mkdir __examples
cp -a examples __examples/examples
rm -f __examples/examples/Makefile*
chmod a-x __examples/examples/*

%build
%configure \
    --without-asan \
    --enable-largefile \
    --disable-maintainer-mode \
    --disable-rpath \
    --enable-shared \
    --disable-static
# --with-taglib actually inhibits the taglib support
%{make_build}

%check
make %{?_smp_mflags} check

%install
%{make_install}
rm -rf $RPM_BUILD_ROOT%{_docdir} $RPM_BUILD_ROOT%{_datadir}/examples

%files
%license COPYING
%doc ChangeLog NEWS README.md __examples/examples
%{_bindir}/ezstream
%{_bindir}/ezstream-cfgmigrate
%{_bindir}/ezstream-file.sh
%{_mandir}/man1/ezstream.1*
%{_mandir}/man1/ezstream-cfgmigrate.1*
%{_mandir}/man1/ezstream-file.sh.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.2-10
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Petr Pisar <ppisar@redhat.com> - 1.0.2-1
- 1.0.2 bump
- Perform tests at build time

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Petr Pisar <ppisar@redhat.com> - 1.0.1-1
- 1.0.1 bump

* Thu Jan 30 2020 Petr Pisar <ppisar@redhat.com> - 1.0.0-1
- 1.0.0 bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 Petr Pisar <ppisar@redhat.com> - 0.6.0-3
- Fix a crash on configuration without format (bug #1244481)
- Build-require gcc instead of glibc-headers (bug #1230472)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Petr Pisar <ppisar@redhat.com> - 0.6.0-1
- Modernize spec file
- Correct dependencies
- Correct license tag from (GPLv2) to (GPLv2 and BSD and MIT)
- 0.6.0 bump (fixes a security bug when processing metadata placeholders
  leading to arbitrary shell command execution)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov  6 2009 Ian Weller <ian@ianweller.org> - 0.5.6-1
- 0.5.6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 14 2009 Ian Weller <ianweller@gmail.com> 0.5.3-2
- Remove doc declaration from the man page
- Move examples into examples/ within the docdir
- Remove need for patch and put commands in the right parts

* Sat Apr 05 2008 Ian Weller <ianweller@gmail.com> 0.5.3-1
- Initial package build.
