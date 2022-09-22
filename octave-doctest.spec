%global octpkg doctest

Name:           octave-%{octpkg}
Version:        0.7.0
Release:        13%{?dist}
Summary:        Documentation tests for Octave
License:        BSD
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  octave-devel
BuildRequires:  texinfo >= 6.0

Requires:       octave(api) = %{octave_api}
Requires:       texinfo >= 6.0
Requires(post): octave
Requires(postun): octave


%description
The Octave-forge Doctest package finds specially-formatted blocks of
example code within documentation files.  It then executes the code
and confirms the output is correct.  This can be useful as part of a
testing framework or simply to ensure that documentation stays
up-to-date during software development.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_pkg_build

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
%dir %{octpkgdir}
%{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/private
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%doc %{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/*.m
%{_metainfodir}/octave-%{octpkg}.metainfo.xml


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 0.7.0-12
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 0.7.0-10
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Orion Poplawski <orion@nwra.com> - 0.7.0-7
- Remove attempts to run upstream tests that fail due to tests not being shipped

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 0.7.0-3
- Rebuild for octave 5.1

* Fri Apr 19 2019 Colin B. Macdonald <cbm@m.fsf.org> - 0.7.0-2
- Run additional tests

* Thu Apr 18 2019 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Update to 0.7.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 0.6.1-4
- Rebuild for octave 4.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Colin B. Macdonald <cbm@m.fsf.org> - 0.6.1-1
- Version bump (bug #1529816)

* Sun Dec 31 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.6.0-1
- Version bump (bug #1529816)

* Mon Aug 14 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.5.0-8
- Drop BR for libappstream-glib, now provided by octave-devel

* Sun Aug 13 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.5.0-7
- Let the new macros deal with metainfo.xml file
- mark packinfo as dir to avoid listing twice
- mark NEWS as a doc
- use octave_pkg_check (currently does nothing, no harm)

* Thu Aug 10 2017 Colin B. Macdonald <cbm@m.fsf.org> - 0.5.0-6
- Validate metainfo.xml
- Own packinfo dir for clean uninstall

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Colin B. Macdonald <cbm@m.fsf.org> - 0.5.0-3
- Remove compiled code, not needed on Octave 4.2

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 0.5.0-2
- Rebuild for octave 4.2

* Tue Nov 15 2016 Colin B. Macdonald <cbm@m.fsf.org> - 0.5.0-1
- Version bump (bug #1394768)

* Wed Feb 03 2016 Colin B. Macdonald <cbm@m.fsf.org> - 0.4.1-3
- Address reviewer comments
- Add BR binutils, add __provides_exclude, drop metainfo validate
- Update patch status

* Wed Jan 20 2016 Colin B. Macdonald <cbm@m.fsf.org> - 0.4.1-2
- Fix for arm arch
- List texinfo dep (although octave already should pull it in)

* Tue Jan 19 2016 Colin B. Macdonald <cbm@m.fsf.org> - 0.4.1-1
- Version bump, enable tests
- Fix incorrect license

* Fri Jul 03 2015 Colin B. Macdonald <cbm@m.fsf.org> - 0.4.0-1
- initial package for Fedora
