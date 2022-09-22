%global fontname thai-arundina
%global fontconf 67-%{fontname}
%global archivename fonts-sipa-arundina-%{version}

%global common_desc \
Arundina fonts were created aiming at Bitstream Vera / Dejavu \
compatibility, under SIPA's initiation.  They were then further \
modified by TLWG for certain aspects, such as Latin glyph size \
compatibility and OpenType conformance.

Name:		%{fontname}-fonts
Version:	0.2.2
Release:	11%{?dist}
Summary:	Thai Arundina fonts

License:	Bitstream Vera
URL:		http://linux.thai.net/projects/fonts-sipa-arundina
Source0:	http://linux.thai.net/pub/thailinux/software/fonts-sipa-arundina/%{archivename}.tar.xz
Source1:	%{name}-sans-fontconfig.conf
Source2:	%{name}-serif-fontconfig.conf
Source3:	%{name}-sans-mono-fontconfig.conf
Source4:	%{fontname}.metainfo.xml
Source5:	%{fontname}-sans.metainfo.xml
Source6:	%{fontname}-sans-mono.metainfo.xml
Source7:	%{fontname}-serif.metainfo.xml

BuildArch:	noarch
BuildRequires: make
BuildRequires:	fontforge
BuildRequires:	fontpackages-devel

%description
%common_desc


%package common
Summary:	Common files of the Thai Arundina font set
Requires:	fontpackages-filesystem

%description common
%common_desc


%package -n %{fontname}-sans-fonts
Summary:	Variable-width sans-serif Thai Arundina fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This package consists of the Thai Arundina sans-serif variable-width
font faces.

%_font_pkg -n sans -f %{fontconf}-sans.conf ArundinaSans.ttf ArundinaSans-Bold.ttf ArundinaSans-Oblique.ttf ArundinaSans-BoldOblique.ttf
%{_datadir}/appdata/%{fontname}-sans.metainfo.xml


%package -n %{fontname}-serif-fonts
Summary:	Variable-width serif Thai Arundina fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

This package consists of the Thai Arundina serif variable-width
font faces.

%_font_pkg -n serif -f %{fontconf}-serif.conf ArundinaSerif.ttf ArundinaSerif-Bold.ttf
%{_datadir}/appdata/%{fontname}-serif.metainfo.xml


%package -n %{fontname}-sans-mono-fonts
Summary:	Monospace sans-serif Thai Arundina fonts
Requires:	%{name}-common = %{version}-%{release}

%description -n %{fontname}-sans-mono-fonts
%common_desc

This package consists of the Thai Arundina sans-serif monospace font
faces.

%_font_pkg -n sans-mono -f %{fontconf}-sans-mono.conf ArundinaSansMono.ttf ArundinaSansMono-Bold.ttf ArundinaSansMono-Oblique.ttf ArundinaSansMono-BoldOblique.ttf
%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml


%prep
%setup -q -n %{archivename}


%build
%configure
make


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p arundina/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-mono.conf

for fconf in %{fontconf}-sans.conf \
    %{fontconf}-serif.conf \
    %{fontconf}-sans-mono.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
     %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE4} \
	%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE5} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-sans.metainfo.xml
install -Dm 0644 -p %{SOURCE6} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-sans-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE7} \
	%{buildroot}%{_datadir}/appdata/%{fontname}-serif.metainfo.xml

%files common
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc README AUTHORS COPYING NEWS


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Peng Wu <pwu@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 10 2016 Daiki Ueno <dueno@redhat.com> - 0.2.1-1
- new upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 Richard Hughes <richard@hughsie.com> - 0.2.0-6
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Daiki Ueno <dueno@redhat.com> - 0.2.0-1
- new upstream release
- change %%archivename to fonts-sipa-arundina per upstream

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Daiki Ueno <dueno@redhat.com> - 0.1.3-1
- new upstream release

* Thu Mar 31 2011 Daiki Ueno <dueno@redhat.com> - 0.1.2-2
- add fontconfig files
- remove buildroot cleanup in %%install

* Mon Mar 28 2011 Daiki Ueno <dueno@redhat.com> - 0.1.2-1
- initial packaging for Fedora
