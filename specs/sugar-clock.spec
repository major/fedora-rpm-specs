Name:           sugar-clock
Version:        22.1
Release:        13%{?dist}
Summary:        Clock activity for Sugar

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://wiki.laptop.org/go/Clock
Source0:        https://download.sugarlabs.org/sources/honey/Clock/Clock-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3

Requires:       sugar
Requires:       sugar-toolkit-gtk3


%description
This activity displays time in analog, digital, and "natural" forms.
The "natural" form will be an image of a sun or moon arcing across
the sky, rising and setting as the day progresses. This is more than
a simple clock; the user will be able to grab any element and readjust
it, which will update each of the other elements. In this manner,
hopefully the children can explore and understand different methods of
telling time. 


%prep
%autosetup -n Clock-%{version}

sed -i 's/python/python3/' speaker.py clock.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Clock.activity/

%find_lang tv.alterna.Clock


%files -f tv.alterna.Clock.lang
%doc README.md
%{sugaractivitydir}/Clock.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 22.1-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 22.1-1 
- Release 22.1

* Thu Feb 5 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 22-2
- Fix python3 bits

* Wed Feb 5 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> - 22-1
- v22

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Kalpa Welivitigoda <callkalpa@gmail.com> - 21-1
- Release 21

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20-1
- Release 20

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 19-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 19-1
- Release 19

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 18-4
- Fix FTBFS issue 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 18-1
- Release 18

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 15-5
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 15-3
- Add gstreamer-python runtime dependency

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Peter Robinson <pbrobinson@fedoraproject.org> 15-1
- Release 15

* Wed May 22 2013 Peter Robinson <pbrobinson@fedoraproject.org> 14-1
- Release 14

* Tue May 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 13-1
- Release 13

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 16 2012 Peter Robinson <pbrobinson@fedoraproject.org> 12-1
- Release 12

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 11-1
- Release 11

* Fri Oct  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 10-1
- Release 10

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 8-1
- Release 8

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 7-1
- Release 7

* Sat Jun  4 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 6-1
- Update to v6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 5-4
- recompiling .py files against Python 2.7 (rhbz#623366)

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 5-3
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 538921

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Fabian Affolter <fabian@bernewireless.net> - 5-1
- Updated to new upstream version 5
- Removed all vcs checkout stuff 

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20090207
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 07 2009 Fabian Affolter <fabian@bernewireless.net> - 0-0.2.20090207
- Fixed version and release

* Mon Jan 26 2009 Fabian Affolter <fabian@bernewireless.net> - 20090126-1
- Initial package for Fedora
