Name:    sugar-chat
Version: 86
Release: 15%{?dist}
Summary: Chat client for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.laptop.org/go/Chat
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Chat/Chat-%{version}.tar.bz2
 
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: telepathy-glib
BuildRequires: telepathy-glib-devel
BuildRequires: gettext

Requires: sugar 
Requires: telepathy-mission-control

BuildArch: noarch

%description
The chat activity provides a chat client for the Sugar interface.

%prep
%autosetup -n Chat-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Chat.activity/

%find_lang org.laptop.Chat


%files -f org.laptop.Chat.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Chat.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 86-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 86-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 86-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 86-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 86-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 86-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 86-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 86-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 86-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 86-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 86-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 2 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 86-3
- Add telepathy-glib and telepathy-glib-devel dependencies

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> 86-1
- Release 86

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Kalpa Welivitigoda <callkalpa@gmail.com> - 85-1
- Release 85

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 84-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 84-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 84-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 84-1
- Release 84

* Sat Apr 22 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 83-1
- Release 83

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 81-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jul 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 81-1
- Release 81

* Mon Jul  7 2014 Peter Robinson <pbrobinson@fedoraproject.org> 80-1
- Release 80

* Sat Jun 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 79-1
- Release 79

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> 78-1
- Release 78

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 77-1
- Release 77

* Sun Apr 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 76-1
- Release 76

* Sun Apr 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 75-1
- Release 75

* Sat Mar 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 74-1
- Release 74

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 73-1
- Release 73

* Mon Sep  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 71-1
- New 71 release

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 70-1
- New 70 release

 * Wed Sep 29 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 68-1
 - New 68 release

 * Sat Sep 11 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 67-1
 - New 67 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 66-2
- recompiling .py files against Python 2.7 (rhbz#623365)

* Sat Sep 12 2009 Simon Schampijer <simon@schampijer.de> - 66-1
- New toolbar design

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 65-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Simon Schampijer <simon@schampijer.de> - 65-1
- Support new activity.info exec parameter
- 'share or invite' hint not when resuming shared instance #402

* Tue Mar 03 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 64-1
- New upstream release
 
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Simon Schampijer <simon@schampijer.de> - 62-1
- Use cjson instead of simple-json (nirbheek)
- Updated translations: he, en_US, sv
- New download url

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 47-2
- Rebuild for Python 2.6

* Wed Sep 17 2008 Jeremy Katz <katzj@redhat.com> - 47-1
- update to Chat-47

* Tue Sep  2 2008 Jeremy Katz <katzj@redhat.com> - 46-1
- update to Chat-46
- Use %%find_lang
- Remove bogus pseudo locale

* Thu Jul 31 2008 Jeremy Katz <katzj@redhat.com> - 44-1
- Initial packaging
