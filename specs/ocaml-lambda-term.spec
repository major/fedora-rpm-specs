# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-lambda-term
Version:        3.3.2
Release:        13%{?dist}
Summary:        Terminal manipulation library for OCaml

License:        BSD-3-Clause
URL:            https://github.com/ocaml-community/lambda-term
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/lambda-term-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel >= 4.2.0
BuildRequires:  ocaml-lwt-react-devel
BuildRequires:  ocaml-mew-vi-devel >= 0.5.0
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-zed-devel >= 3.2.0

%description
Lambda-term is a cross-platform library for manipulating the terminal. It
provides an abstraction for keys, mouse events, colors, as well as a set of
widgets to write curses-like applications.

The main objective of lambda-term is to provide a higher level functional
interface to terminal manipulation than, for example, ncurses, by providing
a native OCaml interface instead of bindings to a C library.

Lambda-term integrates with zed to provide text editing facilities in
console applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}
Requires:       ocaml-lwt-react-devel%{?_isa}
Requires:       ocaml-mew-vi-devel%{?_isa}
Requires:       ocaml-uucp-devel%{?_isa}
Requires:       ocaml-zed-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n lambda-term-%{version}

%build
%dune_build

%install
%dune_install

mkdir -p %{buildroot}%{_datadir}/lambda-term
mv %{buildroot}%{_datadir}/lambda-term{rc,-inputrc} %{buildroot}%{_datadir}/lambda-term
sed -e 's,%{_datadir}/lambda-termrc,%{_datadir}/lambda-term,' \
    -e '\,%{_datadir}/lambda-term-inputrc,d' \
    -i .ofiles

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc CHANGES.md README.md

%files devel -f .ofiles-devel
%license LICENSE

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 3.3.2-13
- OCaml 5.3.0 rebuild for Fedora 42

* Tue Oct 08 2024 Richard W.M. Jones <rjones@redhat.com> - 3.3.2-12
- Rebuild for ocaml-lwt 5.8.0

* Tue Sep 17 2024 Jerry James <loganjerry@gmail.com> - 3.3.2-11
- Rebuild for ocaml-uucp 16.0.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 3.3.2-9
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 3.3.2-8
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 3.3.2-5
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 3.3.2-4
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 3.3.2-3
- OCaml 5.1 rebuild for Fedora 40

* Tue Sep 19 2023 Jerry James <loganjerry@gmail.com> - 3.3.2-2
- Rebuild to fix ocaml-zed dependency in F39

* Mon Sep 11 2023 Jerry James <loganjerry@gmail.com> - 3.3.2-1
- Version 3.3.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 3.3.1-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 3.3.1-1
- Version 3.3.1

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2.0-4
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 3.2.0-2
- Bump and rebuild

* Mon Aug  8 2022 Jerry James <loganjerry@gmail.com> - 3.2.0-1
- Version 3.2.0
- Convert license to SPDX
- Use new OCaml macros

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-14
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-13
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Jerry James <loganjerry@gmail.com> - 3.1.0-11
- Rebuild for changed ocaml-lwt hashes

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-10
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun  3 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-8
- Rebuild for new ocaml-lwt.

* Mon Mar  1 19:41:30 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-7
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 3.1.0-6
- Rebuild for ocaml-lwt 5.4.0

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-5
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-2
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Version 3.1.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-2
- OCaml 4.11.0 pre-release attempt 2

* Thu Apr 16 2020 Jerry James <loganjerry@gmail.com> - 2.0.3-1
- Version 2.0.3
- Drop unneeded libev-devel BR
- Relink the stublib with $RPM_LD_FLAGS

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-3
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.2-1
- Update build scripts to use dune
- Update to latest upstream release

* Fri Aug 02 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.1-1
- Updated to latest upstream release (rhbz#1714129).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.13-1
- Updated to latest upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Dec 15 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.12.0-1
- Updated to latest upstream release.

* Thu Aug 31 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.11-1
- Initial packaging.
