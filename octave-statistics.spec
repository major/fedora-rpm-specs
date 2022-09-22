%global octpkg statistics

Name:           octave-%{octpkg}
Version:        1.4.3
Release:        4%{?dist}
Summary:        Additional statistics functions for Octave
License:        GPLv3+ and Public Domain
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel
BuildRequires:  octave-io
Requires:       octave(api) = %{octave_api}
Requires:       octave-io
Requires(post): octave
Requires(postun): octave

# Built out of boulddir
%undefine _debugsource_packages

%description
Additional statistics functions for Octave.


%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install
chmod a-x %{buildroot}/%{octpkgdir}/*.m

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%{octpkgdir}/*.m
%{octpkgdir}/carbig.mat
%{octpkgdir}/fisheriris.mat
%{octpkgdir}/@cvpartition/
%{octpkgdir}/base/
%{octpkgdir}/distributions/
%{octpkgdir}/fisheriris.txt
%{octpkgdir}/models/
%{octpkgdir}/private/*.m
%{octpkgdir}/packinfo/
%{octpkgdir}/test/
%{octpkgdir}/tests/
%{_metainfodir}/octave-%{octpkg}.metainfo.xml


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 1.4.3-3
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Orion Poplawski <orion@nwra.com> - 1.4.3-1
- Update to 1.4.3

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 1.4.2-3
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Orion Poplawski <orion@nwra.com> - 1.4.2-1
- Update to 1.4.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 1.4.1-4
- Rebuild with octave 64bit indexes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 1.4.1-2
- Rebuild for octave 5.1

* Sat Apr 13 2019 Orion Poplawski <orion@nwra.com> - 1.4.1-1
- Update to 1.4.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-2
- Rebuild for octave 4.4

* Mon Jul 23 2018 Orion Poplawski <orion@nwra.com> - 1.4.0-1
- Update to 1.4.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Orion Poplawski <orion@nwra.com> - 1.3.0-5
- Rebuild to ship metainfo.xml so this package will appear in Software (bug #1480103)
- Add %%check

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-2
- Rebuild for octave 4.2.0

* Tue Oct 11 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-1
- Update to 1.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.2.4-1
- Update to 1.2.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0.6-1
- Initial package for Fedora
