# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# OCaml 5.x support was added after the most recent release
%global commit  58459992ee9b3d56f09f6ff3dd434a52657b836c
%global date    20230115
%global forgeurl https://github.com/ocaml-obuild/obuild

# The binary is OCaml bytecode
%global debug_package %{nil}

Name:           ocaml-obuild
Version:        0.1.10
Summary:        Simple package build system for OCaml

%forgemeta

Release:        22%{?dist}
License:        BSD-2-Clause
URL:            https://github.com/ocaml-obuild/obuild
Source0:        %{forgesource}

# Fix a partial function application
# https://github.com/ocaml-obuild/obuild/issues/187
Patch0:         %{name}-partial.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  help2man

Requires:       ocaml-findlib%{?_isa}

%description
A parallel, incremental and declarative build system for OCaml.

The goal is to make a very simple build system for users and developers of
OCaml libraries and programs.

Obuild acts as a building black box: users only declare what they want to
build and with which sources; the build system will consistently build it.

The design is based on Haskell's Cabal and borrows most of the layout and
way of working, adapting parts where necessary to fully support OCaml.


%prep
%forgeautosetup -p1


%build
./bootstrap


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp "dist/build/obuild/obuild" "dist/build/obuild-simple/obuild-simple" "$RPM_BUILD_ROOT%{_bindir}"

# generate manpages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
help2man \
    --output "$RPM_BUILD_ROOT%{_mandir}/man1/obuild.1" \
    --name "parallel, incremental and declarative build system for OCaml" \
    --help-option "" \
    --no-discard-stderr \
    --no-info \
    dist/build/obuild/obuild
help2man \
    --output "$RPM_BUILD_ROOT%{_mandir}/man1/obuild-simple.1" \
    --name "simple package build system for OCaml" \
    --version-string " " \
    --no-discard-stderr \
    --no-info \
    dist/build/obuild-simple/obuild-simple


%files
%doc README.md OBUILD_SPEC.md DESIGN.md
%license LICENSE
%{_bindir}/obuild*
%{_mandir}/man1/obuild*.1*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-21
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.1.10-20.20230115git5845999
- Update to git head for OCaml 5.x support
- Convert License tag to SPDX
- Add patch to fix a partial function application

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-19
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-16
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-15
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-13
- Bump release and rebuild.

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-12
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 28 22:24:15 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-10
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-8
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-7
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Andy Li <andy@onthewings.net> - 0.1.10-1
- New upstream release (RHBZ#1572211).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Andy Li <andy@onthewings.net> - 0.1.9-1
- New upstream release.
- Remove obuild-arg-parsing.patch, which has been merged upstream.

* Fri Nov 17 2017 Andy Li <andy@onthewings.net> - 0.1.8-1
- Initial RPM release.
