%global avahi_version   0.6
%global soup_version    2.3
%global gtk2_version    2.10
%global glib2_version   2.15.1
%global gnutls_version  1.4
%global uuid_version    1.36

Name:           libepc
Version:        0.4.0
Release:        30%{?dist}
Summary:        Easy Publish and Consume library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://live.gnome.org/libepc/
Source0:        http://ftp.gnome.org/pub/gnome/sources/%{name}/0.4/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libuuid-devel >= %{uuid_version}
BuildRequires:  libsoup-devel >= %{soup_version}
BuildRequires:  avahi-ui-devel >= %{avahi_version}
BuildRequires:  gnutls-devel >= %{gnutls_version}
BuildRequires:  gtk2-devel >= %{gtk2_version}
BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool
BuildRequires: make


%description
A library to easily publish and consume values on networks


%package        ui
Summary:        Widgets for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    ui
The %{name}-ui package contains widget for use with %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{version}-%{release}
Requires:       libuuid-devel >= %{uuid_version}
Requires:       avahi-ui-devel%{?_isa} >= %{avahi_version}
Requires:       libsoup-devel%{?_isa} >= %{soup_version}
Requires:       gnutls-devel%{?_isa} >= %{gnutls_version}
Requires:       gtk2-devel%{?_isa} >= %{gtk2_version}
Requires:       glib2-devel%{?_isa} >= %{glib2_version}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --enable-static=no
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_flags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}



%ldconfig_scriptlets


%ldconfig_scriptlets ui


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_libdir}/%{name}-1.0.so.*


%files ui
%{_libdir}/%{name}-ui-1.0.so.*


%files devel
%{_includedir}/%{name}-ui-1.0/
%{_includedir}/%{name}-1.0/
%{_libdir}/%{name}-1.0.so
%{_libdir}/%{name}-ui-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/pkgconfig/%{name}-ui-1.0.pc
%{_datadir}/gtk-doc/html/%{name}-1.0/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-29
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4.0-2
- Rebuild for new libpng

* Fri Aug 05 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 0.4.0-1
- upstream 0.4.0
- reenable compilation with %%{?_smp_mflags}
- spec cleanup

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 24 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.11-1
- Update to 0.3.11.

* Tue Sep 29 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.3.10-3
- Add BR on libuuid-devel, and drop BR on e2fsprogs-devel.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun  5 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.3.10-1
- Update to 0.3.10.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.3.9-1
- Update to 0.3.9.

* Fri Oct 24 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8.
- Drop build patch.  Fixed upstream.

* Sat Sep 20 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.5-3
- Add patch to fix building from source.

* Tue Jun 24 2008 Tomas Mraz <tmraz@redhat.com> - 0.3.5-2
- rebuild with new gnutls

* Tue Apr 22 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5.

* Thu Feb 14 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.4-3
- Rebuild for new libsoup.

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.4-2
- Rebuild for gcc-4.3.

* Tue Jan 29 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4.
- Add BR on perl-xml-parser & gettext.
- Bump min version of libsoup.

* Tue Jan 15 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3.

* Tue Dec 18 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1.
- drop pk-config patch. fixed upstream.

* Sat Dec  8 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.0-3
- Remove rpath.
- Add requires for gtk2-devel to -devel.

* Sat Dec  8 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.0-2
- Merge ui-devel into devel.
- Add patch to fix .pc files.
- Add requires for gnutls-devel to -devel.
- keep timestamp on installed files.

* Tue Dec  4 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.3.0-1
- Intial Fedora spec.
