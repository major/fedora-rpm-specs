%undefine _package_note_flags
# cudf includes C bindings, but it produces a static library.
# therefore for now, we'll not build them.

Name:           ocaml-cudf
Version:        0.9
Release:        33%{?dist}
Summary:        Format for describing upgrade scenarios

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# Linking exception, see included COPYING file.
License:        LGPLv3+ with exceptions
URL:            http://www.mancoosi.org/cudf/
Source0:        https://gforge.inria.fr/frs/download.php/file/36602/cudf-0.9.tar.gz

# Use ounit2.
%global _default_patch_fuzz 2
Patch1:         cudf-0.9-ounit2.patch

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-ounit-devel

# Depend on pod2man.
BuildRequires:  /usr/bin/pod2man

%description
CUDF (for Common Upgradeability Description Format) is a format for
describing upgrade scenarios in package-based Free and Open Source
Software distribution.

In every such scenario there exists a package universe (i.e. a set
of packages) known to a package manager application, a package status
(i.e. the currently installed packages), and a user request (i.e. a
wish to change the set of installed packages) that need to be
fulfilled.

CUDF permits to describe an upgrade scenario in a way that is
both distribution-independent and package-manager-independent.

CUDF offers a rigorous semantics of dependency solving that
enables to independently check the correctness of upgrade
solutions proposed by package managers.

CUDF adoption would enable to share dependency solver components
across different package managers, both intra- and
inter-distributions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version} -p1

# Add debug tag.
sed 's/pkg_extlib/pkg_extlib, debug/g' -i _tags

%build
%make_build
%ifarch %{ocaml_native_compiler}
%make_build opt
%endif

%make_build doc

%install
make install DESTDIR=%{buildroot}

# Install the man page for cudf-check.
mkdir -p %{buildroot}%{_mandir}/man1
cp -a doc/cudf-check.1* %{buildroot}%{_mandir}/man1

# Remove .o files from cudf directory.
rm -rf %{buildroot}%{_libdir}/ocaml/cudf/*.o

%check
make test

%files
%license COPYING
%doc README
%{_bindir}/cudf-check
%{_mandir}/man1/cudf-check.1*
%{_bindir}/cudf-parse-822
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/*/*.mli

%files devel
# include API documentation here.
%doc cudf.docdir/*
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.9-32
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.9-31
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.9-29
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 21:30:57 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.9-27
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Richard W.M. Jones <rjones@redhat.com> - 0.9-25
- Rebuild for new ocaml-extlib.

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-24
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-23
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-20
- Rebuild for updated ocaml-extlib (RHBZ#1837823).

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-19
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-18
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-17
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-16
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9-14
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9-13
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9-12
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9-11
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9-9
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9-8
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9-5
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9-4
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9-2
- OCaml 4.06.0 rebuild.

* Fri Aug 11 2017 Ben Rosser <rosser.bjr@gmail.com> 0.9-1
- Initial package.
