Name:           sugar-calculator
Version:        47
Release:        10%{?dist}
Summary:        Calculator for Sugar

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.laptop.org/go/Calculate
Source0:        http://download.sugarlabs.org/sources/sucrose/fructose/Calculate/Calculate-%{version}.tar.bz2

BuildRequires:  python3 gettext python3-devel sugar-toolkit-gtk3
Requires:       sugar >= 0.116
BuildArch:      noarch

%description
The calculate activity provides a calculator for the Sugar interface.

%prep
%autosetup -n Calculate-%{version}
sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Calculator.activity/

%find_lang org.laptop.Calculate

%files -f org.laptop.Calculate.lang
%doc NEWS
%{sugaractivitydir}/Calculate.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 47-9
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Kalpa Welivitigoda <callkalpa@gmail.com> - 47-1
- v47

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 46-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jan 27 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 46-1
- v46
- Update Python 3 dependency declarations

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 44-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 44-1
- Release 44

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 43-1
- Release 43

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 42-5
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 Peter Robinson <pbrobinson@fedoraproject.org> 42-1
- Release 42

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> 41-1
- Release 41

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 40-1
- Release 40

* Wed Mar 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 39-1
- Release 39

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 38-1
- Release 38

* Wed Jun  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 37-1
- New 37 release

* Mon Apr  4 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 36-1
- New 36 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 35-1
- bump build

* Fri Oct  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 34-1
- New 34 release

* Fri Jul 30 2010 Sebastian Dziallas <sebastian@when.com> - 32-1
- New upstream release

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 30-3
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539143

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> - 30-1
- Add support for matplotlib as plotting backend
- Add support for complex plot ranges, e.g. -2*pi..2*pi
- Fix superscript display bug

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Simon Schampijer <simon@schampijer.de> - 28-1
- Support 'real' scientific notation (#4250)
- Add switching between exponential/scientific notation
- Allow changing of number of displayed digits
- Change cursor on equations to Hand (#6612)
- Fix fall-through of unhandled CTRL keys (eg CTRL+Q)
- Add recursion detection
- Fixed error-handling bug
- New download url

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 23-2
- Rebuild for Python 2.6

* Tue Sep  2 2008 Jeremy Katz <katzj@redhat.com> - 23-1
- update to Calculate-23
- use %%find_lang 

* Thu Jul 31 2008 Jeremy Katz <katzj@redhat.com> - 19-1
- Initial packaging
