Name:           sugar-distance
Version:        36
Release:        14%{?dist}
Summary:        Distance measurement for Sugar

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.laptop.org/go/Distance
Source0:        http://download.sugarlabs.org/sources/honey/Distance/Distance-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar >= 0.116

%description
Distance (aka Acoustic Tape Measure) determines the physical distance 
between two XOs by measuring how long it takes sound pulses to travel 
between them. 

%prep
%autosetup -n Distance-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build


%install
mkdir -p %{buildroot}%{sugaractivitydir}
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
find %{buildroot}%{sugaractivitydir}Distance.activity/arange.py -type f -name \* -exec chmod 644 {} \;

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Distance.activity/

%find_lang org.laptop.AcousticMeasure

%files -f org.laptop.AcousticMeasure.lang
%doc NEWS
%{sugaractivitydir}/Distance.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 36-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 36-2
- fix sugar version

* Tue Feb 11 2020 Peter Robinson <pbrobinson@fedoraproject.org> 36-1
- Update to 36

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 35-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 35-5
- Fix FTBFS issue

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 35-3
- Minor fixups

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 09 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 35-1
- Update to 35 (also fixes FTBFS rh#1240037)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 34-1
- Update to 34

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 31-1
- Update to 31

* Thu Apr 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 30-1
- Update to 30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 19 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 25-1
- Update to 25

* Fri Aug 12 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 24-1
- Update to 24

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 21-1
- Update to 21

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 13-5
- recompiling .py files against Python 2.7 (rhbz#623368)

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 13-4
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539162

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 19 2008 Fabian Affolter <fabian@bernewireless.net> - 13-1
- Initial package for Fedora
