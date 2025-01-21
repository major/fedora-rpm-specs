Name:           stalonetray
Version:        0.8.5
Release:        4%{?dist}
Summary:        A stand alone notification area

# License is only mentioned in COPYING
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://kolbusa.github.io/%{name}
Source0:        https://github.com/kolbusa/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/kolbusa/stalonetray/pull/34
Patch0:         stalonetray-0.8.5--Werror-format-security.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libX11-devel

%description
The stalonetray is a STAnd-aLONE system TRAY (notification area).
It has minimal build and run-time dependencies: the Xlib only. The XEMBED
support is planned. Stalonetray runs under virtually any window manager.

%prep
%setup -q
%patch -P0 -p1 -b .error-format

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -D -m644 stalonetrayrc.sample %{buildroot}%{_sysconfdir}/stalonetrayrc


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc stalonetrayrc.sample stalonetray.html stalonetray.xml
%{_sysconfdir}/stalonetrayrc
%{_bindir}/stalonetray
%{_mandir}/man1/stalonetray.*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.5-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 30 2024 Ben Boeckel <fedora@me.benboeckel.net> - 0.8.5-1
- Update to 0.8.5
- Resolves #2097004

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Ben Boeckel <mathstuf@gmail.com> - 0.8.3-11
- Fix install like to use %%{_sysconfdir}

* Tue Oct 29 2019 Ben Boeckel <mathstuf@gmail.com> - 0.8.3-10
- Install /etc/stalonetrayrc (rhbz#1511145)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Ben Boeckel <mathstuf@gmail.com> - 0.8.3-1
- Update to 0.8.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.8.1-6
- Additional fixes for -Werror=format-security (#1107373)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 20 2013 Ben Boeckel <mathstuf@gmail.com> - 0.8.1-4
- Add patch to fix compilation with -Werror=format-security

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 04 2012 Ben Boeckel <mathstuf@gmail.com> - 0.8.1-1
- Update to 0.8.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 26 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 0.8.0-1
- 0.8.0
- Introduces the 'slot_size' option which defines the size of a slot
  containing an icon
- Changed the way the 'geometry' option works: now it's expressed in
  slot_size multiples instead of pixels.
  See the ChangeLog for more information.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.7.6-2
- license is GPLv2+
- some minor changes in spec

* Tue Jan 15 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.7.6-1
- New upstream version: 0.7.6

* Wed Oct 31 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.7.3-1
- New upstream version: 0.7.3

* Tue Sep 25 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.7-1
- Initial Release
