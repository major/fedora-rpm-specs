Version:        2.009
Release:        12%{?dist}
URL:            https://github.com/MarcSabatella/Campania
VCS:            git:%{url}.git

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

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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

%check
%fontcheck

%fontfiles

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 2.009-8
- Stop building for 32-bit x86

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jerry James <loganjerry@gmail.com> - 2.009-7
- Remove redundant metadata check

* Fri Jul 14 2023 Jerry James <loganjerry@gmail.com> - 2.009-7
- Simplify the font config file

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
