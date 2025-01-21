Name:           vobcopy
Version:        1.2.1
Release:        7%{?dist}
Summary:        Utility to copy DVD .vob files to disk

License:        GPL-2.0-or-later
URL:            https://github.com/barak/vobcopy
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Update GPLv2 license text
Patch:          %{url}/pull/19.patch

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  gettext-devel
BuildRequires:  libdvdread-devel

%description
Vobcopy copies DVD .vob files to disk via libdvdread and merges them into
file(s) with the name extracted from the DVD. There is one drawback though:
at the moment vobcopy doesn't deal with multi-angle DVDs. But since these are
rather sparse this shouldn't matter much.

%prep
%autosetup -p1
autoreconf -fiv

# Convert German manpage to UTF-8
# https://github.com/barak/vobcopy/pull/18
iconv -f iso8859-1 -t utf-8 vobcopy.1.de > vobcopy.1.de.conv && \
  mv -f vobcopy.1.de.conv vobcopy.1.de

%build
%configure
%make_build

%install
%make_install

# Remove the docs we include ourselves as %%doc
rm -r %{buildroot}%{_datadir}/doc

%files
%doc Changelog README Release-Notes TODO
%doc alternative_programs.txt
%license COPYING
%{_bindir}/vobcopy
%{_mandir}/man1/vobcopy.1*
%lang(de) %{_mandir}/de/man1/vobcopy.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 28 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 1.2.1-4
- Convert license tag to SPDX
- Rework specfile to follow the Fedora packaging guidelines
- Fix outstanding rpmlint issues
- Rework package description

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon May 09 2022 Leigh Scott <leigh123linux@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.2.0-16
- Rebuild for new libdvdread

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.2.0-13
- rebuild for libdvdread ABI bump

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-10
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-4
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.2.0-2
- rebuilt

* Wed Aug 11 2010 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0 (#1051).

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.1.2-3
- rebuild for new F11 features

* Sun Oct 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.1.2-1
- Update to 1.1.2
- drop vobcopy-1.1.1-gcc43.patch

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.1.1-2
- rebuild for RPM Fusion

* Tue May 13 2008 Matthias Saou <http://freshrpms.net/> 1.1.1-1
- Update to 1.1.1.
- Include gcc 4.3 patch.

* Mon Jan 14 2008 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0.

* Sun Jun 24 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Mon Nov 27 2006 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.
- Remove no longer needed gcc change in the Makefile patch.

* Tue Apr 18 2006 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0.
- Add s/gcc-3.4/gcc/ to the Makefile patch.

* Mon Mar 27 2006 Matthias Saou <http://freshrpms.net/> 0.5.16-1
- Major spec file cleanup.

* Fri Jan 6 2006 Robos  <robos@muon.de>
- 0.5.16: -see changelog

* Fri Jul 29 2005 Robos  <robos@muon.de>
- 0.5.15: -option to skip already present files with -m.
  copying of dvd's with files ending in ";?" should work now.

* Sun Oct 24 2004 Robos  <robos@muon.de>
- 0.5.14-rc1: - misc *bsd fixes and first straight OSX support

* Mon Mar 7 2004 Robos  <robos@muon.de>
- 0.5.12-1: -m off-by-one error fixed

* Mon Jan 19 2004 Robos <robos@muon.de>
- 0.5.10-1: -O now works
  cleanup

* Wed Nov 13 2003 Robos <robos@muon.de>
- 0.5.9-1: -F now accepts factor number
  cleanups and small bugfix
  new vobcopy.spec

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- 0.5.8-2: libdvdread is now a pre-requisite

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- first package, 0.5.8-1
