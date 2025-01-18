%global fontname allgeyer

%global common_desc \
Robert Allgeyer's MusiQwik and MusiSync are a set of original True Type fonts \
that depict musical notation. Each music font may be used within a word \
processing document without the need for special music publishing software, or\
embedded in PDF files.

Name:		%{fontname}-fonts
Summary: 	Musical Notation True Type Fonts
Version:	5.002
Release:	33%{?dist}
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
# The source was originally downloaded from:
# http://www.icogitate.com/~ergosum/fonts/musiqwik_musisync_y6.zip
# But the website is gone now.
Source0:	musiqwik_musisync_y6.zip
Source1:       %{fontname}.metainfo.xml
Source2:       %{fontname}-musisync.metainfo.xml
Source3:       %{fontname}-musiqwik.metainfo.xml

# This website is gone. :(
URL:		http://www.icogitate.com/~ergosum/fonts/musicfonts.htm
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}

%description
%common_desc

%package common
Summary:	Common files for MusiSync and MusiQwik fonts (documentation...)
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other Allgeyer font packages.

%package -n %{fontname}-musisync-fonts
Summary:	A musical notation font family that provides general musical decorations
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-musisync-fonts
%common_desc

This font family provides a collection of general musical decorations.

%_font_pkg -n musisync MusiSync*.ttf
%{_datadir}/appdata/%{fontname}-musisync.metainfo.xml

%package -n %{fontname}-musiqwik-fonts
Summary:	A musical notation font family intended for writing lines of actual music
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-musiqwik-fonts
%common_desc

This font family is intended for writing lines of actual music.

%_font_pkg -n musiqwik MusiQwik*.ttf
%{_datadir}/appdata/%{fontname}-musiqwik.metainfo.xml

%prep
%setup -q -c -n %{name}

# correct end-of-line encoding
for i in OFL-FAQ.txt FONTLOG.txt SOURCE.txt README_MusiQwik_MusiSync.txt LICENSE_OFL.txt; do
	sed -i 's/\r//' $i
done

# Convert to UTF-8
iconv -f iso-8859-1 -t utf-8 -o README_MusiQwik_MusiSync.txt{.utf8,}
mv README_MusiQwik_MusiSync.txt{.utf8,}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musisync.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-musiqwik.metainfo.xml

%files common
%doc FONTLOG.txt LICENSE_OFL.txt MusiQwik_character_map.htm musiqwik_demo.png 
%doc MusiSync_character_map.htm musisync_demo.png MusiSync-README.htm OFL-FAQ.txt 
%doc README_MusiQwik_MusiSync.txt SOURCE.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 5.002-32
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.002-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Richard Hughes <richard@hughsie.com> - 5.002-13
- Fix the description in GNOME software

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 09 2014 Parag Nemade <pnemade AT redhat DOT com> - 5.002-11
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove buildroot which is optional now
- Remove removal of buildroot in %%install
- Remove %%defattr
- Remove group tag
- Replace %%define with %%global

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 5.002-4
- fix urls

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> 5.002-1
- initial package for Fedora
