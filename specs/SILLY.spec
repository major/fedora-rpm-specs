Name:           SILLY
Version:        0.1.0
Release:        41%{?dist}
Summary:        Simple and easy to use library for image loading
License:        MIT
URL:            http://www.cegui.org.uk
Source0:        http://downloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
Patch0:         SILLY-0.1.0-libpng15.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel

%description
The Simple Image Loading LibrarY is a companion library of the CEGUI project.
It provides a simple and easy to use library for image loading.

It currently supports the following formats:
TGA (Targa)
JPEG (Joint Photographic Experts Group)
PNG (Portable Network Graphics)


%package devel
Summary:        Development files for SILLY
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for SILLY


%prep
%setup -q -a1
%patch -P0 -p1

# Don't use full path, otherwise it shows buildroot as part of the path
sed -i 's|\(FULL_PATH_NAMES[ \t][ \t]*= \)YES|\1NO|' Doxyfile

# Get rid of some useless noise
sed -i 's|\(WARNINGS[ \t][ \t]*= \)YES|\1NO|' Doxyfile
sed -i 's|\(WARN_IF_UNDOCUMENTED[ \t][ \t]*= \)YES|\1NO|' Doxyfile
sed -i 's|\(WARN_IF_DOC_ERROR[ \t][ \t]*= \)YES|\1NO|' Doxyfile

# Generate developer man pages
sed -i 's|\(GENERATE_MAN[ \t][ \t]*= \)NO|\1YES|' Doxyfile

# Multiarch hack, we are now using prebuilt HTML
sed -i 's|\(GENERATE_HTML[ \t][ \t]*= \)YES|\1NO|' Doxyfile

#Fix encoding on AUTHORS
iconv -f iso8859-1 AUTHORS -t utf8 > AUTHORS.conv && /bin/mv -f AUTHORS.conv AUTHORS


%build
%configure --disable-static --with-pic
make %{?_smp_mflags}

#Build developer documentation
doxygen


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

#Install man pages
mkdir -p %{buildroot}%{_mandir}/man3
cp -a doc/man/man3/* %{buildroot}%{_mandir}/man3

#Fix so that RPM's strip works (only strips files marked executable)
chmod 0755 %{buildroot}%{_libdir}/*.so.*


%ldconfig_scriptlets


%files
%{_libdir}/*.so.*
%exclude %{_libdir}/*.la
%doc AUTHORS ChangeLog COPYING


%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*
%doc %{name}-%{version}/doc/html


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.0-19
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.1.0-14
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.1.0-13
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Hans de Goede <hdegoede@redhat.com> - 0.1.0-10
- Fix building with libpng-1.5

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.0-9
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.0-5
- Autorebuild for GCC 4.3

* Sun Oct 28 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-4
- Multiarch fixes (BZ 343181)

* Wed Aug 22 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-3
- Release bump for F8 mass rebuild

* Sun Mar 11 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-2
- Preserve timestamps on install
- Changed source URL
- Improved sed replacements
- Changed encoding of AUTHORS to UTF-8

* Mon Feb 26 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-1
- Initial Release