%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-deriving-yojson
Version:        3.7.0
Release:        1%{?dist}
Summary:        JSON codec generator for OCaml

License:        MIT
URL:            https://github.com/ocaml-ppx/ppx_deriving_yojson
Source0:        %{url}/archive/v%{version}/ppx_deriving_yojson-%{version}.tar.gz

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-ppx-deriving-devel >= 5.1
BuildRequires:  ocaml-ppxlib-devel >= 0.26.0
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-yojson-devel >= 1.6.0

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-ppx-deriving-yojson-doc < 3.6.1-15

%description
Deriving_Yojson is a ppx_deriving plugin that generates JSON serializers
and deserializers that use the Yojson library from an OCaml type
definition.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%prep
%autosetup -n ppx_deriving_yojson-%{version} -p1

%build
%dune_build

%install
%dune_install

# Help the debuginfo generator find the source files
ln -s ../../src/ppx_deriving_yojson.cppo.ml _build/default

%check
%dune_check

%files -f .ofiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%files devel -f .ofiles-devel

%changelog
* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 3.7.0-1
- Version 3.7.0
- Drop upstreamed -pext-decl patch

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 3.6.1-14
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 3.6.1-14
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 3.6.1-13
- Add -pext-decl patch for ppxlib 0.26.0 compatibility

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 3.6.1-13
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-11
- Rebuild for ocaml-ppxlib 0.24.0

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-10
- Rebuild for ocaml-base 0.15.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 3.6.1-9
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-8
- Rebuild for ocaml-ppxlib 0.23.0

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-7
- Rebuild for ocaml-ppxlib 0.22.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-5
- Rebuild for ocaml-ppxlib 0.22.1

* Mon Mar  1 23:31:09 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 3.6.1-4
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 3.6.1-3
- Rebuild for ocaml-ppx-deriving 5.2.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 3.6.1-1
- Version 3.6.1

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.3-4
- Bump release and rebuild.

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.3-3
- OCaml 4.11.1 rebuild

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.3-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 3.5.3-1
- Version 3.5.3
- Drop upstreamed ocaml-411.patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.5.2-2
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 10 2020 Jerry James <loganjerry@gmail.com> - 3.5.2-1
- Initial RPM
