%undefine _package_note_flags

# Uncomment this for bugfix releases
%global bugfix bugfix2

Name:           ocaml-mlmpfr
Version:        4.1.0
Release:        14%{?dist}%{?bugfix:.%{bugfix}}
Summary:        OCaml bindings for MPFR

License:        LGPLv3
URL:            https://github.com/thvnx/mlmpfr
Source0:        %{url}/archive/mlmpfr.%{version}%{?bugfix:-%{bugfix}}.tar.gz
# Fix a race between 2 invocations of the same test rule
Patch0:         %{name}-test.patch

BuildRequires:  ocaml >= 4.04
BuildRequires:  ocaml-dune >= 1.11.0
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
%autosetup -n mlmpfr-mlmpfr.%{version}%{?bugfix:-%{bugfix}} -p1

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
%doc Changes README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
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
