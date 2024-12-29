Name:           ocaml-gsl
Version:        1.25.1
Release:        1%{?dist}
Summary:        Interface to GSL (GNU scientific library) for OCaml
License:        GPL-3.0-or-later

# "Architectures with double-word alignment for doubles are not supported"
# Specifically you should look at this file:
# %%{_libdir}/ocaml/caml/config.h
# and if it has '#define ARCH_ALIGN_DOUBLE' then it is not supported,
# but if it has '#undef ARCH_ALIGN_DOUBLE' then it is OK.
#
# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{arm} %{ix86}

URL:            https://github.com/mmottl/gsl-ocaml
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/gsl-%{version}.tbz

BuildRequires:  ocaml >= 4.12
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gsl) >= 2.0


%description
This is an interface to GSL (GNU scientific library), for the
Objective Caml language.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gsl-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n gsl-%{version} -p1


%build
export GSL_CBLAS_LIB="-lflexiblas"
%dune_build


%install
export GSL_CBLAS_LIB="-lflexiblas"
%dune_install


%check
export GSL_CBLAS_LIB="-lflexiblas"
%dune_check


%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md


%files devel -f .ofiles-devel
%doc examples
%license LICENSE.md


%changelog
* Sat Dec 21 2024 Jerry James <loganjerry@gmail.com> - 1.25.1-1
- Version 1.52.1
- Drop upstreamed patch to link with flexiblas after gsl
- Add VCS field

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.25.0-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.25.0-2
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 1.25.0-1
- Version 1.25.0
- Drop all patches
- Add patch to link with flexiblas after gsl

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.24.3-7
- Bump release and rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.24.3-6
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.24.3-5
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.24.3-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.24.3-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.24.3-1
- Version 1.24.3
- Convert License tag to SPDX
- Drop upstreamed patches
- Add upstream post-release bug fix patches
- Apply upstream PR for OCaml 5.0 compatibility
- Build with dune

* Sun Apr 16 2023 Florian Weimer <fweimer@redhat.com> - 1.19.1-47
- Apply upstream patch to fix C99 compatibility issues

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-46
- Bump release and rebuild.

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-45
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.19.1-43
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-41
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-40
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-38
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 17:15:52 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-36
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-34
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-33
- OCaml 4.11.0 rebuild

* Fri Aug 14 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.19.1-32
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-30
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-29
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-28
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-27
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-26
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-24
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-23
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-22
- OCaml 4.09.0 (final) rebuild.

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.19.1-21
- Rebuilt for GSL 2.6.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-20
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-19
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-16
- Use OpenBLAS on %%{openblas_arches} (RHBZ#1619050).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-14
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-13
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-11
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-10
- OCaml 4.05.0 rebuild.
- Use ocaml_native_compiler macro instead of opt test.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 1.19.1-7
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-6
- Rebuild for new gsl 2.4 (thanks: Arthur Mello).

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-5
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.19.1-2
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.19.1-1
- New upstream version 1.19.1.
- Add explicit dependency on ocamlbuild.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.19.0-3
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.19.0-1
- Update to 1.19.0 for gsl 2

* Wed Jul 29 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.4-1
- New upstream version 1.18.4.
- Exclude armv7hl because it uses double-word alignment for doubles.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.2-7
- OCaml 4.02.3 rebuild.

* Mon Jul 27 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.2-6
- Remove ExcludeArch since bytecode build should now work.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.2-5
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.2-4
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.2-2
- Link against ATLAS for improved performance.
  https://lists.fedoraproject.org/pipermail/devel/2015-February/thread.html#208146

* Sun Feb 22 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.2-1
- New upstream version 1.18.2.
- Remove the patch, now upstream.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.18.1-1
- New upstream version 1.18.1.
- Include a fix for use of uint32, sent upstream.
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-7
- Bump release and rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-6
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-5
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-3
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-2
- Bump release and rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.17.2-1
- New upstream version 1.17.2.
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.13.0-1
- New upstream version 1.13.0.
- Switched to Markus Mottl semi-official upstream version which is
  much livelier than the official upstream.
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Info files disappeared from upstream source, probably for the better.
- Missing BR ocamldoc.
- Missing BR ocaml-camlp4-devel.

* Sun Aug  4 2013 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-19
- Exclude armv7hl (not supported by upstream C code).
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 0.6.0-16
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-14
- Rebuild for OCaml 4.00.0.

* Sat Jan 07 2012 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-13
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-11
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-10
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-8
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-6
- Force rebuild.

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-5
- Rebuild.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-4
- Rebuild for OCaml 3.11.0

* Fri Apr 25 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-3
- Fixed typo in description.
- Mixed use of buildroot macro / RPM_BUILD_ROOT variable fixed.
- Remove BR gsl (brought in by gsl-devel, so unnecessary).

* Tue Mar  4 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-2
- Rebuild for ppc64.

* Wed Feb 20 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6.0-1
- Initial RPM release.
