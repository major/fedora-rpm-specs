# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-parsexp
Version:        0.16.0
Release:        3%{?dist}
Summary:        S-expression parsing library

License:        MIT
URL:            https://github.com/janestreet/parsexp
Source0:        %{url}/archive/v%{version}/parsexp-%{version}.tar.gz

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-sexplib0-devel >= 0.16

%description
This library provides generic parsers for parsing S-expressions from
strings or other media.

The library is focused on performance but still provides full generic
parsers that can be used effortlessly with strings, bigstrings, lexing
buffers, character streams or any other source.

It provides three different classes of parsers:
- the normal parsers, producing [Sexp.t] or [Sexp.t list] values;
- the parsers with positions, building compact position sequences so
  that one can recover original positions in order to properly report
  error locations at little cost; and
- the Concrete Syntax Tree parsers, producing values of type
  [Parsexp.Cst.t] which record the concrete layout of the s-expression
  syntax, including comments.

This library is portable and doesn't provide I/O functions.  To read
s-expressions from files or other external sources, you should use
parsexp_io.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n parsexp-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.org
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- Version 0.16.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-9
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-7
- Rebuild for ocaml-base 0.15.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-5
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-4
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- Version 0.14.1

* Mon Mar  1 17:07:34 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-9
- OCaml 4.12.0 build

* Mon Feb 22 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-8
- Rebuild for ocaml-base 0.14.1

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-7
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-8
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-7
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-3
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Change -devel subpackage Requires to ocaml-base-devel
- Build in parallel

* Fri Jan 10 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
