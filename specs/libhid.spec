Name:		libhid
Version:	0.2.17
Release:	51%{?dist}
Summary:	User space USB HID access library
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://libhid.alioth.debian.org
# The source for this package was pulled from upstream's Subversion.  Use the
# following commands to generate the tarball:
#  svn co svn://svn.debian.org/libhid/trunk libhid-0.2.17
#  tar -czvf libhid-0.2.17.tar.gz libhid-0.2.17
Source0:	%{name}-%{version}.tar.gz

# Use db2x_docbook2man instead xsltproc to generate man pages
Patch0:		libhid-0.2.17-fix_manpage.patch
# Stop the configure script to mess the flags
Patch1:		libhid-0.2.17-fix_compiler_flags.patch
# Fix FTBFS rhbz#716191
Patch2:		libhid-0.2.17-buildfix.patch
# Fix Python installation on x86_64
Patch3:		libhid-0.2.17-fix_python.patch
BuildRequires:	libusb-compat-0.1-devel, libtool, pkgconfig, docbook2X, docbook-style-xsl
BuildRequires:	make

%description
libhid provides a generic and flexible way to access and interact with USB
HID devices, much like libusb does for plain USB devices. It is based on
libusb, thus it requires no HID support in the kernel and provides means to
take control over a device even if the kernel governs it.


%package devel
Summary: Development files for libhid
Requires: %{name} = %{version}-%{release}
Requires: libusb-compat-0.1-devel

%description devel
This package provides the development files for libhid.
You need this if you want to develop an application with libhid


%prep
%setup -q
%patch -P0 -p1 -b .fix_manpage
%patch -P3 -p1 -b .fix_python
# Allow build against swig-3.0
sed -i 's|AC_PROG_SWIG(1.3)|AC_PROG_SWIG(3.0)|' configure.ac
autoreconf -i
%patch -P1 -p1 -b .fix_compiler_flags
%patch -P2 -p1


%build
# Fix swig and disable doxygen for now
%configure --disable-static --disable-werror --without-doxygen --disable-swig
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} LDFLAGS="$LDFLAGS -lusb"


%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
# Excluded INSTALL and COPYING as they are symlinks to nothing
%license README.licence
%{_libdir}/*.so.*
%{_bindir}/libhid-detach-device
%{_mandir}/man1/*

%files devel
%doc AUTHORS README ChangeLog
%{_libdir}/pkgconfig/libhid.pc
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.17-50
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 18 2022 Hans de Goede <hdegoede@redhat.com> - 0.2.17-43
- Honor rpmrc LDFLAGS

* Wed Mar 16 2022 Manuel F Martinez <manpaz@bashlinux.com> - 0.2.17-42
- libusb with libusb-0.1.x has been renamed to libusb-compat-0.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.17-34
- Remove python2 subpackage (#1634547)

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.2.17-33
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.17-32
- Rebuild for new binutils

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.17-31
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.17-28
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.17-27
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.17-26
- Python 2 binary package renamed to python2-libhid
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Hans de Goede <hdegoede@redhat.com> - 0.2.17-23
- Fix FTBFS (rhbz#1421114)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-21
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 23 2016 Dan Horák <dan[at]danny.cz> - 0.2.17-20
- drop ExcludeArch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May  5 2014 Hans de Goede <hdegoede@redhat.com> - 0.2.17-15
- Fix FTBFS (rhbz#1094307)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Ian Weller <iweller@redhat.com> - 0.2.17-12
- Fix Python module for 64-bit machines

* Thu Aug  2 2012 Hans de Goede <hdegoede@redhat.com> - 0.2.17-11
- libhid still uses the old libusb-0.1.x, adjust [Build]Requires to match this
- Fix FTBFS (rhbz#716191)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Manuel F Martinez <manpaz@bashlinux.com> 0.2.17-7
- Build against libusb1

* Sun Aug 01 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> 0.2.17-6
- Allow build against swig-2.0 on Fedora > 13.

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> 0.2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Mar 06 2010 Manuel F Martinez <manpaz@bashlinux.com> 0.2.17-4
- Applied patch0 before autoreconf
- Added patch to fix compiler flags
- Fixed "duplicate file entries" warning on ppc
- Matched comment about files on python sub-package

* Sat Feb 27 2010 Manuel F Martinez <manpaz@bashlinux.com> 0.2.17-3
- Added autoreconf and cleaned build section
- Removed maintainer mode on configure
- Removed static library from python sub-package
- Cleaned up sed modifications
- Fixed Build Root name
- Removed CFLAGS and added _smp_mflags to make
- Fixed python subpackage conditional
- Fixed typos in description
- Added release number to requires in python sub-package

* Sat Feb 20 2010 Manuel F Martinez <manpaz@bashlinux.com> 0.2.17-2
- Fixed GPL version
- Removed unnecessary "makeinstall" and "defattr"
- Added libusb-devel to libhid-devel

* Wed Feb 17 2010 Manuel F Martinez <manpaz@bashlinux.com> 0.2.17-1
- Build on Fedora 12
- Added patch to fix manpage creation

* Thu May 03 2007 Charles Lepple <clepple+libhid@ghz.cc> 0.2.16-1
- Built on Fedora Core 6

* Sat Jan 15 2005 Jason Watson <jason.watson@agrios.net> 0.2.10-1
- Initial RPM build
