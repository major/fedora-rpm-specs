%undefine _package_note_flags

Name:           ocaml-lwt-log
Version:        1.1.1
Release:        25%{?dist}
Summary:        Lwt logging library

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocsigen/lwt_log
Source0:        https://github.com/ocsigen/lwt_log/archive/%{version}/lwt-log-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-lwt-devel

BuildRequires:  ocaml-dune

%description
Lwt-friendly logging library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n lwt_log-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license COPYING
%doc README.md CHANGES

%files devel -f .ofiles-devel

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug  8 2022 Jerry James <loganjerry@gmail.com> - 1.1.1-24
- Rebuild for ocaml-lwt 5.6.1
- Use SPDX license name
- Use new OCaml macros

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-22
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-21
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Jerry James <loganjerry@gmail.com> - 1.1.1-19
- Rebuild for changed ocaml-lwt hashes

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-18
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun  3 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-16
- Rebuild for new ocaml-lwt.

* Mon Mar  1 17:33:25 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-15
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 1.1.1-14
- Rebuild for ocaml-lwt 5.4.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-12
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-11
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-8
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-7
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-3
- Rebuilt for lwt 4.4.

* Tue Aug 27 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-2
- Rebuilt for lwt 4.3.

* Thu Aug 08 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-1
- Update to latest upstream release, 1.1.1.

* Wed Aug 07 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-5
- Fix use of deprecated Lwt_main.exit_hooks in lwt 4.1+.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-2
- Mark cmxs files as executable to generate debuginfo.
- Correct license (it's LGPLv2+, not BSD).
- Remove license from devel package.
- Fix FSF address in mli header files.

* Tue Oct 16 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-1
- Initial packaging.
