Name:           ocaml-ppx-js-style
Version:        0.16.0
Release:        1%{?dist}
Summary:        Code style checker for Jane Street OCaml packages

License:        MIT
URL:            https://github.com/janestreet/ppx_js_style
Source0:        %{url}/archive/v%{version}/ppx_js_style-%{version}.tar.gz

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-base-devel >= 0.16
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-octavius-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_js_style is an identity ppx rewriter that enforces Jane Street
coding styles.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-octavius-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_js_style-%{version}

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
* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- Version 0.16.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-11
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-9
- Rebuild for ocaml-ppxlib 0.28.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-8
- Rebuild for ocaml-ppxlib 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-6
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-6
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Version 0.15.0 rerelease
- Build documentation unconditionally

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-2
- Rebuild for ocaml-ppxlib 0.24.0

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0
- Switch back from autochangelog until Richard's scripts can handle it

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-1.1
- OCaml 4.13.1 build

* Wed Sep 01 2021 Jerry James <loganjerry@gmail.com> 0.14.1-5
- Rebuild for ocaml-ppxlib 0.23.0

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> 0.14.1-4
- Rebuild for ocaml-ppxlib 0.22.2.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-10
- Rebuild for ocaml-ppxlib 0.22.1

* Tue Mar  2 10:06:37 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-9
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-8
- Rebuild for ocaml-base 0.14.1

* Wed Feb  3 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-7
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-5
- Rebuild for ocaml-ppxlib 0.15.0

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-4
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.0 rebuild

* Sat Aug 15 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-2
- Build verbosely
- Use 'with' instead of 'and' in BuildRequires

* Sat Jun 20 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Initial RPM
