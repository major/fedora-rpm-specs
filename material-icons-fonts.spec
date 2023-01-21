Version:        4.0.0
Release:        8%{?dist}
URL:            https://google.github.io/material-design-icons/

%global fontlicense     Apache-2.0
%global fontlicenses    LICENSE
%global fontdocs        README.md
%global fontfamily      Material Icons
%global fontsummary     Google material design system icons
%global fonts           font/*.otf font/*.ttf
%global fontorg         com.google
%global fontconfs       %{SOURCE1}

%global fontdescription %{expand:
Material design icons is the official icon set from Google.  The icons
are designed under the material design guidelines.}

Source0:        https://github.com/google/material-design-icons/archive/%{version}/material-design-icons-%{version}.tar.gz
Source1:        65-%{fontpkgname}.conf

BuildRequires:  appstream

%fontpkg

%prep
%autosetup -n material-design-icons-%{version}

%build
%fontbuild

%install
%fontinstall
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{name}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\(.*\)\]\]>,\1,' \
    -e 's,<font></font>,<font>Material Icons Outlined Regular</font>\n    <font>Material Icons Round Regular</font>\n    <font>Material Icons Sharp Regular</font>\n    <font>Material Icons Two Tone Regular</font>,' \
    -i $metainfo

appstreamcli validate --no-net $metainfo

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%fontfiles

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 4.0.0-7
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Jerry James <loganjerry@gmail.com> - 4.0.0-5
- Add a font organization
- Validate metadata with appstream

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 29 2021 Jerry James <loganjerry@gmail.com> - 4.0.0-3
- Fix problems in the generated metainfo (bz 1943727)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Jerry James <loganjerry@gmail.com> - 4.0.0-1
- Initial RPM
