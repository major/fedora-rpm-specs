# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Enable building and running the tests
# This is disabled by default, because ocaml-lwt requires this package to build.
%bcond_with test

Name:           ocaml-ctypes
Version:        0.20.2
Release:        3%{?dist}
Summary:        Combinators for binding to C libraries without writing any C

License:        MIT
URL:            https://yallop.github.io/ocaml-ctypes/
Source0:        https://github.com/yallop/ocaml-ctypes/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-bigarray-compat-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-integers-devel >= 0.3.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  pkgconfig(libffi)
BuildRequires:  python3

%if %{with test}
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  ocaml-bisect-ppx-devel
BuildRequires:  ocaml-lwt-devel >= 3.2.0
BuildRequires:  ocaml-ounit-devel
%endif

%description
Ctypes is a library for binding to C libraries using pure OCaml.  The
primary aim is to make writing C extensions as straightforward as
possible.

The core of ctypes is a set of combinators for describing the structure
of C types -- numeric types, arrays, pointers, structs, unions and
functions.  You can use these combinators to describe the types of the
functions that you want to call, then bind directly to those functions --
all without writing or generating any C!

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-bigarray-compat-devel%{?_isa}
Requires:       ocaml-integers-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains developer documentation for
%{name}.

%prep
%autosetup

# Use Fedora flags
sed -i 's|-fPIC -Wall -O3|-fPIC %{build_cflags}|' Makefile.rules
sed -i 's|-fPIC -Wall -g|-fPIC %{build_cflags}|' Makefile.rules
sed -i 's|=-Wl,--no-as-needed|=%{build_ldflags} -lm|' src/discover/determine_as_needed_flags.sh

# Flags for bigarray-compat are missing
sed -i 's/(OCAMLFIND_BISECT_FLAGS)/& -package bigarray-compat/' Makefile.rules
sed -i 's/^DOCFLAGS=/&-I $(shell ocamlfind query bigarray-compat) /' Makefile

# Don't try to update the system ld.conf
sed -i 's|-add ctypes|& -ldconf %{buildroot}%{ocamldir}/ld.conf|' Makefile

# Fix the name of ounit
sed -i 's/oUnit/ounit2/g' Makefile.tests

# For OCaml 5.0, do not depend on bytes
sed -i 's/ bytes//' META

%build
# FIXME: Infrequent build failures with parallel build
# It looks like the configuration step isn't done before its results are needed
make all XEN=disable OCAMLMKLIB_EXTRA_FLAGS='-g -lm'
%make_build doc XEN=disable

%install
export DESTDIR=%{buildroot}%{ocamldir}
export OCAMLFIND_DESTDIR=$DESTDIR
mkdir -p $DESTDIR/stublibs
touch $DESTDIR/ld.conf
make install XEN=disable
rm $DESTDIR/ld.conf

# We install the documentation elsewhere
rm $DESTDIR/ctypes/*.md

# Install the opam files, fixing the version number
mkdir -p $DESTDIR/ctypes-foreign
sed 's/"dev"/"%{version}"/' ctypes-foreign.opam > $DESTDIR/ctypes-foreign/opam
sed 's/"dev"/"%{version}"/' ctypes.opam > $DESTDIR/ctypes/opam

%ocaml_files

%if %{with test}
%check
make test
%endif

%files -f .ofiles
%license LICENSE
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%files doc
%license LICENSE
%doc *.html *.css

%changelog
* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.20.2-3
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.20.2-2
- OCaml 5.0.0 rebuild

* Tue Mar 21 2023 Jerry James <loganjerry@gmail.com> - 0.20.2-1
- Version 0.20.2

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.20.1-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Jerry James <loganjerry@gmail.com> - 0.20.1-3
- New URLs

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.20.1-2
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.20.1-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 0.20.1-1
- Version 0.20.1
- Link with -lm

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.20.0-5
- Rebuild for ocaml-integers 0.6.0

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.20.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Dec  9 2021 Jerry James <loganjerry@gmail.com> - 0.20.0-1
- Version 0.20.0

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.19.1-4
- OCaml 4.13.1 build

* Fri Aug  6 2021 Jerry James <loganjerry@gmail.com> - 0.19.1-3
- Rebuild for ocaml-integers 0.5.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 26 2021 Jerry James <loganjerry@gmail.com> - 0.19.1-1
- Version 0.19.1

* Mon Mar  1 13:12:29 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.18.0-2
- OCaml 4.12.0 build

* Tue Feb 09 2021 Jerry James <loganjerry@gmail.com> - 0.18.0-1
- Initial package
