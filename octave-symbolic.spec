%global octpkg symbolic

# Disable automatic compilation of Python files in extra directories
%global _python_bytecompile_extra 0

Name:           octave-%{octpkg}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Symbolic computations for Octave
License:        GPLv3+
URL:            https://octave.sourceforge.io/%{octpkg}
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  octave-devel
BuildRequires:  octave-doctest >= 0.7.0
BuildRequires:  python3
BuildRequires:  python%{python3_pkgversion}-sympy >= 1.4

Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave
Requires:       python%{python3_pkgversion}-sympy >= 1.4


%description
Adds symbolic calculation features to GNU Octave.
These include common Computer Algebra System tools such as algebraic
operations, calculus, equation solving, Fourier and Laplace transforms,
variable precision arithmetic and other features.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check

# "octave_pkg_check" macro uses "runtests" which doesn't test classes
pushd %{buildroot}/%{octpkgdir}
%octave_cmd r=octsympy_tests; if r, type fntests.log; end; exit(r)
rm -f fntests.log
# mfile encoding: see https://github.com/cbm755/octsympy/issues/1191
%octave_cmd pkg load doctest; __mfile_encoding__("utf-8"); syms x; r=doctest("."); exit(~r)
popd

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/*.m
%{octpkgdir}/*.tst
%{octpkgdir}/@logical
%{octpkgdir}/private
%{octpkgdir}/@sym
%{octpkgdir}/@symfun
%{octpkgdir}/@double
%dir %{octpkgdir}/packinfo
%license %{octpkgdir}/packinfo/COPYING
%doc %{octpkgdir}/packinfo/NEWS
%{octpkgdir}/packinfo/DESCRIPTION
%{octpkgdir}/packinfo/INDEX
%{octpkgdir}/packinfo/*.m
%{_metainfodir}/octave-%{octpkg}.metainfo.xml


%changelog
* Thu Aug 11 2022 Colin B. Macdonald <cbm@m.fsf.org> - 3.0.1-1
- new version

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Colin B. Macdonald <cbm@m.fsf.org> - 3.0.0-2
- Workaround encoding troubles when running doctests

* Wed Jul 06 2022 Colin B. Macdonald <cbm@m.fsf.org> - 3.0.0-1
- Update to 3.0.0 (bugz#2104613)

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.9.0-9
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.9.0-7
- Rebuild for octave 6.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 José Matos <jamatos@fedoraproject.org> - 2.9.0-4
- Add patch to work with sympy 1.6
- Tests are disabled for now (all the failures have already been reported)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Colin B. Macdonald <cbm@m.fsf.org> - 2.9.0-1
- Update to 2.9.0 (bugz#1797854)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Colin B. Macdonald <cbm@m.fsf.org> - 2.8.0-4
- Upstream patch for doctest failurs on Python 3.8 (bugz#1772304)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Colin B. Macdonald <cbm@m.fsf.org> - 2.8.0-2
- Fix test log file name and minimum deps

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 2.8.0-1
- Update to 2.8.0

* Sun Apr 28 2019 Orion Poplawski <orion@nwra.com> - 2.7.1-5
- Increate tolerance on failing test (bugz#1703856)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Orion Poplawski <orion@cora.nwra.com> - 2.7.1-3
- Add patch to avoid test failure on some arches

* Wed Nov 14 2018 Orion Poplawski <orion@cora.nwra.com> - 2.7.1-2
- Rebuild for octave 4.4

* Wed Oct 03 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2.7.1-1
- Version bump.

* Fri Jul 27 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2.7.0-1
- Version bump (#1609268)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2.6.0-7
- Call "python3" instead of "python", depend on python3
  (https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)
- Don't bytecompile our small .py helper
  (https://fedoraproject.org/wiki/Packaging:Python_Appendix#Manual_byte_compilation)

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.6.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.6.0-4
- Drop BR for libappstream-glib, now provided by octave-devel

* Sun Aug 13 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.6.0-3
- Let new macros deal with metainfo.xml

* Thu Aug 10 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.6.0-2
- Own packinfo dir for clean uninstall

* Fri Jul 28 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.6.0-1
- Version bump.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 03 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2.5.0-1
- Version bump.

* Sun Dec 11 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.4.0-3
- Minor upstream patch for failing doctest
- Patch for tests to pass on i686 arch

* Sun Dec 11 2016 cbm - 2.4.0-2
- Remove src subdir, remove bat file in prep
- Do not use -T for now

* Wed May 25 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.4.0-1
- Update to 2.4.0
- More testing

* Mon Apr 11 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.3.0-2
- Update to 2.3.0 (#1325897)
- Fix broken checks

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2.2.4-3
- Use current id in metainfo: www.octave.org-octave.desktop

* Sun Dec 27 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.2.4-2
- Run tests

* Sun Dec 27 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.2.4-1
- Update to 2.2.4, add metainfo.xml

* Sat Nov 28 2015 Colin B. Macdonald <cbm@m.fsf.org> - 2.2.3-1
- Update to 2.2.3

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.2-1
- Update to 2.2.2
- Add BR sympy

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.0.0-1
- update to 1.1.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 06 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-8
- rebuild for ginac

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 29 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-6
- Rebuild for octave 3.8.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.1.0-1
- update to 1.1.0

* Sat Aug 06 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.9-3
- Bump spec due to change of octave api version.

* Wed Jun 15 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.9-2
- Review input

* Fri Jun 03 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.0.9-1
- initial package for Fedora
