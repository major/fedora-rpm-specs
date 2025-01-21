Name:		xmbdfed
Summary: 	Bitmap Font Editor
Version:	4.7
Release:	38%{?dist}
License:	MIT
Source0:	http://crl.nmsu.edu/~mleisher/%{name}-%{version}.tar.bz2
Source1:	http://crl.nmsu.edu/~mleisher/%{name}.png
Source2:	xmbdfed.desktop
Patch0:		http://crl.nmsu.edu/~mleisher/%{name}-4.7-patch1
Patch1:		xmbdfed-4.7-linux.patch
Patch2:		xmbdfed-4.7-staticfix.patch
Patch3:		xmbdfed-4.7-getline.patch
Patch4:		xmbdfed-4.7-format-security.patch
Patch5:		xmbdfed-4.7-gcc10.patch
URL:		http://crl.nmsu.edu/~mleisher/xmbdfed.html
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	freetype-devel, libXpm-devel, libXmu-devel
%if 0%{?fedora} >= 24
BuildRequires:  motif-devel
%else
BuildRequires:  lesstif-devel
%endif
BuildRequires:	libXext-devel, libX11-devel, libSM-devel, libICE-devel
BuildRequires:	desktop-file-utils
Requires:	xorg-x11-fonts-misc

%description
The XmBDFEditor lets you interactively create new bitmap font files or 
modify existing ones. It allows editing multiple fonts and multiple 
glyphs, it allows cut and paste operations between fonts and glyphs and 
editing font properties. The editor works natively with BDF fonts.

%prep
%setup -q 
%patch -P0 -p0 -b .patch1
%patch -P1 -p1 -b .linux
%patch -P2 -p1 -b .staticfix
%patch -P3 -p1 -b .getline
%patch -P4 -p1 -b .format-security
%patch -P5 -p1 -b .gcc10

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 xmbdfed %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m0644 xmbdfed.man %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps
desktop-file-install					\
	--dir %{buildroot}%{_datadir}/applications	\
	%{SOURCE2}

%files
%doc README COPYRIGHTS xmbdfedrc CHANGES
%{_bindir}/xmbdfed
%{_datadir}/pixmaps/xmbdfed.png
%{_datadir}/applications/*.desktop
%{_mandir}/man1/xmbdfed*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Tom Callaway <spot@fedoraproject.org> - 4.7-28
- fix FTBFS

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.7-18
- Fix typo in previous change.

* Thu Oct 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.7-17
- Build against motif on fedora >= 24.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec  9 2013 Tom Callaway <spot@fedoraproject.org> - 4.7-13
- fix format-security issues

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.7-7
- actually apply patch3

* Wed Aug  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.7-6
- fix function naming conflict of "getline" with stdio.h

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.7-3
- add -p to install to preserve timestamps
- add BR: desktop-file-utils

* Mon Dec  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.7-2
- correct usage of defattr
- add Requires: xorg-x11-fonts-misc
- fix desktop file

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.7-1
- initial Fedora package
