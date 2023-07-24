Name:           zlib-ada
Version:        1.4
Release:        0.34.20120830CVS%{?dist}
Summary:        Zlib for Ada
Summary(sv):    Zlib för ada

License:        GPLv3+ with exceptions
URL:            http://zlib-ada.sourceforge.net/
# The tarball was made with these commands:
# cvs -z3 -d:pserver:anonymous@zlib-ada.cvs.sourceforge.net:/cvsroot/zlib-ada co -P zlib-ada
# tar --create --exclude-vcs --bzip2 --file=zlib-ada-20120830.tar.bz2 zlib-ada
Source:         zlib-ada-20120830.tar.bz2
# This will be the source when there is a new release:
#Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2:        build_zlib_ada.gpr
Source3:        zlib_ada.gpr

BuildRequires:  gcc-gnat fedora-gnat-project-common
BuildRequires:  gprbuild
BuildRequires:  zlib-devel
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Zlib-Ada is a thick Ada binding to the popular compression/decompression \
library Zlib.

%global common_description_sv \
Zlib-Ada är en tjock adabindning till det populära komprimerings- och \
avkomprimeringsbiblioteket Zlib.

%description %{common_description_en}

%description -l sv %{common_description_sv}


%package devel
Summary:        Development files for Zlib-Ada
Summary(sv):    Filer för programmering med Zlib-Ada
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use Zlib-Ada.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder Zlib-Ada.


%prep
%setup -q -n zlib-ada
chmod a-x *  # Remove bogus executable bits.
cp %{SOURCE2} .


%build
gprbuild -P build_zlib_ada.gpr %{GPRbuild_optflags} -XDESTDIR=build_target -XLDFLAGS='%{__global_ldflags}'


%install
mv build_target/* --target-directory=%{buildroot}
# Add the project file for projects that use this library.
mkdir --parents %{buildroot}%{_GNAT_project_dir}
cp --preserve=timestamps %{SOURCE3} %{buildroot}%{_GNAT_project_dir}/


%files
%doc readme.txt
%license COPYING3 COPYING.RUNTIME
%{_libdir}/*.so.*

%files devel
%doc test.adb mtest.adb read.adb buffer_demo.adb
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/zlib-ada
%{_GNAT_project_dir}/*


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.34.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.33.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 1.4-0.32.20120830CVS
- Rebuilt with GCC 13.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.31.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.30.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.29.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.28.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Pavel Zhukov <pzhukov@redhat.com> - 1.4-0.27.20120830CVS
- Rebuild with new libgnat

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.26.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.25.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.24.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Pavel Zhukov <pzhukov@redhat.com> - 1.4-0.23.20120830CVS
- Rebuild for i686

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.22.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.21.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org - 1.4-0.20.20120830CVS
- rebuilt

* Sun Feb 04 2018 Björn Persson <Bjorn@Rombobjörn.se> - 1.4-0.19.20120830CVS
- Switched to building with GPRbuild as project file support was removed from
  Gnatmake in GCC 8.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.18.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.17.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 1.4-0.16.20120830CVS
- rebuild with new gnat

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-0.15.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Björn Persson <Bjorn@Rombobjörn.se> - 1.4-0.14.20120830CVS
- Rebuilt with GCC 7 prerelease.

* Fri Aug 12 2016 Björn Persson <Bjorn@Rombobjörn.se> - 1.4-0.13.20120830CVS
- Rebuilt to let it be built on new architectures.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 1.4-0.12.20120830CVS
- Rebuilt with GCC 6 prerelease.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-0.11.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Björn Persson <bjorn@rombobjörn.se> - 1.4-0.10.20120830CVS
- Tagged the license files as such.

* Sat Feb 07 2015 Björn Persson <bjorn@rombobjörn.se> - 1.4-0.9.20120830CVS
- Rebuilt with GCC 5.0.0.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-0.8.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-0.7.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Björn Persson <bjorn@rombobjörn.se> - 1.4-0.6.20120830CVS
- Rebuilt with GCC 4.9.0 prerelease.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-0.5.20120830CVS
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 24 2013 Björn Persson <bjorn@rombobjörn.se> - 1.4-0.4.20120830CVS
- Rebuilt with GCC 4.8.

* Mon Sep 03 2012 Björn Persson <bjorn@rombobjörn.se> - 1.4-0.3.20120830CVS
- Switched from GPRbuild to Gnatmake because the library fails to initialize
  itself when built with GPRbuild.

* Sat Sep 01 2012 Björn Persson <bjorn@rombobjörn.se> - 1.4-0.2.20120830CVS
- Remove bogus executable bits.

* Thu Aug 30 2012 Björn Persson <bjorn@rombobjörn.se> - 1.4-0.1.20120830CVS
- ready to be submitted for review
