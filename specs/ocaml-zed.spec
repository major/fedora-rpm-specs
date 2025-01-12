# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-zed
Version:        3.2.3
Release:        12%{?dist}
Summary:        Abstract engine for text editing in OCaml

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/zed
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/zed-%{version}.tar.gz
# We don't need the uchar forwards compatibility package
Patch0:         %{name}-uchar.patch

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-uucp-devel >= 2.0.0
BuildRequires:  ocaml-uuseg-devel
BuildRequires:  ocaml-uutf-devel

%description
Zed is an abstract engine for text editing.  It can be used to
write text editors, editing widgets, readlines, ...  You just
have to connect an engine to your inputs and rendering functions
to get an editor.

Zed provides: editing state management, multiple cursor support,
key-binding helpers, and general purpose unicode rope
manipulation functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-react-devel%{_isa}
Requires:       ocaml-result-devel%{_isa}
Requires:       ocaml-uucp-devel%{_isa}
Requires:       ocaml-uuseg-devel%{_isa}
Requires:       ocaml-uutf-devel%{_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n zed-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 3.2.3-12
- OCaml 5.3.0 rebuild for Fedora 42

* Tue Sep 17 2024 Jerry James <loganjerry@gmail.com> - 3.2.3-11
- Rebuild for ocaml-uucp and ocaml-uuseg 16.0.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 3.2.3-9
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 3.2.3-8
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2.3-5
- Bump release and rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2.3-4
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2.3-3
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2.3-2
- OCaml 5.1 rebuild for Fedora 40

* Mon Sep 11 2023 Jerry James <loganjerry@gmail.com> - 3.2.3-1
- Version 3.2.3

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2.2-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 3.2.2-1
- Version 3.2.2
- Convert License tag to SPDX
- Use new dune macros

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-14
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-11
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-10
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-8
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 16:58:00 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-6
- OCaml 4.12.0 build

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-5
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-2
- OCaml 4.11.0 rebuild

* Tue Aug  4 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Version 3.1.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-9
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-8
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-7
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-6
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-4
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-3
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-2
- OCaml 4.08.1 (final) rebuild.

* Sun Aug 11 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.3-1
- Updated to latest upstream release.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-2
- OCaml 4.08.1 (rc2) rebuild.

* Mon Jul 29 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.2-1
- Updated to latest upstream release.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.6-8
- OCaml 4.08.0 (final) rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.6-7
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.6-4
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.6-3
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.6-1
- New upstream version 1.6 (includes safe-string fixes).
- OCaml 4.06.0 rebuild.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> 1.5-2
- Modernize OCaml packaging.

* Fri Aug 11 2017 Ben Rosser <rosser.bjr@gmail.com> 1.5-1
- Initial packaging.
