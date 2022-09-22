Name:              libstroke
Version:           0.5.1
Release:           47%{?dist}

Summary:           A stroke interface library
License:           GPLv2
URL:               http://www.etla.net/%{name}/

Source:            http://www.etla.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:     libtool automake autoconf
BuildRequires:     pkgconfig
BuildRequires:     make
BuildRequires:     libX11-devel

Patch0:            libstroke-aclocal.patch
Patch1:            libstroke-automake-typos.patch
Patch2:            libstroke-0.5.1-no_gtk1.patch

Obsoletes:         libgstroke < %{version}-%{release}
Provides:          libgstroke = %{version}-%{release}
Obsoletes:         libgstroke-devel < %{version}-%{release}
Provides:          libgstroke-devel = %{version}-%{release}


%description
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.

%package devel
Summary:           Development files for the libstroke library
Requires:          %{name}%{?_isa} = %{version}-%{release} automake

%description devel
Development files for the libstroke library.

%package -n javastroke
Summary:           Optional java files
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description -n javastroke
Java interface for stroke and example application

%prep
%autosetup -p1

autoreconf -if

%build
%configure \
    --disable-static \
    --with-x=yes
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/stroke/java
cp -p javastroke/*.java  %{buildroot}%{_datadir}/stroke/java


rm %{buildroot}%{_libdir}/*.la


%files
%doc README ChangeLog NEWS AUTHORS TODO CREDITS
%license COPYRIGHT
%{_libdir}/libstroke.so.*

%files devel
%doc doc/standard_strokes*
%{_datadir}/aclocal/libstroke.m4
%{_libdir}/libstroke.so
%{_includedir}/stroke.h

%files -n javastroke
%doc javastroke/README
%{_datadir}/stroke/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 10 2022 Leigh Scott <leigh123linux@gmail.com> - 0.5.1-46
- Drop unused sub-package to remove gtk+-devel build requires
- Spec file clean up

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Adam Goode <adam@spicenitz.org> - 0.5.1-24
- Run automake at build time to remove various fragile workarounds
- -22 and -23 don't have changelog entries, I think those were mass rebuilds

* Mon Dec 29 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-21
- fix for EL-5 build; pdgconfig as BR

* Sat Dec 20 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-20
- fix for rawhide's libtool 2.2.6

* Sat Dec 20 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-19
- rebuild for proper tagging

* Sat Dec 20 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-18
- fix for x86_64 build fix RHBZ # 465030

* Mon Jun 16 2008 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-17
- Bugfix 449516 FTBFS libstroke-0.5.1-17.fc9

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-16
- mass rebuild for fedora 8 - ppc32

* Tue Jun 26 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-15
- patch for multilib #241448

* Thu Mar 01 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-14
- patch for underquoted definitions #226886

* Mon Feb 26 2007 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-13
- Fixed multilibs issues for rawhide

* Fri Sep 01 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-12
- Removed automake as BR

* Fri Sep 01 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-11
- fixed ownership of directories

* Wed Aug 30 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-10
- Removed duplicates

* Wed Aug 30 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-9
- Removed "conflicts: libstroke-devel"

* Wed Aug 30 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-8
- fixed ownership of directories

* Wed Aug 30 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-7
- rebuilt for FC5 and later with minor fixes

* Tue Aug 29 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.5.1-6
- rebuilt for FC5 and later with minor fixes

* Sun Apr 2 2006 Wojciech Kazubski <wk at ire.pw.edu.pl> - 0.5.1-5
- rebuilt for FC5,
- specfile cleanups

* Sun Jun 19 2005 Wojciech Kazubski <wk at ire.pw.edu.pl>
- rebuilt for Fedora Core 4

* Thu May 5 2005 Wojciech Kazubski <wk at ire.pw.edu.pl>
- re-divided

* Sat Dec 11 2004 Wojciech Kazubski <wk at ire.pw.edu.pl>
- rebuilt for Fedora Core 3

* Tue Feb 4 2003 Wojciech Kazubski <wk at ire.pw.edu.pl>
- libstroke-gnome splited.

* Wed Dec 19 2001 Wojciech Kazubski <wk at ire.pw.edu.pl>
- first RedHat version.
