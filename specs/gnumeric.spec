Name:             gnumeric
Epoch:            1
Version:          1.12.57
Release:          2%{?dist}
Summary:          Spreadsheet program for GNOME
License:          GPL-2.0-only AND GPL-3.0-only AND LicenseRef-Callaway-LGPLv2+
URL:              http://www.gnumeric.org
Source:           https://download.gnome.org/sources/%{name}/1.12/%{name}-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gnumeric/-/merge_requests/34
Patch:            gnumeric-1.12.56-gcc14.patch
BuildRequires:    bison
BuildRequires:    desktop-file-utils
BuildRequires:    docbook-dtds
BuildRequires:    gcc
BuildRequires:    goffice-devel >= 0.10.46
BuildRequires:    intltool
BuildRequires:    itstool
BuildRequires:    libappstream-glib
BuildRequires:    libgda-ui-devel
BuildRequires:    make
BuildRequires:    perl-devel
BuildRequires:    perl-generators
BuildRequires:    perl(ExtUtils::Embed)
BuildRequires:    perl(Getopt::Long)
BuildRequires:    perl(IO::Compress::Gzip)
BuildRequires:    psiconv-devel
BuildRequires:    python3-gobject-devel
BuildRequires:    python3-devel
BuildRequires:    zlib-devel

# https://gitlab.gnome.org/GNOME/goffice/-/issues/70
ExcludeArch:    %{ix86}

Requires:         hicolor-icon-theme

%description
Gnumeric is a spreadsheet program for the GNOME GUI desktop
environment.


%package devel
Summary:          Files necessary to develop gnumeric-based applications
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Gnumeric is a spreadsheet program for the GNOME GUI desktop
environment. The gnumeric-devel package includes files necessary to
develop gnumeric-based applications.


%package plugins-extras
Summary:          Additional plugins for Gnumeric incl. Perl and Python support
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:         python(abi) = %{python3_version}

%description plugins-extras
This package contains the following additional plugins for gnumeric:
* gda and gnomedb plugins:
  Database functions for retrieval of data from a database.
* perl plugin:
  This plugin allows writing of plugins in Perl.
* python-loader plugin:
  This plugin allows writing of plugins in Python.
* py-func plugin:
  Sample Python plugin providing some (useless) functions.
* gnome-glossary:
  Support for saving GNOME Glossary in .po files. 


%prep
%autosetup -p1
chmod -x plugins/excel/rc4.?


%build
%configure --disable-silent-rules --disable-maintainer-mode
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install

%find_lang %{name} --all-name --with-gnome

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --delete-original                                  \
  --remove-category Science                                             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.%{name}.%{name}.appdata.xml

#remove .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Bytecompile Python plugins
%py_byte_compile %{__python3} $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}/plugins

%ldconfig_scriptlets


%files -f %{name}.lang
%doc HACKING AUTHORS ChangeLog NEWS BUGS README
%license COPYING
%{_bindir}/*
%{_libdir}/libspreadsheet-%{version}.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{version}
%exclude %{_libdir}/%{name}/%{version}/plugins/perl-*
%if 0%{?fedora} >= 37
%exclude %{_libdir}/%{name}/%{version}/plugins/gdaif
%endif
%exclude %{_libdir}/%{name}/%{version}/plugins/psiconv
%exclude %{_libdir}/%{name}/%{version}/plugins/gnome-glossary
%exclude %{_libdir}/%{name}/%{version}/plugins/py-*
%exclude %{_libdir}/%{name}/%{version}/plugins/python-*
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.*
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{version}
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_metainfodir}/org.%{name}.%{name}.appdata.xml
%{_mandir}/man1/*

%files devel
%{_libdir}/libspreadsheet.so
%{_libdir}/pkgconfig/libspreadsheet-1.12.pc
%{_includedir}/libspreadsheet-1.12

%files plugins-extras
%{_libdir}/%{name}/%{version}/plugins/perl-*
%if 0%{?fedora} >= 37
%{_libdir}/%{name}/%{version}/plugins/gdaif
%endif
%{_libdir}/%{name}/%{version}/plugins/psiconv
%{_libdir}/%{name}/%{version}/plugins/gnome-glossary
%{_libdir}/%{name}/%{version}/plugins/py-*
%{_libdir}/%{name}/%{version}/plugins/python-* 
%{_libdir}/goffice/*/plugins/gnumeric/gnumeric.so
%{_libdir}/goffice/*/plugins/gnumeric/plugin.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 08 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 1:1.12.57-1
- Update to 1.12.57
- Correct license tag
- Remove obolete patches and conditional

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.12.56-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.56-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.56-8
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:1.12.56-7
- Rebuilt for Python 3.13

* Mon Apr 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.12.56-6
- Update python3-gobject BuildRequires

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 David King <amigadave@amigadave.com> - 1:1.12.56-3
- Fix building against libxml2 2.12.0

* Mon Nov 06 2023 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.56-2
- Rebuild

* Sat Nov 04 2023 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.56-1
- Update to 1.12.56
- Drop i686 architecture

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.55-3
- Perl 5.38 rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1:1.12.55-2
- Rebuilt for Python 3.12

* Sat Feb 04 2023 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.55-1
- Update to 1.12.55

* Sat Jan 21 2023 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.54-1
- Update to 1.12.54

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 18 2022 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.53-1
- Update to 1.12.53
- Re-enable gdaif plugin on f37 and above

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:1.12.52-3
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.52-2
- Perl 5.36 rebuild

* Wed Apr 20 2022 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.52-1
- Update to 1.12.52
- Enable appdata file validation

* Sun Jan 23 2022 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.51-1
- Update to 1.12.51

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 13 2021 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.50-1
- Update to 1.12.50
- Drop upstreamed patch
- Fix URL and Source URL
- Drop gdaif plugin

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:1.12.49-3
- Rebuilt for Python 3.10

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.49-2
- Perl 5.34 rebuild

* Sun Mar 21 2021 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.49-1
- Update to 1.12.49
- Reenable python support

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.47-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.47-2
- Perl 5.32 rebuild

* Mon May 11 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.47-1
- Update to 1.12.47

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.46-1
- Update to 1.12.46
- Drop upstreamed patch

* Thu Aug 22 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.45-3
- Disable python support (RH #1737993)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.45-1
- Update to 1.12.45
- Update python2 patch
- Drop obsolete .spec sections

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.44-6
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1:1.12.44-4
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jan 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.12.44-3
- Move Python 2 plugins to gnumeric-plugins-extras to avoid unnecessary Python 2 dependency
- Drop pygtk2-devel BuildRequires

* Sat Jan 05 2019 Björn Esser <besser82@fedoraproject.org> - 1:1.12.44-2
- Add patch to explicitly use python2 shebangs, fixes FTBFS

* Mon Dec 24 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.44-1
- Update to 1.12.44
- Drop included patches

* Sun Aug 12 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.42-2
- Patched the install location of tools and widget headers using an upstream
  patch

* Sat Aug 11 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.42-1
- Updated to 1.12.42
- Fixed build failure using a patch from upstream git

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.41-2
- Perl 5.28 rebuild

* Thu May 10 2018 Julian Sikorski <belegdol@fedoraproject.org> - 0:1.12.41-2
- Updated to 1.12.41
- Ensured python2 is called explicitly as per https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build

* Sun May 06 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.40-1
- Updated to 1.12.40

* Sat Mar 17 2018 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.39-1
- Updated to 1.10.39
- Removed and/or updated obsolete scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1:1.12.38-2
- Rebuilt for switch to libxcrypt

* Sun Dec 31 2017 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.38-1
- Updated to 1.12.38

* Tue Nov 21 2017 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.36-1
- Updated to 1.12.36

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.35-1
- Updated to 1.12.35
- Corrected -plugins-extras subpackage summary (RH #1464742)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.34-2
- Perl 5.26 rebuild

* Mon Mar 27 2017 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.34-1
- Updated to 1.12.34
- Dropped upstreamed patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.33-1
- Updated to 1.12.33
- Fixed missing $DESTDIR in doc/Makefile.{in,am}
- Added docbook-dtds and itstool to BuildRequires, removed rarian-compat
- Patched to use xml-dtd-4.5 instead of xmlcharent

* Sat Aug 27 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.32-1
- Updated to 1.12.32

* Mon Jul 04 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.31-1
- Updated to 1.12.31

* Mon Jun 20 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.30-1
- Updated to 1.12.30
- Dropped upstreamed patches
- Spec file cleanups

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.29-3
- Perl 5.24 rebuild

* Sun May 15 2016 Hans de Goede <hdegoede@redhat.com> - 1:1.12.29-2
- Fix "usage of MIME type "zz-application/zz-winassoc-xls" is discouraged"
  warning showing every time a rpm transaction runs update-desktop-database
- Prune spec-file changelog

* Sat May 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.29-1
- Updated to 1.12.29

* Wed Mar 23 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.28-1
- Updated to 1.12.28

* Sun Feb 07 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.27-1
- Updated to 1.12.27
- Added bison to BuildRequires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.12.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.26-1
- Updated to 1.12.26

* Mon Dec 28 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.25-1
- Updated to 1.12.25

* Mon Oct 26 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.24-1
- Updated to 1.12.24

* Thu Jul 30 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.23-1
- Updated to 1.12.23

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.12.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.22-2
- Perl 5.22 rebuild

* Thu May 28 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.22-1
- Updated to 1.12.22

* Tue Apr 07 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.21-1
- Updated to 1.12.21

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 1:1.12.20-2
- Use better AppData screenshots

* Fri Feb 06 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.20-1
- Updated to 1.12.20

* Thu Jan 29 2015 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.19-1
- Updated to 1.12.19

* Sat Sep 27 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.18-1
- Updated to 1.12.18

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.12.17-3
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.12.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.17-1
- Updated to 1.12.17

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.12.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.16-1
- Updated to 1.12.16

* Sun May 04 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.15-1
- Updated to 1.12.15

* Mon Apr 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.14-1
- Updated to 1.12.14

* Fri Mar 21 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.13-1
- Updated to 1.12.13

* Mon Mar 17 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.12-2
- Fixed crash on strange .xls files (RH #1076912)

* Tue Mar 04 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.12-1
- Updated to 1.12.12

* Wed Feb 19 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.11-1
- Updated to 1.12.11

* Sun Feb 16 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.10-1
- Updated to 1.12.10

* Wed Jan 01 2014 Julian Sikorski <belegdol@fedoraproject.org> - 1:1.12.9-1
- Updated to 1.12.9
