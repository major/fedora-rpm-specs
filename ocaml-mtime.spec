%undefine _package_note_flags

Name:           ocaml-mtime
Version:        1.4.0
Release:        5%{?dist}
Summary:        Monotonic wall-clock time for OCaml

License:        ISC
URL:            https://erratique.ch/software/mtime
Source0:        %{url}/releases/mtime-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  python3

%description
Mtime has platform independent support for monotonic wall-clock time in
pure OCaml.  This time increases monotonically and is not subject to
operating system calendar time adjustments.  The library has types to
represent nanosecond precision timestamps and time spans.

The additional Mtime_clock library provide access to a system
monotonic clock.

Mtime has no dependencies.  Mtime_clock depends on your system library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n mtime-%{version}

# link with the math library
echo $'\ntrue: cclib(-lm)' >> _tags

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

# Relink with Fedora linker flags
cd _build
ocamlopt -shared -linkall -cclib '%{build_ldflags} -lm' -I src src/mtime.cmxa \
  -g -o src/mtime.cmxs
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' -package \
  compiler-libs.toplevel -I src src/mtime_top.cmxa -g -o src/mtime_top.cmxs
ocamlfind ocamlmklib -ldopt '%{build_ldflags}' -o src-clock/mtime_clock_stubs \
  -g src-clock/mtime_clock_stubs.o
ocamlfind ocamlopt -shared -linkall -cclib '%{build_ldflags}' \
  src-clock/libmtime_clock_stubs.a -I src-clock src-clock/mtime_clock.cmxa -g \
  -o src-clock/mtime_clock.cmxs
cd -

%install
mkdir -p %{buildroot}%{_libdir}/ocaml/mtime/clock/os
mkdir -p %{buildroot}%{_libdir}/ocaml/mtime/top
cp -p _build/src/mtime.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,mli} _build/pkg/META \
   _build/opam %{buildroot}%{_libdir}/ocaml/mtime
cp -p _build/src/mtime_clock.{cmi,cmti,mli} \
   %{buildroot}%{_libdir}/ocaml/mtime/clock
cp -p _build/src-clock/*.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,js,mli} \
   %{buildroot}%{_libdir}/ocaml/mtime/clock/os
cp -p _build/src/mtime_top_init.ml %{buildroot}%{_libdir}/ocaml/mtime
cp -p _build/src/mtime_top.{a,cma,cmi,cmt,cmx,cmxa,cmxs} \
   %{buildroot}%{_libdir}/ocaml/mtime/top
mkdir -p %{buildroot}%{_libdir}/ocaml/stublibs
cp -p _build/src-clock/*.so %{buildroot}%{_libdir}/ocaml/stublibs
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
* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.4.0-2
- Link with the math library
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-2
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Version 1.4.0

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  1 2021 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Initial RPM
