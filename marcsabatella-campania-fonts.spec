Version:        2.009
Release:        7%{?dist}
URL:            https://github.com/MarcSabatella/Campania

%global foundry           MarcSabatella
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      LICENSE
%global fontdocs          README.md
%global fontfamily        Campania
%global fontsummary       Font for Roman numeral analysis (music theory)
%global fonts             *.otf
%global fontorg           com.github
%global fontconfs         %{SOURCE1}

%global fontdescription   %{expand:
This font is inspired by the work of Florian Kretlow and the impressive
Figurato font he developed for figured bass, as well as the work of
Ronald Caltabiano and his pioneering Sicilian Numerals font.  This
version of Campania is not directly based on either of these, however.
Instead, it uses the glyphs from Doulos and adds some relatively
straightforward contextual substitutions and positioning rules to allow
you to enter the most common symbols just by typing naturally.}

Source0:        https://github.com/MarcSabatella/Campania/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        65-%{fontpkgname}.conf

BuildRequires:  appstream
BuildRequires:  fontforge

%fontpkg

%prep
%autosetup -n Campania-%{version}

%build
%fontbuild
fontforge -lang=ff -c 'Open($1); Generate($2)' Campania.sfd Campania.otf

%install
%fontinstall
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{name}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -e 's,updatecontact,update_contact,g' \
    -e 's,<!\[CDATA\[\(.*\)\]\]>,\1,' \
    -i $metainfo

appstreamcli validate --no-net $metainfo

%check
# FIXME: This should not be necessary
ln -s %{_datadir}/xml/fontconfig/fonts.dtd %{buildroot}%{_fontconfig_templatedir}
%fontcheck
rm %{buildroot}%{_fontconfig_templatedir}/fonts.dtd

%fontfiles

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 2.009-6
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Jerry James <loganjerry@gmail.com> - 2.009-4
- Add font organization
- Small fixes to the metainfo
- Validate the metainfo with appstream

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct  5 2020 Jerry James <loganjerry@gmail.com> - 2.009-1
- Initial RPM
