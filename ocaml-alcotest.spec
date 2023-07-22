# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# To build all parts of alcotest requires the async, js_of_ocaml, and lwt
# packages.  The async package in particular requires many packages that test
# with alcotest.  We build only the base alcotest package to break the circular
# dependency.
%bcond_with async

%global srcname alcotest

Name:           ocaml-%{srcname}
Version:        1.7.0
Release:        4%{?dist}
Summary:        Lightweight and colorful test framework for OCaml

License:        ISC
URL:            https://github.com/mirage/alcotest
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# We neither need nor want the stdlib-shims or ocaml-syntax-shims packages in
# Fedora.  They are forward compatibility packages for older OCaml
# installations.  Patch them out instead.  Upstream does not want this patch
# until stdlib-shims and ocaml-syntax-shims are obsolete.
Patch0:         0001-Drop-the-stdlib-shims-subpackage.patch
# Fix a test failure on bytecode-only architectures
Patch1:         https://github.com/mirage/alcotest/commit/219dc8b.patch

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-fmt-devel >= 0.8.7
BuildRequires:  ocaml-re-devel >= 1.7.2
BuildRequires:  ocaml-uutf-devel >= 1.0.1

%if %{with async}
BuildRequires:  js-of-ocaml-compiler-devel >= 3.11.0
BuildRequires:  ocaml-async-devel >= 0.15.0
BuildRequires:  ocaml-async-kernel-devel
BuildRequires:  ocaml-async-unix-devel >= 0.15.0
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-core-devel >= 0.15.0
BuildRequires:  ocaml-core-unix-devel >= 0.15.0
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel
%endif

%description
Alcotest is a lightweight and colorful test framework.

Alcotest exposes a simple interface to perform unit tests, including a
simple `TESTABLE` module type, a `check` function to assert test
predicates, and a `run` function to perform a list of `unit -> unit`
test callbacks.

Alcotest provides quiet and colorful output where only faulty runs are
fully displayed at the end of the run (with the full logs ready to
inspect), with a simple (yet expressive) query language to select the
tests to run.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}

%if %{with async}
Requires:       ocaml-async-devel
Requires:       ocaml-lwt-devel
%endif

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%if %{with async}
%dune_build
%else
%dune_build -p alcotest
%endif

%install
%if %{with async}
%dune_install
%else
%dune_install alcotest
%endif

%check
%if %{with async}
%dune_check
%else
%dune_check -p alcotest
%endif

%files -f .ofiles
%doc CHANGES.md README.md alcotest-help.txt
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-3
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.7.0-2
- OCaml 5.0.0 rebuild
- Add upstream patch to fix bytecode build

* Tue Mar 21 2023 Jerry James <loganjerry@gmail.com> - 1.7.0-1
- Version 1.7.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.6.0-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Jerry James <loganjerry@gmail.com> - 1.6.0-1
- Version 1.6.0
- Optionally build with lwt, js, and async support

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.5.0-5
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-5
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 1.5.0-4
- Rebuild for ocaml-uutf 1.0.3
- Drop unnecessary ocaml-uuidm BR

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Version 1.5.0

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Version 1.4.0

* Mon Mar  1 14:32:28 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-2
- OCaml 4.12.0 build

* Tue Feb 16 2021 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Version 1.3.0

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-4
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  2 2020 Jerry James <loganjerry@gmail.com> - 1.2.3-2
- Rebuild for ocaml-fmt 0.8.9

* Sun Sep 13 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.2.3-1
- New upstream release 1.2.3 (rhbz#1876739)

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.2-2
- OCaml 4.11.1 rebuild

* Wed Aug 26 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.2.2-1
- New upstream release 1.2.2 (rhbz#1872839)

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.2.1-1
- New upstream release 1.2.1 (rhbz#1856364)

* Fri Jun 19 2020 Jerry James <loganjerry@gmail.com> - 1.1.0-4
- Rebuild for ocaml-astring 0.8.4

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr  4 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.1.0-1
- New upstream release 1.1.0
- Rebase ocaml-alcotest-stdlib-shims.patch as 0001-Drop-the-stdlib-shims-subpackage.patch

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-3
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-2
- OCaml 4.10.0 final.

* Wed Feb 12 2020 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Version 1.0.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-2
- OCaml 4.10.0+beta1 rebuild.

* Tue Jan 14 2020 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- Version 1.0.0

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 0.8.5-1
- Initial RPM
