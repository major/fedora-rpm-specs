# build with a bootstrap Common Lisp binary
%bcond_with bootstrap

%global common_lisp_controller 1

# generate/package docs
%global docs 1

# define to enable verbose build for debugging
%global sbcl_verbose 0
%global sbcl_shell /bin/bash

# SBCL name for the architecture
%ifarch %{ix86}
%global sbcl_arch x86
%else
%ifarch x86_64
%global sbcl_arch x86-64
%else
%ifarch aarch64
%global sbcl_arch arm64
%else
%ifarch %{power64}
%global sbcl_arch ppc64
%else
%endif
%endif
%endif
%endif

# Latest upstream binary releases, used for bootstrapping
%global bs_x86    1.4.3
%global bs_x86_64 2.3.11
%global bs_arm64  1.4.2
%global bs_ppc64  1.5.8

Name: 	 sbcl
Summary: Steel Bank Common Lisp
Version: 2.3.11
Release: 4%{?dist}

# See COPYING for a license breakdown
# FIXME: The files in src/pcl have a license similar, but not identical, to the
# Xerox license
License: LicenseRef-Fedora-Public-Domain AND LOOP AND BSD-3-Clause
URL:	 https://sbcl.sourceforge.io/
Source0: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{version}-source.tar.bz2

# Upstream has riscv32 and riscv64 support, but you need a Common Lisp binary
# to bootstrap with, and none seem to be available for RISC-V.  It might be
# possible to cross-compile the bootstrap SBCL from another architecture.
#
# Architectures supported by upstream that are no longer built by Fedora:
# - 32-bit ARM
# - 32-bit PowerPC
# - MIPS
# - Sparc
ExclusiveArch: %{ix86} x86_64 aarch64 %{power64}

# Pre-generated html docs
Source1: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{version}-documentation-html.tar.bz2

%if %{with bootstrap}
Source10: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{bs_x86}-x86-linux-binary.tar.bz2
Source20: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{bs_x86_64}-x86-64-linux-binary.tar.bz2
Source30: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{bs_arm64}-arm64-linux-binary.tar.bz2
Source40: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{bs_ppc64}-ppc64le-linux-binary.tar.bz2
%endif

%if %{with bootstrap}
%ifarch %{ix86}
%global sbcl_bootstrap_src -b 10
%global sbcl_bootstrap_dir sbcl-%{bs_x86}-x86-linux
%endif
%ifarch x86_64
%global sbcl_bootstrap_src -b 20
%global sbcl_bootstrap_dir sbcl-%{bs_x86_64}-x86-64-linux
%endif
%ifarch aarch64
%global sbcl_bootstrap_src -b 30
%global sbcl_bootstrap_dir sbcl-%{bs_arm64}-arm64-linux
%endif
%ifarch %{power64}
%global sbcl_bootstrap_src -b 40
%global sbcl_bootstrap_dir sbcl-%{bs_ppc64}-ppc64le-linux
%endif
%else
BuildRequires: sbcl
%endif

%if 0%{?common_lisp_controller}
BuildRequires: common-lisp-controller
Requires:      common-lisp-controller
Requires(post): common-lisp-controller
Requires(preun): common-lisp-controller
Source200: sbcl.sh
Source201: sbcl.rc
Source202: sbcl-install-clc.lisp
%endif

Patch1: sbcl-1.4.14-personality.patch
Patch2: sbcl-1.4.2-optflags.patch
Patch3: sbcl-2.0.1-verbose-build.patch

## upstreamable patches

## upstream patches

BuildRequires: make
BuildRequires: emacs-common
BuildRequires: gcc
BuildRequires: libzstd-devel
# %%check/tests
BuildRequires: ed
BuildRequires: hostname
BuildRequires: strace
%if 0%{?docs}
# doc generation
BuildRequires: ghostscript
BuildRequires: texinfo
BuildRequires: time
%endif

%description
Steel Bank Common Lisp (SBCL) is a Open Source development environment
for Common Lisp. It includes an integrated native compiler,
interpreter, and debugger.


%prep
%autosetup -N -c -n sbcl-%{version} %{?sbcl_bootstrap_src}
%setup -q -T -D -a 1
cd sbcl-%{version}
%autopatch -M 2 -p1
%{?sbcl_verbose:%patch 3 -p1 -b .verbose-build}

# upstream patches
#%%autopatch -m 4 -p1

# set version.lisp-expr
sed -i.rpmver -e "s|\"%{version}\"|\"%{version}-%{release}\"|" version.lisp-expr

# make %%doc items available in parent dir to make life easier
cp -alf BUGS COPYING README CREDITS NEWS TLA TODO PRINCIPLES ..
ln -s sbcl-%{version}/doc ../doc
cd -


%build
cd sbcl-%{version}

export CFLAGS='%{build_cflags}'
export LDFLAGS='%{build_ldflags}'
export CC=gcc

export SBCL_HOME=%{_prefix}/lib/sbcl
%{?sbcl_arch:export SBCL_ARCH=%{sbcl_arch}}
%{?sbcl_shell} \
./make.sh \
  --prefix=%{_prefix} \
  --with-sb-core-compression \
  %{?sbcl_bootstrap_dir:--xc-host='%{_builddir}/%{sbcl_bootstrap_dir}/run-sbcl.sh'}

# docs
%if 0%{?docs}
make -C doc/manual info

# Handle pre-generated docs
tar xvjf %{SOURCE1}
cp -av %{name}-%{version}/doc/manual/* doc/manual/
%endif
cd -


%install
cd sbcl-%{version}
mkdir -p %{buildroot}{%{_bindir},%{_prefix}/lib,%{_mandir}}

unset SBCL_HOME
export INSTALL_ROOT=%{buildroot}%{_prefix}
%{?sbcl_shell} ./install.sh

%if 0%{?common_lisp_controller}
install -m744 -p -D %{SOURCE200} %{buildroot}%{_prefix}/lib/common-lisp/bin/sbcl.sh
install -m644 -p -D %{SOURCE201} %{buildroot}%{_sysconfdir}/sbcl.rc
install -m644 -p -D %{SOURCE202} %{buildroot}%{_prefix}/lib/sbcl/install-clc.lisp
# linking ok? -- Rex
cp -p %{buildroot}%{_prefix}/lib/sbcl/sbcl.core %{buildroot}%{_prefix}/lib/sbcl/sbcl-dist.core
%endif
cd -

## Unpackaged files
rm -rfv %{buildroot}%{_docdir}/sbcl
rm -fv  %{buildroot}%{_infodir}/dir
# CVS crud
find %{buildroot} -name .cvsignore -delete
# 'test-passed' files from %%check
find %{buildroot} -name 'test-passed' -delete


%check
cd sbcl-%{version}
ERROR=0
# sanity check, essential contrib modules get built/included?
CONTRIBS="sb-posix.fasl sb-bsd-sockets.fasl"
for CONTRIB in $CONTRIBS ; do
  if [ ! -f %{buildroot}%{_prefix}/lib/sbcl/contrib/$CONTRIB ]; then
    echo "WARNING: ${CONTRIB} awol!"
    ERROR=1
    echo "ulimit -a"
    ulimit -a
  fi
done
pushd tests
# verify --version output
test "$(. ./subr.sh; "$SBCL_RUNTIME" --core "$SBCL_CORE" --version --version 2>/dev/null | cut -d' ' -f2)" = "%{version}-%{release}"
# still seeing Failure: threads.impure.lisp / (DEBUGGER-NO-HANG-ON-SESSION-LOCK-IF-INTERRUPTED)
time %{?sbcl_shell} ./run-tests.sh ||:
popd
exit $ERROR
cd -

%post
%if 0%{?common_lisp_controller}
/usr/sbin/register-common-lisp-implementation sbcl > /dev/null 2>&1 ||:
%endif

%preun
if [ $1 -eq 0 ]; then
%if 0%{?common_lisp_controller}
/usr/sbin/unregister-common-lisp-implementation sbcl > /dev/null 2>&1 ||:
%endif
fi

%files
%license COPYING
%doc BUGS CREDITS NEWS PRINCIPLES README TLA TODO
%{_bindir}/sbcl
%dir %{_prefix}/lib/sbcl/
%{_prefix}/lib/sbcl/sbcl.mk
%{_prefix}/lib/sbcl/contrib/
%{_mandir}/man1/sbcl.1*
%if 0%{?docs}
%doc doc/manual/sbcl.html
%doc doc/manual/asdf.html
%{_infodir}/asdf.info*
%{_infodir}/sbcl.info*
%endif
%if 0%{?common_lisp_controller}
%{_prefix}/lib/common-lisp/bin/*
%{_prefix}/lib/sbcl/install-clc.lisp
%{_prefix}/lib/sbcl/sbcl-dist.core
%verify(not md5 size) %{_prefix}/lib/sbcl/sbcl.core
%config(noreplace) %{_sysconfdir}/sbcl.rc
%else
%{_prefix}/lib/sbcl/sbcl.core
%endif


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Anthony Green <green@redhat.com> - 2.3.11-1
- Update to 2.3.11

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jerry James <loganjerry@gmail.com> - 2.3.6-1
- Version 2.3.6
- Convert License tag to SPDX
- Drop upstreamed gcc10 patch
- Build for ppc64le
- Compress cores with zstd instead of zlib
- Various minor spec file cleanups

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 16 2021 Than Ngo <than@redhat.com> - 2.0.1-7
- Fixed FTBFS

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 2.0.1-4
- Disable LTO for now

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Than Ngo <than@redhat.com> - 2.0.1-1
- update to 2.0.1

* Mon Feb 17 2020 Than Ngo <than@redhat.com> - 1.4.14-5
- Fixed FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.4.14-1
- 1.4.14

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.4.6-1
- 1.4.6

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.4.2-3
- BR: gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.4.2-1
- 1.4.2

* Wed Oct 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.4.0-1
- 1.4.0

* Fri Sep 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3.21-1
- 1.3.21

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3.19-1
- 1.3.19

* Sun Jun 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3.18-1
- 1.3.18

* Fri Jun 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3.17-1
- 1.3.17, de-bootstrap aarch64

* Wed Mar 29 2017 Than Ngo <than@redhat.com> - 1.3.16-2
- add support for aarch64

* Mon Mar 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.3.16-1
- 1.3.16

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.12-1
- 1.3.12

* Sat Dec 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.11-2
- %%build: --with-sb-core-compression

* Mon Nov 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.11-1
- 1.3.11

* Tue Aug 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.9-1
- 1.3.9

* Fri Apr 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.5-1
- 1.3.5

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.4-1
- 1.3.4

* Sat Mar 05 2016 Rex Dieter <rdieter@fedoraproject.org> 1.3.3-1
- 1.3.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-1
- 1.3.2

* Wed Nov 11 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-1
- 1.3.0
- initial aarch64 support (work in progress)

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.16-1
- 1.2.16

* Mon Sep 14 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.15-1
- 1.2.15

* Mon Jun 22 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.12-1
- 1.2.12

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.11-1
- 1.2.11

* Fri Feb 13 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.8-1
- 1.2.8

* Sat Jan 03 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.7-1
- 1.2.7

* Tue Dec 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.6-1
- 1.2.6

* Thu Oct 09 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.4-1
- 1.2.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-1
- 1.2.1

* Thu Jun 12 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.0-2
- rebuild using native sbcl

* Tue Jun 10 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.0-0.1.arm_bootstrap
- 1.2.0 (#1104857), arm(bootstrap)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.18-1
- 1.1.18

* Fri Mar 07 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.16-1
- 1.1.16

* Wed Jan 29 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.15-1
- 1.1.15

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.14-1
- 1.1.14

* Fri Nov 01 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.13-1
- 1.1.13

* Mon Sep 30 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.1.12-1
- 1.1.12
- (re)enable makeinfo docs on f19+
- .spec cleanup

* Sat Sep 07 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.11-1
- 1.1.11

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-2
- sbcl-1.1.8-nconc.patch (courtesy of jjames)

* Sun Jun 02 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-1
- 1.1.8

* Mon Apr 29 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.7-1
- 1.1.7

* Tue Feb 26 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.5-1
- 1.1.5

* Wed Feb 20 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.4-1
- 1.1.4
- omit texinfo generation on f19, texinfo-5.0 is borked (#913274)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.3-1
- 1.1.3
- fix build against glibc-2.17 (launchpad#1095036)

* Sat Dec 08 2012 Rex Dieter <rdieter@fedoraproject.org> 1.1.2-1
- 1.1.2

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-1
- 1.1.1

* Sat Oct 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-1
- 1.1.0

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.58-1
- 1.0.58

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.0.57-1
- sbcl-1.0.57
- fix/renable common-lisp support (accidentally disabled since 1.0.54-1)

* Thu Apr 12 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.56-1
- 1.0.56

* Thu Apr 05 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.55-1
- 1.0.55

* Mon Dec 05 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.54-1
- 1.0.54

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.53-1
- 1.0.53

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.52-1
- 1.0.52

* Mon Aug 22 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.51-2
- drop unused-for-a-long-time my_setarch.c
- fix sbcl --version output if built within git checkout

* Sun Aug 21 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.51-1
- 1.0.51

* Tue Jul 12 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.50-1
- 1.0.50

* Fri Mar 04 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.46-1
- 1.0.46

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Rex Dieter <rdieter@fedoraproject.org> -  1.0.44-1
- sbcl-1.0.44
- BR: ed (for %%check , tests)

* Thu Sep 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.43-1
- sbcl-1.0.43
- remove explict threading options, already enabled by default where
  it makes sense

* Wed Sep 29 2010 jkeating - 1.0.42-2
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.42-1
- sbcl-1.0.42

* Mon Aug 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.41-1
- sbcl-1.0.41

* Sat Jul 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.40-1
- sbcl-1.0.40

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.38-2
- shorten docs dangerously close to maxpathlen

* Fri Apr 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.38-1
- sbcl-1.0.38

* Wed Apr 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.37-1
- sbcl-1.0.37

* Mon Feb 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.35-1
- sbcl-1.0.35

* Tue Dec 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.33-1
- sbcl-1.0.33

* Mon Dec 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.32-2
- %%check: (re)enable run-tests.sh

* Mon Oct 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.32-1
- sbcl-1.0.32

* Tue Aug 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.30-2
- customize version.lisp-expr for rpm %%release
- s|%%_libdir|%%_prefix/lib|, so common-lisp-controller has at least
  a chance to work

* Tue Jul 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.30-1
- sbcl-1.0.30

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.29-1
- sbcl-1.0.29

* Thu Apr 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.28-1
- sbcl-1.0.28

* Wed Mar 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.26-1
- sbcl-1.0.26

* Fri Feb 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.25-3
- ExclusiveArch: s/i386/%%ix86/

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.25-1
- sbcl-1.0.25

* Wed Dec 31 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.24-1
- sbcl-1.0.24

* Mon Dec 01 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.23-1
- sbcl-1.0.23

* Thu Oct 30 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.22-1
- sbcl-1.0.22

* Thu Oct 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.21-1
- sbcl-1.0.21
- common-lisp-controller bits f10+ only (for now)
- drop never-used min_bootstrap crud

* Mon Sep 22 2008 Anthony Green <green@redhat.com> - 1.0.20-3
- Create missing directories.

* Sun Sep 21 2008 Anthony Green <green@redhat.com> - 1.0.20-2
- Add common-lisp-controller bits.

* Tue Sep 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.20-1
- sbcl-1.0.20

* Wed Jul 30 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.19-1
- sbcl-1.0.19

* Thu May 29 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.17-3
- info removal should be done in %%preun (#448933)
- omit ppc only on f9+ (#448734)

* Wed May 28 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.17-2
- omit ppc build (#448734)
- skip tests, known to (sometimes) hang

* Wed May 28 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0.17-1
- sbcl-1.0.17
