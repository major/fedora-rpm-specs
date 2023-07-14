%global gimpdatadir %(%{_bindir}/gimptool --gimpdatadir || echo blah)

Summary: Extra files for GIMP
Name: gimp-data-extras
Version: 2.0.2
Release: 28%{?dist}
License: GPL-2.0-or-later
URL: http://www.gimp.org/
Source0: http://download.gimp.org/pub/gimp/extras/gimp-data-extras-%{version}.tar.bz2
Source1: license-clarification.txt
Source2: gimp-data-extras.metainfo.xml
BuildArch: noarch
BuildRequires: gimp-devel-tools
BuildRequires: gimp-devel >= 2:2.0
BuildRequires: make
Requires: gimp >= 2:2.0

%description
Patterns, gradients, and other extra files for GIMP.

%prep
%setup -q
cp %{SOURCE1} %{SOURCE2} .

%build
%configure
make

%install
make DESTDIR=%{buildroot} install

install -d -m 0755 %{buildroot}%{_datadir}/appdata
install -m 0644 %{name}.metainfo.xml %{buildroot}%{_datadir}/appdata/

%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING license-clarification.txt
%{gimpdatadir}/*
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
* Wed Jul 12 2023 Josef Ridky <jridky@redhat.com> - 2.0.2-28
- Move to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 27 2016 Nils Philippsen <nils@redhat.com> - 2.0.2-14
- install AppStream metadata file (#1316293)
- use %%license for license files
- remove some old cruft

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Nils Philippsen <nils@redhat.com>
- use %%global instead of %%define

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 05 2014 Nils Philippsen <nils@redhat.com> - 2.0.2-11
- update source URL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 18 2012 Nils Philippsen <nils@redhat.com> - 2.0.2-7
- GIMP doesn't have an article anymore

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nils Philippsen <nils@redhat.com> - 2.0.2-1
- bump release for importing

* Fri Feb 13 2009 Nils Philippsen <nils@redhat.com> - 2.0.2-0.3
- merge review (#225797): include IRC log which clarifies the package license

* Mon Feb 09 2009 Nils Philippsen <nils@redhat.com> - 2.0.2-0.2
- don't require gimptool file, but gimp-devel-tools package for building
- merge review (#225797)
  - don't require /usr/share/gimp/2.0 directory, but specific minimum gimp
    version
  - work around problematic gimpdatadir macro definition if gimptool is not
    available 

* Wed Nov 14 2007 Nils Philippsen <nphilipp@redhat.com> - 2.0.2-0.1
- version 2.0.2
- use RPM macros where appropriate
- use "make DESTDIR=... install"
- merge review (#225797)
  - add dist tag
  - change license tag to GPLv2+
  - sanitize buildroot
  - set default mode 0755 for directories
  - add documentation files
  - separate BuildRequires, add epoch to BR: gimp-devel ...
  - sanitize summary
  - recode SPEC file to UTF-8
  - clean buildroot at beginning of %%install

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-1.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.1-1
- version 2.0.1

* Mon Oct 18 2004 Nils Philippsen <nphilipp@redhat.com> 2.0.0-1
- rather cosmetic version upgrade
- fix BuildRoot

* Tue Sep 21 2004 Than Ngo <than@redhat.com> 1.2.0-12 
- rebuilt

* Mon Apr 05 2004 Nils Philippsen <nphilipp@redhat.com>
- require gimp (#70753)

* Thu Feb 19 2004 Nils Philippsen <nphilipp@redhat.com>
- build with gimp-2.0
- run %%setup quietly
- use path macros
- fix source URL

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 23 2002 Matt Wilson <msw@redhat.com> 1.2.0-7
- rebuild in new collection

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Feb 25 2002 Than Ngo <than@redhat.com> 1.2.0-4
- rebuild in new enviroment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Aug 27 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.2.0-2
- s/Copyright/License/
- Use %%{_tmppath}
- Add gimp-devel as a build dependency (#44744)

* Mon Dec 25 2000 Matt Wilson <msw@redhat.com>
- 1.2.0

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Sun May 28 2000 Matt Wilson <msw@redhat.com>
- pass GIMP_DATA_DIR to make install target so we get in the buildroot

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- packaged for rawhide

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- packaged for 5.2
