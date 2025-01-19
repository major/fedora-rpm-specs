# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/c-cube/qcheck

Name:           ocaml-qcheck
Version:        0.23
Release:        2%{?dist}
Summary:        QuickCheck inspired property-based testing for OCaml

License:        BSD-2-Clause
URL:            https://c-cube.github.io/qcheck/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Expose a dependency on the math library so RPM can see it
Patch:          %{name}-mathlib.patch

BuildRequires:  asciidoc
BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-dune >= 2.8.0
BuildRequires:  ocaml-alcotest-devel >= 1.4.0
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.22.0
BuildRequires:  ocaml-ppx-deriving-devel >= 5.2.1
BuildRequires:  python3-pygments

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-ounit%{?_isa} = %{version}-%{release}

# This can be removed when F40 reaches EOL
Obsoletes:      %{name}-doc < 0.19

%global _desc %{expand:
Qcheck enables checking invariants (properties of a type) over randomly
generated instances of the type.  It provides combinators for generating
instances and printing them.}

%description %_desc

This package is a compatibility wrapper for qcheck.  New code should
use either ocaml-qcheck-alcotest or ocaml-qcheck-ounit.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ounit-devel%{?_isa} = %{version}-%{release}


%description    devel %_desc

The %{name}-devel package contains libraries and signature files
for developing applications that use the qcheck compatibility wrapper.
New code should instead use %{name}-alcotest-devel or
%{name}-ounit-devel.


%package        core
Summary:        QuickCheck inspired property-based testing for OCaml


%description    core %_desc
This package provides alcotest support for qcheck.


%package        core-devel
Summary:        Development files for %{name}-core
Requires:       %{name}-core%{?_isa} = %{version}-%{release}


%description    core-devel %_desc

The %{name}-core-devel package contains libraries and signature
files for developing applications that use %{name}-core.


%package        ounit
Summary:        OUnit support for %{name}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}


%description    ounit %_desc

This package provides ounit support for qcheck.


%package        ounit-devel
Summary:        Development files for %{name}-ounit
Requires:       %{name}-ounit%{?_isa} = %{version}-%{release}
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-ounit-devel%{?_isa}


%description    ounit-devel %_desc

The %{name}-ounit-devel package contains libraries and signature
files for developing applications that use %{name}-ounit.


%package        alcotest
Summary:        Alcotest support for %{name}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}


%description    alcotest %_desc

This package provides alcotest support for qcheck.


%package        alcotest-devel
Summary:        Development files for %{name}-alcotest
Requires:       %{name}-alcotest%{?_isa} = %{version}-%{release}
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-alcotest-devel%{?_isa}


%description    alcotest-devel %_desc

The %{name}-alcotest-devel package contains libraries and signature
files for developing applications that use %{name}-alcotest.


%package     -n ocaml-ppx-deriving-qcheck
Summary:        PPX deriver for QCheck
Requires:       %{name}-core%{?_isa} = %{version}-%{release}


%description  -n ocaml-ppx-deriving-qcheck %_desc

This package provides a PPX deriver for QCheck.


%package     -n ocaml-ppx-deriving-qcheck-devel
Summary:        Development files for ocaml-ppx-deriving-qcheck
Requires:       %{name}-core-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}


%description -n ocaml-ppx-deriving-qcheck-devel %_desc

The ocaml-ppx-deriving-qcheck-devel package contains libraries and
signature files for developing applications that use
ocaml-ppx-deriving-qcheck.


%prep
%autosetup -n qcheck-%{version} -p1


%build
%dune_build
asciidoc README.adoc


%install
%dune_install -s


%check
%dune_check


%files -f .ofiles-qcheck
%doc README.html CHANGELOG.md
%license LICENSE


%files devel -f .ofiles-qcheck-devel
%doc README.html CHANGELOG.md
%license LICENSE


%files core -f .ofiles-qcheck-core


%files core-devel -f .ofiles-qcheck-core-devel


%files ounit -f .ofiles-qcheck-ounit


%files ounit-devel -f .ofiles-qcheck-ounit-devel


%files alcotest -f .ofiles-qcheck-alcotest


%files alcotest-devel -f .ofiles-qcheck-alcotest-devel

%files -n ocaml-ppx-deriving-qcheck -f .ofiles-ppx_deriving_qcheck

%files -n ocaml-ppx-deriving-qcheck-devel -f .ofiles-ppx_deriving_qcheck-devel

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 0.23-1
- OCaml 5.3.0 rebuild for Fedora 42
- Version 0.23

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 0.22-4
- Rebuild for ocaml-ppxlib 0.33.0

* Thu Jul 25 2024 Jerry James <loganjerry@gmail.com> - 0.22-3
- Rebuild for ocaml-alcotest 1.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Jerry James <loganjerry@gmail.com> - 0.22-1
- Version 0.22

* Wed Jul  3 2024 Jerry James <loganjerry@gmail.com> - 0.21.3-9
- Rebuild for ocaml-sexplib0 0.17.0

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.21.3-8
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 0.21.3-7
- OCaml 5.2.0 for Fedora 41

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 0.21.3-6
- Rebuild for changed ocamlx(Location) hash

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.21.3-3
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.21.3-2
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Dec  7 2023 Jerry James <loganjerry@gmail.com> - 0.21.3-1
- Version 0.21.3
- Drop upstreamed ocaml5 and asciidoc patches

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.21.2-2
- OCaml 5.1 rebuild for Fedora 40

* Fri Sep  1 2023 Jerry James <loganjerry@gmail.com> - 0.21.2-1
- Version 0.21.2
- Add patch to fix an asciidoc error

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.21.1-3
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.21.1-2
- OCaml 5.0.0 rebuild

* Thu Jun  8 2023 Jerry James <loganjerry@gmail.com> - 0.21.1-1
- Version 0.21.1

* Tue May 16 2023 Jerry James <loganjerry@gmail.com> - 0.21-1
- Version 0.21

* Tue Mar 21 2023 Jerry James <loganjerry@gmail.com> - 0.20-4
- Rebuild for ocaml-alcotest 1.7.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.20-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov  8 2022 Jerry James <loganjerry@gmail.com> - 0.20-1
- Version 0.20

* Mon Nov  7 2022 Jerry James <loganjerry@gmail.com> - 0.19.1-5
- Rebuild for ocaml-ppxlib 0.28.0

* Wed Sep 21 2022 Jerry James <loganjerry@gmail.com> - 0.19.1-4
- Rebuild for ocaml-alcotest 1.6.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 0.19.1-3
- Rebuild for ocaml-ounit 2.2.6
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 0.19.1-1
- Version 0.19.1
- Add ocaml-ppx-deriving-qcheck subpackage
- Reenable tests on 32-bit x86
- Add patch to expose a dependency on libm
- Build the documentation with asciidoc
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.18.1-2
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.18.1-1
- Version 0.18.1
- Disable tests on 32-bit x86
- Give ppc64le extra stack space for running tests

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.18-6
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Jerry James <loganjerry@gmail.com> - 0.18-4
- Rebuild for alcotest 1.5.0
- Split into subpackages to manage dependencies

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.18-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 0.18-1
- Move META to the main package

* Fri Jun 25 2021 Jerry James <loganjerry@gmail.com> - 0.18-1
- Version 0.18

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 0.17-4
- Rebuild for alcotest 1.4.0

* Mon Mar  1 23:22:40 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.17-3
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.17-2
- Rebuild for alcotest 1.3.0

* Tue Feb 16 2021 Jerry James <loganjerry@gmail.com> - 0.17-1
- Version 0.17
- Drop upstream patches

* Tue Feb  2 2021 Jerry James <loganjerry@gmail.com> - 0.16-4
- Bump and rebuild for updated ocaml-alcotest dep

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 0.16-2
- Add upstream patches to fix numeric range issues

* Thu Nov  5 2020 Jerry James <loganjerry@gmail.com> - 0.16-1
- Version 0.16

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 0.15-1
- Version 0.15

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14-4
- OCaml 4.11.1 rebuild

* Fri Aug 28 2020 Jerry James <loganjerry@gmail.com> - 0.14-3
- Rebuild for alcotest 1.2.2

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 0.14-1
- Version 0.14

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-6
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-5
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-4
- Bump release and rebuild.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-2
- OCaml 4.10.0 final.

* Wed Feb 19 2020 Jerry James <loganjerry@gmail.com> - 0.13-1
- New upstream release.
- Build with alcotest support.
- Build documentation with odoc, and ship it in a new doc subpackage.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.12-2
- OCaml 4.10.0+beta1 rebuild.

* Wed Dec 18 2019 Andy Li <andy@onthewings.net> - 0.12-1
- New upstream release. (RHBZ#1757625)
- Remove unneeded BuildRequires on opam-installer.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10-3
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10-2
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Andy Li <andy@onthewings.net> - 0.10-1
- New upstream release.
- Update build system and commands from jbuilder to dune.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.8-5
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.8-4
- OCaml 4.07.0-rc1 rebuild.

* Mon May 14 2018 Andy Li <andy@onthewings.net> - 0.8-3
- Rebuilt against ounit.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Andy Li <andy@onthewings.net> - 0.8-1
- New upstream release. (RHBZ#1541681)
- Enable debug package.

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 0.7-2
- OCaml 4.06.0 rebuild.

* Mon Nov 20 2017 Andy Li <andy@onthewings.net> - 0.7-1
- Initial RPM release.
