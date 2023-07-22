#
# Copyright (c) 2006 Mellanox Technologies. All rights reserved.
#
# This Software is licensed under one of the following licenses:
#
# 3) under the terms of the "GNU General Public License (GPL) Version 2" a
#    copy of which is available from the Open Source Initiative, see
#    http://www.opensource.org/licenses/gpl-license.php.
#
# Redistributions of source code must retain the above copyright
# notice and one of the license notices.
#
# Redistributions in binary form must reproduce both the above copyright
# notice, one of the license notices in the documentation
# and/or other materials provided with the distribution.
#
#
#  $Id: ibutils.spec.in 7656 2006-06-04 09:38:34Z vlad $
#

Summary: OpenIB Mellanox InfiniBand Diagnostic Tools
Name: ibutils
Version: 1.5.7
Release: 40%{?dist}
# This is dual-licensed upstream, all code available under either license
License: GPLv2 or BSD
Url: https://www.openfabrics.org/
Source0: https://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.2.gbd7e502.tar.gz
Patch0: ibutils-1.5.7-tk86.patch
Patch1: ibutils-1.5.7-format-security.patch
Patch2: add-ibdev2netdev.patch
Patch3: ibutils-1.5.7-gcc10.patch
Requires: tcl, tk, graphviz-tcl
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires: libibverbs-devel >= 1.1
BuildRequires: opensm-devel >= 3.3.0
BuildRequires: tcl-devel
BuildRequires: swig
BuildRequires: tk-devel
BuildRequires: libibumad-devel
BuildRequires: autoconf
BuildRequires: graphviz-tcl
BuildRequires: chrpath
BuildRequires: perl-podlators
BuildRequires: autoconf, automake, libtool
BuildRequires: libstdc++-devel
BuildRequires: gcc, gcc-c++
BuildRequires: make
# RDMA is not currently built on 32-bit ARM: #1484155
ExcludeArch:   s390 s390x %{arm}

%description 
ibutils provides IB network and path diagnostics.

%package libs
Summary: Shared libraries used by ibutils binaries
%description libs
Shared libraries used by the Mellanox Infiniband diagnostic utilities

%package devel
Summary: Development files to use the ibutils shared libraries
Requires: ibutils-libs%{?_isa} = %{version}-%{release}
%description devel
Headers and static libraries needed to develop applications that use
the Mellanox Infiniband diagnostic utilities libraries

%package static
Summary: Static libraries for ibutils
Requires: ibutils-devel%{?_isa} = %{version}-%{release}
%description static
Static libraries from the Mellanox Infiniband diagnostic utilities

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2
%patch3 -p1 -b .gcc10

%build
autoreconf -fiv -I config
sed -i "s/^libibmscli_la_LIBADD =/& -lpthread/" ibmgtsim/src/Makefile.in
sed -e 's#all-am: Makefile $(PROGRAMS) $(LIBRARIES) $(LTLIBRARIES)#all-am: Makefile $(LIBRARIES) $(LTLIBRARIES) $(PROGRAMS)#' -i ibis/src/Makefile.in
%configure --with-osm=%{_prefix} --enable-ibmgtsim --disable-rpath CXXFLAGS="$CXXFLAGS -fno-strict-aliasing -fPIC -std=c++03"
# Workaround libtool reordering -Wl,--as-needed after all the libraries.
sed -e 's|^LTCC="gcc"|LTCC="gcc -Wl,--as-needed"|' \
    -e 's|^CC="g++"|CC="g++ -Wl,--as-needed"|' \
    -i ibdm/libtool ibis/libtool ibmgtsim/libtool

# The build isn't smp safe, so no %{?_smp_mflags}
export CXXFLAGS="$CXXFLAGS -fno-strict-aliasing -fPIC"
make

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_bindir}/git_version.tcl
# None of these files are scripts, but because in the tarball some have
# execute privs, that gets copied on install and rpmlint doesn't like them
chmod -x %{buildroot}%{_libdir}/ibdm%{version}/ibnl/*
find %{buildroot} -name \*.la -delete
chrpath -d %{buildroot}%{_bindir}/ib{mssh,nlparse,dmsh,topodiff,is,msquit,dmtr,dmchk}
chrpath -d %{buildroot}%{_libdir}/libib{sysapi,dm}.so.1.[01].[01]
chrpath -d %{buildroot}%{_libdir}/*/libib{dm,is}.so.%{version}
install -m 0755 ibdev2netdev %{buildroot}%{_bindir}

%ldconfig_scriptlets libs

%files
%{_bindir}/dump2psl.pl
%{_bindir}/dump2slvl.pl
%{_bindir}/ibis
%{_bindir}/ibdmsh
%{_bindir}/ibtopodiff
%{_bindir}/ibnlparse
%{_bindir}/ibdmtr
%{_bindir}/ibdmchk
%{_bindir}/ibdiagnet
%{_bindir}/ibdiagpath
%{_bindir}/ibdiagui
%{_bindir}/mkSimNodeDir
%{_bindir}/ibmssh
%{_bindir}/ibmsquit
%{_bindir}/RunSimTest
%{_bindir}/IBMgtSim
%{_bindir}/ibdev2netdev
%{_datadir}/ibmgtsim
%{_mandir}/*/*

%files libs
%license COPYING
%{_libdir}/libibdmcom.so.*
%{_libdir}/libibdm.so.*
%{_libdir}/libibmscli.so.*
%{_libdir}/libibsysapi.so.*
%dir %{_libdir}/ibis%{version}
%dir %{_libdir}/ibdm%{version}
%dir %{_libdir}/ibdiagnet%{version}
%dir %{_libdir}/ibdiagpath%{version}
%dir %{_libdir}/ibdiagui%{version}
%{_libdir}/ibis%{version}/*
%{_libdir}/ibdm%{version}/*
%{_libdir}/ibdiagnet%{version}/*
%{_libdir}/ibdiagpath%{version}/*
%{_libdir}/ibdiagui%{version}/*

%files devel
%{_libdir}/libibdmcom.so
%{_libdir}/libibdm.so
%{_libdir}/libibmscli.so
%{_libdir}/libibsysapi.so
%{_includedir}/ibdm
%{_includedir}/ibmgtsim

%files static
%{_libdir}/*.a

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 06 2020 Than Ngo <than@redhat.com> - 1.5.7-33
- Fixed FTBFS against gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Björn Esser <besser82@fedoraproject.org> - 1.5.7-30
- rebuilt(opensm)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Honggang Li <honli@redhat.com> - 1.5.7-27
- Add Buildrequires: gcc, gcc-c++
- Fix a bug in ibis Makefile.in
- Add script ibdev2netdev
- Resolves: bz1556746

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 26 2017 Honggang Li <honli@redhat.com> - 1.5.7-25
- Disable support for ARM32
- Resolves: bz1484155

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 18 2016 Honggang Li <honli@redhat.com> - 1.5.7-21
- Fix g++ compiling issue for Fedora 24 and later

* Wed Mar 16 2016 Doug Ledford <dledford@redhat.com> - 1.5.7-20
- Update to latest git tarball

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.7-17
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.7-15
- Sync platform Excludes with rest of OpenFabrics package set
- Minor spec cleanups

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.5.7-14
- Fix FTBFS with tcl-8.6 and -Werror=format-security (#1037127, #1106783)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.7-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue May 13 2014 Jaromir Capik <jcapik@redhat.com> - 1.5.7-11
- Replacing ppc64 with the power64 macro (#1076681)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.7-9
- Build on ARM too

* Tue Feb 12 2013 Jon Stanley <jonstanley@gmail.com> - 1.5.7-8
- Bump

* Tue Feb 12 2013 Jon Stanley <jonstanley@gmail.com> - 1.5.7-7.1
- perl-podlators added to BR for F19 build

* Wed Oct 24 2012 Jon Stanley <jonstanley@gmail.com> - 1.5.7-7
- Minor spec cleanup

* Wed Oct 24 2012 Jon Stanley <jonstanley@gmail.com> - 1.5.7-6
- Drop a static lib from -devel that I missed
- Add comment explaining dual license
- Drop swig runtime requirement
- Eliminate unnecessary linkage and undefined weak symbols
- Drop autoconf BR

* Tue Oct 23 2012 Jon Stanley <jonstanley@gmail.com> - 1.5.7-5
- Split out static libs into their own subpackage
- Remove unnecesary BuildRoot and defattr
- Add %%{?_isa} to explict deps
- Related: bz773485

* Fri Sep 02 2011 Doug Ledford <dledford@redhat.com> - 1.5.7-4
- Add a Requires for ibutils-libs to base ibutils package (found by rpmdiff)

* Thu Sep 01 2011 Doug Ledford <dledford@redhat.com> - 1.5.7-3
- Add a Requires on graphviz-tcl
- Resolves: bz734979

* Mon Aug 08 2011 Doug Ledford <dledford@redhat.com> - 1.5.7-2
- Fix the build so it generates proper debuginfo files
- Resolves: bz729019
- Related: bz725016

* Thu Aug 04 2011 Doug Ledford <dledford@redhat.com> - 1.5.7-1
- Update to latest upstream release
- Related: bz725016

* Thu Apr 28 2011 Doug Ledford <dledford@redhat.com> - 1.5.4-3.el6
- Build for i686 too
- Related: bz695204

* Tue Apr 19 2011 Dennis Gregorovic <dgregor@redhat.com> - 1.5.4-2.el6
- Build for ppc64
- Resolves: bz695204

* Mon Mar 08 2010 Doug Ledford <dledford@redhat.com> - 1.5.4-1.el6
- Update to latest upstream version, which cleans up some licensing issues
  found in the previous versions during review
- Related: bz555835

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 1.2-12.el6
- Update license for pkgwranger approval
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 1.2-11.el5
- Update to latest compatible upstream version
- Related: bz518218

* Fri Apr 17 2009 Doug Ledford <dledford@redhat.com> - 1.2-10
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Tue Nov 11 2008 Doug Ledford <dledford@redhat.com> - 1.2-9
- Oops, forgot to remove the man page for ibdiagui, fix that
- Related: bz468122

* Mon Nov 10 2008 Doug Ledford <dledford@redhat.com> - 1.2-8
- Remove ibdiagui from the package entirely since it still doesn't work
  without graphviz-tcl
- Related: bz468122

* Thu Oct 23 2008 Doug Ledford <dledford@redhat.com> - 1.2-7
- Grab the upstream ibutils git repo, find a checkout that supports the
  recent opensm library versions and yet doesn't require graphviz-tcl,
  export that tree to a tarball with a git designation, build from it.
- Resolves: bz468122

* Thu Sep 18 2008 Doug Ledford <dledford@redhat.com> - 1.2-6
- Add a build flag to silence some compile warnings

* Wed Sep 17 2008 Doug Ledford <dledford@redhat.com> - 1.2-4
- Upstream has updated the tarball without changing the version number,
  grab the tarball from the OFED-1.4-beta1 tarball and use it.
- Resolves: bz451467

* Tue Jan 29 2008 Doug Ledford <dledford@redhat.com> - 1.2-3
- Bump and rebuild against OFED 1.3 libraries
- Resolves: bz428198

* Wed Jun 27 2007 Doug Ledford <dledford@redhat.com> - 1.2-2
- Bump and rebuild against openib-1.2 libraries

* Mon Jun 25 2007 Doug Ledford <dledford@redhat.com> - 1.2-1
- Update to OFED 1.2 released package
- Related: bz245817

* Wed Oct 25 2006 Tim Powers <timp@redhat.com> - 1.0-3
- rebuild against openib package set due to soname change

* Fri Oct 20 2006 Doug Ledford <dledford@redhat.com>
- Bump and rebuild against latest openib packages
- Disable ibmgtsim until I can figure out why it's failing to wrap a
  perfectly existent library function (I hate c++)

* Mon Jul 31 2006 Doug Ledford <dledford@redhat.com> 1.0-2
- Make spec file name convention/multilib compliant
- Move all the files to FHS compliant locations for a distributor

* Tue May 16 2006 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Added ibutils sh, csh and conf to update environment

* Sun Apr  2 2006 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Initial packaging for openib gen2 stack
