%global fontname lohit-tamil

Version:       2.91.3
Release:       24%{?dist}
URL:           https://github.com/lohit-fonts/lohit-tamil-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README.md ChangeLog src/test-tamil.txt 

%global fontfamily        Lohit Tamil
%global fontsummary       Free truetype font for Tamil language
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Tamil truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://github.com/lohit-fonts/lohit-tamil-fonts/archive/refs/tags/%{version}.tar.gz#/%{fontname}-fonts-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf

%fontpkg

%prep
%setup -q -n %{fontname}-fonts-%{version}
%linuxtext OFL.txt AUTHORS README.md ChangeLog COPYRIGHT src/test-tamil.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 1 2024 Sudip Shil <sshil@redhat.com> - 2.91.3-22
- reverted unexpected sfd changes with correcting version of .sfd file
- refreshed github tarball

* Mon Jan 29 2024 Sudip Shil <sshil@redhat.com> - 2.91.3-21
- Fixed version mismatch https://bugzilla.redhat.com/show_bug.cgi?id=1580458 

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 15 2023 Sudip Shil <sshil@redhat.com> - 2.91.3-18
- lowering priority of lohit-tamil-fonts

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Sudip Shil <sshil@redhat.com> - 2.91.3-16
- Convert to new fonts packaging guidelines
- Update the fonts package
- https://fedoraproject.org/wiki/Changes/New_Fonts_Packaging

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 17 2019 Vishal Vijayraghavan <vvijayra AT redhat DOT com> - 2.91.3-7
- Added CI tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.91.3-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.3-1
- Upstream new release 2.91.3
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.2-1
- Added  BuildRequires: python3-devel.
- Resolves: #1423909 - FTBFS in rawhide
- Upstream new release, migrated from fedorahosted.org to pagure.io.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 03 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.1-1
- Upstream release 2.91.1
- Resolves #1170137 - Lohit Tamil 2.91.0 hinting issues

* Mon Oct 27 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-2
- Added metainfo for gnome-software

* Tue Oct 14 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-1
- Resolves 1152203 :- Upstream release 2.91.0
- Rewritten all Open type tables with supporting taml and tml2 tags.
- Renamed all the glyphs by following AGL syntax.
- Open type tables are available in .fea file and this time it is compiled with AFDKO.
- Reusing glyphs by "COPY REFERENCE"
- Added GRID FITTING table and auto-hinting by fontforge.
- Tested with Harfbuzz NG and Uniscribe (W8).
- Auto test module available with test files.


* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolves bug 829143

* Wed Jun 06 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream release 2.5.1

* Thu May 10 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.0-3
- Resolves bug 820478

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-7
- fixed bug 673419, asterisk character and rupee sign

* Thu Sep 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-6
- improved fixe to bug 629824, punctuations marks

* Fri Sep 10 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- fixed bug 629824, punctuations mark size

* Mon Aug 23 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- fixed bug 621445, conf file

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- fixed bug 578039, conf file

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- fixed bug 548686, license field

* Tue Nov 24 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release

* Wed Nov 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- resolved rh bug 536724

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
