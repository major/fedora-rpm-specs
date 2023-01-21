%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-bos
Version:        0.2.1
Release:        6%{?dist}
Summary:        Basic OS interaction for OCaml

License:        ISC
URL:            https://erratique.ch/software/bos
Source0:        %{url}/releases/bos-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel >= 0.8.10
BuildRequires:  ocaml-fpath-devel >= 0.7.3
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-mtime-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rresult-devel >= 0.7.0
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  python3

%description
Bos provides support for basic and robust interaction with the operating
system in OCaml.  It has functions to access the process environment,
parse command line arguments, interact with the file system and run
command line programs.  Bos works equally well on POSIX and Windows
operating systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-fpath-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-rresult-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n bos-%{version}

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

# Relink with Fedora linker flags
cd _build
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g \
  -package rresult -package astring -package fpath -package fmt -package logs \
  -package unix -I src src/bos.cmxa -o src/bos.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g \
  -package fmt.tty -package logs.fmt -package rresult -package astring \
  -package fpath -package fmt -package logs -package unix -I src \
  src/bos_setup.cmxa -o src/bos_setup.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g \
  -package compiler-libs.toplevel -package rresult -package astring \
  -package fpath -package fmt -package logs -package unix -I src \
  src/bos_top.cmxa -o src/bos_top.cmxs
cd -

%install
mkdir -p %{buildroot}%{ocamldir}/bos
cp -p _build/src/*.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,mli} _build/pkg/META \
   _build/src/bos_top_init.ml _build/opam %{buildroot}%{ocamldir}/bos
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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.2.1-4
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-4
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.2.1-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Jerry James <loganjerry@gmail.com> - 0.2.1-1
- Initial RPM
