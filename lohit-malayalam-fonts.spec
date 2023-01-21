%global fontname lohit-malayalam
%global fontconf 67-%{fontname}.conf
%global metainfo io.pagure.lohit.malayalam.font.metainfo

Name:           %{fontname}-fonts
Version:        2.92.2
Release:        15%{?dist}
Summary:        Free Malayalam font
License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires:  python3-devel
BuildRequires: make
Requires:       fontpackages-filesystem

%description
This package provides a free Malayalam truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 

%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README std-test-out.txt test-malayalam.txt
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Vishal Vijayraghavan <vvijayra AT redhat DOT com> - 2.92.2-7
- Added CI tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.92.2-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.92.2-1
- Upstream new release 2.92.2
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.92.1-1
- Added  BuildRequires: python3-devel.
- Resolves: #1423905 - FTBFS in rawhide
- Migrated from fedorahosted.org to pagure.io

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.92.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Pravin Satpute <psatpute@redhat.com> - 2.92.0-3
- Added metainfo for gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Pravin Satpute <psatpute@redhat.com> - 2.92.0-1
- Upstream release 2.92.0
- Further removal 12 not required glyphs from fonts.
- Added reference of glyph instead of full glyphs points wherever possible.
- Resolved 10 issues reported on github: #35,#36,#37,#38,.#39,#40.#41,#42,#43,#44.
- More test cases in test file
- Renamed Anchor to MLAnchor

* Wed Feb 05 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-1
- Upstream release 2.91.0
- First release under Lohit2 project.
- Rewritten all Open type tables for mlm2 and mlym
- User friendly glyph names, Following AGL syntax
- Testing done with Harfbuzz and Uniscribe
- Test file available with release tarball
- Removed number of glyphs nearly around .75 %  { 214/288 ~= .75(0.743) % }
- Looksup are reduced by { 10/18 = 55.5 % }
- Improved GASP table


* Tue Oct 08 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.4-1
- Upstream release 2.5.4

* Thu Sep 19 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-3
- Removed wrong script tags

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-1
- Upstream release 2.5.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug #799565 and #798870

* Mon Apr 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Mon May 09 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- Upstream Release of 2.4.5

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-9
- Resolved bug 694561

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-8
- Resolved bug 692363

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-6
- resolved bug 673415, rupee sign

* Fri Apr 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.4-5
- fixed bug 578036, .conf fix

* Thu Dec 10 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-4
- fixed bug 548686, license field

* Wed Dec 09 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- bugfix 520041

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
