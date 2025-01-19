Name:           naev-data
Version:        0.11.4
Release:        4%{?dist}
Summary:        Data files for NAEV
License:        GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC-BY-3.0 AND CC-BY-4.0 AND (GPL-3.0-only OR CC-BY-SA-3.0) AND GFDL-1.2-no-invariants-only
URL:            http://naev.org
Source0:        https://github.com/naev/naev/archive/v%{version}/naev-%{version}-source.tar.xz
Requires:       naev = %{version}
BuildArch:      noarch

%description
NAEV is a 2D space trading and combat game, in a similar vein to Escape
Velocity.

NAEV is played from a top-down perspective, featuring fast-paced combat, many
ships, a large variety of equipment and a large galaxy to explore. The game is
highly open-ended, letting you proceed at your own pace.

This package contains the data files needed to play the game

%prep
%autosetup -n naev-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/naev
cp -a artwork %{buildroot}%{_datadir}/naev/dat

%files
%{_datadir}/naev

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 17 2024 Jonathan Dieter <jdieter@gmail.com> - 0.11.4-2
- Update to 0.11.4
- Build in side-tag

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jonathan Dieter <jdieter@gmail.com> - 0.10.2-1
- Update to 0.10.2

* Thu Dec 29 2022 Jonathan Dieter <jdieter@gmail.com> - 0.10.1-1
- Update to 0.10.1

* Sun Oct 09 2022 Jonathan Dieter <jdieter@gmail.com> - 0.9.4-1
- Update to 0.9.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Jonathan Dieter <jdieter@gmail.com> - 0.9.0-1
- Update to 0.9.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 28 2021 Jonathan Dieter <jdieter@gmail.com> - 0.8.2-1
- Update to 0.8.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Jonathan Dieter <jdieter@gmail.com> - 0.7.0-6
- Remove obsolete Group tag

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Jonathan Dieter <jdieter@lesbg.com> - 0.7.0-3
- Build again because koji put 0.7.0-1 in the repository after 0.7.0-2

* Sat Jul 15 2017 Jonathan Dieter <jdieter@lesbg.com> - 0.7.0-2
- Update to new version with new missions
- Fix ndata location

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Jonathan Dieter <jdieter@lesbg.com> - 0.6.1-1
- Update to 0.6.1 with improved AI and new missions
 
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Jonathan Dieter <jdieter@lesbg.com> - 0.6.0-1
- Update to 0.6.0 which includes:
   + Greatly expanded galaxy
   + New missions
   + Hidden jumps
 
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Jonathan Dieter <jdieter@lesbg.com> - 0.5.3-8
- Attempt another rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.5.3-1
- Update to 0.5.3 - with new missions and bugfixes

* Fri Mar  2 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.5.1-1
- Update to 0.5.1 - with new missions, a new faction and other improvements 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-4
- Add dist tag

* Tue Jun 28 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-3
- Fix license
- Remove unneeded defattr

* Mon Jun 27 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-2
- Spec file cleanup

* Sun Jun  5 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-1
- Convert openSUSE Build Service RPM to Fedora RPM
- Split data into separate source rpm

* Wed Jun  9 2010 dbuck <noone@example.com> - 0.4.2-1
- initial build
