# SPDX-License-Identifier: MIT
Version:        20141121
Release:        22%{?dist}
URL:            http://www.paratype.com/public/

%global foundry         paratype
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    PTSSM_OFL.txt

%global fontfamily      PT Mono
%global fontsummary     A pan-Cyrillic monospace typeface
%global fonts           *.ttf
%global fontconfs       %{SOURCE10}
%global fontconf 57-%{fontname}

%global fontdescription %{expand:\
Font PT Mono™ is the last addition to the pan-Cyrillic font superfamily \
including PT Sans and PT Serif developed for the project “Public Types \
of Russian Federation”. \
\
PT Mono was developed for the special needs — for use in forms, tables, \
work sheets etc. Equal widths of characters are very helpful in setting \
complex documents, with such font you may easily calculate size of entry \
fields, column widths in tables and so on. One of the most important area \
of use is Web sites of “electronic governments” where visitors have to fill \
different request forms. PT Mono consists of Regular and Bold styles. \
\
PT Mono was designed by Alexandra Korolkova with participation of \
Isabella Chaeva and with financial support of Google.
}


Source0:        http://www.fontstock.com/public/PTMonoOFL.zip
Source10:       %{fontpkgname}.conf
Source11:       %{fontpkgname}.metainfo.xml


%fontpkg

%prep
%setup -q -c
sed -i "s|\r||g" *.txt

%build
%fontbuild

%install
%fontinstall
# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontpkgname}.metainfo.xml

%check
%fontcheck

%fontfiles
%{_datadir}/appdata/%{fontpkgname}.metainfo.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 19 2023 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 20141121-17
- Adapted spec file to new template

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 21 2014 Rajeesh K V <rajeesh AT inflo DOT ws> - 20141121-1
- Changed version to today in YYYYMMDD format
- Fixed wrong end of line encoding in license text

* Mon Nov 17 2014 Rajeesh K V <rajeesh AT inflo DOT ws> - 20113012-1
- Initial packaging
