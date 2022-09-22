%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# This package is now a transitive dependency of ocaml-ppx-inline-test, so using
# it to test this package creates a circular dependency.
%bcond_with test

Name:           ocaml-ppx-sexp-conv
Version:        0.15.1
Release:        4%{?dist}
Summary:        Generate S-expression conversion functions from type definitions
License:        MIT
URL:            https://github.com/janestreet/ppx_sexp_conv
Source0:        %{url}/archive/v%{version}/ppx_sexp_conv-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-base-devel >= 0.15
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-ppxlib-devel >= 0.23.0
BuildRequires:  ocaml-sexplib0-devel >= 0.15

%if %{with test}
BuildRequires:  ocaml-ppx-inline-test-devel
%endif

%description
Ppx_sexp_conv is a PPX syntax extension that generates code for
converting OCaml types to and from s-expressions, as defined in the
sexplib0 library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_sexp_conv-%{version}

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.org
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 0.15.1-4
- Rebuild for ocaml-ppxlib 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.1-2
- Use new Ocaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.1-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- Version 0.15.1

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Feb  3 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-3
- Conditionally build docs to avoid circular dependency on odoc

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-2
- Rebuild for ocaml-ppxlib 0.24.0

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.3-7
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 0.14.3-6
- Rebuild for ocaml-ppxlib 0.23.0

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 0.14.3-5
- Rebuild for ocaml-ppxlib 0.22.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 0.14.3-3
- Rebuild for ocaml-ppxlib 0.22.1
- There is no circular dependency, so build with ocaml-odoc always

* Mon Mar  1 17:33:59 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.3-2
- OCaml 4.12.0 build
- Make ocaml-odoc dependency conditional.

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.3-1
- Version 0.14.3

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-3
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- Version 0.14.1

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-4
- OCaml 4.11.1 rebuild

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- Bump and rebuild.

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Drop CONTRIBUTING.md
- Use boolean dependencies to more fully reflect upstream version dependencies

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
