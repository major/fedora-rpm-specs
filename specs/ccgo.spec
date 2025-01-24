Name:       ccgo
Version:    0.3.6.5
Release:    26%{?dist}
Summary:    An IGS (Internet Go Server) client written in C++
# *.cc and *.hh:    GPL-3.0-or-later
# COPYING:  GPL-3.0 text
## Unbundled
# aclocal.m4:   GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFULLR
# configure:    FSFUL
# compile:      GPL-2.0-or-later WITH Autoconf-exception-generic
# config.guess: GPL-3.0-or-later
# config.sub:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# depcomp:      GPL-2.0-or-later
# gettext.h:    GPL-3.0-or-later
# go/Makefile.in:   FSFULLRWD
# igs/Makefile.in:  FSFULLRWD
# igs/parser/Makefile.in:   FSFULLRWD
# install-sh:   X11 AND LicenseRef-Fedora-Public-Domain
# m4/gettext.m4:    FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# Makefile.in:      FSFULLRWD
# missing:      GPL-2.0-or-later WITH Autoconf-exception-generic
# po/Makefile.in.in:   "This file can be copied and used freely without restrictions"
License:    GPL-3.0-or-later
SourceLicense:  GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND LicenseRef-Fedora-Public-Domain
URL:        http://ccdw.org/~cjj/prog/%{name}/
Source0:    %{url}src/%{name}-%{version}.tar.gz
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
# See <http://www.freedesktop.org/software/appstream/docs/> for more details.
Source1:    %{name}.appdata.xml
# Fix building against libsigc++-2.6.0, bug #1304679
Patch0:     ccgo-0.3.6.5-Port-to-libsigc-2.6.0.patch
# Adapt to assert() macro changes in glibc > 2.26, bug #1482990
Patch1:     ccgo-0.3.6.5-Adapt-to-glibc-assert-change.patch
# Update config.sub to support aarch64, bug #925132
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gconfmm-2.6)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  sed
# Optional, but ccgo does not signal missing gnugo through GUI
Requires:       gnugo

%description
ccGo allows you to play go with GNU Go on your computer or with other players
on an Internet Go Server (IGS) on the Internet. It supports smart game format
(SGF) suitable for exchanging game records.

%prep
%autosetup -p1
# Make XDG desktop file compliant
sed -i -e '/^Encoding/d' -e '/^Categories/s/Application;//' \
    %{name}.desktop.in
# Update config.sub to support aarch64, bug #925132
# Remove bundled files
rm ABOUT-NLS aclocal.m4 configure compile config.guess config.sub depcomp gettext.h \
    go/Makefile.in igs/Makefile.in igs/parser/Makefile.in install-sh m4/* \
    Makefile.in missing po/Makefile.in.in
# gettextize breaks configure.ac. Rather symlink the header file.
ln -s /usr/share/gettext/gettext.h gettext.h
autoreconf -i -f

%build
%configure
%{make_build}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%install
%{make_install}

# Register as an application to be visible in the software center
install -d %{buildroot}%{_datadir}/appdata
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/ccgo
%{_mandir}/man6/ccgo.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ccgo
%{_datadir}/pixmaps/ccgo.xpm

%changelog
* Wed Jan 22 2025 Petr Pisar <ppisar@redhat.com> - 0.3.6.5-26
- Modernize a spec file
- Declare a source license

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.6.5-24
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Kalev Lember <klember@redhat.com> - 0.3.6.5-10
- Fix component type typo in appdata file

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Petr Pisar <ppisar@redhat.com> - 0.3.6.5-7
- Adapt to assert() macro changes in glibc > 2.26 (bug #1482990)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Mar 09 2017 Petr Pisar <ppisar@redhat.com> - 0.3.6.5-3
- Modernize spec file
- Add content rating to the AppData file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Petr Pisar <ppisar@redhat.com> - 0.3.6.5-1
- 0.3.6.5 bump
- Fix building against libsigc++-2.6.0 (bug #1304679)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.6.4-14
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.3.6.4-13
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Petr Pisar <ppisar@redhat.com> - 0.3.6.4-10
- Pass compilation with -Wformat-security (bug #1037009)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 0.3.6.4-8
- Update config.sub to support aarch64 (bug #925132)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-5
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Petr Pisar <ppisar@redhat.com> - 0.3.6.4-3
- Rebuild against new libpng-1.5.6 and clean spec file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Petr Pisar <ppisar@redhat.com> - 0.3.6.4-1
- 0.3.6.4 imported
