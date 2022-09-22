Name:           sugar-recall
Version:        7
Release:        6%{?dist}
Summary:        A series of memory games

License:        GPLv3+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/Recall
Source0:        http://download.sugarlabs.org/sources/honey/Recall/Recall-%{version}.tar.bz2

BuildRequires:  python3 python3-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.116

%description
Recall is a series of memory games for sugar. The game becomes
difficult as the user keeps on playing. This helps to increase
the memorizing ability of children.

%prep
%autosetup -n Recall-%{version}

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Recall.activity/

%find_lang org.sugarlabs.RecallActivity

%files -f org.sugarlabs.RecallActivity.lang
%license COPYING
%doc NEWS CREDITS
%{sugaractivitydir}/Recall.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct  2 2020 José Matos <jamatos@fedoraproject.org> - 7-2
- Shebang lines already refer to python3 (remove unneeded sed call)

* Tue Aug 11 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 7-1
- Release version 7
- Change to py_byte_compile as stated in phase 3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 6-1
- Version 6 release with gtk3 port

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 4-2
- translations added

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 4-1
- version 4 release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 10 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 2-2
- fixed license, removed defattr in files section and fixed a typo in description

* Sun May 20 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 2-1
- initial packaging
