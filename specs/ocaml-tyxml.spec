# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocsigen/tyxml

Name:           ocaml-tyxml
Version:        4.6.0
Release:        16%{?dist}
Summary:        Build valid HTML and SVG documents

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://ocsigen.org/tyxml/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/tyxml-%{version}.tbz
# Fedora's OCaml is new enough that we do not need the seq shim
Patch:          %{name}-seq.patch

BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-markup-devel >= 0.7.2
BuildRequires:  ocaml-ppxlib-devel >= 0.18
BuildRequires:  ocaml-re-devel >= 1.5.0
BuildRequires:  ocaml-uutf-devel >= 1.0.0

%description
TyXML provides a set of convenient combinators that uses the OCaml type
system to ensure the validity of the generated documents.  TyXML can be
used with any representation of HTML and SVG: the textual one, provided
directly by this package, or DOM trees (`js_of_ocaml-tyxml`), virtual DOM
(`virtual-dom`) and reactive or replicated trees (`eliom`).  You can also
create your own representation and use it to instantiate a new set of
combinators.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        syntax
Summary:        Common layer for the JSX and PPX syntaxes for TyXML

%description    syntax
This package contains common code used by both the JSX and the PPX
syntaxes for TyXML.

%package        syntax-devel
Summary:        Development files for %{name}-syntax
Requires:       %{name}-syntax%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}

%description    syntax-devel
The %{name}-syntax-devel package contains libraries and signature files
for developing applications that use %{name}-syntax.

%package        jsx
Summary:        JSX syntax for writing TyXML documents
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax%{?_isa} = %{version}-%{release}

%description    jsx
This package enables writing TyXML documents with reasons's JSX syntax,
from textual trees to reactive virtual DOM trees.

  open Tyxml
  let to_ocaml = <a href="ocaml.org"> "OCaml!" </a>;

%package        jsx-devel
Summary:        Development files for %{name}-jsx
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-jsx%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    jsx-devel
The %{name}-jsx-devel package contains libraries and signature files for
developing applications that use %{name}-jsx.

%package        ppx
Summary:        PPX for writing TyXML documents with HTML syntax
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax%{?_isa} = %{version}-%{release}

%description    ppx
This package contains PPX for writing TyXML documents with HTML syntax.

  open Tyxml
  let%%html to_ocaml = "<a href='ocaml.org'>OCaml!</a>"

The TyXML PPX is compatible with all TyXML instance, from textual trees
to reactive virtual DOM trees.

%package        ppx-devel
Summary:        Development files for %{name}-ppx
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-syntax-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ppx%{?_isa} = %{version}-%{release}
Requires:       ocaml-markup-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}

%description    ppx-devel
The %{name}-ppx-devel package contains libraries and signature files for
developing applications that use %{name}-ppx.

%prep
%autosetup -n tyxml-%{version} -p1

%build
%dune_build

%install
%dune_install -s

%check
# As of version 4.4.0, the tyxml-jsx tests fail due to lack of the reason
# package in Fedora.
%dune_check -p tyxml,tyxml-syntax,tyxml-ppx

%files -f .ofiles-tyxml
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-tyxml-devel

%files syntax -f .ofiles-tyxml-syntax

%files syntax-devel -f .ofiles-tyxml-syntax-devel

%files jsx -f .ofiles-tyxml-jsx

%files jsx-devel -f .ofiles-tyxml-jsx-devel

%files ppx -f .ofiles-tyxml-ppx

%files ppx-devel -f .ofiles-tyxml-ppx-devel

%changelog
* Wed Feb 12 2025 Jerry James <loganjerry@gmail.com> - 4.6.0-16
- Rebuild for ocaml-ppxlib 0.35.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 4.6.0-14
- OCaml 5.3.0 rebuild for Fedora 42

* Sun Oct  6 2024 Jerry James <loganjerry@gmail.com> - 4.6.0-13
- Rebuild for ocaml-re 1.13.3

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 4.6.0-12
- Rebuild for ocaml-ppxlib 0.33.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul  3 2024 Jerry James <loganjerry@gmail.com> - 4.6.0-10
- Rebuild for ocaml-sexplib0 0.17.0

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 4.6.0-9
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 4.6.0-8
- OCaml 5.2.0 for Fedora 41

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 4.6.0-7
- Rebuild for changed ocamlx(Location) hash

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 4.6.0-4
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.6.0-3
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 4.6.0-2
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- Version 4.6.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-18
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 4.5.0-17.20230622git407f41b
- Build from git HEAD for OCaml 5.0.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-16
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 4.5.0-14
- Rebuild for ocaml-ppxlib 0.28.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 4.5.0-13
- Rebuild for ocaml-ppxlib 0.27.0
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 4.5.0-11
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-11
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 4.5.0-10
- Rebuild for ocaml-uutf 1.0.3
- Build in release mode

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-9
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 4.5.0-7
- Rebuild for ocaml-ppxlib 0.24.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-6
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 4.5.0-5
- Rebuild for ocaml-ppxlib 0.23.0

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 4.5.0-4
- Rebuild for ocaml-ppxlib 0.22.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 4.5.0-2
- Rebuild for ocaml-markup 1.0.1

* Fri Apr 23 2021 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- Version 4.5.0
- Drop all patches

* Mon Mar  1 21:39:52 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-10
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 4.4.0-9
- Apply upstream merge request to migrate to ppxlib

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-8
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 4.4.0-6
- Rebuild for ocaml-migrate-parsetree 1.8.0

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 4.4.0-5
- Rebuild for the re-release of ocaml-markup 1.0.0

* Fri Oct 23 2020 Jerry James <loganjerry@gmail.com> - 4.4.0-4
- Rebuild for ocaml-markup 1.0.0

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-2
- OCaml 4.11.0 rebuild

* Tue Aug  4 2020 Jerry James <loganjerry@gmail.com> - 4.4.0-1
- Version 4.4.0
- Drop documentation subpackage until dependency loop can be handled
- Disable tests since no reason package is available

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-6
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-5
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-4
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 4.3.0-2
- Add ocaml-re-dvel and ocaml-uutf-devel Rs to -devel
- Add ocaml-ppx-derivers-devel and ocaml-ppx-tools-versioned-devel Rs to
  -ppx-devel
- Build in parallel

* Fri Jan 10 2020 Jerry James <loganjerry@gmail.com> - 4.3.0-1
- Initial RPM
