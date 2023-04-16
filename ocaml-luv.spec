%undefine _package_note_flags

Name:           ocaml-luv
Version:        0.5.12
Release:        2%{?dist}
Summary:        OCaml binding to libuv for cross-platform asynchronous I/O

License:        MIT
URL:            https://github.com/aantron/luv
Source0:        %{url}/releases/download/%{version}/luv-%{version}.tar.gz

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
%autosetup -n luv-%{version}

# Remove spurious executable bits
find . -type f -exec chmod 0644 {} +

%build
export LUV_USE_SYSTEM_LIBUV=yes
%dune_build

# Relink the stublibs with Fedora flags
cd _build/default/src/c
ocamlmklib -g -ldopt "%{build_ldflags}" -o luv_c_stubs \
  $(ar t libluv_c_stubs.a) -luv
cd -
cd _build/default/src/unix
ocamlmklib -g -ldopt "%{build_ldflags}" -o luv_unix_stubs \
  $(ar t libluv_unix_stubs.a)
cd -

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
