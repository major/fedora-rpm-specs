Name:           xmakemol
Version:        5.16
Release:        22%{?dist}
Summary:        Program for visualizing atomic and molecular systems
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.nongnu.org/xmakemol/
Source0:        http://savannah.nongnu.org/download/xmakemol/xmakemol-%{version}.tar.gz

# Fix FSF address
Patch0:         xmakemol-5.16-fsf.patch
# Patches from debian
Patch1:         xmakemol-5.16-fix_vectors_on_atoms.patch
Patch2:         xmakemol-5.16-h-bond.patch
Patch3:         xmakemol-5.16-print_torsions.patch
# Fix multiple definition of bbox
Patch4:         xmakemol-5.16-extern.patch
# Fix BZ#1914657, crash about NULL widget class
Patch5:         xmakemol-5.16-widget.patch
# Fix BZ#2261809, initialization of XmString from incompatible pointer type
Patch6:         xmakemol-5.16-pointertype.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGLw-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXpm-devel
BuildRequires:  libICE-devel
BuildRequires:  zlib-devel
BuildRequires:  motif-devel
BuildRequires:  freeglut-devel

%description
XMakemol is a mouse-based program, written using the LessTif widget
set, for viewing and manipulating atomic and other chemical
systems. It reads XYZ input and renders atoms, bonds and hydrogen
bonds.  Features include:
- Animating multiple frame files
- Interactive measurement of bond lengths, bond angles and torsion angles
- Control over atom/bond sizes
- Exporting to Xpm, Encapsulated PostScript and XYZ formats
- Toggling the visibility of groups of atoms
- Editing the positions of subsets of atoms

%prep
%autosetup -N
%patch -P0 -p1 -b .fsf
%patch -P1 -p0 -b .vecat
%patch -P2 -p1 -b .hbond
%patch -P3 -p1 -b .torsion
%patch -P4 -p1 -b .extern
%patch -P5 -p1 -b .widget
%patch -P6 -p1 -b .pointertype

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS PROBLEMS README
%{_datadir}/xmakemol/
%{_bindir}/xmakemol
%{_mandir}/man1/xmakemol.1.*
%{_bindir}/xmake_anim.pl

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.16-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.16-19
- Fix FTBFS on Fedora 40.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.16-15
- Freeglut is now available in RHEL9.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.16-10
- Fix crash for NULL widget class (BZ #1914657).

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 01 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.16-8
- Patch out multiple definition of bbox.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 5.16-6
- Rebuilt for new freeglut

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep  7 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.16-3
- Import patches from Debian.

* Fri Sep  7 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.16-2
- Review fixes.

* Thu Sep  6 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 5.16-1
- First release.

