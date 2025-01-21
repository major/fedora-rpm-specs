%define fontname sil-gentium
%define archivename ttf-sil-gentium
%define common_desc \
SIL Gentium ("belonging to the nations" in Latin) is a Unicode typeface family\
designed to enable the many diverse ethnic groups around the world who use\
the Latin script to produce readable, high-quality publications. It supports\
a wide range of Latin-based alphabets.


Name:           %{fontname}-fonts
Version:        1.02
Release:        37%{?dist}
Summary:        SIL Gentium fonts

License:        OFL-1.1
URL:            http://scripts.sil.org/Gentium_linux
# Source0 can be downloaded from the above URL, search for "tar.gz"
Source0:        %{archivename}_1.0.2.tar.gz
Source1:        %{fontname}.metainfo.xml
Source2:        %{fontname}-alt.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       %{name}-common = %{version}-%{release}

# Obsoleting and providing the old RPM name
Obsoletes:      gentium-fonts < 1.02-7

%description
%common_desc

This package consists of the main SIL Gentium family.


%_font_pkg Gen[RI]*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%package common
Summary:        Common files of SIL Gentium fonts
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-alt-fonts
Summary:        SIL GentiumAlt fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-alt-fonts
%common_desc

This package consists of the SIL GentiumAlt family. GentiumAlt is a
alternative version of Gentium with flatter diacratics, to make it more
suitable for languages that use stacking diacratics, like Vietnamese. There
is no problem with having both Gentium and GentiumAlt installed at the same
time.


%_font_pkg -n alt GenA*.ttf
%{_datadir}/appdata/%{fontname}-alt.metainfo.xml


%prep
%setup -q -n %{archivename}-%{version}

# Convert GENTIUM-FAQ from MacRoman
iconv --from=MACINTOSH --to=UTF-8 GENTIUM-FAQ > GENTIUM-FAQ.new
touch -c -r GENTIUM-FAQ GENTIUM-FAQ.new
mv GENTIUM-FAQ.new GENTIUM-FAQ


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-alt.metainfo.xml

%files common
%doc FONTLOG GENTIUM-FAQ OFL-FAQ QUOTES README
%license OFL

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Parag Nemade <pnemade AT redhat DOT com> - 1.02-34
- Migrate to SPDX license expression

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 21 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.02-17
- Add metainfo file to show this font in gnome-software
- Remove duplicate dir %%{_fontdir}
- Clean the spec to follow current packaging guidelines

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Roozbeh Pournader <roozbeh@gmail.com> 1.02-8
- Better description for GentiumAlt subpackage, remove
  Provides (Nicolas Mailhot)

* Tue Jan 27 2009 Roozbeh Pournader <roozbeh@gmail.com> 1.02-7
- Update to new F11 fonts policy, including renaming and splitting

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.02-6
- fix license tag

* Thu Nov 09 2006 Roozbeh Pournader <roozbeh@farsiweb.info> 1.02-5
- Remove ghost-ed fontconfig caches (fontconfig mechanism is changed)

* Tue Sep 19 2006 Kevin Fenzi <kevin@tummy.com> 1.02-4
- Rebuild for Fedora Extras 6
- Add dist tag

* Mon Feb 13 2006 Roozbeh Pournader <roozbeh@farsiweb.info> 1.02-3
- Rebuild for Fedora Extras 5

* Wed Dec 21 2005 Roozbeh Porunader <roozbeh@farsiweb.info> 1.02-2
- Added comment to Source0 about where to get the file
- Added Provides and Obsoletes for upsteam RPM name

* Mon Dec 19 2005 Roozbeh Pournader <roozbeh@farsiweb.info> 1.02-1
- Initial packaging, borrowing many things from dejavu-fonts
