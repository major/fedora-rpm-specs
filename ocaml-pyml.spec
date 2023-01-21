%undefine _package_note_flags

# Conditionally build the custom toplevels
%bcond_with toplevel

Name:           ocaml-pyml
Version:        20220615
Release:        4%{?dist}
Summary:        OCaml bindings for Python

# The project is BSD except for pycaml.mli, which is LGPLv2+
License:        BSD and LGPLv2+
URL:            https://github.com/thierry-martinez/pyml
Source0:        %{url}/archive/%{version}/pyml-%{version}.tar.gz
# Fix various incompatibilities with python 3.11.  See:
# https://github.com/thierry-martinez/pyml/issues/84
Patch0:         %{name}-python3.11.patch

BuildRequires:  ocaml >= 3.12.1
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdcompat-devel >= 18
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist numpy}

%if %{with toplevel}
BuildRequires:  utop-devel
%else
Obsoletes:      pymltop < 20220322
Obsoletes:      pymlutop < 20220322
%endif

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-pyml-doc < 20220615-3

%description
py.ml provides OCaml bindings for Python 2 and Python 3.  This library
subsumes the pycaml library, which is no longer actively maintained.

The Python library is linked at runtime and the same executable can be
run in a Python 2 or a Python 3 environment.  py.ml does not require any
Python library at compile time.  The only compile time dependency is
Stdcompat to ensure compatibility with all OCaml compiler versions from
3.12.

Bindings are split in three modules:

- Py provides the initialization functions and some high-level bindings,
  with error handling and naming conventions closer to OCaml usages.

- Pycaml provides a signature close to the old Pycaml module, so as to
  ease migration.

- Pywrappers provides low-level bindings, which follow closely the
  conventions of the C bindings for Python.  Submodules
  Pywrappers.Python2 and Pywrappers.Python3 contain version-specific
  bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-stdcompat-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%if %{with toplevel}
%package     -n pymltop
Summary:        Custom OCaml toplevel for Python interaction
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n pymltop
This package contains a custom OCaml toplevel for Python interaction.

%package     -n pymlutop
Summary:        Custom utop-based OCaml toplevel for Python interaction
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       utop%{?_isa}

%description -n pymlutop
This package contains a custom utop-based OCaml toplevel for Python
interaction.
%endif

%prep
%autosetup -n pyml-%{version} -p1

%build
%dune_build

# Relink with Fedora linker flags
cd _build/default
ocamlfind ocamlmklib -ldopt '%{build_ldflags}' -g -o pyml_stubs pyml_stubs.o
cd -

%if %{with toplevel}
# Build custom toplevels without rebuilding the entire library
cp -p pytop.ml pyutop.ml _build/default
cd _build/default
ocamlfind ocamlc -cclib "-L. -lpyml_stubs" -g -a -dllib -lpyml_stubs \
  .pyml.objs/byte/{pyml_arch,pyutils,pytypes,pywrappers,py,pycaml,pyops}.cmo \
  -o pyml2.cma
ocamlfind ocamlmklib -ldopt '%{build_ldflags}' -g -o numpy_stubs numpy_stubs.o
ocamlfind ocamlc -cclib "-L. -lnumpy_stubs" -g -a -dllib -lnumpy_stubs \
  .pyml.objs/byte/numpy.cmo -o numpy.cma
echo "let libdir=\"%{ocamldir}/pyml/\"" > pymltop_libdir.ml
ocamlfind ocamlc -g -package stdcompat -c pymltop_libdir.ml \
  -o pymltop_libdir.cmo
ocamlfind ocamlc -I +compiler-libs -g -c pytop.ml
ocamlfind ocamlmktop -g -linkpkg -cclib "-L. -lnumpy_stubs" \
  -package unix,stdcompat,bigarray pyml2.cma numpy.cma pymltop_libdir.cmo \
  pytop.cmo -o pymltop
ocamlfind ocamlc -g -package stdcompat -thread -package utop -c pyutop.ml \
  -o pyutop.cmo
ocamlfind ocamlc -thread -linkpkg -linkall -predicates create_toploop \
  -package compiler-libs.toplevel,utop,stdcompat pyml2.cma numpy.cma \
  pymltop_libdir.cmo pytop.cmo pyutop.cmo -g -o pymlutop
cd -
%endif

%install
%dune_install

%if %{with toplevel}
# Install the custom top levels
mkdir -p %{buildroot}%{_bindir}
cp -p _build/default/{pymltop,pymlutop} %{buildroot}%{_bindir}
cp -p _build/default/dllnumpy_stubs.so %{buildroot}%{ocamldir}/stublibs
%endif

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE
%if %{with toplevel}
%{ocamldir}/stublibs/dllnumpy_stubs.so
%endif

%files devel -f .ofiles-devel

%if %{with toplevel}
%files -n pymltop
%{_bindir}/pymltop

%files -n pymlutop
%{_bindir}/pymlutop
%endif

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220615-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug  1 2022 Jerry James <loganjerry@gmail.com> - 20220615-3
- Add patch for compatibility with python 3.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220615-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 20220615-2
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 20220615-2
- OCaml 4.14.0 rebuild

* Thu Jun 16 2022 Jerry James <loganjerry@gmail.com> - 20220615-1
- Version 20220615

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 20220325-1
- Version 20220325
- Drop upstreamed -wide-character patch
- Conditionally build the custom toplevels

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 20211015-5
- Rebuild for ocaml-stdcompat 18

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 20211015-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan  7 2022 Jerry James <loganjerry@gmail.com> - 20211015-2
- Modify license to include LGPLv2+
- Change doc subpackage to noarch
- Build the binaries without rebuilding the entire library

* Fri Dec 31 2021 Jerry James <loganjerry@gmail.com> - 20211015-1
- Initial RPM
