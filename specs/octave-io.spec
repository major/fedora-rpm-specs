%global octpkg io

Name:           octave-%{octpkg}
Version:        2.6.4
Release:        13%{?dist}
Summary:        Input/Output in external formats
# Automatically converted from old format: GPLv3+ and BSD - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            http://octave.sourceforge.net/%{octpkg}/
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel >= 6:4.0
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
Input/Output in external formats.

%prep
%setup -qcT

%build
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
%{octpkgdir}/*.m
%{octpkgdir}/PKG_ADD
%{octpkgdir}/PKG_DEL
%doc %{octpkgdir}/doc/
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%{octpkgdir}/private/
%{octpkgdir}/templates/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 2.6.4-12
- Rebuild for octave 9.2

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.4-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 2.6.4-6
- Rebuild with octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.6.4-3
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Orion Poplawski <orion@nwra.com> - 2.6.4-1
- Update to 2.6.4

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.6.3-4
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Orion Poplawski <orion@nwra.com> - 2.6.3-1
- Update to 2.6.3

* Mon Oct 12 2020 Orion Poplawski <orion@nwra.com> - 2.6.2-1
- Update to 2.6.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Orion Poplawski <orion@nwra.com> - 2.6.1-1
- Update to 2.6.1

* Tue Mar 24 2020 Orion Poplawski <orion@nwra.com> - 2.6.0-1
- Update to 2.6.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov  6 2019 Orion Poplawski <orion@nwra.com> - 2.4.13-2
- Rebuild with octave 64bit indexes

* Fri Oct 18 2019 Orion Poplawski <orion@cora.nwra.com> - 2.4.13-1
- Update to 2.4.13

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 2.4.12-3
- Rebuild for octave 5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.12-1
- Update to 2.4.12
- Drop patch applied upstream

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.11-3
- Rebuild for octave 4.4

* Mon Jul 23 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.11-2
- Add patch to fix string access in csv2cell

* Mon Jul 23 2018 Orion Poplawski <orion@cora.nwra.com> - 2.4.11-1
- Update to 2.4.11

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Orion Poplawski <orion@cora.nwra.com> - 2.4.7-1
- Update to 2.4.7

* Tue Mar 7 2017 Orion Poplawski <orion@cora.nwra.com> - 2.4.6-1
- Update to 2.4.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.5-2
- Rebuild for octave 4.2

* Wed Nov 9 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.5-1
- Update to 2.4.5

* Thu Sep 15 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-1
- Update to 2.4.3

* Fri Jul 8 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-1
- Update to 2.4.2

* Mon Mar 14 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.1-1
- Update to 2.4.1

* Thu Feb 4 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-1
- Update to 2.4.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.10-1
- Update to 2.2.10
- Add %%check

* Mon Jul 6 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.8-1
- Update to 2.2.8

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.7-1
- Update to 2.2.7

* Sun Jan 4 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.6-1
- Update to 2.2.6

* Tue Nov 25 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.5-1
- Update to 2.2.5

* Sun Nov 2 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.4-1
- Update to 2.2.4

* Wed Aug 20 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.3-1
- Update to 2.2.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.2-1
- Update to 2.2.2

* Sat Apr 26 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-1
- Update to 2.2.1

* Sat Apr 19 2014 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-1
- Update to 2.2.0

* Tue Apr 15 2014 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-1
- initial package for Fedora
