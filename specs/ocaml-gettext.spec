# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Optionally disable camomile dep on RHEL.
%if !0%{?rhel}
%bcond_without camomile
%bcond_without tests
%else
%bcond_with    camomile
%bcond_with    tests
%endif

Name:           ocaml-gettext
Version:        0.5.0
Release:        5%{?dist}
Summary:        OCaml library for i18n

License:        LGPL-2.1-or-later with OCaml-LGPL-linking-exception
URL:            https://github.com/gildor478/ocaml-gettext
VCS:            git:%{url}.git

Source0:        %{url}/archive/v%{version}.tar.gz

# Fix to stop using dune-site
# https://github.com/gildor478/ocaml-gettext/issues/36
# https://github.com/gildor478/ocaml-gettext/pull/37
Patch:          https://github.com/gildor478/ocaml-gettext/pull/37.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-fileutils-devel >= 0.6.6-1
BuildRequires:  ocaml-dune >= 1.11.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-cppo
# This was orphaned and dropped from Fedora back in 2023, but may be
# needed to run the tests.
# https://github.com/gildor478/ocaml-gettext/issues/35
#BuildRequires: ocaml-seq-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  libxml2
%if %{with tests}
BuildRequires:  ocaml-ounit-devel
%endif
%if %{with camomile}
BuildRequires:  ocaml-camomile-devel >= 0.8.6-3
BuildRequires:  ocaml-camomile-data
%endif

%if %{with camomile}
# ocaml-gettext program needs camomile data files
Requires:       ocaml-camomile-data
%endif


%description
Ocaml-gettext provides support for internationalization of Ocaml
programs.

Constraints :

* provides a pure Ocaml implementation,
* the API should be as close as possible to GNU gettext,
* provides a way to automatically extract translatable
  strings from Ocaml source code.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-fileutils-devel%{?_isa} >= 0.6.6


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%if %{with camomile}
%package        camomile
Summary:        Parts of %{name} which depend on Camomile
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    camomile
The %{name}-camomile package contains the parts of %{name} which
depend on Camomile.


%package        camomile-devel
Summary:        Development files for %{name}-camomile
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-camomile%{?_isa} = %{version}-%{release}
Requires:       ocaml-camomile-devel%{?_isa}


%description    camomile-devel
The %{name}-camomile-devel package contains libraries and
signature files for developing applications that use
%{name}-camomile.
%endif


%prep
%autosetup -p1

# Remove ocaml-seq dependency.  See note above.
sed -i 's/ seq / /' test/dune

%if %{without camomile}
# Remove dependency on camomile.
rm -f gettext-camomile.opam
rm -r src/lib/gettext-camomile
rm -r test/test-camomile
sed -i -e 's/camomile//' `find -name dune`
awk -i inplace -v RS='^\\(package' -v ORS= \
     '{while(sub(/\(package\n *\(name gettext-camomile\).*\)\)\)\)/,""));} {print}' dune-project
%endif


%build
%dune_build


%install
%dune_install -s
sed -i '\@%{_bindir}@d;\@%{_mandir}@d' .ofiles-gettext
cat .ofiles-gettext-stub >> .ofiles-gettext
cat .ofiles-gettext-stub-devel >> .ofiles-gettext-devel


%if %{with tests}
%check
%dune_check
%endif


%files -f .ofiles-gettext
%license LICENSE.txt


%files devel -f .ofiles-gettext-devel
%doc README.md CHANGES.md THANKS TODO.md
%{_bindir}/ocaml-gettext
%{_bindir}/ocaml-xgettext
%{_mandir}/man1/ocaml-gettext.1*
%{_mandir}/man1/ocaml-xgettext.1*
%{_mandir}/man5/ocaml-gettext.5*


%if %{with camomile}
%files camomile -f .ofiles-gettext-camomile
%license LICENSE.txt


%files camomile-devel -f .ofiles-gettext-camomile-devel
%doc README.md
%endif


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jul 12 2025 Jerry James  <loganjerry@gmail.com> - 0.5.0-4
- Rebuild to fix OCaml dependencies

* Thu Apr 03 2025 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-3
- Remove use of dune-site

* Thu Feb 27 2025 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-2
- Add dependency from devel to ocaml-dune-site-devel.
  https://src.fedoraproject.org/rpms/ocaml-gettext/pull-request/3#comment-249424

* Wed Feb 26 2025 Richard W.M. Jones <rjones@redhat.com> - 0.5.0-1
- New version 0.5.0
- New dependency ocaml-dune-site-devel (copied from opam).
- Remove upstream patches.

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 0.4.2-23
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-21
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-20
- OCaml 5.2.0 for Fedora 41

* Wed May  8 2024 Jerry James <loganjerry@gmail.com> - 0.4.2-19
- Add patch to fix tests with OCaml 5.2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-17
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-16
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-15
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-13
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.4.2-12
- OCaml 5.0.0 rebuild
- Convert License tag to SPDX
- Enable tests
- Use new dune macros

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-11
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-8
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-7
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-5
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-3
- Bump and rebuild for ELN.

* Mon Mar  8 23:22:35 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-2
- Better handling of optional camomile subpackage.

* Tue Mar  2 23:22:35 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.2-1
- New upstream version 4.2
- Remove patch now upstream.
- BR ocaml-cppo

* Mon Mar  1 23:22:35 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.1-9
- OCaml 4.12.0 build

* Wed Feb 24 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.1-8
- Remove ocaml-camomile dep on RHEL 9.

* Mon Feb  1 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.1-7
- Bump and rebuild for updated ocaml-camomile.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.1-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.1-4
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.1-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.4.1-1
- New upstream version 0.4.1.
- Add small fix for OCaml 4.11.
- Package the man pages.

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.3.8-0.7.git3aecf8e5350f
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.3.8-0.6.git3aecf8e5350f
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 0.3.8-0.5.git3aecf8e5350f
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-0.4.git3aecf8e5350f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.3.8-0.3.git3aecf8e5350f
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.3.8-0.2.git3aecf8e5350f
- OCaml 4.09.0 (final) rebuild.

* Tue Oct  1 2019 Richard W.M. Jones <rjones@redhat.com> - 0.3.8-0.1
- Move to pre-release of 0.3.8.
- Requires dune.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-13
- Bump release and rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-12
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-11
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-9
- Remove camlp4 dependency.
- Add all upstream patches since 0.3.7.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-5
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-4
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-2
- OCaml 4.06.0 rebuild.
- Add fix for immutable strings.

* Sat Sep 23 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.7-1
- Update to new upstream version 0.3.7.
- New URL.
- Include upstream patches since 0.3.7 was released.

* Wed Aug 30 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-18
- Subpackage ocaml-gettext-camomile-devel should depend on
  ocaml-gettext-camomile (thanks: Pino Toscano).

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-17
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-14
- Bump release and rebuild.

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-13
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-12
- Bump release and rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-11
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-9
- Disable a warning produced with OCaml 4.04.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-7
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-6
- Enable bytecode builds.
- Disable the tests on bytecode-only platforms.

* Tue Jun 23 2015 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-5
- Bump release and rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-4
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-3
- Bump release and rebuild.
- Drop upstream patch.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 0.3.5-1
- New upstream version 0.3.5.
- ocaml-4.02.1 rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-18
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-17
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-15
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-14
- OCaml 4.02.0 beta rebuild.

* Tue Jul 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-13
- Rebuild for OCaml 4.02.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-11
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-8
- BR >= OCaml 4.00.1 so we can't be built against the wrong OCaml.

* Fri Oct 19 2012 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-7
- Rebuild for OCaml 4.00.1.
- Remove Group lines from the spec file.

* Tue Sep 25 2012 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-6
- (RHEL only) Disable camomile, ocaml-ounit, tests.
- Modernize the spec file.

* Sat Jul 28 2012 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-5
- Bump and rebuild against new OCaml 4.00.0 official release.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-3
- Rebuild for OCaml 4.00.0.

* Sat May 19 2012 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-2
- Bump release and rebuild for new OCaml on ARM.
- Enable ppc64 support for camomile.

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 0.3.4-1
- New upstream version 0.3.4.
- Remove patch, now upstream.

* Wed Dec 21 2011 Karsten Hopp <karsten@redhat.com> 0.3.3-8
- fix configure line

* Wed Dec 21 2011 Karsten Hopp <karsten@redhat.com> 0.3.3-7
- build with 'make all', not 'make' as that defaults to 'make test' and fails on ppc64
  due to the missing gettext-camomile

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 0.3.3-5
- Add patch for compiling against camomile 0.8.

* Wed Jan 05 2011 Richard W.M. Jones <rjones@redhat.com> - 0.3.3-4
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Mon Jan 11 2010 Richard W.M. Jones <rjones@redhat.com> - 0.3.3-3
- Remove BR ocaml-camlidl.  No longer required to build this.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.3.3-2
- Rebuild for OCaml 3.11.2.

* Mon Nov  2 2009 Richard W.M. Jones <rjones@redhat.com> - 0.3.3-1
- New upstream release 0.3.3 (mainly small bugfixes).
- This requires ocaml-fileutils 0.4.0 and is incompatible with
  any earlier version.
- Fixed a number of rpmlint warnings with *.ml files in the
  non-devel package.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.3.2-8
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.2-6
- Patch to temporarily fix missing dynlink.cma.
- Rebuild for OCaml 3.11.0.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.2-5
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.2-4
- Rebuild for OCaml 3.11.0

* Mon Jun  9 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.2-2
- Need to disable tests on ppc64 as well since the tests only work
  with gettext-camomile.

* Mon Jun  9 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.2-1
- New upstream release 0.3.2 (fixeds rhbz 446916).

* Tue May 27 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.1-3
- Enable tests, add check section.

* Tue May 27 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.1-2
- Patch to fix BZ 446916.

* Tue May 27 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.1-1
- New upstream version 0.3.1.
- Extra runtime requirements (BZ 446919).

* Wed Apr 30 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-1
- New upstream version 0.3.0.
- Big patch no longer required (integrated with upstream).
- findlib < 1.2.1-3 known not to work with this.
- build/ -> _build/
- Re-enable documentation.
- Prevent *.o files from being distributed.
- Distribute *.cmx and *.mli files.

* Sat Apr 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.2.0-3.20080321patch
- Change the naming scheme to conform with "Snapshot packages" guideline.
- Don't duplicate all the docs in camomile-devel.
- Disable documentation.  Wants 'fop', but 'fop' throws a giant Java
  exception when present.

* Thu Apr 17 2008 Richard W.M. Jones <rjones@redhat.com> - 0.2.0-2rwmj20080321
- Build camomile subpackages because the camomile dependency is
  rather large.  However we can't build camomile on ppc64 yet so
  don't build those subpackages there.

* Fri Mar 21 2008 Richard W.M. Jones <rjones@redhat.com> - 0.2.0-1rwmj20080321
- Initial RPM release.
