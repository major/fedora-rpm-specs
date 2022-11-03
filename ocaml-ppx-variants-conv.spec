%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-variants-conv
Version:        0.15.0
Release:        8%{?dist}
Summary:        Generate accessor & iteration functions for OCaml variant types

License:        MIT
URL:            https://github.com/janestreet/ppx_variants_conv
Source0:        %{url}/archive/v%{version}/ppx_variants_conv-%{version}.tar.gz

BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-base-devel >= 0.14
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-ppxlib-devel >= 0.14.0
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-variantslib-devel >= 0.14

%description
Ppx_variants_conv is a ppx rewriter that can be used to define
first-class values representing variant constructors, and additional
routines to fold, iterate and map over all constructors of a variant
type.  It provides corresponding functionality for variant types as
ppx_fields_conv provides for record types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-variantslib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_variants_conv-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-8
- Rebuild for ocaml-ppxlib 0.28.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-7
- Rebuild for ocaml-ppxlib 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-5
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-4
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.14.2-2
- Rebuild for ocaml-sexplib0 0.15.0

* Sat Oct 16 2021 Jerry James <loganjerry@gmail.com> - 0.14.2-1
- Version 0.14.2
- Drop upstreamed -ppxlib patch

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-10
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-9
- Rebuild for ocaml-ppxlib 0.23.0
- Add upstream -ppxlib patch

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-8
- Rebuild for ocaml-ppxlib 0.22.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-6
- Rebuild for ocaml-ppxlib 0.22.1

* Tue Mar  2 10:42:16 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-5
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-4
- Rebuild for ocaml-base 0.14.1

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-3
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- Version 0.14.1

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Wed Aug 19 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Drop CONTRIBUTING.md
- Use boolean dependencies to more fully reflect upstream version dependencies

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
