# Build from git HEAD for OCaml 5.x support
%global commit      d53390d788027fe0a2282c4745eb3d1626341f99
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20240529

Name:           ocaml-stdcompat
Version:        19^%{date}.%{shortcommit}
Release:        2%{?dist}
Summary:        Compatibility module for the OCaml standard library

License:        BSD-2-Clause
URL:            https://github.com/thierry-martinez/stdcompat
VCS:            git:%{url}.git
Source:         %{url}/archive/%{commit}/stdcompat-%{shortcommit}.tar.gz
# Fix detection of OCaml tools
# https://github.com/thierry-martinez/stdcompat/pull/31
Patch:          %{name}-configure.patch
# Add support for OCaml 5.3
# https://github.com/thierry-martinez/stdcompat/pull/35
Patch:          %{name}-ocaml5.3.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros

# Needed only until the configure patch is merged upstream
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

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
%autosetup -n stdcompat-%{commit} -p1

%conf
# Regenerate configure after Patch0 and Patch1
autoreconf -fi .

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
chmod a-x %{buildroot}%{ocamldir}/stdcompat/{META,*.{a,cma,cmi,cmt,h}}
%ifarch %{ocaml_native_compiler}
chmod a-x %{buildroot}%{ocamldir}/stdcompat/*.{cmx,cmxa}
%endif

%ocaml_files

%ifarch %{ocaml_native_compiler}
# The tests assume that ocamlopt is available
%check
LD_LIBRARY_PATH=$PWD make test
%endif

%files -f .ofiles
%doc AUTHORS CHANGES.md README.md
%license COPYING

%files devel -f .ofiles-devel

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19^20240529.d53390d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 19^20240529.d53390d-1
- OCaml 5.3.0 rebuild for Fedora 42
- Update to git HEAD for OCaml 5.x compatibility
- Add patch for OCaml 5.3.0 compatibility

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 19-17
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 19-16
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 19-15
- Add patch for OCaml 5.2.0 compatibility

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 19-13
- Bump release and rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 19-12
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 19-11
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 19-10
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 19-8
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 19-7
- OCaml 5.0.0 rebuild
- Add patch to fix tool detection on bytecode-only arches

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 19-6
- Rebuild OCaml packages for F38

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
