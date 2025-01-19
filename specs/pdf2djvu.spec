Name:           pdf2djvu
Version:        0.9.19
Release:        13%{?dist}
Summary:        PDF to DjVu converter
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://jwilk.net/software/pdf2djvu
Source0:        https://github.com/jwilk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# both patches are included in 0.9.19 release, remove these lines next commit
# Patch0:         pdf2djvu-PDFDoc-constructor.patch
# Patch1:         pdf2djvu-Destination-copy-constructor.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  djvulibre-devel djvulibre
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  poppler-devel
BuildRequires:  fontconfig-devel
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  exiv2-devel libuuid-devel
Requires:       djvulibre

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract:
graphics, text layer, hyperlinks, document outline (bookmarks) and
metadata.

%prep
%autosetup

%build
export CXXFLAGS="-std=c++20 $RPM_OPT_FLAGS"
%configure
%make_build

%install
%make_install
install -p -m 644 -D {doc,%{buildroot}%{_mandir}/man1}/%{name}.1

%find_lang %{name}

%files -f %{name}.lang
%doc doc/changelog
%license doc/COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/de/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_mandir}/pl/man1/%{name}.1*
%{_mandir}/pt/man1/%{name}.1*
%{_mandir}/ru/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 Marek Kasik <mkasik@redhat.com> - 0.9.19-12
- Rebuild for poppler 24.08.0

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.19-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.19-9
- Rebuilt for exiv2 0.28.2

* Thu Feb 08 2024 Marek Kasik <mkasik@redhat.com> - 0.9.19-8
- Rebuild for poppler 24.02.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 07 2023 Marek Kasik <mkasik@redhat.com> - 0.9.19-5
- Rebuild for poppler 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Marek Kasik <mkasik@redhat.com> - 0.9.19-3
- Rebuild for poppler-23.02.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.19-1
- Updated to 0.9.19 fixes rhbz#2113575 and rhbz#2117084

* Mon Aug 08 2022 Marek Kasik <mkasik@redhat.com> - 0.9.18.2-5
- Rebuild for poppler-22.08.0
- Remove requirement of pstrams-devel as they are not supported
- and has been removed from Fedora
- Backport 2 commits from upstream to build with current poppler

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Marek Kasik <mkasik@redhat.com> - 0.9.18.2-2
- Rebuild for poppler-22.01.0
- Switch to C++17 because it is needed by poppler now

* Mon Nov 22 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.18.2-1
- Update to 0.9.18.2 fixes rhbz#2025677

* Mon Oct 18 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.18.1-1
- Update to 0.9.18.1 fixes rhbz#2013685

* Thu Oct 07 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.18-1
- Update to 0.9.18 fixes rhbz#1969290

* Thu Aug 05 2021 Marek Kasik <mkasik@redhat.com> - 0.9.17.1-5
- Rebuild for poppler-21.08.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Marek Kasik <mkasik@redhat.com> - 0.9.17.1-2
- Rebuild for poppler-21.01.0

* Fri Jan  1 2021 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.17.1-1
- Update to 0.9.17.1 fixes rhbz#1805167

* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 0.9.17-4
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Marek Kasik <mkasik@redhat.com> - 0.9.17-2
- Rebuild for poppler-0.90.0

* Sun Mar 15 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.17-1
- Update to 0.9.17 fixes rhbz#1805167

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.15-1
- Update to 0.9.15 fixes rhbz#1766275

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.13-1
- update to new 0.9.13 upstream release, fixes rhbz #1719015
- removed upstreamed patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.9.11-3
- rebuild (exiv2)

* Fri Jan 25 2019 Marek Kasik <mkasik@redhat.com> - 0.9.11-2
- Rebuild for poppler-0.73.0

* Sat Oct 27 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.11-1
- Rebuilt for new upstream release 0.9.11
- Upstream changelog https://github.com/jwilk/pdf2djvu/blob/master/doc/changelog

* Sun Sep 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.10-1
- Rebuilt for new upstream release 0.9.10, fixes rhbz #1609442

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 0.9.9-3
- Rebuild for poppler-0.67.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 21 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.9-1
- Rebuilt for new upstream release 0.9.9, fixes rhbz #1569280
- Remove upstreamed patches, spec cleanup

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 0.9.8-4
- Rebuild for poppler-0.63.0

* Wed Feb 14 2018 David Tardon <dtardon@redhat.com> - 0.9.8-3
- rebuild for poppler 0.62.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.8-1
- Rebuilt for new upstream release 0.9.8, fixes rhbz #1488273
- Remove upstreamed patches, spec cleanup
- Fix source URL

* Wed Nov 08 2017 David Tardon <dtardon@redhat.com> - 0.9.5-11
- rebuild for poppler 0.61.0

* Fri Oct 06 2017 David Tardon <dtardon@redhat.com> - 0.9.5-10
- rebuild for poppler 0.60.1

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 0.9.5-9
- rebuild for poppler 0.59.0

* Sat Aug 05 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.5-8
- Add patch to remove '-std=gnu++98', fixing build with new poppler
- Add %%license and %%doc
- Add BR: GraphicsMagick-c++-devel exiv2-devel libuuid-devel
- Adapt spec to recent guidelines

* Thu Aug 03 2017 David Tardon <dtardon@redhat.com> - 0.9.5-7
- rebuild for poppler 0.57.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 David Tardon <dtardon@redhat.com> - 0.9.5-4
- rebuild for poppler 0.53.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 0.9.5-2
- rebuild for poppler 0.50.0

* Thu Dec 15 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.5-1
- Rebuilt for new upstream release 0.9.5, fixes rhbz #1405026

* Thu Nov 24 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-6
- Rebuild for poppler 0.49.0

* Fri Oct 21 2016 Marek Kasik <mkasik@redhat.com> - 0.9.4-5
- Rebuild for poppler-0.48.0

* Mon Jul 18 2016 Marek Kasik <mkasik@redhat.com> - 0.9.4-4
- Rebuild for poppler-0.45.0

* Tue May 17 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.9.4-3
- Spec clean-up

* Tue May  3 2016 Marek Kasik <mkasik@redhat.com> - 0.9.4-2
- Rebuild for poppler-0.43.0

* Mon Mar 28 2016 François Cami <fcami@fedoraproject.org> - 0.9.4-1
- Update to latest upstream.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Marek Kasik <mkasik@redhat.com> - 0.7.21-3
- Rebuild for poppler-0.40.0

* Wed Jul 22 2015 Marek Kasik <mkasik@redhat.com> - 0.7.21-2
- Rebuild (poppler-0.34.0)

* Tue Jul 07 2015 François Cami <fcami@fedoraproject.org> - 0.7.21-1
- Update to latest upstream.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.17-9
- Rebuilt for GCC 5 C++11 ABI change

* Fri Jan 23 2015 Marek Kasik <mkasik@redhat.com> - 0.7.17-8
- Rebuild (poppler-0.30.0)

* Mon Jan 05 2015 François Cami <fcami@fedoraproject.org> - 0.7.17-7
- Fix changelog date + use PIC

* Thu Nov 27 2014 Marek Kasik <mkasik@redhat.com> - 0.7.17-6
- Rebuild (poppler-0.28.1)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Marek Kasik <mkasik@redhat.com> - 0.7.17-3
- Rebuild (poppler-0.26.0)

* Mon Aug 19 2013 Marek Kasik <mkasik@redhat.com> - 0.7.17-2
- Rebuild (poppler-0.24.0)

* Tue Aug 06 2013 François Cami <fcami@fedoraproject.org> - 0.7.17-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Marek Kasik <mkasik@redhat.com> - 0.7.16-2
- Rebuild (poppler-0.22.5)

* Wed May 22 2013 François Cami <fcami@fedoraproject.org> - 0.7.16-1
- Update to latest upstream.
- Drop throw-specifier.patch, annot-link.patch and pdf2djvu-0.7.4-poppler-0.20.0.patch

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Marek Kasik <mkasik@redhat.com> - 0.7.4-17
- Rebuild (poppler-0.22.0)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 0.7.4-15
- Fix building of pdf2djvu with poppler-0.20.x
- Resolves: #822407

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 0.7.4-14
- Rebuild (poppler-0.20.1)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-13
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.7.4-11
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.7.4-10
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.7.4-9
- Rebuild (poppler-0.17.3)

* Mon Aug  8 2011 Marek Kasik <mkasik@redhat.com> - 0.7.4-8
- Use AnnotLink instead of Link (poppler-0.17.0)
- Resolves: #698161

* Tue Mar 15 2011 Marek Kasik <mkasik@redhat.com> - 0.7.4-7
- Correct definition of derived class.

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.7.4-6
- Rebuild (poppler-0.16.3)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.7.4-4
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.7.4-3
- rebuild (poppler)

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.7.4-2
- rebuilt (poppler)

* Wed Oct  6 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7.4-1
- update to 0.7.4

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.7.3-4
- rebuild (poppler)

* Tue May 25 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.7.3-1
- Patch removed (in upstream now)

* Wed May 05 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.7.2-3
- Fixed pdf-backend.cc error (pdf2djvu-0.7.2-pdf_backend_cc.patch)

* Wed May 05 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.7.2-2
- Bump for new libpoppler.so.6

* Mon May 03 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.7.2-1
- Updated to 0.7.2

* Sat Jan 30 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.6.2-1
- Updated to 0.6.2

* Tue Aug 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.5.11-1
- Updated to 0.5.11

* Mon Aug 03 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.5.0-5
- Fixed the missing djvulibre require #500306

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.5.0-3
- Fix FTBFS: added BR: djvulibre, fontconfig-devel.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Rakesh Pandit <rakesh@fedoraproject.org> 0.5.0-1
- Updated to 0.5.0

* Mon Nov 10 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.4.13-3
- Cleaned useless permissions in %%files section

* Sat Nov 08 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.4.13-2
- Saving timestamp, fixed buildrequires, corrected license and did some cleaning.

* Tue Nov 04 2008 Rakesh Pandit <rakesh@fedoraproject.org> 0.4.13-1
- Initial package.
