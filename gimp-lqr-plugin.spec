Name:           gimp-lqr-plugin
Version:        0.7.2
Release:        23%{?dist}
Summary:        Content-aware resizing plug-in for the GIMP
License:        GPLv2+
URL:            http://liquidrescale.wikidot.com/
Source0:        http://liquidrescale.wikidot.com/local--files/en:download-page-sources/%{name}-%{version}.tar.bz2
# Filed upstream as https://github.com/carlobaldassi/gimp-lqr-plugin/issues/1
Source1:        %{name}.metainfo.xml
Patch0:         gimp-lqr-plugin-0.7.2-gcc10.patch
BuildRequires:  gcc
BuildRequires:  gimp-devel >= 2.4
BuildRequires:  perl(XML::Parser)
BuildRequires:  gettext
BuildRequires:  liblqr-1-devel >= 0.3.0
BuildRequires:  intltool
BuildRequires:  /usr/bin/appstream-util
BuildRequires: make
Requires:       gimp%{?_isa} >= 2.4

%description
This package is a plug-in for the GIMP 2.4. It implements the algorithm
described in the paper "Seam Carving for Content-Aware Image Resizing"
by Shai Avidan and Ariel Shamir, which can be found at
http://www.faculty.idc.ac.il/arik/imret.pdf

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install INSTALL="install -p"
mkdir -p %{buildroot}/%{_datadir}/appdata/
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%find_lang gimp20-lqr-plugin 

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%files -f gimp20-lqr-plugin.lang
%license COPYING
%doc README ChangeLog TODO AUTHORS NEWS
%{_libdir}/gimp/2.0/plug-ins/%{name}
%{_libdir}/gimp/2.0/plug-ins/plug_in_lqr_iter
%{_datadir}/gimp/2.0/scripts/batch-gimp-lqr.scm
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 Than Ngo <than@redhat.com> - 0.7.2-15
- Fixed bz#1799406, FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.2-6
- Fixes in packaging

* Sun Mar 13 2016 Sven Lankes <sven@lank.es> - 0.7.2-5
- include AppStream metadata (closes rhbz #1317187 - thanks Jiri Eischmann)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.2-1
- 0.7.2 upstream release
- spec cleanups

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Nils Philippsen <nils@redhat.com> - 0.7.1-3
- rebuild against gimp 2.8.0 release candidate

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Sven Lankes <sven@lank.es> - 0.7.1-1
- Update to latest upstream release
- Change image-add-layer to image-insert-layer as suggested by gimp-upstream

* Fri Dec 16 2011 Nils Philippsen <nils@redhat.com> - 0.6.1-5
- rebuild for GIMP 2.7

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.1-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 03 2009 Sven Lankes <sven@lank.es> - 0.6.1-2
- Add BR on intltool
- Bump liblqr-1-devel BR to 0.3

* Mon Aug 03 2009 Sven Lankes <sven@lank.es> - 0.6.1-1
- Update to latest upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Mar 02 2008 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.4.0.4-2
- Fixed typos, buildrequires and requires.

* Wed Feb 20 2008 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.4.0.4-1
- Remove hyphen from versioning.

* Tue Feb 19 2008 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.4.0-3
- Fixed licensing issue.

* Mon Feb 4 2008 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.4.0-2
- Removed CFLAGS.
- Fixed ownership issues.

* Thu Jan 17 2008 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.4.0-1
- Update to 0.4.0-3. 
- Added liblqr dependency. 

* Mon Dec 10 2007 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.4.0-0
- Update to 0.4.0. 

* Thu Nov 22 2007 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.3.0-1
- Updated languages.
- Removed DEBUG flag.
  http://liquidrescale.wikidot.com/forum/t-23531/bugfix
- Cleaned .spec file to meet Fedora Guidelines. 

* Fri Oct 12 2007 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.3.0-0
- Update to latest upstream release.

* Fri Oct 5 2007 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.2.1-4
- Added more translation: Romanian, Spanish Spanish, Serbian.

* Wed Oct 3 2007 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.2.1-3
- Added Basque, Chinese, Argentinian Spanish, Hungarian translations.

* Tue Oct 2 2007 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.2.1-2
- Added German translation.

* Tue Oct 2 2007 Alexandru Ciobanu <alex@tvtransilvania.ro> - 0.2.1-1
- Initial RPM release.
