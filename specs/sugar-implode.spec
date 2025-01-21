%global shortname implode

Name:           sugar-%{shortname}
Version:        20
Release:        13%{?dist}
Summary:        Implode for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.sugarlabs.org/go/Activities/Implode
Source0:        http://download.sugarlabs.org/sources/honey/Implode/Implode-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar

%description
Implode is a logic game based on the "falling block" model of Tetris. The game
starts with a grid partially filled with blocks. The player makes a move by 
removing adjacent blocks of the same color in groups of three or more. When 
blocks are removed, higher blocks fall to fill their space, and when a column 
is cleared, the blocks on either side close to fill the gap. The object of the
game is to remove all the blocks. Since the patterns of blocks above changes
when lower blocks are removed, the player must carefully decide what order
in which to remove the blocks so that there are no isolated blocks left at
the end of the game. The levels are generated in such a way that there is
always a sequence of removals that clears the board. 

%prep
%setup -q -n Implode-%{version}
echo "summary = Logic game based on the “falling block” model of Tetris." >> activity/activity.info

sed -i 's/python/python3/' *.py
sed -i '/^summary/d' activity/activity.info

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
#executables
find  %{buildroot}%{sugaractivitydir}Implode.activity/*.py -type f | xargs chmod a+x
for file in %{buildroot}%{sugaractivitydir}Implode.activity/{board,boardgen,color,gridwidget,implodeactivity,implodegame,setup}.py; do
   chmod a+x $file
done

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Implode.activity/

%find_lang com.jotaro.ImplodeActivity

%files -f com.jotaro.ImplodeActivity.lang
%license COPYING
%{sugaractivitydir}/Implode.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 20-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 2 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 20-1
- v20
- Update Python 3 dependency declarations

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 19-1
- Release 19

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 18-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 18-1
- Release 18

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 09 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 15-6
- fixes FTBFS rh#1240038

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 15-1
- Release 15

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 12-1
- Release 12

* Thu Mar  8 2012 Tom Callaway <spot@fedoraproject.org> - 10-1
- update to v10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4.20091228
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-3.20091228
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 9-2.20091228
- recompiling .py files against Python 2.7 (rhbz#623374)

* Mon Dec 28 2009 Fabian Affolter <fabian@bernewireless.net> - 9-1.20090717
- Added python-olpcgames as requirement
- Prepared translations
- Updated to new upstream version 9

* Mon Dec 14 2009 Peter Robinson <pbrobinson@gmail.com> - 5-5.20090717
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539177

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-4.20090717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Fabian Affolter <fabian@bernewireless.net> - 5-3.20090717
- Changed release because it's still a git checkout
- Modified donwload script
- Translation support will follow, I hope
- Changed URL to new upstream location

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 19 2008 Fabian Affolter <fabian@bernewireless.net> - 5-1
- Initial package for Fedora
