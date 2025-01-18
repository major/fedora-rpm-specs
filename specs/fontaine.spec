%global revision 70

Name:             fontaine
Version:          0
Release:          37.svn%{revision}%{?dist}
Summary:          Font file meta information utility
License:          GPL-2.0-or-later
URL:              http://unifont.org/fontaine/

Source0:          https://sourceforge.net/code-snapshots/svn/f/fo/fontaine/code/fontaine-code-r%{revision}-trunk.zip

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:    cmake gettext
BuildRequires:    freetype-devel

%description
Fontaine is a command-line utility that displays key meta information about
font files, including but not limited to font name, style, weight,
glyph count, character count, copyright, license information  and 
orthographic coverage.

%prep
%setup -q -n fontaine-code-r%{revision}-trunk
find -type d -name .svn | xargs -r rm -rf

%build
%cmake -DCMAKE_POLICY_DEFAULT_CMP0057=NEW
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc documentation/html
%license documentation/GPL-2.0-LICENSE
%{_bindir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-37.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-36.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-35.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-34.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-33.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul  7 2023 Yanko Kaneti <yaneti@declera.com> - 0-32.svn70
- SPDX migration. Drop doxygen BR for no usefull docs are generated with it

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-31.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-30.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-29.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-28.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.svn70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Yanko Kaneti <yaneti@declera.com> - 0-26.svn70
- Latest revision. Rework source and cmake bits

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-21.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Yanko Kaneti <yaneti@declera.com> - 0-19.svn68
- Explicit CMP0057 cmake policy for latest FindDoxygen.cmake

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.svn68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul  1 2015 Yanko Kaneti <yaneti@declera.com> - 0-15.svn68
- Latest revision. Drop freetype patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-14.svn57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-13.svn57
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-12.svn57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun  8 2014 Yanko Kaneti <yaneti@declera.com> - 0-11.svn57
- Patch to adapt to latest freetype include changes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-10.svn57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-9.svn57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-8.svn57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.svn57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Yanko Kaneti <yaneti@declera.com> - 0-6.svn57
- a few revisions later
- Use an upstream released tarball
- Drop some packaging legacy

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.svn39
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-4.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.svn39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 17 2010 Yanko Kaneti <yaneti@declera.com> - 0-2.svn39
- a few revisions later

* Sat Jan 30 2010 Yanko Kaneti <yaneti@declera.com> - 0-1.svn35
- Initial packaging
