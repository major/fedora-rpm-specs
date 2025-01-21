Name:           xdemorse
Version:        3.5
Release:        18%{?dist}
Summary:        GTK based application for decoding and displaying Morse code signals

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.qsl.net/5b4az/pkg/morse/xdemorse/xdemorse.html
Source0:        http://www.qsl.net/5/5b4az//pkg/morse/%{name}/%{name}-%{version}.tar.bz2
#Wrapper script for user config
Source3:        xdemorse.sh.in
Patch0:         %{name}-3.5-desktopfile.patch
Patch1:         %{name}-3.5-Makefile.patch
Patch2: xdemorse-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel, desktop-file-utils, alsa-lib-devel

%description
xdemorse is a GTK+ graphical version of demorse, using the same
decoding engine as demorse.

It has an FFT-derived "waterfall" display of the incoming audio signal's
spectrum, as well as a 'scope-like display of the audio detector's output
and status of the mark/space discriminator ("slicer"). xdemorse also has
CAT for the FT-847 and this can be used to net the receiver's frequency
to the incoming signal, by clicking near its trace in the waterfall display.

%prep
%setup -q
%patch -P0 -p1 -b .desktop
%patch -P1 -p1 -b .makefile
%patch -P2 -p1

%build

%configure
make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

make install DESTDIR=$RPM_BUILD_ROOT

#install default user configuration file
install -p -D -m 0644 .xdemorse/xdemorserc $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -p -D -m 0644 .xdemorse/%{name}.glade $RPM_BUILD_ROOT%{_datadir}/%{name}/

#move original binary to libexecdir
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}/%{name}-bin

#install wrapper script
install -p -D -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/xdemorse

install -p -D -m 644 AUTHORS ChangeLog README doc/Morsecode.txt doc/%{name}.html $RPM_BUILD_ROOT%{_pkgdocdir}

%files
%{_pkgdocdir}
%license COPYING
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/xdemorserc
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man*/%{name}*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.5-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 3.5-13
- Fix bundled configure check for C99 compatibility (#2167315)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Lucian Langa <lucilanga@gnome.eu.org> - 3.5-2
- misc cleanups
- install man and doc files
- update BR
- fix desktop icon
- patch out install config data (we handle that spearately)
- update wraper config location

* Fri Jun 22 2018 Lucian Langa <lucilanga@gnome.eu.org> - 3.5-1
- use png file for icon
- new upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 28 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.9-1
- Update to 2.9 to fix F23FTBFS, RHBZ#1240083.
- Remove BR: autoconf, automake; Don't run autogen.sh.
- Add %%license.
- Append AM_CFLAGS= AM_LDFLAGS= to prevent Makefiles from interfering with
  RPM_OPT_FLAGS.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Richard Hughes <richard@hughsie.com> - 2.7-2
- Use RPM_OPT_FLAGS when compiling
- Resolves: #1102031

* Tue May 06 2014 Richard Hughes <richard@hughsie.com> - 2.7-1
- New upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 07 2012 Lucian Langa <cooly@gnome.eu.org> - 2.1-1
- update BR
- update patch for a proper build
- update to latest upstream release

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3-8
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3-6
- fix implicit dso linking (#564831)

* Thu Nov 26 2009 Lucian Langa <cooly@gnome.eu.org> - 1.3-5
- improve desktop file (#530843)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Lucian Langa <cooly@gnome.eu.org> - 1.3-3
- upstream modified current release source

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Lucian Langa <cooly@gnome.eu.org> - 1.3-1
- misc cleanups
- fix desktop file
- new upstream release

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 1.2-2
- fix for #458818

* Sat Aug 02 2008 Lucian Langa <cooly@gnome.eu.org> - 1.2-1
- update to 1.2 release

* Wed Jul 16 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9-4
- Add missing doc

* Sun Mar 02 2008 Sindre Pedersen Bjordal <sindrepb@fedoraproject.org> - 0.9-3
- Add wrapper script to ensure required user configuration is present

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 0.9-2
- Add .desktop and icon
- Submit for review

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 0.9-1
- Upstream Version Bump

* Mon Dec 10 2007 Sindre Pedersen Bjørdal - 0.8-1
- Initial build
