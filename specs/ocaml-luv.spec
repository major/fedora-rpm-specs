# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/aantron/luv

Name:           ocaml-luv
Version:        0.5.12
Release:        18%{?dist}
Summary:        OCaml binding to libuv for cross-platform asynchronous I/O

License:        MIT
URL:            https://aantron.github.io/luv/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/luv-%{version}.tar.gz
# Fix incompatible pointer type errors with ocaml-cyptes 0.23.0
Patch:          %{name}-incompatible-pointer-type.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-alcotest-devel >= 0.8.1
BuildRequires:  ocaml-ctypes-devel >= 0.14.0
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  pkgconfig(libuv)

%description
Luv is a binding to libuv, the cross-platform C library that does
asynchronous I/O in Node.js and runs its main loop.

Besides asynchronous I/O, libuv also supports multiprocessing and
multithreading.  Multiple event loops can be run in different threads.
Libuv also exposes a lot of other functionality, amounting to a full OS
API, and an alternative to the standard module Unix.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ctypes-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n luv-%{version} -p1

# Remove spurious executable bits
find . -type f -exec chmod 0644 {} +

%build
export LUV_USE_SYSTEM_LIBUV=yes
%dune_build

%install
export LUV_USE_SYSTEM_LIBUV=yes
%dune_install

%check
export LUV_USE_SYSTEM_LIBUV=yes
%dune_check

%files -f .ofiles
%license LICENSE.md
%doc README.md

%files devel -f .ofiles-devel

%changelog
* Wed Jan 22 2025 Jerry James <loganjerry@gmail.com> - 0.5.12-18
- Bump and rebuild (rhbz#2338802)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 0.5.12-16
- OCaml 5.3.0 rebuild for Fedora 42

* Mon Aug 12 2024 Jerry James <loganjerry@gmail.com> - 0.5.12-15
- Rebuild for ocaml-ctypes 0.23.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.5.12-13
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 0.5.12-12
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.5.12-9
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.5.12-8
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.5.12-7
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Jerry James <loganjerry@gmail.com> - 0.5.12-5
- Rebuild for ocaml-ctypes 0.21.0

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.5.12-4
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.5.12-3
- OCaml 5.0.0 rebuild

* Fri Apr 14 2023 Jerry James <loganjerry@gmail.com> - 0.5.12-2
- Rebuild for respun upstream tarball

* Mon Apr 10 2023 Jerry James <loganjerry@gmail.com> - 0.5.12-1
- Version 0.5.12

* Tue Mar 21 2023 Jerry James <loganjerry@gmail.com> - 0.5.11-8
- Rebuild for ocaml-ctypes 0.20.2

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.5.11-7
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.5.11-4
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.5.11-4
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.5.11-3
- Rebuild for ocaml-integers 0.6.0

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.5.11-2
- OCaml 4.13.1 rebuild to remove package notes

* Thu Feb  3 2022 Jerry James <loganjerry@gmail.com> - 0.5.11-1
- Version 0.5.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.5.10-2
- OCaml 4.13.1 build

* Fri Aug  6 2021 Jerry James <loganjerry@gmail.com> - 0.5.10-1
- Version 0.5.10
- Drop -32bit patch, fixed upstream

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 0.5.9-1
- Version 0.5.9
- ESOCKTNOSUPPORT is unavailable on 32-bit systems due to integer overflow

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 26 2021 Jerry James <loganjerry@gmail.com> - 0.5.8-2
- Rebuild for ocaml-ctypes 0.19.1

* Mon May 10 2021 Jerry James <loganjerry@gmail.com> - 0.5.8-1
- Version 0.5.8

* Mon Mar  1 15:16:17 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.5.7-2
- OCaml 4.12.0 build
- Make the -doc subpackage conditional.

* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 0.5.7-1
- Version 0.5.7

* Tue Feb 09 2021 Jerry James <loganjerry@gmail.com> - 0.5.6-1
- Initial package
