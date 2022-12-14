%undefine _package_note_flags

Name:           ocaml-bin-prot
Version:        0.15.0
Epoch:          1
Release:        8%{?dist}
Summary:        Read and write OCaml values in a type-safe binary protocol

# The project as a whole is MIT.
# Code in the src subdirectory is BSD-3-Clause.
License:        MIT AND BSD-3-Clause
URL:            https://github.com/janestreet/bin_prot
Source0:        %{url}/archive/v%{version}/bin_prot-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-base-devel >= 0.15
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-ppx-compare-devel >= 0.15
BuildRequires:  ocaml-ppx-custom-printf-devel >= 0.15
BuildRequires:  ocaml-ppx-fields-conv-devel >= 0.15
BuildRequires:  ocaml-ppx-optcomp-devel >= 0.15
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.15
BuildRequires:  ocaml-ppx-variants-conv-devel >= 0.15

%description
This library contains functionality for reading and writing OCaml
values in a type-safe binary protocol. These functions are extremely
efficient and provide users with a convenient and safe way of
performing I/O on any extensionally defined data type. This means that
functions, objects, and values whose type is bound through a
polymorphic record field are not supported, but everything else is.

As of now, there is no support for cyclic or shared values. Cyclic
values will lead to non-termination whereas shared values, besides
requiring significantly more space when encoded, may lead to a
substantial increase in memory footprint when they are read back in.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = 1:%{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-fieldslib-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
Requires:       ocaml-variantslib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
%autosetup -n bin_prot-%{version}

%build
%dune_build

# Relink with Fedora linker flags
cd _build/default/src
ocamlmklib -g -ldopt "%{build_ldflags}" -o bin_prot_stubs blit_stubs.o

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license COPYRIGHT.txt LICENSE.md LICENSE-Tywith.txt THIRD-PARTY.txt

%files devel -f .ofiles-devel

%changelog
* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 1:0.15.0-8
- Rebuild for ocaml-ppxlib 0.28.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 1:0.15.0-7
- Rebuild for ocaml-ppxlib 0.27.0
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1:0.15.0-5
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.15.0-5
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 1:0.15.0-4
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.15.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 1:0.15.0-1
- Version 0.15.0

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 1:0.14.0-12
- Rebuild for ocaml-sexplib0 0.15.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.14.0-11
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 1:0.14.0-10
- Rebuild for ocaml-ppxlib 0.23.0

* Tue Aug 17 2021 Jerry James <loganjerry@gmail.com> - 1:0.14.0-9
- Rebuild for ocaml-ppx-optcomp 0.14.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 10:50:30 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.14.0-7
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 1:0.14.0-6
- Rebuild for ocaml-base 0.14.1

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.14.0-5
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.14.0-3
- OCaml 4.11.1 rebuild

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.14.0-2
- OCaml 4.11.0 rebuild

* Wed Aug 19 2020 Jerry James <loganjerry@gmail.com> - 1:0.14.0-1
- Version 0.14.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.13.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.13.0-3
- Rebuild to resolve build order symbol problems.

* Wed Jun 24 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-2
- Fix the -devel subpackage dependency on the main package

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-1
- Version 0.13.0
- Add Epoch to deal with new version numbering scheme
- License change to MIT and BSD
- Build with dune

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-32
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-31
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-29
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-28
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-25
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-24
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-22
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-20
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-19
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-18
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-16
- ocaml-4.02.1 rebuild.

* Thu Sep 25 2014 Jerry James <loganjerry@gmail.com> - 2.0.9-15
- Add -fix-ints patch for ocaml 4.02
- Use native, rather than emulated endian-specific, 64-bit arithmetic
- Fix license handling

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-14
- Bump release and rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-13
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-12
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-10
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Sat Jul 19 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-9
- OCaml 4.02.0 beta rebuild.

* Wed Jun 18 2014 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-8
- Remove -Werror from compiler flags.  Fixes FTBFS (RHBZ#1106613).
- Move configure into build section (instead of prep).
- Use global instead of define.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-6
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Modernize spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-3
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.9-1
- New upstream version 2.0.9.
- Recompile for OCaml 4.00.0.

* Thu Jan 12 2012 Richard W.M. Jones <rjones@redhat.com> - 2.0.7-1
- New upstream version 2.0.7.
- Rebuild for OCaml 3.12.1.

* Wed Sep 28 2011 Michael Ekstrand <michael@elehack.net> - 2.0.6-1
- New upstream version from forge.ocamlcore.org (#741484)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 1.2.24-1
- New upstream version 1.2.24.
- Fix upstream URL.
- Rebuild for OCaml 3.12.0.

* Mon Jan 11 2010 Richard W.M. Jones <rjones@redhat.com> - 1.2.21-1
- New upstream version 1.2.21.
- Change %%define to %%global.
- Use upstream RPM 4.8 OCaml dependency generator.

* Mon Nov  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.20-2
- The final license of the code is LGPLv2+ with the OCaml linking
  exception.  It was derived from earlier BSD code.
- Don't duplicate the license files across base and -devel packages.
- Add note to spec about inclusion of *.ml file in -devel package.

* Mon Oct 12 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.20-1
- New upstream version 1.2.20.

* Sat Sep  5 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.18-1
- New upstream version 1.2.18.

* Fri May 16 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.5-3
- Force signed chars when compiling, as per comment from upstream author.
- Remove the part in the description which says this is only
  supported on little endian architectures.

* Mon May 12 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.5-2
- Remove ExclusiveArch, but add a Fedora README file warning about
  shortcomings on non-x86 architectures.
- Added missing dependency ocaml-type-conv.
- Move *.ml file to devel package.

* Sat May  3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.0.5-1
- Initial RPM release.
