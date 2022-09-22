Name:           sugar-flip
Version:        10
Release:        5%{?dist}
Summary:        Simple strategic game of flipping coins

License:        GPLv3+ and MIT
URL:            http://wiki.sugarlabs.org/go/Activities/Flip
Source0:        http://download.sugarlabs.org/sources/honey/Flip/Flip-%{version}.tar.bz2

BuildRequires:  python3-devel python3
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
Requires:       sugar >= 0.116

BuildArch:      noarch

%description
Flip is a simple strategic game where you have to flip coins until 
they are all heads up. Each time you win, the challenge gets more 
difficult. You can play flips with your friends over the net. 

%prep
%setup -q -n Flip-%{version}
sed -i "s|python|python3|g" setup.py

%build
%{__python3} ./setup.py build

%install
%{__python3} ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

%find_lang org.sugarlabs.FlipActivity

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{__python3} %{buildroot}/%{sugaractivitydir}/Flip.activity/

%files -f org.sugarlabs.FlipActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Flip.activity/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 10-1
- Release version 10
- Change to py_byte_compile as stated in phase 3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 9-13
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 9-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 9-7
- Remove the generated .desktop file (#1424489)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 9-1
- Release version 9

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 5-4
- Cleanup spec

* Wed Oct 31 2012 Tom Callaway <spot@fedoraproject.org> - 5-3
- require sugar >= 0.97.6 (not 0.98, which is not in Fedora yet)

* Fri Oct 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 5-2
- gtk3 update

* Fri Oct 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 5-1
- Release version 5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 4-1
- Release version 4

* Sat Mar 31 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 3-2
- added localisation

* Sat Mar 31 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 3-1
- Release version 3

* Fri Mar 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 1-3
- removed setup.py

* Fri Mar 30 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 1-2
- updated license info
- removed gettext
- added python2-devel
- updated license

* Sun Dec 18 2011 Kalpa Welivitigoda <callkalpa@gmail.com> - 1-1
- initial packaging
