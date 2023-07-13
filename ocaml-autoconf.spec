# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%undefine _package_note_flags
Name:           ocaml-autoconf
Version:        1.1
Release:        34%{?dist}
Summary:        Autoconf macros for OCaml


# https://fedoraproject.org/wiki/Licensing/BSD#3ClauseBSD
License:        BSD

URL:            http://forge.ocamlcore.org/projects/ocaml-autoconf/
Source0:        https://forge.ocamlcore.org/frs/download.php/282/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  /usr/bin/perldoc

# Runtime requires /usr/share/aclocal subdirectory.
Requires:       automake


%description
Autoconf macros for OCaml projects.


%prep
%setup -q


%build
make


%install
rm -rf $RPM_BUILD_ROOT
make install \
  prefix=%{_prefix} \
  datadir=%{_datadir} \
  mandir=%{_mandir} \
  DESTDIR=$RPM_BUILD_ROOT



%files
%doc README LICENSE
%{_mandir}/man1/*.1*
%{_datadir}/aclocal/ocaml.m4


%changelog
* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-34
- OCaml 5.0 rebuild for Fedora 39

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1-33
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1-30
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1-29
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1-27
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 28 22:24:17 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1-25
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-23
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1-22
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Richard Jones <rjones@redhat.com> - 1.1-12
- Remove useless defattr in files section.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1.1-6
- Rebuild for OCaml 4.00.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-3
- Rebuild for OCaml 3.11.2.

* Mon Oct 12 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-2
- New upstream version 1.1.
- Fix source URL.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0-4
- Upstream has released version 1.0 and it is properly licensed.

* Thu Jan 22 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1-0.1.git20090122
- Initial RPM release.
