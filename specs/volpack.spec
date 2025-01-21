Name:          volpack
Version:       1.0c7
Release:       33%{?dist}
Summary:       Portable library for fast volume rendering
License:       BSD-3-Clause
URL:           http://amide.sourceforge.net
Source0:       http://downloads.sourceforge.net/amide/%{name}/%{name}-%{version}.tgz
Patch0:        volpack-aarch64.patch
Patch1:        volpack-c99.patch
Patch2:        volpack-1.0c7-fix-casts.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: m4

%description 
VolPack is a portable library of fast volume rendering algorithms that
produce high-quality images.


%package       devel
Summary:       Shared libraries and header files for development using volpack
Requires:      volpack = %{version}-%{release}

%description   devel
The volpack-devel package contains the header files and shared libraries
necessary for developing programs using the volpack volume rendering 
library.


%package       doc
Summary:       Documentation and examples for help using volpack
Requires:      volpack = %{version}-%{release}

%description   doc
The volpack-doc package contains docs and examples helpful for developing
programs using the volpack volume rendering library.


%prep
%setup -q
%patch -P0 -p1 -b .aarch64
%patch -P1 -p1 -b .c99
%patch -P2 -p1 -b .fix-casts


%build
%configure --disable-dependency-tracking --disable-static
# no %{?_smp_mflags} because parallel builds will fail very often
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# remove doc and example files we don't want to package
rm -f doc/vp_userguide..pdf doc/Makefile*
pushd examples
make clean
rm -f Makefile.*
chmod 644 test.csh
popd


%ldconfig_scriptlets



%files
%doc AUTHORS COPYING ChangeLog README
%{_mandir}/man3/*.3*
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so


%files doc
%doc doc/ examples/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb  3 2024 Tom Callaway <spot@fedoraproject.org> - 1.0c7-31
- fix casts to resolve FTBFS

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec  3 2022 Florian Weimer <fweimer@redhat.com> - 1.0c7-27
- Port to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0c7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0c7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0c7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0c7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0c7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Tom Callaway <spot@fedoraproject.org> - 1.0c7-8
- revive, fix for aarch64

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0c7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0c7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0c7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 04 2009 Sandro Mathys <red at fedoraproject.org> - 1.0c7-3
- Disabled parallel building due to problems

* Sat Oct 03 2009 Sandro Mathys <red at fedoraproject.org> - 1.0c7-2
- Fixed some bits and added a doc subpackage

* Sat Oct 03 2009 Sandro Mathys <red at fedoraproject.org> - 1.0c7-1
- initial build

