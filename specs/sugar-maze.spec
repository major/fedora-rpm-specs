Name:      sugar-maze
Version:   32
Release:   4%{?dist}
Summary:   Maze game for Sugar
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:   GPL-3.0-or-later
URL:       http://wiki.laptop.org/go/Maze
Source0:   https://download.sugarlabs.org/sources/honey/Maze/Maze-%{version}.tar.bz2
BuildArch: noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar

%description
A simple maze game for the XO laptop. You can play by yourself or race
to solve it with your buddies. Up to 3 people can play on a single XO
laptop and lots more can play when shared over the network.

%prep
%autosetup -n Maze-%{version}
# remove olpcgames library
rm -rf olpcgames

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{buildroot}/%{_prefix}
find  %{buildroot}%{sugaractivitydir}Maze.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
mv player.py %{buildroot}%{sugaractivitydir}/Maze.activity/player.py
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Maze.activity/

%find_lang vu.lux.olpc.Maze

%files -f vu.lux.olpc.Maze.lang
%license COPYING
%{sugaractivitydir}/Maze.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 32-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 13 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 32-1
- Release 32

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 29-2
- fix python3 env

* Mon Feb 10 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 29-1
- Release 29

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 28-1
- Release 28

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 27-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 26-5
- Fix FTBFS issue

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 26-1
- Release 26

* Tue Jun 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 25-1
- Release 25

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 18 2013 Kalpa Welivitigoda <callkalpa@gmail.com> -24-1
- Release 24

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Kalpa Welivitigoda - 22-1
- Release 22

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 01 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-1
- Release 21

* Thu May 10 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 20-1
- Release 20

* Tue Apr 17 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 18-1
- Release 18

* Fri Apr 13 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 17-1
- Release 17

* Thu Mar 29 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 16-1
- Release 16

* Sun Jan 22 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 15-1
- Release 15

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 14-1
- Release 14

* Mon Sep 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 13-1
- Release 13

* Wed Jun  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 11-1
- Release 11

* Wed Jun  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 10-1
- Release 10

* Sun Apr  3 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 9-1
- Release 9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 6-3
- recompiling .py files against Python 2.7 (rhbz#623379)

* Sun Jun 27 2010 Fabian Affolter <fabian@bernewireless.net> - 6-2
- Fixed BZ #604800

* Thu Mar 18 2010 Sebastian Dziallas <sebastian@when.com> - 6-1
- use xo source file to fix load issue

* Sun Dec 27 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.4.20091227
- Python-olpcgames is needed (Replace pygame)
- Changed numbering system

* Wed Nov 26 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.3
- Added Requires: pygame

* Wed Nov 19 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.2
- Spec file clean-up

* Sun Oct 19 2008 Fabian Affolter <fabian@bernewireless.net> - 0-0.1
- Initial package for Fedora
