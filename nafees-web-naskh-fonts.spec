%global fontname        nafees-web-naskh
%global fontconf        67-%{fontname}.conf
%global archivename     NafeesWeb
%global archivedate     20080509

Name:           %{fontname}-fonts
Version:        1.2
Release:        28%{?dist}
Summary:        Nafees Web font for writing Urdu in the Naskh script 

License:        Bitstream Vera
URL:            http://www.crulp.org/Downloads/NafeesWeb.zip

## NOTE: the original archive is unversioned, so we rename it to add a date stamp
# The Source0 is obtained by doing the following:
# $ wget -S http://www.crulp.org/Downloads/NafeesWeb.zip
# $ mv %{archivename}.zip %{fontname}-%{archivedate}.zip
Source0:        %{fontname}-%{archivedate}.zip

## Fix RHBZ# while not fixed upstream
Source1:        %{fontname}-update-preferred-family.pe
Source2:        %{fontconf}
Source3:        %{fontname}.metainfo.xml

BuildArch:      noarch
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge

%description

Character based Nafees Web Naskh Open Type Font for writing Urdu in Naskh
script based on Unicode standard. This version has complete support of
Aerabs for Urdu and updated glyphs for Latin characters.
Nafees Web Naskh OTF contains approximately 330 glyphs, including 5 ligatures.


%prep
%setup -q -c

%build
# Fix RHBZ#490830 while not fixed upstream
%{_bindir}/fontforge %{SOURCE1} %{archivename}.ttf

%install
rm -rf %{buildroot}

#fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
                %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml



%_font_pkg -f %{fontconf} *.ttf

%doc
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Pravin Satpute <psatpute@redhat.com> - 1.2-13
- Added metainfo for gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 24 2010 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-6
- bumping spec as I forgot to add the fontconfig file in previous commit

* Wed Feb 24 2010 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-5
- minor spec fixes

* Wed Feb 24 2010 Pravin Satpute <psatpute@redhat.com> - 1.2-4
- adding .conf file
- bugfix 567612

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-2
- added comment explaining how the source is obtained (as it is modified from upstream)
- temporary fix for RHBZ#490830 while not fixed upstream

* Sat Apr 11 2009 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-1
- update to 1.2 release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> 1.0-4
- Builddep on fontpackages-devel

* Sun Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> 1.0-3
- Typo: fontdir -> _fontdir

* Sun Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> 1.0-2
- Updated to current Fedora font packaging guidelines

* Sat Sep 15 2007 Bernardo Innocenti <bernie@codewiz.org> 1.0-1
- Initial packaging, borrowing many things from abyssinica-fonts
