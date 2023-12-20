# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifarch %{ocaml_native_compiler}
# The only source file for this package consists of a single "include" line.
# It exports some private functions from the library in ocaml-base.  Although
# debuginfo is generated, it is tagged with the file names from ocaml-base,
# rather than the single 1-line source file in this project.  That leads to
# this error:
#
# Processing files: ocaml-variantslib-debugsource-0.13.0-1.fc32.x86_64
# error: Empty %%files file /builddir/build/BUILD/variantslib-0.13.0/debugsourcefiles.list
#
# Do not try to gather debug sources to workaround the problem.
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif

Name:           ocaml-variantslib
Version:        0.16.0
Release:        6%{?dist}
Summary:        OCaml variants as first class values

License:        MIT
URL:            https://github.com/janestreet/variantslib
Source0:        %{url}/archive/v%{version}/variantslib-%{version}.tar.gz

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-base-devel >= 0.16
BuildRequires:  ocaml-dune >= 2.0.0

%description
This package contains an OCaml syntax extension to define first class
values representing variants.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n variantslib-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.0-6
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.0-5
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.0-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.16.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- Version 0.16.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-9
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-7
- Rebuild for ocaml-base 0.15.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-5
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-5
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.15.0-4
- Version 0.15.0 rerelease

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.15.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-9
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-7
- There is no circular dependency so always build docs

* Mon Mar  1 17:28:39 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-7
- OCaml 4.12.0 build
- Make ocaml-odoc dependency conditional.

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.14.0-6
- Rebuild for ocaml-base 0.14.1

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-5
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-2
- OCaml 4.11.0 rebuild

* Wed Aug  5 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Drop CONTRIBUTING.md
- Use boolean dependencies to more fully reflect upstream version dependencies

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
