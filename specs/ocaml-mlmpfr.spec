# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Uncomment this for bugfix releases
#%%global bugfix bugfix2

%global giturl  https://github.com/thvnx/mlmpfr

Name:           ocaml-mlmpfr
Version:        4.2.1
Release:        7%{?dist}%{?bugfix:.%{bugfix}}
Summary:        OCaml bindings for MPFR

# FIXME: the individual files say LGPL-3.0-or-later, but opam says this:
License:        LGPL-3.0-only
URL:            https://thvnx.github.io/mlmpfr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/mlmpfr.%{version}.tar.gz
# Fix a build failure with OCaml 5.3.0
Patch:          %{name}-internals.patch
# Adapt the tests to dune 3.17.0
# https://github.com/thvnx/mlmpfr/commit/1e0c151ec39898dcb12d5b2cdc8184e7669f02a3
Patch:          %{name}-dune.patch

BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-dune >= 2.9
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(mpfr)

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-mlmpfr-doc < 4.1.0-13

%description
This library provides OCaml bindings for MPFR.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mpfr-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
%autosetup -n mlmpfr-mlmpfr.%{version} -p1

%build
# Make sure this version is compatible with our mpfr version
cd utils
gcc %{build_cflags} %{build_ldflags} mlmpfr_compatibility_test.c \
    -o mlmpfr_compatibility_test -lmpfr
./mlmpfr_compatibility_test
cd -

# Build the binary artifacts and documentation
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 4.2.1-7
- OCaml 5.3.0 rebuild for Fedora 42
- Add patch to fix a build failure with OCaml 5.3.0
- Add patch to adapt the tests to dune 3.17.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 4.2.1-5
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 4.2.1-4
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jerry James <loganjerry@gmail.com> - 4.2.1-1
- Version 4.2.1

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 4.2.0-6
- Bump release and rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 4.2.0-5
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.2.0-4
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 4.2.0-3
- Bump release and rebuild

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 4.2.0-2
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- Update to git HEAD for MPFR 4.2.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-6.20230309git14fce8a
- Update to git HEAD for MPFR 4.2.0

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-5
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-4
- OCaml 5.0.0 rebuild
- The 4.1.1 release was respun without needing the compatibility patch

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- Version 4.1.1
- Drop upstreamed -test patch
- Add -compatibility patch
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 4.1.0-14.bugfix2
- Add -test patch to fix FTBFS

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-14.bugfix2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul  7 2022 Jerry James <loganjerry@gmail.com> - 4.1.0-13.bugfix2
- Update to 4.1.0-bugfix2
- Drop the doc subpackage and the odoc dependency
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-12
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-11
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-9
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 4.1.0-7
- Run mlmpfr_compatibility_test in %%build
- There is no circular dependency so always build docs

* Mon Mar  1 17:08:40 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-7
- OCaml 4.12.0 build
- Make -doc subpackage conditional.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- Version 4.1.0
- Drop upstreamed -32bit patch

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.2-4
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.2-3
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.2-2
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 4.0.2-1
- Initial RPM
