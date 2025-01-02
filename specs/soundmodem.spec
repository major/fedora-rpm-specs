Name: soundmodem
Version: 0.20
Release: 33%{?dist}
Summary: Soundcard Packet Radio Modem
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://gna.org/projects/soundmodem
Source: http://download.gna.org/soundmodem/%{name}-%{version}.tar.gz
Source1: soundmodem.service
Patch1: %{name}-0.16-dirfix.patch
#fixes security error caused by non-void return in void function
#as function seems used we silently drop it to avoid reusing it.
Patch2: %{name}-0.20-void.patch
Patch3: %{name}-0.20-i386-fix.patch
Patch4: %{name}-0.20-gcc10-fix.patch
Patch5: soundmodem-hamlib42.patch
ExcludeArch:   i686
# Requires: /sbin/ifconfig /sbin/route /sbin/arp
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: gtk2-devel
BuildRequires: alsa-lib-devel
BuildRequires: libxml2-devel
BuildRequires: audiofile-devel
BuildRequires: hamlib-devel
BuildRequires:  systemd
%{?systemd_requires}


%description
This package contains the driver and the diagnostic utility for
userspace SoundModem. It allows you to use soundcards
as Amateur Packet Radio modems.

%package devel

Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%if "%version" < "0.20"
# Versions prior to 0.20 are not c11 compiliant
# Work-around by fallin back to -std=gnu89
%configure CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"
%else
# Versions >= 0.20 seem to be c11 compliant
%configure
%endif
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/ax25
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/soundmodem.service
mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/modem.h %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/simd.h %{buildroot}%{_includedir}/%{name}
%find_lang %{name}

%post
%systemd_post soundmodem.service

%preun
%systemd_preun soundmodem.service

%postun
%systemd_postun_with_restart soundmodem.service


%files -f %{name}.lang
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/*/*
%{_unitdir}/soundmodem.service
%doc AUTHORS ChangeLog NEWS README newqpsk/README.newqpsk
%license COPYING

%files devel
%{_includedir}/%{name}

%changelog
* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 0.20-33
- Rebuild for Hamlib 4.6.

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20-32
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 0.20-27
- Rebuild for hamlib 4.5.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 0.20-24
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 0.20-23
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 0.20-22
- Rebuild for hamlib 4.3.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 0.20-20
- Rebuild for hamlib 4.2.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.20-19
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 0.20-18
- Rebuild for hamlib 4.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 0.20-15
- Rebuild for hamlib 4.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Lucian Langa <lucilanga@gnome.eu.org> - 0.20-13
- add gcc10 fix

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Richard Shaw <hobbes1069@gmail.com> - 0.20-5
- Rebuild for hamlib 3.1.

* Wed Feb 17 2016 Lucian Langa <lucilanga@gnome.eu.org> - 0.20-4
- rebuilt with all patches installed

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Lucian Langa <lucilanga@gnome.eu.org> - 0.20-2
- add patch to fix compiler errors

* Mon Feb 01 2016 Lucian Langa <lucilanga@gnome.eu.org> - 0.20-1
- update source urls
- update to latest upstream

* Thu Aug 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-5
- Append -std=gnu89 to CFLAGS (Fix F23FTBFS, RHBZ#1240015).
- Add %%license.
- Modernize spec.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Lucian Langa <cooly@gnome.eu.org> - 0.18-1
- update to latest upstream
- use temporary url for source

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Lucian Langa <cooly@gnome.eu.org> - 0.16-1
- add patch to fix ax25 config directory
- build against hamlib
- add systemd migration from Alan Crosswell (fixes #854046)
- new upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.15-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 18 2010 Lucian Langa <cooly@gnome.eu.org> - 0.15-1
- new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Lucian Langa <cooly@gnome.eu.org> - 0.14-1
- new upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Lucian Langa <cooly@gnome.eu.org> - 0.12-1
- update BR
- drop autoreconf
- drop all patches as fixed ustream
- new upstream release

* Sun Jan 25 2009 Lucian Langa <cooly@gnome.eu.org> - 0.10-6
- apply debian patch for tx switching in ALSA mode

* Sat Dec 06 2008 Alan Crosswell <alan@columbia.edu> - 0.10-5
- Apply patch to remove spurious printfs.

* Wed Dec 03 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10-4
- move include files to it's own separate include dir
- fix duplicated doc files

* Thu Nov 20 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10-3
- update scriptlets
- update BR
- fix old configure script

* Thu Jul 17 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10-2
- Description update

* Fri Jul 11 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10-1
- Initial spec file

