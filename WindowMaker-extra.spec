Name:           WindowMaker-extra
Version:        0.1
Release:        21%{?dist}
Summary:        Extra icons and themes for WindowMaker

License:        GPLv2
URL:            http://www.windowmaker.org
Source0:        http://windowmaker.org/pub/source/release/WindowMaker-extra-0.1.tar.gz
BuildArch:      noarch

BuildRequires:  make
Requires:       WindowMaker

%description
This is the extra data package for Window Maker. For now it only contains some
icons and a few themes.

%prep
%setup -q

%build
%configure

%install
%make_install

%files
%doc COPYING README
%{_datadir}/WindowMaker/Icons/Ant.xpm
%{_datadir}/WindowMaker/Icons/Antennae.xpm
%{_datadir}/WindowMaker/Icons/Bee48x48.xpm
%{_datadir}/WindowMaker/Icons/Beer.xpm
%{_datadir}/WindowMaker/Icons/Bird.xpm
%{_datadir}/WindowMaker/Icons/Book.xpm
%{_datadir}/WindowMaker/Icons/Bookshelf.xpm
%{_datadir}/WindowMaker/Icons/Brain.xpm
%{_datadir}/WindowMaker/Icons/BulletHole.xpm
%{_datadir}/WindowMaker/Icons/CashRegister.xpm
%{_datadir}/WindowMaker/Icons/Clipboard.xpm
%{_datadir}/WindowMaker/Icons/Cola.xpm
%{_datadir}/WindowMaker/Icons/ColorGNU.xpm
%{_datadir}/WindowMaker/Icons/Correspondence.dir.xpm
%{_datadir}/WindowMaker/Icons/CrystalSkull.dir.xpm
%{_datadir}/WindowMaker/Icons/Daemon.xpm
%{_datadir}/WindowMaker/Icons/Detergent.dir.xpm
%{_datadir}/WindowMaker/Icons/DoomII.xpm
%{_datadir}/WindowMaker/Icons/Draw.xpm
%{_datadir}/WindowMaker/Icons/EscherCube.xpm
%{_datadir}/WindowMaker/Icons/EscherTriangle.xpm
%{_datadir}/WindowMaker/Icons/Fish5.dir.xpm
%{_datadir}/WindowMaker/Icons/Football.xpm
%{_datadir}/WindowMaker/Icons/FootballUS.xpm
%{_datadir}/WindowMaker/Icons/Gear.xpm
%{_datadir}/WindowMaker/Icons/Ghost.xpm
%{_datadir}/WindowMaker/Icons/HP-16C-48.xpm
%{_datadir}/WindowMaker/Icons/HandOpen.xpm
%{_datadir}/WindowMaker/Icons/HandPointing.xpm
%{_datadir}/WindowMaker/Icons/HandPointingLeft.xpm
%{_datadir}/WindowMaker/Icons/HandPunch.xpm
%{_datadir}/WindowMaker/Icons/HandReach.xpm
%{_datadir}/WindowMaker/Icons/HeroSandwich.dir.xpm
%{_datadir}/WindowMaker/Icons/LadyBug48x48.xpm
%{_datadir}/WindowMaker/Icons/Microphone.xpm
%{_datadir}/WindowMaker/Icons/Netscape.xpm
%{_datadir}/WindowMaker/Icons/NewsAgent.xpm
%{_datadir}/WindowMaker/Icons/PDF.xpm
%{_datadir}/WindowMaker/Icons/Padlock.xpm
%{_datadir}/WindowMaker/Icons/Paint.xpm
%{_datadir}/WindowMaker/Icons/Pencils.24.xpm
%{_datadir}/WindowMaker/Icons/Penguin.xpm
%{_datadir}/WindowMaker/Icons/Radio.xpm
%{_datadir}/WindowMaker/Icons/Reference.xpm
%{_datadir}/WindowMaker/Icons/Rumi.xpm
%{_datadir}/WindowMaker/Icons/Snail.xpm
%{_datadir}/WindowMaker/Icons/T2-Film.xpm
%{_datadir}/WindowMaker/Icons/TagIcon.xpm
%{_datadir}/WindowMaker/Icons/TapeIcon1.xpm
%{_datadir}/WindowMaker/Icons/TrueDie48.xpm
%{_datadir}/WindowMaker/Icons/WheelbarrowFull.xpm
%{_datadir}/WindowMaker/Icons/WordEditor.xpm
%{_datadir}/WindowMaker/Icons/Wrench-12bit.xpm
%{_datadir}/WindowMaker/Icons/bomb2.xpm
%{_datadir}/WindowMaker/Icons/inspect.xpm
%{_datadir}/WindowMaker/Icons/monitor.xpm
%{_datadir}/WindowMaker/Icons/paint.xpm
%{_datadir}/WindowMaker/Icons/tile.black.xpm
%{_datadir}/WindowMaker/Icons/tile.snow.xpm
%{_datadir}/WindowMaker/Icons/tile.xpm
%{_datadir}/WindowMaker/Icons/tile2.xpm
# included with WindowMaker
%exclude %{_datadir}/WindowMaker/Icons/xv.xpm
%{_datadir}/WindowMaker/Themes/Checker.themed/
%{_datadir}/WindowMaker/Themes/LeetWM.themed/
%{_datadir}/WindowMaker/Themes/Night.themed/
%{_datadir}/WindowMaker/Themes/STEP2000.themed/



%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.1-2
- spec cleanup

* Mon Jan 07 2013 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 0.1-1
- Create separate package for -extras. This has been included with WindowMaker
  a while back.
