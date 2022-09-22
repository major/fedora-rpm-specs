%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppxlib
Epoch:          1
Version:        0.27.0
Release:        2%{?dist}
Summary:        Base library and tools for ppx rewriters

License:        MIT
URL:            https://github.com/ocaml-ppx/ppxlib
Source0:        %{url}/archive/%{version}/ppxlib-%{version}.tar.gz
# Fedora does not have, and does not need, stdlib-shims
Patch0:         %{name}-stdlib-shims.patch
# Work around differences in parentheses in test output
Patch1:         %{name}-test.patch

BuildRequires:  ocaml >= 4.04.1
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-cinaps-devel >= 0.12.1
BuildRequires:  ocaml-compiler-libs-janestreet-devel >= 0.11.0
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ppx-derivers-devel >= 1.0
BuildRequires:  ocaml-re-devel >= 1.9.0
BuildRequires:  ocaml-sexplib0-devel >= 0.12
BuildRequires:  ocaml-stdio-devel

# This can be removed when F40 reaches EOL
Obsoletes:      %{name}-doc < 1:0.26.0-3

%description
The ppxlib project provides the basis for the ppx system, which is
currently the officially supported method for meta-programming in Ocaml.
It offers a principled way to generate code at compile time in OCaml
projects.  It features:
- an OCaml AST / parser/ pretty-printer snapshot, to create a full
  frontend independent of the version of OCaml;
- a library for ppx rewriters in general, and type-driven code generators
  in particular;
- a full-featured driver for OCaml AST transformers;
- a quotation mechanism for writing values representing OCaml AST in the
  OCaml syntax;
- a generator of open recursion classes from type definitions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       ocaml-compiler-libs-janestreet-devel%{?_isa}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%prep
%autosetup -n ppxlib-%{version} -p1

# Adapt to grep 3.8
sed -i 's/egrep/grep -E/g' test/expansion_context/run.t

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md HISTORY.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep  6 2022 Jerry James <loganjerry@gmail.com> - 1:0.27.0-2
- Adapt to grep 3.8

* Mon Aug  8 2022 Jerry James <loganjerry@gmail.com> - 1:0.27.0-1
- Version 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1:0.26.0-2
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.26.0-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 1:0.26.0-1
- Version 0.26.0

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 1:0.24.0-5
- Rebuild due to changed base, sexplib0, and stdio
- Drop unused ocaml-migrate-parsetree-devel BR

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.24.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Wed Jan 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.24.0-3
- Rebuild to pick up new ocaml dependency

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Jerry James <loganjerry@gmail.com> - 1:0.24.0-1
- Version 0.24.0
- Drop upstreamed OCaml 4.13 compatibility patches

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 1:0.23.0-3
- Rebuild for ocaml-stdio 0.15.0
- Add -ocaml413 patch from upstream to address OCaml 4.13 issues

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.23.0-2
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 1:0.23.0-1
- Version 0.23.0
- Reenable tests on ARM

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 1:0.22.2-1
- Version 0.22.2

* Tue Jul 27 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.22.1-4
- Rebuild for changed ocamlx(Dynlink)

* Tue Jul 27 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.22.1-3
- Rebuild for changed ocamlx(Dynlink)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 1:0.22.1-1
- Version 0.22.1

* Mon Mar  1 15:56:36 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.22.0-2
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 1:0.22.0-1
- Version 0.22.0
- Drop upstreamed -longident-parse patch
- Do not build documentation by default due to circular dependency

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.15.0-3
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.15.0-1
- Version 0.15.0
- Drop upstreamed patches: -execption-format and -whitespace
- Add -stdlib-shims patch

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.13.0-6
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.13.0-5
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-4
- Add Epoch to Requires from -devel to main package

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-3
- Some ppx rewriters do not work with version 0.14.0 or 0.15.0, so revert to
  version 0.13.0 until they can be updated

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.14.0-1
- New upstream release 0.14.0

* Thu Jun 18 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Rebuild for ocaml-stdio 0.14.0

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
