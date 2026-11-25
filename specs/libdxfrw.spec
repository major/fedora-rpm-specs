%global commit d73a25c61fa6b7f41000b38b4b4c8b32ed4e2fd1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global buildbin 1


Name:		libdxfrw
Version:	1.1.0
Release:	0.14.rc1%{?dist}
Summary:	Library to read/write DXF files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/LibreCAD/libdxfrw
Source0:	https://github.com/LibreCAD/libdxfrw/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:	gcc-c++
%if 0%{?epel} == 7
BuildRequires:	cmake3
%else
BuildRequires:	cmake
%endif
# Upstream development has only happened in the LibreCAD fork since 2022.
# Bring those changes here so we still have a viable library.

# Treat infinity bulge as zero angle for tangential polylines
# https://github.com/LibreCAD/LibreCAD/commit/aec7b7161087a7783f77369c77c6807b32b5bd2f
Patch1:		aec7b7161087a7783f77369c77c6807b32b5bd2f.patch
# Save closed splines with wrapped control points
# https://github.com/LibreCAD/LibreCAD/commit/25c2e472b0cd83e2b7ae28e523b89fe094fbd246
Patch2:		25c2e472b0cd83e2b7ae28e523b89fe094fbd246.patch
# drw_entities: coding style: initialize class members
# https://github.com/LibreCAD/LibreCAD/commit/6fd84ff6a952ab8a35e6e701ddac23a4c39d9fae
Patch3:		6fd84ff6a952ab8a35e6e701ddac23a4c39d9fae.patch
# avoid risky c style string functions
# https://github.com/LibreCAD/LibreCAD/commit/4fa20f7db90705ef30705857d404756e6ae48ad0
Patch4:		4fa20f7db90705ef30705857d404756e6ae48ad0.patch
# parseDWG specified override
# https://github.com/LibreCAD/LibreCAD/commit/0778a64d9535dc1b04495cf6b8b206ee68509004
Patch5:		0778a64d9535dc1b04495cf6b8b206ee68509004.patch
# Change DXF Export to use ext Style handle ID for 340 Dimstyle
# https://github.com/LibreCAD/LibreCAD/commit/cb7043c7c44a10dc4a89813faee9357ae21ffac7
Patch6:		cb7043c7c44a10dc4a89813faee9357ae21ffac7.patch
# more override fixes
# https://github.com/LibreCAD/LibreCAD/commit/3e6dbf7eb43ae3f5141ac7a74a75f93105d206ea
Patch7:		3e6dbf7eb43ae3f5141ac7a74a75f93105d206ea.patch
# Fixes for CodeQL scan (issue #1646)
# https://github.com/LibreCAD/LibreCAD/commit/d7b5b0a30bc096ec7a6802a2806258f9e6e39fea
Patch8:		d7b5b0a30bc096ec7a6802a2806258f9e6e39fea.patch
# Fix compiler warning
# https://github.com/LibreCAD/LibreCAD/commit/4dc3d5fa4b328873af07be05d7b67e5846628eb7
Patch9:		4dc3d5fa4b328873af07be05d7b67e5846628eb7.patch
# Header cleanup
# https://github.com/LibreCAD/LibreCAD/commit/1603a1ac5ef804b50b8fb583662c0bdcbf9ec72c
Patch10:	1603a1ac5ef804b50b8fb583662c0bdcbf9ec72c.patch
# MText: RTL bidi support backport
Patch11:	1a8202f1dc39c52d20ca49e697de9cc2c2d4fb0c.patch
# drw_entities: static analysis fixes
Patch12:	03fa108ab2fd74ab7b070daf5b36b29eb0428536.patch
# Backport a bounded hyperbola entity, drawing action and spline conversion
Patch13:	1eeda16c23f738fd934d467e90582f86e4d77794.patch
# 2.2.1: preserve entity visibility independently of frozen layers
Patch14:	fb40d56d42d96866af25aed56b1f60a627e43a49.patch
# 2.2.1: Fix undefined behavior found with sanitizers
Patch15:	d11a8d909ede733aa5fa3b20da17bbb5aeb2f21e.patch
# 2.2.1: Fix defects identified by static analysis
Patch16:	a536057a928aa051b6339d51f6764ff5c386c92f.patch
# 2.2.1: Let a hidden layer be current, and open DWG/DXF layers with their lock, current layer and off state
Patch17:	8477afa53995841d84d209eaa3516c98e3830052.patch
# Bound R2004 DWG page decoding
Patch18:	17ba2b273b89cc9c8b6fcf71882e327ccf1eebf6.patch
# NOT UPSTREAM: Properly init buffer var
Patch19:	libdxfrw-dwgbuffer-uninit.patch


%description
libdxfrw is a free C++ library to read and write DXF files in both formats,
ASCII and binary form.

%package devel
Summary:	Development files for libdxfrw
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libdxfrw.


%prep
%setup -q -n %{name}-%{commit}
%patch -P1 -p1 -b .aec7b7161087a7783f77369c77c6807b32b5bd2f
%patch -P2 -p1 -b .25c2e472b0cd83e2b7ae28e523b89fe094fbd246
%patch -P3 -p1 -b .6fd84ff6a952ab8a35e6e701ddac23a4c39d9fae
%patch -P4 -p1 -b .4fa20f7db90705ef30705857d404756e6ae48ad0
%patch -P5 -p1 -b .0778a64d9535dc1b04495cf6b8b206ee68509004
%patch -P6 -p1 -b .cb7043c7c44a10dc4a89813faee9357ae21ffac7
%patch -P7 -p1 -b .3e6dbf7eb43ae3f5141ac7a74a75f93105d206ea
%patch -P8 -p1 -b .d7b5b0a30bc096ec7a6802a2806258f9e6e39fea
%patch -P9 -p1 -b .4dc3d5fa4b328873af07be05d7b67e5846628eb7
%patch -P10 -p1 -b .1603a1ac5ef804b50b8fb583662c0bdcbf9ec72c
%patch -P11 -p1 -b .1a8202f1dc39c52d20ca49e697de9cc2c2d4fb0c
%patch -P12 -p1 -b .03fa108ab2fd74ab7b070daf5b36b29eb0428536
%patch -P13 -p1 -b .1eeda16c23f738fd934d467e90582f86e4d77794
%patch -P14 -p1 -b .fb40d56d42d96866af25aed56b1f60a627e43a49
%patch -P15 -p1 -b .d11a8d909ede733aa5fa3b20da17bbb5aeb2f21e
%patch -P16 -p1 -b .a536057a928aa051b6339d51f6764ff5c386c92f
%patch -P17 -p1 -b .8477afa53995841d84d209eaa3516c98e3830052
%patch -P18 -p1 -b .17ba2b273b89cc9c8b6fcf71882e327ccf1eebf6
%patch -P19 -p1 -b .dwgbuffer-uninit

%build
export CXXFLAGS="%{optflags} -Wno-error=unused-parameter -Wno-error=return-type"
%if 0%{?epel} == 7
%cmake3
%cmake3_build
%else
%if 0%{?buildbin}
%cmake -DLIBDXFRW_BUILD_DWG2DXF=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%else
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DLIBDXFRW_BUILD_DWG2DXF=0
%endif
%cmake_build
%endif

%install
%if 0%{?epel} == 7
%cmake3_install
%else
%cmake_install
%endif

%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog README
%if 0%{?buildbin}
%{_bindir}/dwg2dxf
%{_mandir}/man1/dwg2dxf.*
%endif
%{_libdir}/*.so.*

%files devel
%{_includedir}/libdxfrw
%{_libdir}/cmake/libdxfrw
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdxfrw.pc

%changelog
* Tue Nov 24 2026 Tom Callaway <spot@fedoraproject.org> - 1.1.0-0.14.rc1
- apply more fixes from the 2.2.1 LibreCAD git tree

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.13.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.12.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Aug  4 2025 Tom Callaway <spot@fedoraproject.org> - 1.1.0-0.11.rc1
- apply lots of fixes from the LibreCAD git tree
- conditionalize the dwg2dxf binary (still works but maybe won't forever)

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.10.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-0.8.rc1
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.7.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Tom Callaway <spot@fedoraproject.org> - 1.1.0-0.2.rc1
- update to latest code in git
- drop patch0 for now

* Wed Sep 14 2022 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-0.1.rc4
- Update to 1.1.0 RC1 per upstream recommendatation.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  1 2022 Tom Callaway <spot@fedoraproject.org> - 1.0.1-3
- apply fixes from upstream, including fix for CVE-2021-45343

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Tom Callaway <spot@fedoraproject.org> - 1.0.1-1
- rebase to new code home, fixes CVE-2021-21898/21899/21900

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Tom Callaway <spot@fedoraproject.org> - 0.6.3-18
- disable rpath

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Tom Callaway <spot@fedoraproject.org> - 0.6.3-16
- more fixes from LibreCAD git

* Wed Nov  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.6.3-15
- add all of the current fixes from LibreCAD git

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Tom Callaway <spot@fedoraproject.org> - 0.6.3-10
- add fix from librecad for CVE-2018-19105

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun  6 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.3-3
- apply changes from LibreCad 2.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.3-1
- update to 0.6.3

* Fri Sep 11 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.1-1
- update to 0.6.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-4
- Rebuilt for GCC 5 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Tom Callaway <spot@fedoraproject.org> - 0.5.11-1
- update to 0.5.11
- resync with librecad changes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-3
- apply fixes from librecad 2.0.0beta5

* Wed Apr 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-2
- drop empty NEWS and TODO files
- force INSTALL to use -p to preseve timestamps

* Sun Feb 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-1
- initial package
