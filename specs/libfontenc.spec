# Must be kept in sync with xorg-x11-fonts !
%define _x11fontdir		%{_datadir}/X11/fonts

Summary: X.Org X11 libfontenc runtime library
Name: libfontenc
Version: 1.1.8
Release: 4%{?dist}
# SPDX
License: MIT
URL: http://www.x.org
Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: libtool
BuildRequires: pkgconfig make
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: zlib-devel
BuildRequires: xorg-x11-font-utils

%description
X.Org X11 libfontenc runtime library

%package devel
Summary: X.Org X11 libfontenc development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libfontenc development package

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static --with-fontrootdir=%{_x11fontdir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Remove all libtool archives (*.la)
find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md ChangeLog
%{_libdir}/libfontenc.so.1
%{_libdir}/libfontenc.so.1.0.0

%files devel
%{_includedir}/X11/fonts/fontenc.h
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 04 2024 José Expósito <jexposit@redhat.com> - 1.1.8-1
- libfontenc 1.1.8

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 José Expósito <jexposit@redhat.com> - 1.1.7-1
- libfontenc 1.1.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.1.6-1
- libfontenc 1.1.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Benjamin Tissoires <benjamin.tissoires@redhat.com> - 1.1.4-2
- libfontenc 1.1.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-14
- Add make to BuildRequires

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Adam Jackson <ajax@redhat.com> - 1.1.3-8
- Use ldconfig scriptlet macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Adam Jackson <ajax@redhat.com> 1.1.3-1
- libfontenc 1.1.3

* Fri Oct 31 2014 Hans de Goede <hdegoede@redhat.com> - 1.1.2-3
- Pass --with-fontrootdir to ./configure so that libfontenc can find the
  encoding files (rhbz#1046341)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Benjamin Tissoires <benjamin.tissoires@redhat.com> 1.1.2-1
- libfontenc 1.1.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Adam Jackson <ajax@redhat.com> 1.1.1-1
- libfontenc 1.1.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Adam Jackson <ajax@redhat.com> 1.1.0-1
- libfontenc 1.1.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 07 2010 Parag Nemade <paragn AT fedoraproject.org> 1.0.5-3
- Merge-review cleanup (#226004)

* Fri Aug 28 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.0.5-2
- libfontenc-1.0.0-get-fontdir-from-pkgconfig.patch: rebase to 1.0.5.

* Fri Aug 28 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.0.5-1
- libfontenc 1.0.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.4-9
- Un-requires xorg-x11-filesystem

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.4-8
- Remove useless %%dir

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.4-6
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-5
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.0.4-4
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.0.4-3
- Don't install INSTALL

* Wed Jan 24 2007 Adam Jackson <ajax@redhat.com> 1.0.4-2
- Add BuildRequires on xorg-x11-font-utils to set encodings path correctly.

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 1.0.4-1
- Update to 1.0.4

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 1.0.3-1.fc7
- Update to 1.0.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.0.2-2.1
- rebuild

* Fri Jun 09 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-2
- Remove package ownership of mandir/libdir/etc.
- Added "BuildRequires: autoconf" temporarily as long as autoconf is needed

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.2-1
- Update to 1.0.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated libfontenc to version 1.0.1 from X11R7.0

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libfontenc to version 1.0.0 from X11R7 RC4
- Added libfontenc-1.0.0-get-fontdir-from-pkgconfig.patch which now replaces
  libfontenc-0.99.2-use-datadir-for-encodings.patch by using pkgconfig to
  query fontutil.pc for fontdir.
- Added "BuildRequires: font-utils >= 1.0.0" to find fontutil.pc
- Removed libfontenc-0.99.2-use-datadir-for-encodings.patch

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Updated libfontenc to version 0.99.3 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-3
- Bump xorg-x11-filesystem dep to >= 0.99.2-3 as -2 had bugs.

* Tue Nov 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-2
- Added libfontenc-0.99.2-use-datadir-for-encodings.patch and invoke aclocal
  and automake to activate the changes.  This fixes a bug reported against
  mkfontscale, in which it looks in _datadir for the font encodings files,
  which was traced back to libfontenc (#173875).
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-2" to ensure that
  /usr/include/X11 is a directory rather than a symlink before this package
  gets installed, to avoid bug (#173384).

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libfontenc to version 0.99.2 from X11R7 RC2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libfontenc to version 0.99.1 from X11R7 RC1

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-4
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Wed Aug 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Added zlib-devel build dependency

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
