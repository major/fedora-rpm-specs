BuildRequires: fontforge
BuildRequires: make

# Do not trust font metadata versionning unless you've checked upstream does
# update versions on file changes. When in doubt use the timestamp of the most
# recent file as version.
%global cvsdate 20090803
Version: 0.6
Release: 33.%{cvsdate}cvs%{?dist}
URL:    http://sinhala.sourceforge.net/

%global fontlicense       GPL-2.0-only
%global fontlicenses      COPYING 
%global fontdocs          CREDITS README.fonts                            
            
%global fontfamily        lklug
%global fontsummary       Fonts for Sinhala language
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}  

%global fontdescription   %{expand:
The lklug-fonts package contains fonts for the display of
Sinhala. The original font for TeX/LaTeX is developed by Yannis
Haralambous and are in GPL. OTF tables are added by Anuradha
Ratnaweera and Harshani Devadithya.
}

# cvs snapshot created with following steps
#cvs -z3 -d:pserver:anonymous@sinhala.cvs.sourceforge.net:/cvsroot/sinhala co -P sinhala/fonts
#cd sinhala/fonts/
#tar -czf lklug-%%{cvsdate}.tar.gz convert.ff COPYING  CREDITS lklug.sfd Makefile README.fonts
Source: lklug-%{cvsdate}.tar.gz
Source1: 65-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c

%build
make
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-33.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-32.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-31.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-30.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 02 2023 Fedora Release Engineering <sshil@redhat.com> - 0.6-29.20090803cvs
- Un-retire this package
- Convert to new fonts packaging guidelines
- Migrate to SPDX license expression

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-28.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-27.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-26.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-25.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-24.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-23.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.6-22.20090803cvs
- Update fontconfig DTD id in conf file

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-21.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-17.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-13.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Pravin Satpute <psatpute@redhat.com> - 0.6-12.20090803cvs
- Added appdata for gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-11.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-10.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-9.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Parag <paragn AT fedoraproject DOT org> - 0.6-8.20090803cvs
- Resolves:rh#879483 - fix build.log warning File listed twice: /usr/share/fonts/lklug

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5.20090803cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 15 2010 Pravin Satpute <psatpute@redhat.com> - 0.6-4.20090803cvs
- resolved bug 578028, updated .conf file

* Thu Feb 25 2010 Pravin Satpute <psatpute@redhat.com> - 0.6-3.20090803cvs
- resolved bug 568262, license tag

* Wed Feb 24 2010 Pravin Satpute <psatpute@redhat.com> - 0.6-2.20090803cvs
-  added .conf file, bug 567610

* Mon Aug 03 2009 Parag <pnemade@redhat.com> - 0.6-1.20090803cvs
- update to cvs snapshot 20090803.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-9
- Dropping previous release.

* Mon Mar 09 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-8
- Following new font packaging guidelines

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 27 2008 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-6
- Updated spec to obsolete fonts-sinhala

* Wed Oct 17 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-5
- Added sfd file into srpm

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-4
- Updated according to the review

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-3
- Using common template of font spec file

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-2
- Spec cleanup

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.2.2-1
- Split package from fonts-sinhala to reflect upstream project name
