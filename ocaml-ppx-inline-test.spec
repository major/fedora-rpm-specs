# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# This package is needed to build ppx_jane, but its tests require ppx_jane.
# Break the dependency cycle here.
%bcond_with test

Name:           ocaml-ppx-inline-test
Version:        0.16.0
Release:        2%{?dist}
Summary:        Syntax extension for writing inline tests in OCaml code

License:        MIT
URL:            https://github.com/janestreet/ppx_inline_test
Source0:        %{url}/archive/v%{version}/ppx_inline_test-%{version}.tar.gz

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-base-devel >= 0.16
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0
BuildRequires:  ocaml-time-now-devel >= 0.16

%if %{with test}
BuildRequires:  ocaml-ppx-jane-devel
%endif

%description
Ppx_inline_test is a syntax extension for writing inline tests in OCaml
code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-time-now-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_inline_test-%{version}

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- Version 0.16.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-10
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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

* Thu Feb  3 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-2
- Conditionally build docs to avoid circular dependency on odoc

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Wed Nov 24 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-12
- Rebuild for ocaml-sexplib0 0.15.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-11
- OCaml 4.13.1 build

* Thu Sep  2 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-10
- Add missing ocaml-time-now-devel dependency to the -devel subpackage

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-9
- Rebuild for ocaml-ppxlib 0.23.0

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-8
- Rebuild for ocaml-ppxlib 0.22.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-6
- Rebuild for ocaml-ppxlib 0.22.1

* Tue Mar  2 10:32:22 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-5
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

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.1-1
- Initial RPM
