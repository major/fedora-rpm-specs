# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/rdicosmo/parmap

Name:           ocaml-parmap
Version:        1.2.5
Release:        16%{?dist}
Summary:        OCaml library for exploiting multicore architectures

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://rdicosmo.github.io/parmap/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/parmap-%{version}.tar.gz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-graphics-devel

%description
Parmap is a minimalistic library for exploiting multicore architectures
in OCaml programs with minimal modifications: if you want to use your
many cores to accelerate an operation which happens to be a map, fold or
map/fold (map-reduce), just use Parmap's parmap, parfold and parmapfold
primitives in place of the standard List.map and friends, and specify
the number of subprocesses to use with the optional parameter ~ncores.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n parmap-%{version}

%build
%dune_build

%install
%dune_install

%ifarch %{ocaml_native_compiler}
# The tests take a really, really long time on bytecode-only systems
%check
%dune_check
%endif

%files -f .ofiles
%doc AUTHORS CHANGES README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 1.2.5-15
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2.5-13
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2.5-12
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.2.5-9
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.2.5-8
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.2.5-7
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.2.5-5
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.2.5-4
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.2.5-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Update SPDX License tag

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Version 1.2.5

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.2.4-5
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-5
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-4
- Bump release and rebuild.

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan  4 2022 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- Version 1.2.4

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.2.3-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May  3 2021 Jerry James <loganjerry@gmail.com> - 1.2.3-1
- Version 1.2.3

* Wed Apr 28 2021 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Version 1.2.1
- Drop upstreamed -float-array patch

* Fri Apr 16 2021 Jerry James <loganjerry@gmail.com> - 1.2-1
- Initial package
