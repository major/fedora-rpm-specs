Name:           fntsample
Version:        5.3
Release:        19%{?dist}
Summary:        A program for making font samples that show Unicode coverage of the font

License:        GPL-3.0-or-later
URL:            https://github.com/eugmes/fntsample/releases
Source0:        https://github.com/eugmes/fntsample/archive/release/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  gettext-devel perl-generators unicode-ucd
BuildRequires:  cairo-devel freetype-devel glib2-devel
BuildRequires:  fontconfig-devel pango-devel
BuildRequires:  gcc cmake
Requires:       perl(Locale::TextDomain)

%description
A program for making font samples that show Unicode coverage of
the font and are similar in appearance to Unicode charts.
Samples can be saved as PDF or PostScript files.

%prep
%autosetup -n %{name}-release-%{version}

%build
%cmake -DUNICODE_BLOCKS=%{_datadir}/unicode/ucd/Blocks.txt
%cmake_build

%install
%cmake_install

%check
ctest -V %{?_smp_flags}

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README.rst
%license COPYING
%{_bindir}/fntsample
%{_bindir}/pdfoutline
%{_mandir}/man1/*.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Parag Nemade <pnemade AT redhat DOT com> - 5.3-13
- Update license tag to SPDX format

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 12:32:07 GMT 2020 Parag Nemade <pnemade@fedoraproject.org> - 5.3-8
- Fix as per https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds#Migration

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Parag Nemade <pnemade AT redhat DOT com> - 5.3-4
- Resolves:rh#1761556 - Add missing dependency perl(Locale::TextDomain)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Parag Nemade <pnemade AT redhat DOT com> - 5.3-2
- Remove previously added patch as pango is fixed

* Sun Feb 03 2019 Parag Nemade <pnemade AT redhat DOT com> - 5.3-1
- Update to 5.3 version
- Added missing glib2-devel while linking in CMakeFiles.txt

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Parag Nemade <pnemade AT redhat DOT com> - 5.2-1
- Update to 5.2 release (rh#1550623)

* Mon Feb 19 2018 Parag Nemade <pnemade AT redhat DOT com> - 3.2-10
- Add BuildRequires: gcc as per packaging guidelines
- Added %%license
- Use %%autosetup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Parag Nemade <pnemade AT redhat DOT com> - 3.2-1
- Initial Fedora release.

