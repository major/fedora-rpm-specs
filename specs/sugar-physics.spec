Name:           sugar-physics
Version:        35
Release:        14%{?dist}
Summary:        A physical world simulator and playground for Sugar

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://wiki.sugarlabs.org/go/Activities/Physics
Source0:        https://download.sugarlabs.org/sources/honey/Physics/Physics-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar
Requires:       python3-pybox2d
BuildArch:      noarch

%description
You can add squares, circles, triangles, or draw your own shapes in
the Physics Activity, and see them come to life with forces (like gravity),
friction, and inertia.

%prep
%autosetup -p1 -n Physics-%{version}

sed -i 's/python/python3/' setup.py
sed -i 's/python/python3/' physics.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# set appropriate permissions
chmod a+x $RPM_BUILD_ROOT%{sugaractivitydir}Physics.activity/physics.py
chmod a-x $RPM_BUILD_ROOT%{sugaractivitydir}Physics.activity/activity/{activity.info,activity-physics.svg}

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Physics.activity/

%find_lang org.laptop.physics

%files -f org.laptop.physics.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Physics.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 35-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 35-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 35-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 7 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 35-2
- Remove python3-elements dependency as package isn't provided in f32

* Fri Mar 6 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 35-1
- Release 35

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 34-1
- Release 34

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-1
- Release 33

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 32.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 32.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Oct 17 2017 Charalampos Stratakis <cstratak@redhat.com> - 32.1-3
- Use system version of Box2D and not the bundled one.
Resolves: rhbz#1446934

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 32.1-1
- Release 32.1

* Thu Jun 08 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 32-1
- Release 32

* Sat Apr 22 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 30-1
- Release 30

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Peter Robinson <pbrobinson@fedoraproject.org> 26-1
- Release 26

* Wed Dec 10 2014 Peter Robinson <pbrobinson@fedoraproject.org> 24-1
- Release 24

* Mon Nov 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 23-1
- Release 23

* Mon Sep  1 2014 Peter Robinson <pbrobinson@fedoraproject.org> 22-1
- Release 21

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 21-1
- Release 21

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 19-1
- Release 19

* Tue Feb  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 17-1
- Release 17

* Mon Jan 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 13-1
- Release 13

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> 11-1
- Release 11

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 10-1
- Release 10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 9-1
- Release 9

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 8-1
- New 8 release

* Thu Oct 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 7-1
- New 7 release

* Fri Jul 30 2010 Sebastian Dziallas <sebastian@when.com> - 5-1
- new upstream release

* Tue Feb 23 2010 Sebastian Dziallas <sebastian@when.com> - 4-2
- now with previously missing locales

* Tue Feb 23 2010 Sebastian Dziallas <sebastian@when.com> - 4-1
- new upstream release

* Mon Feb 01 2010 Sebastian Dziallas <sebastian@when.com> - 3-3
- bump for building with correct source

* Sun Jan 31 2010 Sebastian Dziallas <sebastian@when.com> - 3-2
- add olpcgames dependency

* Sun Jan 03 2009 Sebastian Dziallas <sebastian@when.com> - 3-1
- initial packaging
