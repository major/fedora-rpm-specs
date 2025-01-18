%global	fontname	beteckna
%global common_desc \
This font is available from beteckna.se, it is a geometric sans-serif \
typeface inspired by Paul Renners popular type, Futura. It was drawn by \
Johan Mattsson in Maj 2007. The font is free, licensed under terms of the \
GNU GPL. This version supports English and a few nordic languages. \
Special character &#x2708; ( ✈ ) depicts two cats.

%global fontconf	60-%{fontname}-fonts

Name:		%{fontname}-fonts
Version:	0.3
Release:	34%{?dist}
Summary:	Beteckna sans-serif fonts

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://gnu.ethz.ch/linuks.mine.nu/beteckna/
Source0:	http://gnu.ethz.ch/linuks.mine.nu/beteckna/beteckna-0.3.tar.gz
Source1:	%{name}-fontconfig.conf
Source2:	%{name}-lower-case-fontconfig.conf
Source3:	%{name}-small-caps-fontconfig.conf
Source4:	%{fontname}.metainfo.xml
Source5:	%{fontname}-lower-case.metainfo.xml
Source6:	%{fontname}-small-caps.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontforge, fontpackages-devel
Requires:	%{name}-common = %{version}-%{release}

%description
%common_desc

%_font_pkg -f %{fontconf}.conf Beteckna.otf

%package	common
Summary:	Common files of %{name}
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


# 1 Lower Case
%package -n	%{fontname}-lower-case-fonts
Summary:	Beteckna lower case sfd fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-lower-case-fonts
%common_desc

These are lower case Beteckna Fonts.

%_font_pkg -f  %{fontconf}-lower-case.conf -n lower-case BetecknaLowerCase*.otf
%{_datadir}/appdata/%{fontname}-lower-case.metainfo.xml


# 1 Small Caps
%package -n	%{fontname}-small-caps-fonts
Summary:	Beteckna small caps sfd fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-small-caps-fonts
%common_desc

These are small caps Beteckna Fonts.

%_font_pkg -n small-caps -f  %{fontconf}-small-caps.conf BetecknaSmallCaps.otf
%{_datadir}/appdata/%{fontname}-small-caps.metainfo.xml

%prep
%setup -q -n beteckna-0.3

fold -s CHANGELOG > CHANGELOG.new
sed -i 's/\r//' CHANGELOG.new
touch -r CHANGELOG CHANGELOG.new
mv CHANGELOG.new CHANGELOG


%build
fontforge -lang=ff -script "-" Beteckna*.sfd << EOF
i = 1
while ( i < \$argc )
	Open (\$argv[i], 1)
	otfile = \$fontname + ".otf"
	Generate(otfile,"otf")
	Close()
	i++
endloop
EOF

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}


install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-small-caps.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lower-case.conf

for fconf in %{fontconf}.conf %{fontconf}-lower-case.conf %{fontconf}-small-caps.conf ; 
do
	ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-lower-case.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-small-caps.metainfo.xml

%files common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc AUTHORS LICENSE CHANGELOG readme.html

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3-33
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Richard Hughes <richard@hughsie.com> - 0.3-13
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3-6
- Rebuilt in accordance with new licensing guidelines

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Ankur Sinha <ankursinha AT fedoraproject.org>
- 0.3-4
- Rebuilt and tested with mock in accordance with #476720
* Mon Feb 16 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org>
- 0.3-3
- Rebuilt using Multi spec


