# Add --with pcc option to build with pcc (for sanity testing the compiler)
%bcond_with pcc

# Use our own configure in order to prevent --target, which makes autotools believe we are cross compiling
%global pccconfigure \
 export CFLAGS="${FLAGS}"; \
 export CXXFLAGS="${FLAGS}"; \
 export FFLAGS="${FLAGS} -I%{_fmoddir}"; \
 ./configure --program-prefix= --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} --infodir=%{_infodir}

# Used CVS snapshot
%global snapshot 20200203

# RPM does not play well with pcc compiled package
%if %{with pcc}
%define debug_package %{nil}
%endif

# Release tag
%define rel 1.1.%{snapshot}cvs

Name:           pcc
Version:        1.1.0

%if %{with pcc}
Release:        %{rel}_pcc%{?dist}.8
%else
Release:        %{rel}%{?dist}.8
%endif

Summary:        The Portable C Compiler
License:        BSD with advertising and BSD and ISC 
URL:            http://pcc.ludd.ltu.se/
Source0:        http://pcc.ludd.ltu.se/ftp/pub/pcc/pcc-%{snapshot}.tgz
Source1:        http://pcc.ludd.ltu.se/ftp/pub/pcc-libs/pcc-libs-%{snapshot}.tgz
# Patch to disable the use of -g in pcc-libs/csu/linux/ which is partly assembler code.
# Also, inlineing is disabled because it will break the code.
# Also, remove default -O flag from the code.
Patch0:         pcc-20141210-flags.patch

# Currently only x86 and x86_64 supported both in ppc and ppc-libs
ExclusiveArch:  %{ix86} x86_64
BuildRequires: make
BuildRequires:  bison
BuildRequires:  flex
Requires:       glibc-devel

%if %{with pcc}
BuildRequires:  pcc
%else
BuildRequires:  gcc
%endif

%description
The compiler is based on the original Portable C Compiler by Stephen
C. Johnson, written in the late 70's. Even though much of the
compiler has been rewritten, some of the basics still remain.

PCC debuted in Unix Version 7 and replaced the DMR compiler (Dennis
Ritchie's original C compiler) in both System V and the BSD 4.x
releases. Some history about pcc is in the A History of UNIX before
Berkeley: UNIX Evolution: 1975-1984 and in the Evolution of C.

About 50% of the front-end code and 80% of the back-end code has been
rewritten.  Most stuff is written by Anders Magnusson, with the
exception of the data-flow analysis part and the SSA conversion code
which is written by Peter A. Jonsson, and the Mips port that were
written as part of a project by undergraduate students at Luleå
University of Technology (LTU).

%prep
%setup -q -n pcc-%{snapshot} -a1
# Rename the libs directory
mv pcc-libs-%{snapshot} pcc-libs

# Apply patches
%patch0 -p1 -b .flags

%build
# Set architecture directory needed for include flag
%ifarch x86_64
export archdir=amd64
%endif
%ifarch %{ix86}
export archdir=i386
%endif

# Use pcc to build?
%if %{with pcc}
export FLAGS="-g -O"
export CC="pcc"
export CPP="pcc -E"
%else
export FLAGS="%{optflags}"
export CC="gcc"
export CPP="gcc -E"
%endif

# Flags for files that can't be built as debug
export CFLAGS_NODEBUG=`echo ${FLAGS} -fno-inline|sed "s| -g | |g"`

# First, build the library.
cd pcc-libs
%pccconfigure
make CFLAGS="-I${archdir} -Ilinux -I. ${FLAGS}" CFLAGS_NODEBUG="-I${archdir} -Ilinux -I. $CFLAGS_NODEBUG" 
#%{?_smp_mflags}
cd ..
# Then, build the compiler
%pccconfigure --with-assembler=%{_bindir}/as --with-linker=%{_bindir}/ld \
 --with-libdir=%{_libdir} --with-incdir=%{_includedir} --enable-tls \
 --disable-stripping
make 
#%{?_smp_mflags}


%install
rm -rf %{buildroot}
# Install the libraries
make -C pcc-libs install DESTDIR=%{buildroot}
# Install the compiler
make install DESTDIR=%{buildroot}
# Fix man file perms
chmod 644 %{buildroot}%{_mandir}/man1/*
# Rename cpp man page
mv  %{buildroot}%{_mandir}/man1/{,pcc-}cpp.1
# Directory for pcc-specific include files
mkdir -p %{buildroot}%{_includedir}/pcc

# Replace identical copied binary with hardlink
cd %{buildroot}%{_bindir}
if diff pcc pcpp > /dev/null; then
   ln -f pcc pcpp
fi

%files
%{_bindir}/pcc
%{_bindir}/p++
%{_bindir}/pcpp
%{_libdir}/pcc/
%{_includedir}/pcc/
%{_libexecdir}/cpp
%{_libexecdir}/cxxcom
%{_libexecdir}/ccom
%{_mandir}/man1/ccom.1.*
%{_mandir}/man1/pcc-cpp.1.*
%{_mandir}/man1/pcc.1.*
%{_mandir}/man1/p++.1.*
%{_mandir}/man1/pcpp.1.*

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20200203cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1.20200203cvs
- Update to 20200203 snapshot.

* Sun Feb 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1.20200201cvs
- Update to 20200201 snapshot.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20180504cvs.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20180504cvs.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20180504cvs.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20180504cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1.20180504cvs
- Update to 20180504 snapshot, fixing BZ #1551537.

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1.20180228cvs
- Update to 20180228 snapshot.
- Added gcc buildrequires.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20161201cvs.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20161201cvs.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20161201cvs.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20161201cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1.20161201cvs
- Update to 20161201 snapshot.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1.1.20160115cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1.20160115cvs
- Update to 20160115 snapshot.

* Thu Dec 31 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.1.20151231cvs
- Update to 20151231 snapshot.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-1.0.20141210cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1.0.20141210cvs
- Update to 20141210, the PCC 1.1.0 release.

* Sun Aug 17 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-0.1.20140817cvs
- Update to 20140817.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.2.20140420cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.1.20140420cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-0.1.20140420cvs
- Disable inlining in low level functions where it should not be done.
- Update to newest CVS release.

* Mon Aug 19 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.0-3.20111216cvs
- Fix FTBFS on rawhide.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2.20111216cvs.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2.20111216cvs.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2.20111216cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2.20111216cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-2.20111216cvs
- Use cvs checkout once again, fixing BZ #708305.

* Fri Apr 01 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-1
- Switch to using stable releases.
- Update to 1.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-0.4.20110203cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.20110203cvs
- Update to 20110203.

* Fri Nov 19 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.101119cvs
- Update to 20101119. x86_64 works now.
- Added possibility in the spec file to build pcc with itself.

* Wed Apr 14 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.100413cvs
- Update to 20100413.

* Sun Aug 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.090816cvs
- Update to 20090816, adding support for x86_64.
- Use own configure macro to disable cross compilation.

* Thu Aug 13 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.3.090813cvs
- Removed unneeded BR: byacc.
- Update to 20090813.

* Tue Aug 11 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.2.090811cvs
- Spec file cleanups.
- Update to 20090811.

* Sun Aug 09 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.2.090809cvs
- Changed --with-libdir to %%{_libdir} to make pcc use the glibc version of
  crt0.o by suggestion of upstream.
- Update to 20090809.

* Sat Aug 08 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.1.090808cvs
- First release.
