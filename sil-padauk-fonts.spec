%global fontname sil-padauk
%global fontconf 65-%{fontname}

%global common_desc \
Padauk is a pan Burma font designed to support all Myanmar script based \
languages. It covers all of the Unicode Myanmar script blocks and works \
on all OpenType and Graphite based systems.

Name:    %{fontname}-fonts
Version: 3.003
Release: 10%{?dist}
Summary: A font for Burmese and the Myanmar script

License: OFL
URL:     https://software.sil.org/padauk/
Source0: https://github.com/silnrsi/font-padauk/releases/download/v%{version}/padauk-%{version}.zip
Source1: %{name}-fontconfig.conf
Source2: %{name}-book-fontconfig.conf
Source3: %{fontname}.metainfo.xml
Source4: %{fontname}-book.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: fonttools
Requires:      fontpackages-filesystem

%description
%common_desc

%_font_pkg -f %{fontconf}.conf Padauk-Regular.ttf Padauk-Bold.ttf
%doc *.txt documentation
%{_datadir}/appdata/%{fontname}.metainfo.xml

%package -n %{fontname}-book-fonts
Summary:  A font for Burmese and the Myanmar script

%description -n %{fontname}-book-fonts
Padauk Book family font.

%common_desc

%_font_pkg -n book -f %{fontconf}-book.conf PadaukBook*.ttf
%{_datadir}/appdata/%{fontname}-book.metainfo.xml
%doc *.txt documentation

%prep
%autosetup -n padauk-%{version}
sed -i 's/\r//' *.txt documentation/DOCUMENTATION.txt

%build
# nothing to do here

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-book.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-book.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-book.metainfo.xml

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 3.003-1
- Update to new upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Parag Nemade <pnemade AT fedoraproject DOT org> - 3.002-1
- Update to 3.002

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 2.8-9
- Fix fonttools issue (rh#1240005,rh#1242549)
- Modernize spec

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 Richard Hughes <richard@hughsie.com> - 2.8-7
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Parag <paragn AT fedoraproject DOT org> - 2.8-4
- Resolves:rh#907330 - Fix the PostScript name in font files

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Parag <paragn AT fedoraproject DOT org> - 2.8-2
- Package Padauk Book family font in separate subpackage

* Thu Nov 29 2012 Parag <paragn AT fedoraproject DOT org> - 2.8-1
- Resolves:rh#880012 - upstream new release available 2.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild


* Tue May 26 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-6
- Changed the URL

* Mon May 25 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-5
- Cleaned up the spec file
- Used Obsoletes for upgrade path from padauk-fonts

* Tue Mar 24 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-4
- Cleaned up the spec file as per new font packaging guidelines
- Replaced padauk-src.ttf and padaukbold-src.ttf with Padauk.ttf and Padauk-Bold.ttf [490583]
- Renamed the package to sil-padauk-fonts

* Sun Feb 22 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-3
- Changed the package as per new font packaging guidelines 


* Tue Jul 15 2008 Minto Joseph <mvaliyav at redhat.com> - 2.4-2
- Changed setup macro and fontconfig rules
- Changed fontconfig prefix


* Tue Jul 15 2008 Minto Joseph <mvaliyav at redhat.com> - 2.4-1
- Changed versioning
- Added configuration file
- Added more description
- Added license file

* Fri Jul 11 2008 Minto Joseph <mvaliyav at redhat.com> - 20080617-1
- initial package

