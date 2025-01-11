# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-pyml
Version:        20231101
Release:        10%{?dist}
Summary:        OCaml bindings for Python

# The project is BSD-2-Clause except for pycaml.mli, which is LGPLv2+
License:        BSD-2-Clause AND LGPL-2.1-or-later
URL:            https://github.com/thierry-martinez/pyml
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/pyml-%{version}.tar.gz
# Fix various incompatibilities with python 3.13.  See:
# https://github.com/thierry-martinez/pyml/issues/84
Patch:          %{name}-python3.13.patch
# Guard against passing NULL to memcpy
Patch:          %{name}-memcpy.patch

BuildRequires:  ocaml >= 3.12.1
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdcompat-devel >= 18
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist numpy}

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

%prep
%autosetup -n pyml-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 20231101-10
- OCaml 5.3.0 rebuild for Fedora 42
- Remove old obsoletes

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231101-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 20231101-8
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 20231101-7
- OCaml 5.2.0 for Fedora 41

* Tue Feb 20 2024 Jerry James <loganjerry@gmail.com> - 20231101-6
- Fix the SPDX expression

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20231101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 20231101-3
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 20231101-2
- OCaml 5.1.1 rebuild for Fedora 40

* Mon Nov  6 2023 Jerry James <loganjerry@gmail.com> - 20231101-1
- Version 20231101
- Drop the library-unload patch
- Drop support for the custom toplevels
- Add memcpy patch

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 20220905-5
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220905-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 20220905-3
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 20220905-2
- OCaml 5.0.0 rebuild

* Wed Feb 15 2023 Jerry James <loganjerry@gmail.com> - 20220905-1
- Version 20220905
- Add library-unload patch to fix test suite crashes
- Convert License tag to SPDX

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 20220615-5
- Rebuild OCaml packages for F38

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
