%global octpkg image

Name:           octave-%{octpkg}
Version:        2.14.0
Release:        13%{?dist}
Summary:        Image processing for Octave
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://octave.sourceforge.net/image/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 6:4.0.0

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave


%description
The Octave-forge Image package provides functions for processing images.
The package also provides functions for feature extraction, image
statistics, spatial and geometric transformations, morphological
operations, linear filtering, and much more.

%prep
%setup -qcT

%build
#export CXXFLAGS="%{optflags} -fPIC"
export XTRA_CXXFLAGS="-fPIC"
%octave_pkg_build -T

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%{octpkglibdir}
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/packinfo
%{octpkgdir}/private/
%{octpkgdir}/@imref2d/
%{octpkgdir}/@imref3d/
%{octpkgdir}/@strel/
%{_metainfodir}/octave-%{octpkg}.metainfo.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 2.14.0-12
- Rebuild for octave 9.2

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.14.0-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 2.14.0-6
- Rebuild with octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 01 2022 Orion Poplawski <orion@nwra.com> - 2.14.0-4
- Use XTRA_CXXFLAGS to set -fPIC
- Drop EL6 conditional

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.14.0-2
- Rebuild for octave 7.1

* Sat Mar 26 2022 Orion Poplawski <orion@nwra.com> - 2.14.0-1
- Update to 2.14.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.12.0-4
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Orion Poplawski <orion@nwra.com> - 2.12.0-1
- Update to 2.12.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 2.10.0-2
- Rebuild with octave 64bit indexes

* Thu Sep 26 2019 Orion Poplawski <orion@cora.nwra.com> - 2.10.0-1
- Update to 2.10.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 2.8.1-3
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Orion Poplawski <orion@cora.nwra.com> - 2.8.1-1
- Update to 2.8.1

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 2.8.0-1
- Update to 2.8.0
- Rebuild for octave 4.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.6.2-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Orion Poplawski <orion@nwra.com> - 2.6.2-1
- Update to 2.6.2

* Tue Aug 15 2017 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-6
- Rebuild to ship metainfo.xml so this package will appear in Software

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-2
- Rebuild for octave 4.2

* Tue Oct 25 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-1
- Update to 2.6.1

* Wed Oct 5 2016 Orion Poplawski <orion@cora.nwra.com> - 2.6.0-1
- Update to 2.6.0

* Thu Feb 4 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.1-1
- Update to 2.4.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-3
- Set compile flags

* Fri Jul 31 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-2
- Run tests

* Mon Jul 6 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-1
- Update to 2.4.0
- Add patch to workaround gcc issue

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Oct 6 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.2-1
- Update to 2.2.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-1
- Update to 2.2.1

* Wed Jan 8 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-1
- Update to 2.2.0

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-4
- Rebuild for octave 3.8.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 8 2012 Orion Poplawski <orion@cora.nwra.com> 2.0.0-1
- Update to 2.0.0
- Add requires octave-signal >= 1.2.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Orion Poplawski <orion@cora.nwra.com> 1.0.15-3
- Rebuild for octave 3.6.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Orion Poplawski <orion@cora.nwra.com> 1.0.15-1
- Update to 1.0.15

* Mon Aug 8 2011 Orion Poplawski <orion@cora.nwra.com> 1.0.14-2
- Rebuild for octave 3.4.2

* Tue Apr 12 2011 Orion Poplawski <orion@cora.nwra.com> 1.0.14-1
- Update to 1.0.14

* Fri Apr 8 2011 Orion Poplawski <orion@cora.nwra.com> 1.0.13-2
- Fix permissions on source file

* Tue Apr 05 2011 Orion Poplawski <orion@cora.nwra.com> 1.0.13-1
- initial package for Fedora
