%define fontname sil-doulos
%define archivename DoulosSIL
%define docversion 4.100

Name:           %{fontname}-fonts
Version:        6.200
Release:        4%{?dist}
Summary:        Doulos SIL fonts

License:        OFL-1.1
URL:            http://scripts.sil.org/DoulosSILFont
Source0:        https://software.sil.org/downloads/r/doulos/%{archivename}-%{version}.zip
Source1:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

# Obsoleting and providing the old RPM name
Obsoletes:      doulos-fonts < 4.104-2

%description
Doulos SIL provides glyphs for a wide range of Latin and Cyrillic
characters. Doulos's design is similar to the design of the Times-like
fonts, but only has a single regular face. It is intended for use alongside
other Times-like fonts where a range of styles (italic, bold) are not
needed.


%prep
%autosetup -n %{archivename}-%{version}
sed -i 's/\r$//' *.txt


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg *.ttf
%doc FONTLOG.txt OFL-FAQ.txt README.txt
%doc documentation/pdf/
%license OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.200-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.200-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Parag Nemade <pnemade AT redhat DOT com> - 6.200-1
- Update to 6.200 version
- Migrate to SPDX license expression

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.104-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Parag Nemade <pnemade AT redhat DOT com> - 4.104-12
- Add metainfo file to show this font in gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Roozbeh Pournader <roozbeh@gmail.com> - 4.104-3
- Cleanup, remove Provides (Nicholas Mailhot)

* Thu Jan 29 2009 Roozbeh Pournader <roozbeh@gmail.com> - 4.104-2
- Update to new F11 fonts policy, renaming from doulos-fonts

* Tue Jan 13 2009 Roozbeh Pournader <roozbeh@gmail.com> - 4.104-1
- Update main font to 4.104 (with Unicode 5.1 support)
- Remove Doulos Literacy (not maintained anymore)
- Last update before conversion to new fonts policy

* Tue Dec 11 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 4.100-1
- Update main font to 4.100, keep old Doulos Literacy which is latest
- Change license tag to OFL

* Thu Nov 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 4.0.14-4
- Include Doulos Literacy
- Don't include font cache files (fontconfig mechanism is changed)

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 4.0.14-3
- Add dist tag

* Wed Nov 08 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 4.0.14-2
- Rebuild to make package available in Rawhide again

* Sat Feb 18 2006 Roozbeh Pournader <roozbeh@farsiweb.info> - 4.0.14-1
- Initial packaging, based on gentium-fonts
