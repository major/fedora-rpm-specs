%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-logs
Version:        0.7.0
Release:        7%{?dist}
Summary:        Logging infrastructure for OCaml

License:        ISC
URL:            https://erratique.ch/software/logs
Source0:        %{url}/releases/logs-%{version}.tbz
# Fix the expected number of errors per test
Patch0:         %{name}-test.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mtime-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel
BuildRequires:  python3

%description
Logs provides a logging infrastructure for OCaml.  Logging is performed
on sources whose reporting level can be set independently.  The log
message report is decoupled from logging and is handled by a reporter.

A few optional log reporters are distributed with the base library and
the API lets you easily implement your own.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n logs-%{version} -p1

# test_lwt needs the thread flag
sed -i 's/package(lwt)/thread, &/' _tags

%build
ocaml pkg/pkg.ml build --with-js_of_ocaml false --with-fmt true \
  --with-cmdliner true --with-lwt true --with-base-threads true --tests true

# Relink with Fedora linker flags
cd _build
ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g -I src src/logs.cmxa \
  -o src/logs.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g -package fmt \
  -I src src/logs_fmt.cmxa -o src/logs_fmt.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g \
  -package cmdliner -I src src/logs_cli.cmxa -o src/logs_cli.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g -thread \
  -package lwt -I src src/logs_lwt.cmxa -o src/logs_lwt.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g \
  -package compiler-libs.toplevel -I src src/logs_top.cmxa -o src/logs_top.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -g -thread \
  -package threads -I src src/logs_threaded.cmxa -o src/logs_threaded.cmxs
cd -

%install
mkdir -p %{buildroot}%{ocamldir}/logs
cp -p _build/src/*.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,mli} _build/pkg/META \
   _build/opam %{buildroot}%{ocamldir}/logs
cp -p src/logs_top_init.ml %{buildroot}%{ocamldir}/logs
%ocaml_files

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Sep 20 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-7
- Rebuild for ocaml-cmdliner 1.1.1

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-6
- Rebuild for ocaml-lwt 5.6.1
- Add patch to fix the tests

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

* Mon Dec  6 2021 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- Initial RPM
