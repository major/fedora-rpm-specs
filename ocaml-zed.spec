%undefine _package_note_flags
Name:           ocaml-zed
Version:        3.1.0
Release:        12%{?dist}
Summary:        Abstract engine for text edition in OCaml

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:        BSD
URL:            https://github.com/ocaml-community/zed
Source0:        https://github.com/ocaml-community/zed/archive/%{version}/%{libname}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-camomile-devel
BuildRequires:  ocaml-react-devel
BuildRequires:  ocaml-charinfo-width-devel

BuildRequires:  ocaml-dune

%description
Zed is an abstract engine for text edition. It can be used to
write text editors, edition widgets, readlines, ... You just
have to connect an engine to your inputs and rendering functions
to get an editor.

Zed provides: edition state management, multiple cursor support,
key-binding helpers, and general purpose unicode rope
manipulation functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-camomile-devel%{_isa}
Requires:       ocaml-react-devel%{_isa}
Requires:       ocaml-charinfo-width-devel%{_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

%build
# It might be nice to have a %jbuilder macro that just does this.
dune build -p %{libname} %{?_smp_mflags}

%install
dune install --destdir=%{buildroot}

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
find %{buildroot}%{_libdir}/ocaml -name \*.cmxs -exec chmod a+x {} \+
%endif

%files
%license LICENSE
%doc README.md CHANGES.md
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/*/*.mli


%files devel
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-11
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-10
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-8
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 16:58:00 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-6
- OCaml 4.12.0 build

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-5
- Bump and rebuild for updated ocaml-camomile dep (RHBZ#1923853).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-3
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-2
- OCaml 4.11.0 rebuild

* Tue Aug  4 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Version 3.1.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-9
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-8
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-7
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-6
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-4
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-3
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.3-2
- OCaml 4.08.1 (final) rebuild.

* Sun Aug 11 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.3-1
- Updated to latest upstream release.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.2-2
- OCaml 4.08.1 (rc2) rebuild.

* Mon Jul 29 2019 Ben Rosser <rosser.bjr@gmail.com> - 2.0.2-1
- Updated to latest upstream release.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.6-8
- OCaml 4.08.0 (final) rebuild.

* Tue Apr 30 2019 Richard W.M. Jones <rjones@redhat.com> - 1.6-7
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.6-4
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.6-3
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 1.6-1
- New upstream version 1.6 (includes safe-string fixes).
- OCaml 4.06.0 rebuild.

* Tue Aug 15 2017 Ben Rosser <rosser.bjr@gmail.com> 1.5-2
- Modernize OCaml packaging.

* Fri Aug 11 2017 Ben Rosser <rosser.bjr@gmail.com> 1.5-1
- Initial packaging.
