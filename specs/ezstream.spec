Name:           ezstream
Version:        1.0.2
Release:        15%{?dist}
Summary:        Command line source client for Icecast media streaming servers
## Not installed files:
# aclocal.m4:               FSFULLRWD
# build-aux/compile:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/config.guess:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/config.rpath:   FSFULLR
# build-aux/config.sub:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/depcomp:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/install-sh:     X11 AND LicenseRef-Fedora-Public-Domain
# build-aux/ltmain.sh:      GPL-2.0-or-later WITH Libtool-exception AND
#                           GPL-3.0-or-later WITH Libtool-exception AND
#                           TODO:
#                           <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/661>
#                           GPL-3.0-or-later
# build-aux/missing:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/test-driver:    GPL-2.0-or-later WITH Autoconf-exception-generic
# compat/getopt.c:          ISC AND BSD-2-Clause
# compat/reallocarray.c:    ISC
# configure:                FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# doc/Makefile.in:          FSFULLRWD
# examples/Makefile.in:     FSFULLRWD
# INSTALL:                  FSFUL
# m4/attribute.m4:          ISC
# m4/ccflags.m4:            ISC
# m4/libshout.m4:           ISC
# m4/libtool.m4:            FSFULLR AND GPL-2.0-or-later WITH Libtool-exception AND FSFUL
# m4/libxml2.m4:            ISC
# m4/ltoptions.m4:          FSFULLR
# m4/ltsugar.m4:            FSFULLR
# m4/ltversion.m4:          FSFULLR
# m4/Makefile.in:           FSFULLRWD
# m4/tree.m4:               ISC
# Makefile.in:              FSFULLRWD
# src/Makefile.in:          FSFULLRWD
# tests/Makefile.in:        FSFULLRWD
## Installed files:
# compat/strlcat.c:         ISC
# compat/strlcpy.c:         ISC
# compat/strtonum.c:        ISC
# COPYING:                  GPL-2.0-only
# doc/ezstream-cfgmigrate.1.in.in:  ISC
# doc/ezstream-file.sh.1.in.in:     ISC
# doc/ezstream.1.in.in:             GPL-2.0-only
# src/cfg.c:                ISC
# src/cfg.h:                ISC
# src/cfg_decoder.c:        ISC
# src/cfg_decoder.h:        ISC
# src/cfg_encoder.c:        ISC
# src/cfg_encoder.h:        ISC
# src/cfg_intake.c:         ISC
# src/cfg_intake.h:         ISC
# src/cfg_private.h:        ISC
# src/cfg_server.c:         ISC
# src/cfg_server.h:         ISC
# src/cfg_stream.c:         ISC
# src/cfg_stream.h:         ISC
# src/cfgfile_xml.c:        ISC
# src/cfgfile_xml.h:        ISC
# src/cmdline.c:            ISC
# src/cmdline.h:            ISC
# src/ezconfig0.c:          GPL-2.0-only
# src/ezconfig0.h:          GPL-2.0-only
# src/ezstream.c:           GPL-2.0-only
# src/ezstream.h:           ISC
# src/ezstream-cfgmigrate.c:    ISC
# src/ezstream-file.sh.in:  ISC
# src/log.c:                ISC
# src/log.h:                ISC
# src/mdata.c:              ISC
# src/mdata.h:              ISC
# src/playlist.c:           ISC
# src/playlist.h:           ISC
# src/stream.c:             ISC
# src/stream.h:             ISC
# src/util.c:               GPL-2.0-only
# src/util.h:               GPL-2.0-only
# src/xalloc.c:             ISC
# src/xalloc.h:             ISC
License:        GPL-2.0-only AND ISC
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
autoreconf -I /usr/share/gettext/m4 -fi
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
* Sun Jan 25 2026 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/TagLib2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu May 22 2025 Petr Pisar <ppisar@redhat.com> - 1.0.2-12
- Adapt to gettext-0.25
- Correct a license tag to "GPL-2.0-only AND ISC"

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
