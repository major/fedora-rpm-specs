# This package depends on automagic byte compilation

%global debug_package %{nil}

Name:          sugar-pippy
Version:       75
Release:       14%{?dist}
Summary:       Pippy for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://wiki.laptop.org/go/Pippy
Source0:       http://download.sugarlabs.org/sources/sucrose/fructose/Pippy/Pippy-%{version}.tar.bz2

BuildRequires: python3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gettext 
BuildRequires: sugar-toolkit-gtk3

Requires:      gobject-introspection
Requires:      python3-pybox2d
Requires:      python3-pygame
Requires:      sugar >= 0.116


%description
Teaches Python programming by providing access to Python code samples
and a fully interactive Python interpreter.

The user can type and execute simple Python expressions. For example,
it would be possible for a user to write Python statements to calculate
expressions, play sounds, or make simple text animation. 

%prep
%setup -q -n Pippy-%{version}

sed -i 's#!/usr/bin/env python#!/usr/bin/env python3#' setup.py
sed -i 's#!/usr/bin/python#!/usr/bin/python3#' activity.py

# Remove shebang
for Files in pippy_app.py ; do
  sed -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  rm ${Files}.orig
done

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%find_lang org.laptop.Pippy

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Pippy.activity/

%files -f org.laptop.Pippy.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Pippy.activity/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 75-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 75-13
- No need to remove pre-compiled pybox2d as it's no longer pre-compiled

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 75-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 75-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 75-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 75-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 75-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 75-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 75-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 75-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 75-2
- Close braces

* Sat Jul 11 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 75-2
- Change to py_byte_compile as stated in phase 3
- Leave library/pippy/physics as removing it throws errors, activity still uses it

* Tue Mar 10 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 75-1
- Release 75

* Wed Mar 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 74-3
- Fix python3 scripts

* Mon Mar 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 74-2
- Fix sugar version

* Mon Mar 02 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 74-1
- Release 74

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 72-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 72-4
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 72-2
- Don't ship bundled box2d

* Sun Sep 09 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 72-1
- Release 72

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Kalpa Welivitigoda <callkalpa@gmail.com> - 71-3
- Fix FTBFS (#1556473)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org>  71-1
- Release 71

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 66-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  8 2015 Peter Robinson <pbrobinson@fedoraproject.org> 66-1
- Release 66

* Wed Dec 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 64-1
- Release 64

* Mon Dec  8 2014 Peter Robinson <pbrobinson@fedoraproject.org> 63-1
- Release 63

* Mon Nov 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 62-1
- Release 62

* Thu Jul  3 2014 Peter Robinson <pbrobinson@fedoraproject.org> 61-1
- Release 61

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 58-1
- Release 58

* Sat Feb 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 57-1
- Release 57

* Thu Feb  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 56-1
- Release 56

* Thu Jan 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 55-1
- Release 55
