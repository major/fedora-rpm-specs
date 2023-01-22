%define debug_package %{nil}
Name: planets
Version:  0.1.13
Release:  34%{?dist}
Summary: A celestial simulator  

License: GPLv2+
URL: http://planets.homedns.org/
Source0: http://planets.homedns.org/dist/planets-%{version}.tgz
Patch0:  planets-0.1.13-ocaml4.patch
# Fix for immutable strings.  NOT sent upstream (because upstream
# is not alive?)
Patch1:  planets-0.1.13-bytes.patch
Patch2:  planets-0.1.13-camlp5o.patch
BuildRequires: make
BuildRequires: desktop-file-utils, ocaml-labltk-devel, ocaml-camlp5-devel
BuildRequires: libX11-devel
Requires: hicolor-icon-theme

%description
Planets is a simple interactive program for playing with simulations
of planetary systems

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build

iconv -f ISO-8859-1 -t UTF-8 TODO > iconv.tmp
mv iconv.tmp TODO

make

%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 planets %{buildroot}%{_bindir}/planets
mkdir -p %{buildroot}/usr/share/man/man1
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
%doc CHANGES codeguide.txt COPYING CREDITS getting_started.html KEYBINDINGS.txt LICENSE README TODO VERSION
%{_bindir}/planets
%{_datadir}/applications/planets.desktop
%{_datadir}/icons/hicolor/32x32/apps/planets.png
%{_mandir}/man1/planets.1.gz

%changelog
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
