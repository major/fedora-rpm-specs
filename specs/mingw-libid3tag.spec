%{?mingw_package_header}

%global _basename libid3tag

Name:           mingw-%{_basename}
Version:        0.15.1b
Release:        41%{?dist}
Summary:        ID3 tag manipulation library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.underbit.com/products/mad/
Source0:        http://downloads.sourceforge.net/mad/%{_basename}-%{version}.tar.gz
# Fix CVE-2008-2109 (rhbz#445812)
Patch0:         libid3tag-0.15.1b-fix_overflow.patch
# Build libraries with "-no-undefined"
Patch1:         libid3tag-mingw.patch
Patch2:         libid3tag-0.15.1b-id3v1-zero-padding.patch
Patch3:         libid3tag-0.15.1b-handle-unknown-encoding.patch
Patch4:         libid3tag-0.15.1b-id3v2-endless-loop.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=869598
Patch5:         libid3tag-0.15.1b-gperf-size_t.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib >= 1.1.4

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib >= 1.1.4

BuildRequires:  gperf

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.


%package -n     mingw32-%{_basename}
Summary:        ID3 tag manipulation library

%description -n mingw32-%{_basename}
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.
This is the MinGW version, built for the win32 target.

%package -n     mingw64-%{_basename}
Summary:        ID3 tag manipulation library

%description -n mingw64-%{_basename}
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.
This is the MinGW version, built for the win64 target.


%{?mingw_debug_package}


%prep
%setup -q -n %{_basename}-%{version}
%patch -P0 -p0 -b .CVE-2008-2109
%patch -P1 -p0 -b .mingw
%patch -P2 -p1 -b .zero-padding
%patch -P3 -p1 -b .unknown-encoding
%patch -P4 -p0 -b .endless-loop
%patch -P5 -p1 -b .gperf

# Force these files to be regenerated from the .gperf sources.
rm compat.c frametype.c

# *.pc originally from the Debian package.
cat << \EOF > %{name}32.pc
prefix=%{mingw32_prefix}
exec_prefix=%{mingw32_exec_prefix}
libdir=%{mingw32_libdir}
includedir=%{mingw32_includedir}

Name: id3tag
Description: ID3 tag manipulation library
Requires:
Version: %{version}
Libs: -lid3tag
Cflags:
EOF

cat << \EOF > %{name}64.pc
prefix=%{mingw64_prefix}
exec_prefix=%{mingw64_exec_prefix}
libdir=%{mingw64_libdir}
includedir=%{mingw64_includedir}

Name: id3tag
Description: ID3 tag manipulation library
Requires:
Version: %{version}
Libs: -lid3tag
Cflags:
EOF


%build
%{mingw_configure} --disable-dependency-tracking --disable-static

# Fix libtool to recognize win64 archives
sed -i 's|file format pei\*-i386(\.\*architecture: i386)?|file format pe-x86-64|g' build_win64/libtool

%{mingw_make} %{?_smp_mflags}


%install
%{mingw_make} install DESTDIR=%{buildroot}
install -Dpm 644 %{name}32.pc %{buildroot}%{mingw32_libdir}/pkgconfig/id3tag.pc
install -Dpm 644 %{name}64.pc %{buildroot}%{mingw64_libdir}/pkgconfig/id3tag.pc
rm -f %{buildroot}/%{mingw32_libdir}/*.la
rm -f %{buildroot}/%{mingw64_libdir}/*.la


%files -n mingw32-%{_basename}
%doc CHANGES CREDITS README
%license COPYING COPYRIGHT
%{mingw32_bindir}/libid3tag-0.dll
%{mingw32_includedir}/id3tag.h
%{mingw32_libdir}/libid3tag.dll.a
%{mingw32_libdir}/pkgconfig/id3tag.pc

%files -n mingw64-%{_basename}
%doc CHANGES CREDITS README
%license COPYING COPYRIGHT
%{mingw64_bindir}/libid3tag-0.dll
%{mingw64_includedir}/id3tag.h
%{mingw64_libdir}/libid3tag.dll.a
%{mingw64_libdir}/pkgconfig/id3tag.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.15.1b-40
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.15.1b-33
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 David King <amigadave@amigadave.com> - 0.15.1b-25
- Add BuildRequires on C++ compilers (#1604838)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 David King <amigadave@amigadave.com> - 0.15.1b-24
- Add ID3v1 zero padding patch from Debian
- Add a fix for CVE-2017-11550 (#1561986)
- Add a fix for CVE-2004-2779 (#1561983)
- Use %%license, remove Group tag
- Add gperf patch from Debian

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 24 2014 David King <amigadave@amigadave.com> - 0.15.1b-18
- More closely match native package (#1076456)

* Fri May 17 2013 Steven Boswell <ulatekh@yahoo.com> - 0.15.1b-13
- Ported Fedora package to MinGW
