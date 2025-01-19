%global commit 020a4c2b7612863600428e0e9f2491b923e54ac2
%global gittag 1.5
%global shortcommit %(c=%{commit0}; echo ${c:0:7})

Name:            libbinio
Version:         %{gittag}
Release:         9%{?dist}
Summary:         A software library for binary I/O classes in C++
URL:             http://adplug.github.io/libbinio
Source0:         https://github.com/adplug/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch0:          libbinio-1.4-includes.patch
License:         LGPL-2.1-or-later AND GFDL-1.1-or-later
BuildRequires:   gcc-c++
BuildRequires:   make

%description
This binary I/O stream class library presents a platform-independent
way to access binary data streams in C++. The library is hardware
independent in the form that it transparently converts between the
different forms of machine-internal binary data representation.
It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

%package devel
Summary:         Development files for libbinio
Requires:        %{name}%{?_isa} = %{version}-%{release}
BuildRequires:   texinfo

%description devel
This package contains development files for the libbinio binary
data stream class for C++.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
# Remove libtool archive remnants
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# Remove doc "dir"
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libbinio.so.1{,.*}
%doc AUTHORS README NEWS TODO

%files devel
%dir %{_includedir}/%{name}
%{_libdir}/libbinio.so
%{_libdir}/pkgconfig/libbinio.pc
%{_includedir}/%{name}/*.h
%{_infodir}/libbinio.info*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 21 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.5-7
- Add missing License

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Charles R. Anderson <cra@alum.wpi.edu> - 1.5-1
- Source moved to github.  Update to 1.5.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.4-30
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4-21
- Rebuild for newest GCC 5 C++ ABI change, so deps can compile/link with this.

* Thu Feb 19 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4-20
- Drop buildroot tag, %%defattr, %%clean.
- Fix -devel group tag.
- Add %%_isa to -devel base package dep.
- Rebuild for GCC 5 C++ ABI change, so deps can compile/link with this.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Caolán McNamara <caolanm@redhat.com> - 1.4-11
- include stdio.h for EOF

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Linus Walleij <triad@df.lth.se> 1.4-9
- Rebuild for GCC 4.3.

* Fri Jan 18 2008 Linus Walleij <triad@df.lth.se> 1.4-8
- New glibc ABI wants a rebuild.

* Fri Aug 17 2007 Linus Walleij <triad@df.lth.se> 1.4-7
- License field update from LGPL to LGPLv2+

* Mon Aug 28 2006 Linus Walleij <triad@df.lth.se> 1.4-6
- Rebuild for Fedora Extras 6.

* Tue Feb 14 2006 Linus Walleij <triad@df.lth.se> 1.4-5
- Rebuild for Fedora Extras 5.

* Thu Oct 6 2005 Linus Walleij <triad@df.lth.se> 1.4-4
- BuildRequire texinfo to get makeinfo.

* Sat Oct 1 2005 Linus Walleij <triad@df.lth.se> 1.4-3
- Conforming pkg-config for FC4 and texinfo bug patch.

* Sun Sep 18 2005 Linus Walleij <triad@df.lth.se> 1.4-2
- More minor corrections.

* Sun Sep 18 2005 Linus Walleij <triad@df.lth.se> 1.4-1
- Upstream fixed header problem.

* Fri Sep 16 2005 Linus Walleij <triad@df.lth.se> 1.3-4
- Trying to resolve dispute about header subdirs.

* Thu Sep 15 2005 Linus Walleij <triad@df.lth.se> 1.3-3
- Reverted some and added some after comments from Ville Skyttä.

* Thu Sep 15 2005 Linus Walleij <triad@df.lth.se> 1.3-2
- Fixed some points raised by Ralf Corsepius.

* Wed Sep 14 2005 Linus Walleij <triad@df.lth.se> 1.3-1
- First try at a libbinio RPM.
