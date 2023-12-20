# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# This package is needed to build ppx_jane, but its tests require ppx_jane.
# Break the dependency cycle here.
%bcond_with test

Name:           ocaml-base
Version:        0.16.3
Release:        4%{?dist}
Summary:        Jane Street standard library for OCaml

# MIT: The project as a whole
# Apache-2.0: src/map.ml, src/random.mli, src/set.ml
License:        MIT AND Apache-2.0
URL:            https://opensource.janestreet.com/base/
Source0:        https://github.com/janestreet/base/archive/v%{version}/base-%{version}.tar.gz
# Expose a dependency on the math library so RPM can see it
Patch0:         %{name}-mathlib.patch

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-sexplib0-devel >= 0.16

%if %{with test}
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-stdio-devel
BuildRequires:  ocaml-uutf-devel
%endif

%description
Base is a standard library for OCaml.  It provides a standard set of
general purpose modules that are well-tested, performant, and
fully-portable across any environment that can run OCaml code.  Unlike
other standard library projects, Base is meant to be used as a wholesale
replacement of the standard library distributed with the OCaml compiler.
In particular it makes different choices and doesn't re-export features
that are not fully portable such as I/O, which are left to other
libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n base-%{version} -p1

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.org ROADMAP.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.3-4
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.3-3
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.3-2
- OCaml 5.1 rebuild for Fedora 40

* Sat Aug  5 2023 Jerry James <loganjerry@gmail.com> - 0.16.3-1
- Version 0.16.3

* Fri Jul 21 2023 Jerry James <loganjerry@gmail.com> - 0.16.2-1
- Version 0.16.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.1-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.16.1-1
- Version 0.16.1
- Drop upstreamed OCaml 4.13 patch

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.15.1-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- Add Apache-2.0 to the License tag while converting to SPDX

* Mon Oct 31 2022 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- Version 0.15.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Optionally run tests
- Link against the math library
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-5
- OCaml 4.14.0 rebuild

* Thu Feb 24 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-4
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0
- Add patch for OCaml 4.13 compatibility

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-4
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 12:17:33 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.1-2
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- Version 0.14.1

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-6
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-4
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Tue May 12 2020 Jerry James <loganjerry@gmail.com> - 0.13.2-1
- Version 0.13.2

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.1-5
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.1-4
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.1-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.1-2
- OCaml 4.10.0 final.

* Tue Feb 18 2020 Jerry James <loganjerry@gmail.com> - 0.13.1-1
- Version 0.13.1
- Drop upstreamed -gc patch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-3
- Add -gc patch to fix FTBFS with OCaml 4.10

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-3
- OCaml 4.10.0+beta1 rebuild.

* Wed Jan 15 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Add R on ocaml-sexplib0-devel to the -devel subpackage
- Pass smp_mflags to dune build

* Thu Jan  2 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
