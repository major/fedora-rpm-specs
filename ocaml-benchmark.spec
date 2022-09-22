%undefine _package_note_flags
Name:           ocaml-benchmark
Version:        1.6
Release:        1%{?dist}
Summary:        Benchmarking module for OCaml

License:        LGPLv3+ with exceptions
URL:            http://ocaml-benchmark.forge.ocamlcore.org/
Source0:        https://github.com/Chris00/ocaml-benchmark/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-dune
BuildRequires:  opam-installer

%description
Benchmark provides functions to measure and compare the run-time of functions.
It is inspired by the Perl module of the same name.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
dune build @install --profile release


%install
dune install --destdir="%{buildroot}" --libdir="%{_libdir}/ocaml" --verbose

# Makes *.cmxs executable such that they will be stripped.
find %{buildroot} -name '*.cmxs' -exec chmod 0755 {} \;

# Remove /usr/doc, we will install it using %%doc directives.
rm -r %{buildroot}$DESTDIR/usr/doc


%check
dune runtest --profile release


%files
%doc README.md CHANGES.md
%license LICENSE.md
%{_libdir}/ocaml/benchmark
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/benchmark/*.a
%exclude %{_libdir}/ocaml/benchmark/*.cmxa
%exclude %{_libdir}/ocaml/benchmark/*.cmx
%endif
%exclude %{_libdir}/ocaml/benchmark/*.mli


%files devel
%doc README.md CHANGES.md
%license LICENSE.md
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/benchmark/*.a
%{_libdir}/ocaml/benchmark/*.cmxa
%{_libdir}/ocaml/benchmark/*.cmx
%endif
%{_libdir}/ocaml/benchmark/*.mli


%changelog
* Tue Aug 09 2022 Andy Li <andy@onthewings.net> - 1.6-1
- New upstream release.
- Fix build (RHBZ#2113556).

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.5-24
- OCaml 4.14.0 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.5-22
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 22:00:48 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.5-20
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-18
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-17
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-14
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-13
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-12
- Bump release and rebuild.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-11
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-10
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.5-8
- OCaml 4.10.0+beta1 rebuild.
- jbuilder -> dune.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.5-7
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 1.5-6
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.5-4
- OCaml 4.08.0 (beta 3) rebuild.
- Set --profile release to disable warn-error.
- Various jbuilder command line fixes.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Andy Li <andy@onthewings.net> - 1.5-1
- New upstream release (RHBZ#1579582).
- Update build commands to use jbuilder.
- Enable debug package.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.4-2
- OCaml 4.06.0 rebuild.

* Mon Nov 20 2017 Andy Li <andy@onthewings.net> - 1.4-1
- Initial RPM release.
