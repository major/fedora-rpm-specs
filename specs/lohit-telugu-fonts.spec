%global fontname lohit-telugu

Version:       2.5.5
Release:       21%{?dist}
URL:           https://github.com/lohit-fonts/lohit-odia-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog

%global fontfamily        Lohit Telugu 
%global fontsummary       Free Telugu font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Telugu truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
BuildRequires: ttfautohint
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -n %{fontname}-%{version}
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Sudip Shil <sshil@redhat.com> - 2.5.5-17
- lowering priority of lohit-telugu-fonts

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Sudip Shil <sshil@redhat.com> - 2.5.5-15
- Convert to new fonts packaging guidelines
- Update the fonts package
- https://fedoraproject.org/wiki/Changes/New_Fonts_Packaging


* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Vishal Vijayraghavan <vvijayra AT redhat DOT com> - 2.5.5-6
- Resolves: #1648612 bad hinting instructions from bug in ttfautohint
- Build against latest ttfautohint 1.8.2-1.fc29
- Added CI tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.5.5-1
- Upstream new release 2.5.5
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 03 2015 Pravin Satpute <psatpute@redhat.com> - 2.5.4-1
- Upstream release 2.5.4
- Added support for Unicode 8.0 characters U0C00, U0C34 and U0C5A
- Added support for Latin characters
- Using TTFAUTOHINT now while building ttf file.
- Resolves #985343, #1229213 and #1258123.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.3-6
- Added metainfo for gnome-software

* Mon Jul 28 2014 Pravin Satpute <psatpute@redhat.com> - 2.5.3-5
- Resolved #1105878 - Rendering problem of స్త్ర

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Resolved #950525

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Fri Nov 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-2
- Upstream release 2.5.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug 803563

* Wed Mar 28 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Wed Feb 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.0-3
- Resolved bug 640607

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Jul 27 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-14
- fixes bug 714557

* Fri Jul 15 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-13
- fixes bug 714560

* Fri Jul 15 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-12
- fixes bug 714563

* Thu Jun 30 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-11
- fixes bug 714561

* Wed Jun 22 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-10
- fixes bug 714562

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-9
- fixes bug 692368

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-7
- fixes bug 673420

* Tue Aug 10 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-6
- fixes bug 622682

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- fixes bug 578040

* Wed Dec 30 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- fixes bug 551317

* Mon Dec 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- corrected patch 

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- fixed bug 548686, license field

* Wed Nov 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release
- bug fix 531201

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
