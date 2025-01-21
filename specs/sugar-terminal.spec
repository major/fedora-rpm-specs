Name:    sugar-terminal
Version: 47
Release: 14%{?dist}
Summary: Terminal for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.laptop.org/go/Terminal
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Terminal/Terminal-%{version}.tar.bz2

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext

Requires: sugar
Requires: vte291

BuildArch: noarch

%description
The terminal activity provides a vte-based terminal for the Sugar interface.

%prep
%autosetup -n Terminal-%{version}
sed -i 's#/usr/bin/python#/usr/bin/python3#' setup.py

# remove bogus pseudo.po
rm -vf po/pseudo.po

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Terminal.activity/

%find_lang org.laptop.Terminal

%files -f org.laptop.Terminal.lang
%license COPYING.GPLv3 COPYING
%{sugaractivitydir}/Terminal.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 47-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 47-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 47-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 47-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 47-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 47-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> 47-1
- release 47

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 46-1
- release 46

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 45.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 45.4-1
- release 45.4

* Sat Oct  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 45.3-1
- release 45.3

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 45.1-6
- Require newer vte291 instead of vte3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 45.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 45.1-1
- release 45.1

* Fri May 26 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 45-1
- release 45

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 44-5
- Fix FTBFS issue 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Peter Robinson <pbrobinson@fedoraproject.org> 44-1
- release 44

* Fri Dec 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 43-1
- release 43

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 42-1
- release 42

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 41-1
- release 41

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 39-1
- 39 release

* Sat May 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 37-1
- 37 release

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 36-1
- 36 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 35-1
- 35 release

* Mon Sep  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 34-1
- New upstream 34 release

* Tue Jun  7 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 33-1
- New upstream 33 release

* Sat May 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 32-1
- New upstream 32 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 31-4
- Bump build

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 31-3
- recompiling .py files against Python 2.7 (rhbz#623388)

* Fri Jan 22 2010 Sebastian Dziallas <sebastian@when.com> - 31-2
- Make sure to switch to correct location during setup

* Fri Jan 22 2010 Sebastian Dziallas <sebastian@when.com> - 31-1
- New upstream release

* Fri Sep 09 2009 Simon Schampijer <simon@schampijer.de> - 26-1
- New toolbar design

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 28 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 25-1
- New upstream release

* Tue Mar 03 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 23-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org>
- New release

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 16-3
- Rebuild for Python 2.6

* Wed Sep  3 2008 Jeremy Katz <katzj@redhat.com> - 16-2
- temporarily BR gettext

* Tue Sep  2 2008 Jeremy Katz <katzj@redhat.com> - 16-1
- update to Terminal-16
- use %%find_lang which works with new bundlebuilder changes
- remove bogus pseudo.po translation

* Tue Jul 22 2008 Jeremy Katz <katzj@redhat.com> - 13-1
- Initial packaging
