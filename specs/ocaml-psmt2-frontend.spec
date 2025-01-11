# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ACoquereau/psmt2-frontend

Name:           ocaml-psmt2-frontend
Version:        0.4.0
Release:        21%{?dist}
Summary:        Parser and typechecker for an extension of SMT-LIB 2

License:        Apache-2.0
URL:            https://acoquereau.github.io/psmt2-frontend/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/psmt2-frontend-%{version}.tar.gz
# Update conf.py for Sphinx 6.x
# https://github.com/ACoquereau/psmt2-frontend/pull/24
Patch:          %{name}-sphinx6.patch

BuildRequires:  make
BuildRequires:  ocaml >= 4.04.2
BuildRequires:  ocaml-dune >= 2.6.0
BuildRequires:  ocaml-menhir >= 20180528
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

# This can be removed when F40 reaches EOL
Obsoletes:      %{name}-doc < 0.4.0-5
Provides:       %{name}-doc = %{version}-%{release}

%description
This package contains a library to parse and typecheck a conservative
extension of the SMT-LIB 2 standard with prenex polymorphism.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}

%description    docs
Documentation for %{name}.

%prep
%autosetup -n psmt2-frontend-%{version} -p1

# Do not use git to find the version; we don't have a git checkout
sed -i '/^git =/d;/^branch=/d;s/^\(version = \).*/\1"%{version}"/' sphinx/conf.py

%build
%dune_build
make sphinx

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%files docs
%doc docs/sphinx

%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 0.4.0-21
- OCaml 5.3.0 rebuild for Fedora 42

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 0.4.0-20
- Rebuild for ocaml-menhir 20240715

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-18
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-17
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-14
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-13
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-12
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-10
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.4.0-9
- OCaml 5.0.0 rebuild

* Tue Mar 21 2023 Jerry James <loganjerry@gmail.com> - 0.4.0-8
- Add patch for Sphinx 6.x compatibility (rhbz#2180496)

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-7
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 0.4.0-5
- New URL
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 21 2022 Jerry James <loganjerry@gmail.com> - 0.4.0-4
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-4
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- Version 0.4.0
- Drop obsolete -autoconf patch
- Add %%check script
- Add -docs subpackage

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1-11
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 0.1-9
- Move META to the main package

* Mon Mar 29 2021 Jerry James <loganjerry@gmail.com> - 0.1-9
- Add -autoconf patch for autoconf 2.71 (bz 1943044)

* Tue Mar  2 11:16:19 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1-8
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-6
- OCaml 4.11.1 rebuild

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-5
- Bump and rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Jerry James <loganjerry@gmail.com> - 0.1-1
- Initial RPM
