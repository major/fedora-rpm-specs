%undefine _package_note_flags
# version 1.1.0
%global commit 6a2ed28ba68cddab6927ac27a9b991f01ea85ec5
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:           ocaml-charinfo-width
Version:        1.1.0
Release:        25%{?dist}
Summary:        Determine column width for a character

%global libname charInfo_width

# MIT-licensed according to opam metadata.
# Issue filed here: https://bitbucket.org/zandoye/charinfo_width/issues/1/include-mit-license-copying-file
License:        MIT
URL:            https://bitbucket.org/zandoye/charinfo_width/
Source0:        https://bitbucket.org/zandoye/charinfo_width/get/%{version}.tar.gz#/%{libname}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-camomile-devel

BuildRequires:  ocaml-dune

%description
Determine column width for a character

This module is implemented purely in OCaml and the width function
follows the prototype of POSIX's wcwidth.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use %{name}.

%prep
%autosetup -n zandoye-charinfo_width-%{shortcommit}

%build
# It might be nice to have a %jbuilder macro that just does this.
dune build -p %{libname} %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}/ocaml/%{libname}/
cp -aLr _build/install/default/lib/%{libname}/* %{buildroot}%{_libdir}/ocaml/%{libname}/

%files
#license LICENSE
%doc README.md CHANGES.md
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/*/*.mli


%files devel
#license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli


%changelog
* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-25
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-22
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-21
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-19
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 15:56:24 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-17
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-15
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-14
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-10
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-8
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-6
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-5
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-4
- OCaml 4.08.1 (final) rebuild.

* Sun Aug 11 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-3
- Rebuilt for camomile 1.0.2.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-1
- Initial package.
