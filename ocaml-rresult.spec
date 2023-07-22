# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-rresult
Version:        0.7.0
Release:        10%{?dist}
Summary:        Result value combinators for OCaml

License:        ISC
URL:            https://erratique.ch/software/rresult
Source0:        %{url}/releases/rresult-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  python3

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Warnings

%description
Rresult is an OCaml module for handling computation results and errors
in an explicit and declarative manner without resorting to exceptions.
It defines combinators to operate on the values of the result type
available from OCaml 4.03 in the standard library.

OCaml 4.08 provides the Stdlib.Result module which you should prefer to
Rresult.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n rresult-%{version}

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
mkdir -p %{buildroot}%{ocamldir}/rresult
%ifarch %{ocaml_native_compiler}
cp -p _build/src/*.{a,cmx,cmxa,cmxs} %{buildroot}%{ocamldir}/rresult
%endif
cp -p _build/src/*.{cma,cmi,cmt,cmti,mli} _build/src/rresult_top_init.ml \
  _build/pkg/META _build/opam %{buildroot}%{ocamldir}/rresult
%ocaml_files

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%if %{with docs}
%doc _build/default/_doc/*
%endif

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-9
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.7.0-8
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-7
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-4
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-4
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- Initial RPM
