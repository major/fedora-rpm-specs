Name:           sugar-nutrition
Version:        16
Release:        5%{?dist}
Summary:        A collection of nutrition games

License:        GPLv3+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/Nutrition
Source0:        http://download.sugarlabs.org/sources/honey/Nutrition/Nutrition-%{version}.tar.bz2

BuildRequires:  python3 gettext python3-devel sugar-toolkit-gtk3
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
Nutrition is a collection of nutrition games for sugar. There are 
four games related to nutrition. In all games the user is asked a 
question and provided with options. If he/she picks the correct 
answer a smiley face will appear. It educates the children about 
food and nutrition.

%prep
%autosetup -n Nutrition-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Nutrition.activity/

%find_lang org.sugarlabs.NutritionActivity

%files -f org.sugarlabs.NutritionActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Nutrition.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 16-1
- Release version 16
- Change to py_byte_compile as stated in phase 3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 15-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 15-1
- New version 15
- Remove the generated .desktop file (#1424505)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-1
- new version 13

* Mon Mar 25 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-1
- new version 11

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 9-1
- new version 9

* Fri Oct 19 2012 Kalpa Welivitiogda <callkalpa@gmail.com> - 7-1
- new version 7 and gtk3 update

* Fri Aug 24 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 6-1
- new version 6 release

* Tue Jul 03 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 4-2
- fixed license issue and removed defattr macro in files section

* Sun May 20 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 4-1
- initial packaging
