Name:           ZipArchive
Version:        4.1.2
Release:        28%{?dist}
Summary:        Library for accessing zip files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.artpol-software.com/ZipArchive/
Source0:        http://www.artpol-software.com/Downloads/ziparchive_src.zip
# switch to Linux version
Patch0:         %{name}-linux-enable.patch
# add autotooled build system
Patch1:         %{name}-autotools.patch
# use system zlib
Patch2:         %{name}-system-zlib.patch
# Fix building with gcc-4.7
Patch3:         %{name}-gcc-4.7.patch 
# Fix ZipArchive not recognising dirs as such in some zips
Patch4:         %{name}-4.1.1-file-attr-fix.patch
# Fix ZipArchive not building with latest version of zlib
Patch5:         %{name}-4.1.1-new-zlib.patch

BuildRequires: make
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++

%description
The ZipArchive Library can be used to add compression functionality to your
software. It is written in C++ and offers the following features:
* Compression, decompression and modification of zip archives.
* Segmented archives support (splitting and spanning).
* Unicode support in archives compatible with WinZip.
* Standard zip encryption.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -c -p1

for i in ZipArchive/*.txt; do
    sed -i.old 's/\r//' "$i"
    touch -r "$i.old" "$i"
done

cd ZipArchive
rm -rf zlib bzip2
sh ./autogen.sh


%build
cd ZipArchive
%configure --disable-static
make %{?_smp_mflags}


%install
cd ZipArchive
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -p -m 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig


%files
%doc ZipArchive/License.txt
%{_libdir}/libziparch-%{version}.so

%files devel
%doc ZipArchive/{Appnote.txt,_readme.txt}
%{_includedir}/ZipArchive/
%{_libdir}/libziparch.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.2-27
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.1.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Dan Horák <dan[at]danny.cz> - 4.1.2-1
- updated to 4.1.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012 Hans de Goede <hdegoede@redhat.com> - 4.1.1-10
- Fix ZipArchive not building with the latest zlib

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-8
- Rebuilt for c++ ABI breakage

* Tue Jan 31 2012 Hans de Goede <hdegoede@redhat.com> - 4.1.1-7
- Fix ZipArchive not recognising dirs as such in some zips

* Mon Jan 23 2012 Hans de Goede <hdegoede@redhat.com> - 4.1.1-6
- Improve package description (rhbz#773313)

* Thu Jan 19 2012 Hans de Goede <hdegoede@redhat.com> - 4.1.1-5
- Drop custom cmake module, cmake using apps can use the .pc file
- Fix the .pc file to properly return -lziparch for --libs

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 4.1.1-4
- Make -devel package Requires on main package include isa
- Drop buildroot and defattr boilerplate (no longer needed with recent rpm)
- Fix building with gcc-4.7
- Fix various rpmlint warnings

* Fri Dec 23 2011 Dan Horák <dan[at]danny.cz> - 4.1.1-3
- use system zlib

* Tue Dec 13 2011 Dan Horák <dan[at]danny.cz> - 4.1.1-2
- add missing *_lnx.cpp files to the library

* Tue Dec 13 2011 Dan Horák <dan[at]danny.cz> - 4.1.1-1
- initial Fedora version
