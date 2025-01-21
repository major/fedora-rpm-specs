%global fontname woodardworks-laconic
%global fontconf 60-%{fontname}

Name:		%{fontname}-fonts
Summary:	An artistic and minimal sans-serif font family
Version:	001.001
Release:	31%{?dist}
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
Source0:	http://www.woodardworks.com/laconic.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}-shadow-fonts-fontconfig.conf
Source3:        %{fontname}.metainfo.xml
Source4:        %{fontname}-shadow.metainfo.xml
URL:		http://www.woodardworks.com/type13.html
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem
BuildArch:	noarch

%description
Laconic is a typeface font design meant to be dry without quite seeming 
parched. Curves and diagonals are kept to a bare minimum without sacrificing
legibility. What it lacks in design features are more than made up for in 
OpenType features. All the weights contain small caps, proportial figures,
old style figures, tabular figures, ligatures and stylistic alternates.

%package -n %{fontname}-shadow-fonts
Summary:	A shadowed version of the Laconic sans-serif font family
Requires:	fontpackages-filesystem

%description -n %{fontname}-shadow-fonts
Laconic is a typeface font design meant to be dry without quite seeming
parched. Curves and diagonals are kept to a bare minimum without sacrificing
legibility. What it lacks in design features are more than made up for in
OpenType features. All the weights contain small caps, proportial figures,
old style figures, tabular figures, ligatures and stylistic alternates.
This package contains the Laconic Shadow font face.

%prep
%setup -q -c -T -n laconic
# We have to do this to avoid leaving a stray __MACOSX dir in the buildroot
unzip -j -L -q %{SOURCE0}
# Get rid of junk files
rm -rf ._*

%build
# Nothing to do here, already in OTF.

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-shadow.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-shadow.conf %{buildroot}%{_fontconfig_confdir}/%{fontconf}-shadow.conf


# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-shadow.metainfo.xml

%_font_pkg -f %{fontconf}.conf Laconic_Bold.otf Laconic_Light.otf Laconic_Regular.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc laconic_eula.pdf

%_font_pkg -n shadow -f %{fontconf}-shadow.conf Laconic_Shadow.otf
%{_datadir}/appdata/%{fontname}-shadow.metainfo.xml
%doc laconic_eula.pdf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 001.001-30
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 001.001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 Richard Hughes <richard@hughsie.com> - 001.001-11
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 001.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 001.001-3
- fix shadow fontconfig file

* Tue May 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 001.001-2
- unzip manually to avoid leaving stray directories
- split off shadow fontface into subpackage
- mark fontconfig files as sans-serif

* Wed Apr 1 2009 Tom "spot" Callaway <tcallawa@redhat.com> 001.001-1
- Initial package for Fedora
