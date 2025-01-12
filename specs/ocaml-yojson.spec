# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-yojson
Version:        2.2.2
Release:        2%{?dist}
Summary:        An optimized parsing and printing library for the JSON format

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/yojson
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/yojson-%{version}.tbz
# Expose a dependency on the math library so RPM can see it
Patch0:         %{name}-mathlib.patch
# Fedora does not need the seq forward compatibility library
Patch1:         %{name}-seq.patch

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-alcotest-devel >= 0.8.5
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-sedlex-devel >= 2.5

%description
Yojson is an optimized parsing and printing library for the JSON
format. It addresses a few shortcomings of json-wheel including 2x
speedup, polymorphic variants and optional syntax for tuples and
variants.

ydump is a pretty-printing command-line program provided with the
yojson package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        five
Summary:        Parsing and printing library for the JSON5 format
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    five
Yojson-five is a parsing and printing library for the JSON5 format.  It
supports parsing JSON5 to Yojson.Basic.t and Yojson.Safe.t types.


%package        five-devel
Summary:        Development files for %{name}-five
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-five%{?_isa} = %{version}-%{release}

%description    five-devel
The %{name}-five-devel package contains libraries and signature
files for developing applications that use %{name}-five.


%prep
%autosetup -n yojson-%{version} -p1


%build
%dune_build -p yojson,yojson-five


%install
%dune_install -s yojson yojson-five


%check
%dune_check -p yojson,yojson-five


%files -f .ofiles-yojson
%doc README.md
%license LICENSE.md


%files devel -f .ofiles-yojson-devel
%doc CHANGES.md examples


%files five -f .ofiles-yojson-five


%files five-devel -f .ofiles-yojson-five-devel


%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 2.2.2-2
- OCaml 5.3.0 rebuild for Fedora 42

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- Version 2.2.2
- New ocaml-yojson-five subpackage
- Remove dependency on ocaml-cppo
- Add dependency on ocaml-sedlex

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-7
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-6
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-3
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.1.2-2
- OCaml 5.1.1 rebuild for Fedora 40

* Mon Dec 11 2023 Jerry James <loganjerry@gmail.com> - 2.1.2-1
- Version 2.1.2

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2.1.0-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 2.1.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Version 2.1.0
- Convert License tag to SPDX
- Use new dune macros

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-25
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-22
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-21
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Jerry James <loganjerry@gmail.com> - 1.7.0-19
- R ocaml-biniou-devel and ocaml-easy-format-devel from the devel subpackage
- Build in release mode
- Enable testing now that alcotest is available

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-18
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 17:10:45 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-16
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-14
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-13
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-10
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-9
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-8
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-7
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-5
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-4
- OCaml 4.09.0 (final) rebuild.

* Thu Sep  5 2019 Jerry James <loganjerry@gmail.com> - 1.7.0-3
- Rebuild for ocaml-easy-format 1.3.2 and ocaml-biniou 1.2.1

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 1.7.0-2
- Rebuild for ocaml-easy-format 1.3.1

* Tue Jul 30 2019 Jerry James <loganjerry@gmail.com> - 1.7.0-1
- New upstream version 1.7.0 (bz 1446344)
- BR ocaml-dune instead of jbuilder
- Use the %%license macro
- Comment out %%check until alcotest is available

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-9
- Bump release and rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-8
- Bump release and rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-7
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-4
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-3
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-1
- New upstream version 1.4.0.
- Remove opt macro.
- Enable debuginfo everywhere.
- OCaml 4.06.0 rebuild.
- Enable SMP builds.
- New upstream URL.
- Remove test files and use upstream tests.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-24
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-21
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-20
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.1.8-18
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-17
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-15
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-14
- Fix bytecode build.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-13
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-12
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-10
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-9
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-8
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-6
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 28 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.8-5
- Rebuild for OCaml 4.02.0 beta.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Jaromir Capik <jcapik@redhat.com> - 1.1.8-3
- Removing ExclusiveArch

* Sat Feb  8 2014 Michel Salim <salimma@fedoraproject.org> - 1.1.8-2
- Incorporate review feedback

* Mon Jan 20 2014 Michel Salim <salimma@fedoraproject.org> - 1.1.8-1
- Initial package
