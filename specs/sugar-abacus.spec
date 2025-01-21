Name:           sugar-abacus
Version:        61
Release:        14%{?dist}
Summary:        A simple abacus activity for Sugar

License:        LGPL-3.0-or-later
URL:            http://activities.sugarlabs.org/addon/4293
Source0:        http://download.sugarlabs.org/sources/honey/Abacus/Abacus-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
Requires:       sugar >= 0.116

%description
Abacus lets the learner explore different representations of numbers using 
different mechanical counting systems developed by the ancient Romans and 
Chinese. There are several different variants available for exploration: a 
suanpan, the traditional Chinese abacus with 2 beads on top and 5 beads below; 
a soroban, the traditional Japanese abacus with 1 bead on top and 4 beads below;
the schety, the traditional Russian abacus, with 10 beads per column, with the 
exception of one column with just 4 beads used for counting in fourths; and the 
nepohualtzintzin, the traditional Mayan abacus, with 3 beads on top and 4 beads 
below (it uses base 20).

%prep
%autosetup -n Abacus-%{version}

sed -i 's/python/python3/' abacus.py

%build
python3 ./setup.py build

# %find_lang org.sugarlabs.AbacusActivity

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}}/%{sugaractivitydir}/Abacus.activity/

%find_lang org.sugarlabs.AbacusActivity

%files -f org.sugarlabs.AbacusActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Abacus.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 61-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 61-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 61-12
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 61-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 61-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 61-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 61-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 61-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 61-6
- Specify sugar version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 61-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 61-2
- be specific for python3 files

* Mon Jan 27 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 61-1
- v61
- Update Python 3 dependency declarations

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 60-1
- Release 60

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 59-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 59-1
- Release 59

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Kalpa Welivitigoda <callkalpa@gmail.com> - 58-1
- Release 58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Peter Robinson <pbrobinson@fedoraproject.org> 57-1
- Release 57

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 56-1
- Release 56

* Sat Dec 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 54-1
- Release 54

* Tue Nov 12 2013 Peter Robinson <pbrobinson@fedoraproject.org> 53-1
- Release 53

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 49-1
- Release 49

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 43-1
- Release 43

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 41-1
- Release 41

* Tue Oct  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 39-1
- Release 39

* Fri Sep 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 37-1
- Release 37

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May  5 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 35-1
- Release 35

* Thu May  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 34-1
- Release 34

* Tue Mar 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 32-1
- Release 32

* Tue Jan  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 31-1
- Release 31, gtk3 support

* Mon Oct 31 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 28-1
- Release 28

* Tue Oct 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 26-1
- Release 26

* Sat Oct  1 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 24-1
- Update to 24

* Mon Sep 26 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 23-1
- Update to 23

* Wed Aug 10 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 22-1
- Update to 22

* Sat Jun 25 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 20-1
- Update to 20

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 19-1
- Update to 19

* Mon Sep 27 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 17-1
- Update to 17

* Fri Jun 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 14-1
- Update to 14

* Sat Jun 19 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 13-2
- Some spec file cleanups

* Thu Jun 10 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 13-1
- Update to version 13

* Thu Jun 10 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 12-1
- Initial package of abacus
