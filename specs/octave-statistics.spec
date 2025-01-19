%global octpkg statistics

Name:           octave-%{octpkg}
Version:        1.6.7
Release:        4%{?dist}
Summary:        Additional statistics functions for Octave
License:        GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/gnu-octave/%{octpkg}
Source0:        https://github.com/gnu-octave/%{octpkg}/archive/refs/tags/release-%{version}/%{octpkg}-%{version}.tar.gz

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
%doc %{octpkgdir}/doc/
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%{octpkgdir}/*.m
%{octpkgdir}/@cvpartition/
%{octpkgdir}/Classification/
%{octpkgdir}/Clustering/
%{octpkgdir}/datasets/
%{octpkgdir}/dist_fit/
%{octpkgdir}/dist_fun/
%{octpkgdir}/dist_obj/
%{octpkgdir}/dist_stat/
%{octpkgdir}/dist_wrap/
%{octpkgdir}/private/*.m
%{octpkgdir}/packinfo/
%{octpkgdir}/Regression/
%{octpkgdir}/shadow9/
%{octpkglibdir}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 1.6.7-3
- Rebuild for octave 9.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Orion Poplawski <orion@nwra.com> - 1.6.7-1
- Update to 1.6.7

* Fri May 17 2024 Orion Poplawski <orion@nwra.com> - 1.6.6-1
- Update to 1.6.6

* Sat Mar 09 2024 Orion Poplawski <orion@nwra.com> - 1.6.5-1
- Update to 1.6.5

* Sat Mar 02 2024 Orion Poplawski <orion@nwra.com> - 1.6.4-1
- Update to 1.6.4

* Fri Feb 09 2024 Orion Poplawski <orion@nwra.com> - 1.6.3-1
- Update to 1.6.3

* Wed Feb 07 2024 Orion Poplawski <orion@nwra.com> - 1.6.2-1
- Update to 1.6.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 13 2024 Orion Poplawski <orion@nwra.com> - 1.6.1-1
- Update to 1.6.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Orion Poplawski <orion@nwra.com> - 1.6.0-1
- Update to 1.6.0
- SPDX License

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 1.5.4-2
- Rebuild with octave 8.1.0

* Mon Mar 20 2023 Orion Poplawski <orion@nwra.com> - 1.5.4-1
- Update to 1.5.4

* Thu Feb 02 2023 Orion Poplawski <orion@nwra.com> - 1.5.3-1
- Update to 1.5.3

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Orion Poplawski <orion@nwra.com> - 1.5.2-1
- Update to 1.5.2

* Wed Dec 07 2022 Orion Poplawski <orion@nwra.com> - 1.5.1-1
- Update to 1.5.1

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
