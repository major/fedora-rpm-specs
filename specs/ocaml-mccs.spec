# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Upstream uses a + character in the version, which RPM does not support.
# We transform the + into a period.  See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/#_upstream_uses_invalid_characters_in_the_version
%global basever  1.1
%global extraver 19

Name:           ocaml-mccs
Version:        %{basever}.%{extraver}
Release:        1%{?dist}
Summary:        Multi Criteria CUDF Solver with OCaml bindings

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# Original C/C++ code is BSD-3-Clause, OCaml bindings are LGPL.
# The bundled glpk code is not used.
License:        BSD-3-Clause AND LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception

URL:            https://github.com/AltGr/ocaml-mccs
VCS:            git:%{url}.git

# Upstream's use of a '+' instead of a '.' makes this hard to use a macro.
Source:         https://github.com/AltGr/ocaml-mccs/archive/%{basever}+%{extraver}/%{name}-%{basever}-%{extraver}.tar.gz

# Link against the system glpk library
Patch:          ocaml-mccs-1.1-glpk.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  gcc, gcc-c++
BuildRequires:  ocaml-cudf-devel
BuildRequires:  glpk-devel

%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem
solver developed at UNS during the European MANCOOSI project.

This project contains a stripped-down version of the mccs solver,
taken from snapshot 1.1, with a binding as an OCaml library, and
building with dune.

The binding enables interoperation with binary CUDF data from the
OCaml CUDF library, and removes the native C++ parsers and printers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cudf-devel%{?_isa}
Requires:       glpk-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{basever}-%{extraver} -p1

# Choose the build method that uses an installed glpk
cp -p src/glpk/dune-shared src/glpk/dune

# Temporary workaround for https://github.com/ocaml-opam/ocaml-mccs/issues/54
sed -i 's,clibs,../clibs,' src/glpk/dune

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENCE
%doc README.md

%files devel -f .ofiles-devel

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 1.1.19-1
- OCaml 5.3.0 rebuild for Fedora 42
- New version 1.1+19
- New versioning scheme

* Thu Aug 22 2024 Jerry James <loganjerry@gmail.com> - 1.1-53.18
- New version 1.1+18

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-52.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.1-51.17
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.1-50.17
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-49.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-48.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Richard W.M. Jones <rjones@redhat.com> - 1.1-47.17
- New upstream version 1.1+17 (RHBZ#2255456)

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-46.16
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-45.16
- Bump release and rebuild

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-44.16
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-43.16
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-42.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-41.16
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.1-40.16
- New version 1.1+16
- Use new dune macros
- Add a %%check script

* Wed Feb 15 2023 Jerry James <loganjerry@gmail.com> - 1.1-40.14
- Convert License tag to SPDX

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-40.14
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-39.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-38.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1-37.14
- OCaml 4.14.0 rebuild

* Sat May 21 2022 Robin Lee <cheeselee@fedoraproject.org> - 1.1-36.14
- New verbose 1.1+14 (RHBZ#2088018)
- Drop unneeded ocaml-mccs-1.1-c++-flags.patch

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 1.1-36.13
- Link with the system glpk library
- Build in release mode

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1-36.13
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-35.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1-34.13
- OCaml 4.13.1 build

* Fri Aug 27 2021 Jerry James <loganjerry@gmail.com> - 1.1-33.13
- New version 1.1+13
- Drop upstreamed ocaml-mccs-gcc11.patch
- Unbundle glpk
- Install with dune

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-33.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 21:39:53 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1-32.11
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-30.11
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-29.11
- OCaml 4.11.0 rebuild

* Wed Jul 29 2020 Jeff Law <law@redha.com> - 1.1-27.12
- Make comparison object be invocable as const

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-26.11
- Rebuild for updated ocaml-extlib (RHBZ#1837823).

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-25.11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-24.11
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-23.11
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-22.11
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-21.11
- New version 1.1+11.
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-19.10
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-18.10
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-17.10
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1-15.10
- Updated to latest upstream release (rhbz#1724723).

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-14.8
- OCaml 4.08.0 (final) rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1-13.8
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-10.8
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.1-9.8
- OCaml 4.07.0-rc1 rebuild.

* Wed Jun 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1-8.8
- Updated to latest upstream release (rhbz#1584456).

* Mon May 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1-7.7
- Update to latest upstream release (rhbz#1577188).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1-5.5
- Updated to latest upstream release (#1512145).

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.1-4.4
- OCaml 4.06.0 rebuild.

* Sat Nov 25 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1.3-4
- Update to latest upstream release (#1512145).

* Sun Oct 22 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1-2.3b
- Update to latest upstream release.

* Sat Sep 02 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1-1.2c
- Initial package.
