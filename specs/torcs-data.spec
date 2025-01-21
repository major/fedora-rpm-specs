Name:           torcs-data
Version:        1.3.7
Release:        19%{?dist}
Summary:        The Open Racing Car Simulator data files

# Automatically converted from old format: GPLv2+ and Free Art - review is highly recommended.
License:        GPL-2.0-or-later AND LAL-1.3
URL:            http://torcs.org/
Source0:        http://downloads.sf.net/torcs/torcs-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  openal-soft-devel
BuildRequires:  plib-devel
BuildRequires:  zlib-devel

Requires:       torcs = %{version}

# Subpackages dropped in F23
Obsoletes:      torcs-data-cars-extra < 1.3.6
Obsoletes:      torcs-data-tracks-dirt < 1.3.6
Obsoletes:      torcs-data-tracks-oval < 1.3.6
Obsoletes:      torcs-data-tracks-road < 1.3.6

%description
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains the data files needed to run the game.


%prep
%setup -q -n torcs-%{version}


%build
%configure


%install
make datainstall DESTDIR=%{buildroot}


%files
# Directory default mode of 0755 is MANDATORY, since installed dirs are 0777
%defattr(-,root,root,0755)
%license COPYING
%{_datadir}/games/torcs/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.7-18
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Pete Walter <pwalter@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Pete Walter <pwalter@fedoraproject.org> - 1.3.6-1
- Update to 1.3.6
- Spec clean up

* Wed Jul 01 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.3.3-7
- Add dist-tag (RHBZ #1237191).

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar  8 2012 Tom Callaway <spot@fedoraproject.org> - 1.3.3-1
- update to 1.3.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Update to 1.3.1.
- Remove no longer existing upstream cars-nascar sub-package (merged in).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-2
- Update License field.
- Don't use _sourcedir.

* Fri Nov 10 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-1
- Update to 1.3.0.

* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.

* Wed Aug  3 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-3
- Replace default tracks requirement (provided by all 3 tracks sub-packages)
  by tracks-road since those are the ones required for a quick race, and yum
  was installing the first available (alphabetically?) package, tracks-dirt.
- Remove now unused virtual provides of tracks sub-packages.

* Mon Feb 28 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-2
- Change %%doc and %%defattr order to fix wrong ownership of doc files.

* Fri Feb 11 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Change License: to "GPL and Free Art License" (#147681).
- Include Free-Art-License and add a copy to each sub-package.

* Mon Feb  7 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3.
- Removed "non-free" cars (kcendra ones, Patwo-Design and VM).

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2
- Added all new tracks : dirt, oval and road.
- Added all new cars : kcendra-gt, kcendra-roadsters, kcendra-sport, nascar
  and VM.
- Updated the %%setup and %%build sections to make them even more flexible.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.2.1-4
- Rebuild for Fedora Core 1.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added a requires on torcs for all packages.

* Mon Apr 28 2003 Matthias Saou <http://freshrpms.net/>
- Fixed the defattr problem, doh!

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

