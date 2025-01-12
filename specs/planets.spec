%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name: planets
Version:  0.1.13
Release:  46%{?dist}
Summary: A celestial simulator  

License: GPL-2.0-or-later
URL: http://planets.homedns.org/
Source0: http://planets.homedns.org/dist/planets-%{version}.tgz
# Adapt to changes in OCaml 4.x
Patch0:  planets-0.1.13-ocaml4.patch
# Fix for immutable strings.  NOT sent upstream (because upstream
# is not alive?)
Patch1:  planets-0.1.13-bytes.patch
# Use camlp5 instead of the dead camlp4 package
Patch2:  planets-0.1.13-camlp5o.patch
# Generate usable debuginfo
Patch3:  planets-0.1.13-debuginfo.patch
# Adapt to changes in OCaml 5.x
Patch4:  planets-0.1.13-ocaml5.patch
# Adapt to changed unix library name in OCaml 5.1.0
Patch5:  planets-0.1.13-ocaml5.1.patch
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: ocaml-camlp-streams-devel
BuildRequires: ocaml-camlp5-devel
BuildRequires: ocaml-labltk-devel
Requires: hicolor-icon-theme

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%description
Planets is a simple interactive program for playing with simulations
of planetary systems

%prep
%autosetup -p1

%build

iconv -f ISO-8859-1 -t UTF-8 TODO > iconv.tmp
mv iconv.tmp TODO

%ifarch %{ocaml_native_compiler}
make
%else
make planets.bc
%endif

%install
mkdir -p  %{buildroot}%{_bindir}
%ifarch %{ocaml_native_compiler}
install -m 755 planets %{buildroot}%{_bindir}/planets
%else
install -m 755 planets.bc %{buildroot}%{_bindir}/planets
%endif
mkdir -p %{buildroot}%{_mandir}/man1
cp -pr planets.1 %{buildroot}%{_mandir}/man1

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --remove-category Application               \
  --add-category Simulation                  \
  --dir %{buildroot}%{_datadir}/applications \
  planets.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 planets.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%doc CHANGES codeguide.txt CREDITS getting_started.html KEYBINDINGS.txt README TODO VERSION
%license COPYING LICENSE
%{_bindir}/planets
%{_datadir}/applications/planets.desktop
%{_datadir}/icons/hicolor/32x32/apps/planets.png
%{_mandir}/man1/planets.1.gz

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 0.1.13-46
- OCaml 5.3.0 rebuild for Fedora 42

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.1.13-44
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 0.1.13-43
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.1.13-40
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.1.13-39
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.1.13-38
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 0.1.13-37
- Adapt to changed unix library name in OCaml 5.1.0

* Sat Sep  9 2023 Jerry James <loganjerry@gmail.com> - 0.1.13-37
- Do not build for 32-bit x86
- Generate usable debuginfo
- Adapt to changes in OCaml 5.x (rhbz#2226113)
- Support bytecode-only architectures
- Minor spec file cleanups

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.1.13-35
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.13-27
- Fix FTBFS.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 01 2019 Richard W.M. Jones <rjones@redhat.com> - 0.1.13-25
- Fix for immutable strings in newer OCaml.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.13-21
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.1.13-14
- Add Debian patch to fix FTBFS with ocaml-4.01 (#1106642)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.13-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.13-10
- Drop ExclusiveArch as PPC64 issue is long fixed and ARM was wrong
- Modernise spec

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.13-9
- Drop desktop vendor tag.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Jon Ciesla <limb@jcomserv.net> - 0.1.13-4
- Disabled debuginfo.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 5 2008 Jon Ciesla <limb@jcomserv.net> - 0.1.13-2
- Dropped unneccessary docs.
- Used rpmmacro for man page.
- Using ExclusiveArch due to ppc64 ocaml issues.

* Sun Feb 3 2008 Jon Ciesla <limb@jcomserv.net> - 0.1.13-1
- create.
