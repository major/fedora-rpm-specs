# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Running the tests requires ocaml-ounit, which introduces a circular
# dependency (also involving ocaml-lwt).  The tests also require ocamlformat,
# introducing a second circular dependency.  Break the cycles with this
# conditional.
%bcond test 0

%global giturl  https://github.com/aantron/bisect_ppx

Name:           ocaml-bisect-ppx
Version:        2.8.3
Release:        15%{?dist}
Summary:        Code coverage for OCaml and Reason

# The project as a whole is MIT.
# The embedded copy of highlight.js is BSD-3-Clause.
License:        MIT AND BSD-3-Clause
URL:            https://aantron.github.io/bisect_ppx/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/bisect_ppx-%{version}.tar.gz

BuildRequires:  git-core
BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-dune >= 2.7.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%if %{with test}
BuildRequires:  ocamlformat
%endif

# This can be removed when Fedora 40 reaches EOL
Obsoletes:      %{name}-doc < 2.5.0-1
Provides:       %{name}-doc = %{version}-%{release}

%description
Bisect_ppx is a code coverage tool for OCaml.  It helps you test
thoroughly by showing which parts of your code are *not* tested.  It is
a small preprocessor that inserts instrumentation at places in your
code, such as if-then-else and match expressions.  After you run tests,
Bisect_ppx gives a nice HTML report showing which places were visited
and which were missed.

Usage is simple - add package bisect_ppx when building tests, run your
tests, then run the Bisect_ppx report tool on the generated visitation
files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n bisect_ppx-%{version}

%build
%dune_build

%install
%dune_install

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
_build/install/default/bin/bisect-ppx-report --help groff > \
  %{buildroot}%{_mandir}/man1/bisect-ppx-report.1

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc doc/advanced.md doc/CHANGES README.md
%license LICENSE.md
%{_mandir}/man1/bisect-ppx-report.1*

%files devel -f .ofiles-devel

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 2.8.3-14
- OCaml 5.3.0 rebuild for Fedora 42

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 2.8.3-13
- Rebuild for ocaml-ppxlib 0.33.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Jerry James <loganjerry@gmail.com> - 2.8.3-11
- Rebuild for ocaml-sexplib0 0.17.0

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 2.8.3-10
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 2.8.3-9
- OCaml 5.2.0 for Fedora 41

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 2.8.3-8
- Rebuild for changed ocamlx hashes

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 2.8.3-5
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.8.3-4
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2.8.3-3
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jerry James <loganjerry@gmail.com> - 2.8.3-1
- Version 2.8.3
- Drop upstreamed patches

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 2.8.2-3
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2.8.2-2
- OCaml 5.0.0 rebuild

* Fri Apr 14 2023 Jerry James <loganjerry@gmail.com> - 2.8.2-1
- Version 2.8.2
- Drop upstreamed ppat-construct patch

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.8.1-8
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Jerry James <loganjerry@gmail.com> - 2.8.1-6
- Rebuild for ocaml-ppxlib 0.28.0
- Add patch to adapt to changed API in ppxlib 0.28.0

* Tue Sep 20 2022 Jerry James <loganjerry@gmail.com> - 2.8.1-5
- Rebuild for ocaml-cmdliner 1.1.1

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 2.8.1-4
- Rebuild for ocaml-ppxlib 0.27.0
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 2.8.1-2
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 2.8.1-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 2.8.1-1
- Add patches for recent ocamlformat and ppxlib

* Fri Mar 25 2022 Jerry James <loganjerry@gmail.com> - 2.8.1-1
- Version 2.8.1

* Fri Feb 11 2022 Jerry James <loganjerry@gmail.com> - 2.8.0-1
- Version 2.8.0

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2.7.1-2
- OCaml 4.13.1 rebuild to remove package notes

* Thu Feb  3 2022 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- Version 2.7.1

* Wed Jan 26 2022 Richard W.M. Jones <rjones@redhat.com> - 2.7.0-4
- Rebuild to pick up new ocaml dependency

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 2.7.0-2
- Rebuild for ocaml-ppxlib 0.24.0

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 2.7.0-1
- Version 2.7.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 2.6.3-3
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 2.6.3-2
- Rebuild for ocaml-ppxlib 0.23.0

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 2.6.3-1
- Version 2.6.3

* Tue Jul 27 2021 Richard W.M. Jones <rjones@redhat.com> - 2.6.2-3
- Rebuild for changed ocamlx(Dynlink)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 2.6.1-2
- Rebuild for ocaml-ppxlib 0.22.1

* Tue May  4 2021 Jerry James <loganjerry@gmail.com> - 2.6.1-1
- Version 2.6.1

* Mon Mar  1 16:58:04 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-2
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- Version 2.6.0

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 2.5.0-4
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 2.5.0-2
- Rebuild for ocaml-migrate-parsetree 1.8.0

* Fri Oct 23 2020 Jerry James <loganjerry@gmail.com> - 2.5.0-1
- Version 2.5.0
- Building documentation with ocamldoc no longer works

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-6
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-5
- OCaml 4.11.0 rebuild

* Mon Aug 03 2020 Richard W.M. Jones <rjones@redhat.com> - 2.4.1-4
- Bump and rebuild to fix Location dependency.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.4.1-1
- New upstream release 2.4.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.3.2-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.3.2-2
- OCaml 4.11.0 pre-release attempt 2

* Sun Apr 19 2020 Jerry James <loganjerry@gmail.com> - 2.3.2-1
- Version 2.3.2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.3.1-1
- Version 2.3.1
- Add conditional for building documentation with odoc

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.1-5.20200106.b2661bf
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.1-4.20200106.b2661bf
- OCaml 4.10.0 final.
- Disable the tests to avoid circular dependency.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3.20200106.b2661bf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.1-2.20200106.b2661bf
- OCaml 4.10.0+beta1 rebuild.

* Wed Jan  8 2020 Jerry James <loganjerry@gmail.com> - 1.4.1-1.20200106.b2661bf
- Initial RPM
