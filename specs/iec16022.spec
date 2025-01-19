# TODO: shared lib calls exit

Name:           iec16022
Version:        0.3.1
Release:        8%{?dist}
Summary:        Generate ISO/IEC 16022 2D barcodes

License:        GPL-2.0-or-later
URL:            https://github.com/rdoeffinger/iec16022
Source0:        https://github.com/rdoeffinger/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/rdoeffinger/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/C61D16E59E2CD10C895838A40899A2B906D4D9C7

BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  popt-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}


%description
The iec16022 is a program for producing ISO/IEC 16022 2D barcodes, also
known as Data Matrix. These barcodes are defined in the ISO/IEC 16022
standard.

%package        libs
Summary:        ISO/IEC 16022 libraries

%description    libs
The iec16022-libs package provides libraries for producing ISO/IEC 16022
2D barcodes, also known as Data Matrix. These barcodes are defined in the
ISO/IEC 16022 standard.

%package        devel
Summary:        Development files for the iec16022 library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The iec16022-devel package includes header files and libraries necessary
for developing programs which use the iec16022 C library.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libiec16022.la


%check
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
make -C test check


%ldconfig_scriptlets libs


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libiec16022.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libiec16022.so
%{_libdir}/pkgconfig/libiec16022.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 11 2022 Robert Scheck <robert@fedoraproject.org> - 0.3.1-1
- Upgrade to 0.3.1 (#2095939)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Robert Scheck <robert@fedoraproject.org> - 0.3.0-1
- Upgrade to 0.3.0 (#1911379)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Peter Gordon <peter@thecodergeek.com> - 0.2.4-12
- Update spec file in accordance with newer packaging guidelines:
  - Remove unnecessary BuildRoot references;
  - Remove %%defattr lines in %%files listings.
- Rerun autoconf in %%build to update for ARM64 arch support.
- Fixes bug #925577 (iec16022: Does not support aarch64 in f19 and rawhide)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 02 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-6
- Rearranging sed positions.

* Wed Jun 02 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-5
- Fixed test-suite(wasn't correctly fixed) and devel dependencies.

* Thu May 27 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-4
- Fixed test-suite and devel dependencies.

* Fri May 21 2010 Tareq Al Jurf <taljurf@fedoraproject.org> - 0.2.4-3
- Modify the spec according to Fedora Package Guidelines.

* Sat Mar 6 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.2.4-2
- Avoid rpath in executable.

* Sun Oct 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.2.4-1
- 0.2.4.

* Tue Jul 22 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.2.3-1
- 0.2.3.

* Sun Dec 30 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.2.2-1
- 0.2.2.

* Sat Nov 10 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.2.1-2
- BuildRequire popt-devel.
- License: GPLv2+

* Wed Nov 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.2.1-1
- 0.2.1.

* Sat Sep 30 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.2-2
- Rebuild.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.2-1
- First build.
