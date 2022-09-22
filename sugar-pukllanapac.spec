Name:           sugar-pukllanapac
Version:        14
Release:        7%{?dist}
Summary:        A sliding puzzle game

License:        GPLv3+
URL:            https://github.com/sugarlabs/pukllanapac
Source0:        http://download.sugarlabs.org/sources/honey/Pukllanapac/Pukllanapac-%{version}.tar.bz2

BuildRequires:  python3 python3-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
Pukllanapac is a sliding puzzle game; the objective is to rearrange 
tiles so that all of the circles (and semicircles) are composed 
of sectors of the same color. There are three different patterns: 
circles, triangles and hexagons. Drag tiles to swap their position; 
click on tiles to rotate them.

%prep
%autosetup -n Pukllanapac-%{version}

sed -i 's/python/python3/' gentiles.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{sugaractivitydir}/Pukllanapac.activity/

%find_lang org.sugarlabs.PukllanapacActivity

%files -f org.sugarlabs.PukllanapacActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Pukllanapac.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 14-3
- Set Requires to 0.116

* Mon Aug 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 14-2
- Fix python3 detection

* Tue Jul 28 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 14-1
- Release version 14
- Update Python3 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
- Change to py_byte_compile as stated in phase 3
  (See https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 13-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 13-3
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 13-1
- Release version 13

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-3
- Release version 11 for gtk3

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 27 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 11-1
- Release version 11
- gtk 3 port

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Kalpa Welivitigofa <callkalpa@gmail.com> - 9-1
- Release version 9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild


* Tue Dec 20 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 8-2
- removed %%{__python} macro

* Thu Dec 15 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 8-1
- initial packaging
