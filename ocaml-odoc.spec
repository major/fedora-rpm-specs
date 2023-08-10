# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-odoc
Version:        2.2.1
Release:        1%{?dist}
Summary:        Documentation compiler for OCaml and Reason

# ISC: The project as a whole
# BSD-3-Clause: src/html_support_files/highlight.pack.js
License:        ISC AND BSD-3-Clause
URL:            https://github.com/ocaml/odoc
Source0:        %{url}/archive/%{version}/odoc-%{version}.tar.gz

BuildRequires:  jq
BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-bisect-ppx-devel > 2.5.0
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-cppo >= 1.1.0
BuildRequires:  ocaml-dune >= 2.9.1
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-fpath-devel
BuildRequires:  ocaml-mdx-devel
BuildRequires:  ocaml-odoc-parser-devel >= 0.9.0
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-sexplib0-devel
BuildRequires:  ocaml-tyxml-devel >= 4.3.0
BuildRequires:  ocaml-yojson-devel

%description
This package contains odoc, a documentation generator for OCaml and
Reason.  It reads doc comments, delimited with `(** ... *)`, and outputs
HTML.  Text inside doc comments is marked up in ocamldoc syntax.

Odoc's main advantage over ocamldoc is an accurate cross-referencer,
which handles the complexity of the OCaml module system.  Odoc also
offers a good opportunity to improve HTML output compared to ocamldoc,
but this is very much a work in progress.

%package        devel
License:        ISC
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-fpath-devel%{?_isa}
Requires:       ocaml-odoc-parser-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-tyxml-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
License:        ISC
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n odoc-%{version}

%build
%dune_build @default @doc

%install
%dune_install

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
_build/install/default/bin/odoc --help groff > %{buildroot}%{_mandir}/man1/odoc.1

# It is no longer possible to run the tests because Fedora lacks ocaml-crunch.
#check
#dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md src/html_support_files/LICENSE
%{_mandir}/man1/odoc.1*

%files devel -f .ofiles-devel

%files doc
%doc _build/default/_doc/_html/*
%license LICENSE.md

%changelog
* Tue Aug  8 2023 Jerry James <loganjerry@gmail.com> - 2.2.1-1
- Version 2.2.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-6
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2.2.0-5
- OCaml 5.0.0 rebuild

* Tue Mar 21 2023 Jerry James <loganjerry@gmail.com> - 2.2.0-4
- Re-enable debuginfo now that dune is fixed

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  9 2023 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Version 2.2.0
- Disable tests due to missing dependency

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 2.1.1-2
- Convert License tags to SPDX

* Thu Sep 15 2022 Jerry James <loganjerry@gmail.com> - 2.1.1-2
- Rebuild for ocaml-cmdliner 1.1.1

* Tue Aug  2 2022 Jerry James <loganjerry@gmail.com> - 2.1.1-1
- Version 2.1.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 21 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-2
- Use new OCaml macros
- Add temporary workaround for a failing test

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 2.1.0-2
- OCaml 4.14.0 rebuild

* Wed Feb  9 2022 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- Version 2.1.0
- License is ISC, not MIT
- Trim BuildRequires

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Jerry James <loganjerry@gmail.com> - 2.0.2-1
- Version 2.0.2

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.5.3-2
- OCaml 4.13.1 build

* Wed Aug 11 2021 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- Version 1.5.3

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 1.5.2-8
- Rebuild for changed ocamlx(Dynlink)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 1.5.2-6
- Rebuild for ocaml-markup 1.0.1

* Fri Apr 23 2021 Jerry James <loganjerry@gmail.com> - 1.5.2-5
- Rebuild for ocaml-tyxml 4.5.0

* Mon Mar  1 2021 Richard W.M. Jones <rjones@redhat.com> - 1.5.2-4
- OCaml 4.12.0 build

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1.5.2-3
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 1.5.2-1
- Version 1.5.2

* Fri Oct 23 2020 Jerry James <loganjerry@gmail.com> - 1.5.1-5
- Rebuild for ocaml-markup 1.0.0

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 1.5.1-4
- Rebuild for ocaml-fpath 0.7.3

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.1-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.1-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- Version 1.5.1
- Drop upstreamed odoc-1.5.0-ocaml411.patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-4
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-2
- OCaml 4.10.0 final.

* Fri Feb  7 2020 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Version 1.5.0
- Drop all patches

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-3
- Add 3 patches for OCaml 4.10 compatibility

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-2
- Remove some BRs needed only for transitive dependencies
- Add ocaml-astring-devel and ocaml-fpath-devel Rs to -devel
- Build in parallel

* Fri Jan 10 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- Initial RPM
