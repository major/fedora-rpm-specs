Name:           unique
Version:        1.1.6
Release:        35%{?dist}
Summary:        Single instance support for applications

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnome.org/~ebassi/source/
Source0:        http://download.gnome.org/sources/libunique/1.1/libunique-%{version}.tar.bz2

# Fix build -- upstream dead (replaced with GtkApplication)
Patch0:    fix-unused-but-set-variable.patch
Patch1:    fix-disable-deprecated.patch
Patch2:    libunique-1.1.6-format-security.patch

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-glib-devel
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libtool
BuildRequires:  glib2-devel >= 2.12.0
BuildRequires:  gtk2-devel >= 2.11.0
BuildRequires:  gtk-doc >= 1.11

%description
Unique is a library for writing single instance applications, that is
applications that are run once and every further call to the same binary
either exits immediately or sends a command to the running instance.

%package devel
Summary: Libraries and headers for Unique
Requires: %{name} = %{version}-%{release}
Requires: dbus-glib-devel
Requires: gtk2-devel

%description devel
Headers and libraries for Unique.

%prep
%setup -q -n libunique-%{?version}
%patch -P0 -p1 -b .unused-but-set-variable
%patch -P1 -p1 -b .disable-deprecated
%patch -P2 -p1 -b .format-security
# fix compatibility with gtk-doc 1.26
gtkdocize
autoreconf -fiv

%build
%configure --enable-gtk-doc --disable-static --enable-introspection=no --enable-maintainer-flags=no
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/unique-1.0/
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.6-34
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Merlin Mathesius <mmathesi@redhat.com> - 1.1.6-19
- Fix FTBFS by updating for compatibility with gtk-doc-1.26.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.6-11
- Add patch for format-security FTBFS

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> - 1.1.6-6
- Rebuild for new libpng

* Wed Jul 06 2011 Richard Hughes  <rhughes@redhat.com> - 1.1.6-5
- Fix compile harder.

* Wed Jul 06 2011 Richard Hughes  <rhughes@redhat.com> - 1.1.6-4
- Fix compile.
- Resolves: #716099

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> - 1.1.6-2
- Co-own /usr/share/gtk-doc (#604419)

* Thu Nov 12 2009 Richard Hughes  <rhughes@redhat.com> - 1.1.6-1
- Update to 1.1.4
- Brown paper bag release

* Thu Nov 12 2009 Richard Hughes  <rhughes@redhat.com> - 1.1.4-3
- Don't ship gir files by disabling introspection.
- BR gtk-doc

* Thu Nov 12 2009 Richard Hughes  <rhughes@redhat.com> - 1.1.4-2
- Don't ship gir files.

* Thu Nov 12 2009 Richard Hughes  <rhughes@redhat.com> - 1.1.4-1
- Update to 1.1.4
- Fixes nautilus segfaulting when launched from Places or the trash applet.

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhatcom> - 1.1.2-1
- Update to 1.1.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Richard Hughes  <rhughes@redhat.com> - 1.0.8-1
- Update to latest upstream version
 * Unbreak subclassing of UniqueApp
 * Remove upstreamed patches

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Matthias Clasen  <mclasen@redhat.com> - 1.0.4-3
- Actually apply the patch

* Sat Dec 20 2008 Matthias Clasen  <mclasen@redhat.com> - 1.0.4-2
- Fix a nautilus segfault

* Mon Nov 24 2008 Richard Hughes  <rhughes@redhat.com> - 1.0.4-1
- Update to latest upstream version
 * Plug a leak in UniqueMessageData
 * Fix linking with --as-needed
 * Do not export private functions symbols

* Sat Nov 22 2008 Richard Hughes  <rhughes@redhat.com> - 1.0.0-2
- Fix up summary text

* Thu Jul 31 2008 Richard Hughes  <rhughes@redhat.com> - 1.0.0-1
- Update to latest upstream version
 * First stable release
 * API is frozen
 * D-Bus and socket backends supported

* Fri May 16 2008 Richard Hughes  <rhughes@redhat.com> - 0.9.4-5
- More updates to the spec file from Dan Horak, rh#446407

* Thu May 15 2008 Richard Hughes  <rhughes@redhat.com> - 0.9.4-4
- Updates to the spec file from Dan Horak, rh#446407

* Thu May 08 2008 Richard Hughes  <rhughes@redhat.com> - 0.9.4-3
- Initial version

