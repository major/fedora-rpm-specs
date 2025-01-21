Name:      sugar-read
Version:   123
Release:   15%{?dist}
Summary:   A document reader for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       http://wiki.laptop.org/go/Read
Source0:   http://download.sugarlabs.org/sources/sucrose/fructose/Read/Read-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: evince-devel
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3-devel

Requires: evince-libs
Requires: evince-djvu
Requires: python3-beautifulsoup4
Requires: sugar-toolkit-gtk3

%description
The Read activity allows the laptop to act as a book reader. It has a
simple interface, and will view many kinds of text and image-based book-
like materials. It will have particular strengths in handheld mode, with
extremely low power consumption and simple navigation controls.

Read can read PDF files, single-page TIFF files, and also read DJVU files.

%prep
%autosetup -n Read-%{version}
sed -i 's#usr/bin/env python#usr/bin/env python3#' setup.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm -rf $RPM_BUILD_ROOT%{sugaractivitydir}/Read.activity/screenshots/
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Read.activity/

%find_lang org.laptop.sugar.ReadActivity

%files -f org.laptop.sugar.ReadActivity.lang
%license COPYING
%doc AUTHORS
%{sugaractivitydir}/Read.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 123-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 123-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 123-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 123-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 123-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 123-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 123-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 123-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 123-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 123-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 123-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 123-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> 123-2
- Require python3-beautifulsoup4 instead of python3-beautifulsoup

* Mon Jan 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> 123-1
- Release 123

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 122-1
- Release 122

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 121-1
- Release 121

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 120-1
- Release 120

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 119-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 119-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-1
- Upgrade to sugar 0.112 stable release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 118-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 118-1
- Release 118

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 117-4
- Fix FTBFS issue 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 117-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 117-1
- Release 117

* Wed Jun 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 115-1
- Release 115

* Thu Nov 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 114-1
- Release 114

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Peter Robinson <pbrobinson@fedoraproject.org> 113-1
- Release 113

* Mon Jan 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 112-1
- Release 112

* Fri Sep  6 2013 Peter Robinson <pbrobinson@fedoraproject.org> 111-1
- Release 111

* Wed Aug  7 2013 Peter Robinson <pbrobinson@fedoraproject.org> 110-1
- Release 110

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Peter Robinson <pbrobinson@fedoraproject.org> 109-1
- Release 109

* Wed Apr 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 108-1
- Release 108

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> 106-1
- Release 106

* Fri Nov 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> 105-1
- Release 105

* Wed Oct 17 2012 Peter Robinson <pbrobinson@fedoraproject.org> 104-1
- Release 104

* Tue Oct  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> 103-1
- Release 103

* Thu Oct  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 102-2
- Update dependencies for gtk3

* Fri Sep 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 102-1
- Release 102

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 99-1
- Release 99

* Tue Apr 10 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 98-1
- Release 98

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 97-2
- Rebuild for libevdocument3 soname bump

* Thu Mar  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 97-1
- Release 97

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 94-1
- Release 94

* Tue Oct 18 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 92-1
- Release 92

* Tue Apr  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 88-1
- New 88 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 29-3
- Bump build

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 79-2
- recompiling .py files against Python 2.7 (rhbz#623384)

* Wed Jul 21 2010 Sebastian Dziallas <sebastian@when.com> - 79-1
- New upstream release fixing issues on F13

* Wed Dec 23 2009 Sebastian Dziallas <sebastian@when.com> - 78-1
- New upstream release

* Sun Oct 11 2009 Sebastian Dziallas <sebastian@when.com> - 76-1
- Fix pagination for IA Epubs
- Updated Vietnamese translations

* Sun Sep 27 2009 Sebastian Dziallas <sebastian@when.com> - 75-1
- Fix search in Epub files (dslo #1319)
- Updated translations for German, Mongolian and Portuguese

* Sat Sep 12 2009 Simon Schampijer <simon@schampijer.de> - 73-1
- New toolbars
- Support for Epub files
- Support for notes associated with bookmarks
- Show a information bar in fullscreen mode, with pagecount and battery information

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 06 2009 Simon Schampijer <simon@schampijer.de> - 66-1
- Support evince binding w/o document_links support #703
- Update translations

* Fri Mar 06 2009 Simon Schampijer <simon@schampijer.de> - 65-2
- make dependency only on gnome-python2-evince to not drag in 
  all gnome-python

* Wed Mar 04 2009 Simon Schampijer <simon@schampijer.de> - 65-1
- Initial packaging
