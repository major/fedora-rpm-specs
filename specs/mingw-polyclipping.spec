# The Clipper C++ crystallographic library already uses the name "clipper".
# The developer is fine with the choosen name.

# API monitoring
# http://upstream-tracker.org/versions/clipper.html

%{?mingw_package_header}

%global mingw_pkg_name polyclipping

Name:           mingw-%{mingw_pkg_name}
Version:        6.4.2
Release:        20%{?dist}
Summary:        MinGW Windows Polygon clipping library

# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0
URL:            http://sourceforge.net/projects/polyclipping
Source0:        http://downloads.sourceforge.net/%{mingw_pkg_name}/clipper_ver%{version}.zip
# Add __declspec annotations; make cmake install the import lib as well
# http://sourceforge.net/p/polyclipping/bugs/62/
Patch0:         polyclipping.patch

BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildArch:      noarch

%description
This package contains the MinGW windows port of the clipper polygon
clipping library.

This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:                MinGW Windows Polygon clipping library for the win32 target

%description -n mingw32-%{mingw_pkg_name}
This package contains the MinGW win32 port of the clipper polygon
clipping library.

This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:                MinGW Windows Polygon clipping library for the win64 target

%description -n mingw64-%{mingw_pkg_name}
This package contains the MinGW win64 port of the clipper polygon
clipping library.

This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%{?mingw_debug_package}

%prep
%setup -qc

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in perl/perl_readme.txt README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done

%patch -P0 -p0 -b .mingw


%build
pushd cpp
  %mingw_cmake
  %mingw_make %{?_smp_mflags}
popd


%install
pushd cpp
  %mingw_make install DESTDIR=%{buildroot}
%if 0%{?mingw_build_win32} == 1
  install -d %{buildroot}/%{mingw32_libdir}
  install build_win32$MINGW_BUILDDIR_SUFFIX/libpolyclipping.dll.a %{buildroot}/%{mingw32_libdir}
%endif
%if 0%{?mingw_build_win64} == 1
  install -d %{buildroot}/%{mingw64_libdir}
  install build_win64$MINGW_BUILDDIR_SUFFIX/libpolyclipping.dll.a %{buildroot}/%{mingw64_libdir}
%endif
popd
install -d %{buildroot}/%{mingw32_libdir}/pkgconfig
install -d %{buildroot}/%{mingw64_libdir}/pkgconfig
mv %{buildroot}/%{mingw32_datadir}/pkgconfig/polyclipping.pc %{buildroot}/%{mingw32_libdir}/pkgconfig
mv %{buildroot}/%{mingw64_datadir}/pkgconfig/polyclipping.pc %{buildroot}/%{mingw64_libdir}/pkgconfig

%files -n mingw32-%{mingw_pkg_name}
%doc License.txt README
%{mingw32_includedir}/*
%{mingw32_libdir}/libpolyclipping.dll.a
%{mingw32_bindir}/libpolyclipping.dll
%{mingw32_libdir}/pkgconfig/polyclipping.pc

%files -n mingw64-%{mingw_pkg_name}
%doc License.txt README
%{mingw64_includedir}/*
%{mingw64_libdir}/libpolyclipping.dll.a
%{mingw64_bindir}/libpolyclipping.dll
%{mingw64_libdir}/pkgconfig/polyclipping.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 6.4.2-19
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.4.2-12
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 6.4.2-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.4.2-1
- update to 6.4.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.4-1
- update to 6.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec  4 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.2.0-1
- update to 6.2.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.3a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 02 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.3a-1
- update to 6.1.3a

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.6-1
- update to 5.1.6

* Thu Mar  7 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.2-2
- export std::vector specializations from DLL as well

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.3-4
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Sat Jan 19 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.0.3-3
- fix summary to contain the correct architecture name

* Sat Jan 19 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.0.3-2
- clarify this is the MinGW version in summary and description
- remove TODO comment

* Fri Jan 18 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.0.3-1
- update to 5.0.3

* Thu Jan 10 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 4.9.7-1
- created from native spec file
