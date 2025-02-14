# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# We used to build documentation with odoc, but did not include the generated
# documentation in any binary package.  Furthermore, there is now a dependency
# loop: ocaml-sedlex -> ocaml-yojson -> ocaml-odoc -> ocaml-sedlex.
%bcond docs 0

Name:           ocaml-sedlex
Version:        3.3
Release:        3%{?dist}
Summary:        Unicode-friendly lexer generator

License:        MIT
URL:            https://github.com/ocaml-community/sedlex
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Use local Unicode files instead of attempting to download them
Patch:          %{name}-no-curl.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-gen-devel
BuildRequires:  unicode-ucd

%if %{with docs}
BuildRequires:  ocaml-odoc
%endif

%description
A lexer generator for OCaml, similar to ocamllex, but supporting Unicode.
Contrary to ocamllex, lexer specifications for sedlex are embedded in
regular OCaml source files.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-gen-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -p1 -n sedlex-%{version}

# Upstream's regression test is written for Unicode 15.0.0 through 16.0.0.  Our
# Unicode files may be from a more recent version of the standard.  The test has
# a good chance of succeeding anyway, so we cross our fingers and give it a try.
# If the regression test fails, we'll have to try another approach.
univer=$(sed -n 's/.*PropList-\([.[:digit:]]*\)\.txt/\1/p' %{_datadir}/unicode/ucd/PropList.txt)
sed -i "s/15\\.0\\.0/$univer/" examples/regressions.ml examples/unicode_old.ml \
  src/generator/data/base_url src/syntax/unicode.ml

%build
%dune_build
%if %{with docs}
%dune_build @doc
%endif


%install
%dune_install


%check
%dune_check


%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE


%files devel -f .ofiles-devel
%doc README.md CHANGES.md
%license LICENSE


%changelog
* Wed Feb 12 2025 Jerry James <loganjerry@gmail.com> - 3.3-3
- Rebuild for ocaml-ppxlib 0.35.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 3.3-1
- OCaml 5.3.0 rebuild for Fedora 42
- Version 3.3

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 3.2-14
- Rebuild for ocaml-ppxlib 0.33.0
- Do not build odoc documentation by default

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul  3 2024 Jerry James <loganjerry@gmail.com> - 3.2-12
- Rebuild for ocaml-sexplib0 0.17.0

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 3.2-11
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 3.2-10
- OCaml 5.2.0 for Fedora 41

* Tue Feb 20 2024 Andy Li <andy@onthewings.net> - 3.2-9
- ocaml-ppxlib rebuild for Fedora 41 (RHBZ#2264259)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2-6
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2-5
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 3.2-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 3.2-1
- Version 3.2

* Wed Mar 22 2023 Jerry James <loganjerry@gmail.com> - 3.1-1
- Version 3.1
- Drop upstreamed uchar patch
- BR ocaml-ppx-expect-devel for new tests

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 3.0-6
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 3.0-5
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 3.0-4
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 3.0-2
- Rebuild for ocaml-ppxlib 0.28.0

* Mon Aug  8 2022 Jerry James <loganjerry@gmail.com> - 3.0-1
- Version 3.0
- Remove unused ocaml-seq-devel BR
- Use new OCaml macros

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 2.6-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 2.6-1
- Version 2.6 (update for ocaml-ppxlib 0.26.0)

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 2.5-4
- Rebuild for ocaml-gen 1.0
- Add ocaml-seq-devel BR

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2.5-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 2.5-1
- Version 2.5 (update for ocaml-ppxlib 0.24.0)

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 2.4-3
- Rebuild for ocaml-sexplib0 0.15.0
- Reenable Unicode standard munging code to fix the tests

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 2.4-2
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 2.4-1
- Version 2.4
- Add -uchar patch to avoid the need for a compatibility package

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 2.3-5
- Rebuild for ocaml-ppxlib 0.22.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 2.3-3
- Rebuild for ocaml-ppxlib 0.22.1

* Mon Mar  1 23:50:55 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2.3-2
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 2.3-1
- Version 2.3
- Drop upstreamed -pervasives patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 2.2-1
- Version 2.2
- Add -pervasives and -no-curl patches
- Use local Unicode tables instead of downloading
- Build documentation with odoc
- Add a %%check script

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-12
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-11
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-8
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-7
- OCaml 4.11.0 pre-release attempt 2

* Sun Apr 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-6
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.1-5
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Andy Li <andy@onthewings.net> - 2.1-3
- Rebuild against latest ocaml package.
- Remove unneeded BuildRequires on opam-installer.

* Fri Nov 08 2019 Andy Li <andy@onthewings.net> - 2.1-2
- Remove dependency on uchar.

* Wed Oct 30 2019 Andy Li <andy@onthewings.net> - 2.1-1
- New upstream version.
- Update URL.

* Thu Aug 08 2019 Andy Li <andy@onthewings.net> - 1.99.4-7
- Add ppx_tools_versioned.diff, fix build.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Andy Li <andy@onthewings.net> - 1.99.4-5
- Do not build in parallel since the Makefile does not support it.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.99.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Andy Li <andy@onthewings.net> - 1.99.4-1
- Initial RPM release.
