%undefine _package_note_flags

Name:           ocaml-stdcompat
Version:        19
Release:        5%{?dist}
Summary:        Compatibility module for the OCaml standard library

License:        BSD-2-Clause
URL:            https://github.com/thierry-martinez/stdcompat
Source0:        %{url}/releases/download/v%{version}/stdcompat-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  python3

%description
Stdcompat is a compatibility layer allowing programs to use some recent
additions to the OCaml standard library while preserving the ability to
be compiled on former versions of OCaml.

The Stdcompat API is not intended to be stable, but there will be
efforts to allow future versions of Stdcompat to be compiled on a large
range of versions of OCaml: Stdcompat should compile (at least) on every
version of OCaml from 3.08 (inclusive).

The module Stdcompat provides some definitions for values and types
introduced in recent versions of the standard library.  These
definitions are just aliases to the matching definition of the standard
library if the latter is recent enough.  Otherwise, the module Stdcompat
provides an alternative implementation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n stdcompat-%{version} -p1

# Generate debuginfo
sed -i 's/-nolabels/-g &/' Makefile.in

%build
%configure --libdir=%{ocamldir}

# Parallel make does NOT work; there seem to be missing dependencies
make all

%install
%make_install

# We do not want the ml files
find %{buildroot}%{ocamldir} -name \*.ml -delete

# Install the mli files
cp -p *.mli %{buildroot}%{ocamldir}/stdcompat

# Install the opam file
cp -p stdcompat.opam %{buildroot}%{ocamldir}/stdcompat/opam

# Remove spurious executable bits
chmod a-x %{buildroot}%{ocamldir}/stdcompat/*.{a,cma,cmi,cmt,cmx,cmxa,h}

%ocaml_files

%check
make test

%files -f .ofiles
%doc AUTHORS ChangeLog README
%license COPYING

%files devel -f .ofiles-devel

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 19-4
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 19-3
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 19-3
- Bump release and rebuild.

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 19-2
- OCaml 4.14.0 rebuild

* Thu Jun 16 2022 Jerry James <loganjerry@gmail.com> - 19-1
- Version 19

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 18-1
- Version 18

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 17-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Jerry James <loganjerry@gmail.com> - 17-1
- Initial RPM
