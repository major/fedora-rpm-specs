Name:           NearTree
Version:        5.1.1
Release:        17%{?dist}
Summary:        An API for finding nearest neighbors

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://neartree.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/neartree/neartree/NearTree-%{version}/NearTree-%{version}.tar.gz
# library should not have version number in their name.
# Sent to upstream but upstream cannot accept.
Patch0:         NearTree-5.1.1-fedora.patch
# to fix libdir for lib64 architecture
Patch1:         NearTree-5.1.1-lib64.patch
BuildRequires: make
BuildRequires:  libtool time CVector-devel
BuildRequires:  gcc-c++

%description
This is a release of an API for finding nearest neighbors among
points in spaces of arbitrary dimensions. This release provides a
C++ template, TNear.h, and a C library, CNearTree.c, with
example/test programs.

%package devel
Summary:        Development tools for compiling programs using NearTree
Requires:       %{name} = %{version}-%{release}
Requires:       CVector-devel

%description devel
The NearTree-devel package includes the header and library files for
developing applications that use NearTree.

%prep
%setup -q
%patch -P0 -p1 -b .fedora
%if 0%{?__isa_bits} == 64
%patch -P1 -p1 -b .lib64
%endif

# convert end of line code from CRFL to LF
mv README_NearTree.txt README_NearTree.txt.orig
tr -d \\r < README_NearTree.txt.orig > README_NearTree.txt

%build
make all CFLAGS="%{optflags} -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1" %{?_smp_mflags}

%install
make install CFLAGS="%{optflags} -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1" INSTALL_PREFIX="%{buildroot}%{_prefix}"

# remove .la and .a files
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

%check
# Fails on i686 for some reason
%ifnarch ( %{ix86} && %{s390x} )
# make tests CFLAGS="%{optflags} -fno-caller-saves -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1"
%endif


%ldconfig_scriptlets

%files
%doc README_NearTree.html README_NearTree.txt lgpl.txt
%{_libdir}/libCNearTree.so.*

%files devel
%{_includedir}/CNearTree.h
%{_includedir}/TNear.h
%{_includedir}/rhrand.h
%{_includedir}/triple.h
%{_libdir}/libCNearTree.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.1.1-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 5.1.1 - 1
- Update to new 5.1.1.
- Disable test for now. They are too arch dependent.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.1-8
- Fix FTBFS, cleanup spec

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Takanori MATSUURA <t.matsuu@gmail.com> - 3.1.1-2
- add missing CVector-devel to Require in devel subpackage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jan  6 2012 Takanori MATSUURA <t.matsuu@gmail.com> - 3.1.1-1
- update to 3.1.1
- add time to BuildRequires

* Wed Jun  8 2011 Takanori MATSUURA <t.matsuu@gmail.com> - 3.1-1
- update to 3.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.4-1
- update to 2.4

* Tue Dec 14 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.2-2
- add "-fno-caller-saves" option for gcc-4.4.x

* Thu Nov 11 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.2-1
-  update to 2.3.2

* Fri Oct 22 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.1-1
- initial import (#545047)

* Mon Oct 18 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.1-0.1
- use "make all" instead of "make"
- add %%check

* Tue Oct 12 2010 Takanori MATSUURA <t.matsuu@gmail.com> - 2.3.1-0
- update to 2.3.1

* Wed Dec  9 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.4-3
- remove static library

* Tue Dec  8 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.4-2
- fit to Fedora Packaging Guidelines

* Thu Dec  3 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.4-1
- update to 2.1.4

* Wed Jul 29 2009 Takanori MATSUURA <t.matsuu@gmail.com> - 2.1.3-1
- initial build
