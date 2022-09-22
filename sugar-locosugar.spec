Name:           sugar-locosugar
Version:        12
Release:        5%{?dist}
Summary:        A game for discovering how to use the mouse and keyboard

License:        GPLv3+ and LGPLv2+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/LocoSugar
Source0:        http://download.sugarlabs.org/sources/honey/LocoSugar/LocoSugar-%{version}.tar.bz2

BuildRequires:  python3-devel python3 sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
LocoSugar is a simple game for discovering how to use the mouse 
and keyboard. The game is inspired by CucoXO which walks the user 
through a series of games. The first game is simply to track a moving 
object with the mouse, game 2 and 3 involve clicking. Game 4 involves 
dragging while game 5,6 and 7 involve typing.

%prep
%setup -q -n LocoSugar-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/LocoSugar.activity/ 

%find_lang org.sugarlabs.LocoSugar

%files -f org.sugarlabs.LocoSugar.lang
%license COPYING
%doc NEWS CREDITS
%{sugaractivitydir}/LocoSugar.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 12-1
- Release version 12
- Change to py_byte_compile as stated in phase 3
  (See https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 11-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-7
- Remove the generated .desktop file (#1424501)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-1
- release of version 11

* Fri May 17 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 9-1
- release of version 9

* Fri Jul 13 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 3-3
- fixed license typo

* Thu Jul 12 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 3-2
- removed defattar in files section, removed comments and fixed license issue

* Sat Jun 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 3-1
- initial packaging
