# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://gitlab.com/irill/camlbz2

Name:           ocaml-camlbz2
Version:        0.8.0
Release:        5%{?dist}
Summary:        OCaml bindings for bzip2

License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://irill.gitlab.io/camlbz2
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{version}/camlbz2-%{version}.tar.gz
# Unbundle the OCaml io.h header file
Patch:          %{name}-io-h.patch
# We do not need the stdlib-shims forward compatibility package
Patch:          %{name}-shims.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  pkgconfig(bzip2)

%description
This package contains OCaml bindings for bzip2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bzip2-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n camlbz2-%{version} -p1

# Fix the version number
sed -i 's/0\.7\.1/%{version}/' dune-project

# Make sure we don't use the bundled copy of io.h
rm src/io.h

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc BUGS ChangeLog README
%license COPYING LICENSE

%files devel -f .ofiles-devel

%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 0.8.0-5
- OCaml 5.3.0 rebuild for Fedora 42
- Update the io-h patch for OCaml 5.3.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.8.0-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.8.0-2
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 0.8.0-1
- Version 0.8.0
- Drop upstreamed patches: debuginfo, pervasives, const, ocaml5
- Add patch to avoid use of stdlib-shims
- Build with dune

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-15
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-14
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-13
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-11
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.7.0-10
- OCaml 5.0.0 rebuild
- Add patch for OCaml 5 compatibility

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-9
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-7
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-6
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-6
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-5
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- Initial package
