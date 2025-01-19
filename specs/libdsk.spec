Name:           libdsk
Version:        1.5.15
Release:        11%{?dist}
Summary:        Library for accessing disk images
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.seasip.info/Unix/LibDsk
Source0:        http://www.seasip.info/Unix/LibDsk/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires: make

%description
A library for accessing disk images, particularly for use with emulators.


%package devel
Summary:    Development files for libdsk
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for libdsk.


%package tools
Summary:    Tools for use with libdsk
Requires:   %{name} = %{version}

%description tools
Tools for use with libdsk.


%prep
%setup -q

# Fix dodgy permissions on files that end up in debuginfo package
find . -name '*.[ch]' | xargs chmod 0644

# EOL fixes for files that end up in the debuginfo package
sed -i 's/\r//' lib/*.h

# Character encoding fixes
iconv -f iso8859-1 doc/libdsk.txt -t utf8 > doc/libdsk.conv \
    && /bin/mv -f doc/libdsk.conv doc/libdsk.txt


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}



%ldconfig_scriptlets


%files
%{_libdir}/libdsk.so.*
%doc doc/COPYING ChangeLog TODO doc/libdsk.{pdf,txt}


%files tools
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*


%files devel
%{_libdir}/libdsk.so
%{_includedir}/libdsk.h
%exclude %{_libdir}/libdsk.la
%doc doc/cfi.html doc/apridisk.html doc/protocol.txt


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.15-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Lucian Langa <lucilanga@gnome.eu.org> - 1.5.15-1
- sync with latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Lucian Langa <lucilanga@gnome.eu.org> - 1.5.10-1
- sync with latest upstream

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.8-1
- sync with latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Lucian Langa <cooly@gnome.eu.org> - 1.2.2-1
- sync with latest upstream
- update source URL
- fix bogus dates
- misc cleanups

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 05 2008 Ian Chapman <packages[AT]amiga-hardware.com> 1.2.1-1
- Upgrade to 1.2.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.0-2
- Autorebuild for GCC 4.3

* Sun Jan 06 2008 Ian Chapman <packages[AT]amiga-hardware.com> 1.2.0-1
- Upgrade to 1.2.0
- Dropped open() patch, fixed upstream

* Wed Aug 22 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.1.14-2
- Release bump for F8 mass rebuild
- Corrected license

* Fri Aug 10 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.1.14-1
- Upgrade to 1.1.14
- Updated license field due to new guidelines
- Added patch to fix open() due to new macros

* Wed Jul 04 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.1.12-1
- Upgrade to 1.1.12
- Removed some extraneous 'docs'
- Moved some docs to the devel sub package

* Sat Sep 16 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.1.9-2
- rebuild

* Sun Apr 02 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.1.9-1
- Bump to new version

* Fri Nov 11 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.1.6.1
- Removed packager
- Altered BR to remove requirement for sed
- Fixed BuildRoot to honour FC rules
- Altered licence to GPL
- Altered numbering scheme for version
- Renamed spec file
- Added in new binaries and man files for dskdump and dskscan
- Bumped to upstream version 1.1.6
- A couple of fiddly fixes suggested by Paul Howard

* Mon Oct 17 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 1.1.4-1.2
- Alterations to Requires: and name

* Mon Jul 11 2005 Paul Johnson <paul@all-the-johnsons.co.uk> - 1.1.4-1.1.FC4
- Changed version for FC4

* Sun May 22 2005 Ian Chapman <packages[AT]amiga-hardware.com> - 1.1.4-1.iss
- Updated to version 1.1.4

* Mon Feb 28 2005 Ian Chapman <packages[AT]amiga-hardware.com> - 1.1.3-1.iss
- Changelog duplicated in spec file, fixed.
- Updated to version 1.1.3
- Removed some install commands, no longer needed with this version

* Fri Jul 16 2004 Ian Chapman <packages[AT]amiga-hardware.com> - 1.1.1-1.iss
- Updated to version to 1.1.1
- Updated for use with Fedora Core 2
- Split the tools from the main libdsk RPM

* Fri Dec 05 2003 Ian Chapman <packages[AT]amiga-hardware.com> - 1.1.0-2
- Minor fixes to changelog
- Changed copyright to distributable
- Moved a file from the main package to the devel package

* Mon Dec 01 2003 Ian Chapman <packages[AT]amiga-hardware.com> - 1.1.0-1
- Initial Release
