# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifarch %{ocaml_native_compiler}
# The only source file for this package consists of a single "include" line,
# referring to the bigarray in stdlib.  Although debuginfo is generated, it is
# tagged with the file names from the ocaml package, rather than the single
# 1-line source file in this project.  That leads to this error:
#
# error: Empty %%files file /builddir/build/BUILD/bigarray-compat-1.1.0/debugsourcefiles.list
#
# Do not try to gather debug sources to workaround the problem.
%undefine _debugsource_packages
%else
%global debug_package %{nil}
%endif

Name:           ocaml-bigarray-compat
Version:        1.1.0
Release:        10%{?dist}
Summary:        Compatibility library to use Stdlib.Bigarray when possible

License:        ISC
URL:            https://github.com/mirage/bigarray-compat
Source0:        %{url}/archive/v%{version}/bigarray-compat-%{version}.tar.gz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 1.0

%description
Bigarray-compat is an OCaml library that exposes `Stdlib.Bigarray` when
possible (OCaml >= 4.07) but can fallback to `Bigarray`.  The compability
bigarray module is exposed under `Bigarray_compat`.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n bigarray-compat-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-10
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-9
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-7
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.1.0-6
- OCaml 5.0.0 rebuild
- Do not produce a debugsource package for OCaml 5+

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.1.0-2
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- Version 1.1.0
- Upstream tarball now includes the license file

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-6
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-4
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 12:17:30 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-2
- OCaml 4.12.0 build

* Tue Feb 09 2021 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- Initial package
