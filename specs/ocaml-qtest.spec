# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-qtest
Version:        2.11.2
Release:        25%{?dist}
Summary:        Inline (Unit) Tests for OCaml

License:        GPL-3.0-or-later
URL:            https://github.com/vincent-hugot/qtest
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Remove references to the bytes library for OCaml 5.0 compatibility
Patch:          %{name}-ocaml5.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 1.1
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-qcheck-devel >= 0.14
BuildRequires:  asciidoc
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  python3-pygments

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-qtest-doc < 2.11.2-9


%description
qtest extracts inline unit tests written using a special syntax in
comments. Those tests are then run using the oUnit framework and the
qcheck library. The possibilities range from trivial tests -- extremely
simple to use -- to sophisticated random generation of test cases.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n qtest-%{version} -p1

# Fix a markup bug in the README
sed -i 's/\[source\]/[source,OCaml]/' README.adoc


%build
%dune_build


%install
%dune_install

# generate manpage
mkdir -p %{buildroot}/%{_mandir}/man1/
help2man %{buildroot}/%{_bindir}/qtest \
    --output %{buildroot}/%{_mandir}/man1/qtest.1 \
    --name "Inline (Unit) Tests for OCaml" \
    --version-string %{version} \
    --no-info

# Build documentation
asciidoc README.adoc


%check
%dune_check


%files -f .ofiles
%doc README.html
%license LICENSE
%{_mandir}/man1/qtest.1*


%files devel -f .ofiles-devel
%doc README.html
%license LICENSE


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 2.11.2-24
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-22
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-21
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-18
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-17
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-16
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-14
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2.11.2-13
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-12
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 2.11.2-10
- Rebuild for ocaml-ounit 2.2.6
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 2.11.2-8
- Generate documentation with asciidoc
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-8
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-7
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-5
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

*  Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 2.11.2-3
- Rebuild for alcotest 1.4.0

* Mon Mar  1 23:32:55 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2.11.2-2
- OCaml 4.12.0 build

* Sat Feb 13 2021 Jerry James <loganjerry@gmail.com> - 2.11.2-1
- Version 2.11.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 2.11.1-1
- Version 2.11.1

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.11-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.11-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Jerry James <loganjerry@gmail.com> - 2.11-1
- New upstream release (bz 1835054)

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-13
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-12
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-11
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-10
- OCaml 4.10.0 final.

* Wed Feb 19 2020 Jerry James <loganjerry@gmail.com> - 2.10.1-9
- Rebuild for ocaml-qcheck 0.13.
- Build documentation with odoc, and ship it in a new doc subpackage.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.10.1-7
- OCaml 4.10.0+beta1 rebuild.

* Wed Dec 18 2019 Andy Li <andy@onthewings.net> - 2.10.1-1
- New upstream release. (RHBZ#1777145)
- Remove unneeded BuildRequires on opam-installer.

* Tue Aug 06 2019 Andy Li <andy@onthewings.net> - 2.9-6
- OCaml 4.08.1 rebuild.

* Mon Jul 29 2019 Andy Li <andy@onthewings.net> - 2.9-5
- Update build depends and commands from jbuilder to dune.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Andy Li <andy@onthewings.net> - 2.9-1
- New upstream release (RHBZ#1570332).
- Enable devel and debug packages.

* Fri Apr 06 2018 Andy Li <andy@onthewings.net> - 2.8-1
- New upstream release.
- Remove ocaml-qtest-LICENSE.patch which has been applied upstream.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Andy Li <andy@onthewings.net> - 2.7-1
- Initial RPM release.
