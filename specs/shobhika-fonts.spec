%global fontname shobhika
%global fontconf 68-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	1.04
Release:	18%{?dist}
Summary:	Free Indian truetype/open type fonts
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
URL:		https://github.com/Sandhi-IITBombay/Shobhika
Source0:	%{url}/releases/download/v%{version}/Shobhika-%{version}.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Requires:	fontpackages-filesystem

%description
Shobhika is a free, open source, Unicode compliant, OpenType font with support \
for Devanagari, Latin, and Cyrillic scripts.\ 
It is available in two weights—regular and bold.\ 
The font is designed with over 1600 Devanāgarī glyphs, including support \
for over 1100 conjunct consonants, as well as vedic accents.

%prep
%autosetup -n Shobhika-%{version}
chmod 644 *.txt

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%doc AUTHORS.txt README.md CONTRIBUTORS.txt
%license OFL.txt Copyright.txt
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.04-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1.04-5
- Font CI test added

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jun 07 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1.04-3
- Updated fontconfig.

* Tue May 29 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1.04-2
- Added metainfo.xml file.

* Mon May 28 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1.04-1
- first release of shobhika fonts  
