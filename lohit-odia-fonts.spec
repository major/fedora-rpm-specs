%global fontname lohit-odia
%global fontconf0 65-0-%{fontname}.conf
%global fontconf1 30-%{fontname}.conf
%global metainfo io.pagure.lohit.odia.font.metainfo


Name:           %{fontname}-fonts
Version:        2.91.2
Release:        14%{?dist}
Summary:        Free truetype font for Odia language

License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source1:        %{name}.conf
BuildArch:      noarch
BuildRequires:  fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires: python3-devel
BuildRequires: make
Requires:       fontpackages-filesystem
Provides:       lohit-oriya-fonts = %{version}-%{release}
Obsoletes:      lohit-oriya-fonts < 2.5.4.1-4

%description
This package provides a free truetype font for Odia language.

%prep
%setup -q -n %{fontname}-%{version} 
# To make it default font for 'or' language.
mv 66-%{fontname}.conf 65-0-lohit-odia.conf


%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf0} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf0}
ln -s %{_fontconfig_templatedir}/%{fontconf0} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf0}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}
ln -s %{_fontconfig_templatedir}/%{fontconf1} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf1}


# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml

%_font_pkg -f *.conf *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Vishal Vijayraghavan <vvijayra AT redhat DOT com> - 2.91.2-7
- Added CI tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.91.2-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.2-1
- Upstream new release 2.91.2
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.1-1
- Added  BuildRequires: python3-devel.
- Resolves: #1423908 - FTBFS in rawhide.
- Upstream new release, migrated from fedorahosted.org to pagure.io.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Pravin Satpute <psatpute@redhat.com> - 2.91.0-1
- Updated with upstream release 2.91.0
- First release of Lohit Odia after re-writing GSUB rules.
- Open type rules are available in .fea file for easy reusability.
- Feature file compiled with AFDKO.
- Supports orya and ory2 both.
- Developer friendly glyphs names with AGL syntax format.
- Corrected glyph class for all glyphs. 
- Improved shape of ka-viramasignodia-taodia.
- Added Glyph positioning rules for below based matra.
- Test file available with release tarball.
- Auto testing support with harfbuzz hb-shape.
- Tested with Harfbuzz and Uniscribe (W8 and XP)
- Corrected feature rules for conjucts ଖ୍ର ଗ୍ର କ୍ଷ୍ଯ


* Mon Oct 20 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.5-4
- Added metainfo for gnome-software

* Fri Sep 05 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.5-4
- Updated obsoletes version. rhbz#1138260

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.5-2
- Updated as per review comments. rhbz#1073378

* Thu Mar 06 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.5-1
- Upstream release 2.5.5 with name change

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.4.1-1
- Upstream release 2.5.4.1

* Wed May 29 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.4-1
- Upstream release 2.5.4

* Thu Apr 25 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-3
- Resolved #923215: UTRRS 123 GSub combination and other ligature

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Resolved #950520

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-9
- Resolved bug 692364

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.3-7
- resolved bug 673417, added rupee sign

* Mon Oct 25 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-6
- fixed bug 639977, resolved problem of ligature rendering with gedit and oowriter

* Wed Aug 25 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- fixed bug 623995, problem with kwrite/qt

* Fri Apr 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-4
- fixed bug 578037, conf file

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- fixed bug 548686, license field
- corrected source url

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
