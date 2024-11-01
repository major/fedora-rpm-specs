%if (0%{?rhel} > 0 && 0%{?rhel} < 8)
# portable jdk 17 specific bug, _jvmdir being missing
%define _jvmdir /usr/lib/jvm
%endif

# debug_package %%{nil} is portable-jdks specific
%define  debug_package %{nil}

# RPM conditionals so as to be able to dynamically produce
# slowdebug/release builds. See:
# http://rpm.org/user_doc/conditional_builds.html
#
# Examples:
#
# Produce release, fastdebug *and* slowdebug builds on x86_64 (default):
# $ rpmbuild -ba java-1.8.0-openjdk.spec
#
# Produce only release builds (no debug builds) on x86_64:
# $ rpmbuild -ba java-1.8.0-openjdk.spec --without slowdebug --without fastdebug
#
# Only produce a release build on x86_64:
# $ fedpkg mockbuild --without slowdebug --without fastdebug

# Enable fastdebug builds by default on relevant arches.
%bcond_without fastdebug
# Enable slowdebug builds by default on relevant arches.
%bcond_without slowdebug
# Enable release builds by default on relevant arches.
%bcond_without release
# Remove build artifacts by default
%bcond_with artifacts
# Build a fresh libjvm.so for use in a copy of the bootstrap JDK
%bcond_without fresh_libjvm
# Build with system libraries
%bcond_with system_libs


%global is_system_jdk 0
%if %{with system_libs}
%global system_libs 1
%global link_type system
%global jpeg_lib |libjavajpeg[.]so.*
%else
%global system_libs 0
%global link_type bundled
%global jpeg_lib |libjpeg[.]so.*
%endif

# The -g flag says to use strip -g instead of full strip on DSOs or EXEs.
# This fixes detailed NMT and other tools which need minimal debug info.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1520879
%global _find_debuginfo_opts -g

# note: parametrized macros are order-sensitive (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter to other macros. If not macro, then it is considered a switch
# see the difference between global and define:
# See https://github.com/rpm-software-management/rpm/issues/127 to comments at  "pmatilai commented on Aug 18, 2017"
# (initiated in https://bugzilla.redhat.com/show_bug.cgi?id=1482192)
%global debug_suffix_unquoted -slowdebug
%global fastdebug_suffix_unquoted -fastdebug
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global fastdebug_suffix "%{fastdebug_suffix_unquoted}"
%global normal_suffix ""

%global debug_warning This package is unoptimised with full debugging. Install only as needed and remove ASAP.
%global fastdebug_warning This package is optimised with full debugging. Install only as needed and remove ASAP.
%global debug_on unoptimised with full debugging on
%global fastdebug_on optimised with full debugging on
%global for_fastdebug for packages with debugging on and optimisation
%global for_debug for packages with debugging on and no optimisation

%if %{with release}
%global include_normal_build 1
%else
%global include_normal_build 0
%endif

%if %{include_normal_build}
%global normal_build %{normal_suffix}
%else
%global normal_build %{nil}
%endif

%global aarch64         aarch64 arm64 armv8
# we need to distinguish between big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
# Set of architectures which support multiple ABIs
%global multilib_arches %{power64} sparc64 x86_64
# Set of architectures for which we build slowdebug builds
%global debug_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64}
# Set of architectures for which we build fastdebug builds
%global fastdebug_arches x86_64 ppc64le aarch64
# Set of architectures with a Just-In-Time (JIT) compiler
%global jit_arches      %{aarch64} %{ix86} %{power64} sparcv9 sparc64 x86_64
# Set of architectures which use the Zero assembler port (!jit_arches)
%global zero_arches %{arm} ppc s390 s390x riscv64
# Set of architectures which run a full bootstrap cycle
%global bootstrap_arches %{jit_arches} %{zero_arches}
# Set of architectures which support SystemTap tapsets
%global systemtap_arches %{jit_arches}
# Set of architectures which support the serviceability agent
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64}
# Set of architectures which support class data sharing
# See https://bugzilla.redhat.com/show_bug.cgi?id=513605
# MetaspaceShared::generate_vtable_methods is not implemented for the PPC JIT
%global shenandoah_arches x86_64 %{aarch64}
%global share_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64}
# Set of architectures which support Java Flight Recorder (JFR)
%global jfr_arches      %{jit_arches}
# Set of architectures for which alt-java has SSB mitigation
%global ssbd_arches x86_64
# Set of architectures where we verify backtraces with gdb
%global gdb_arches %{jit_arches} %{zero_arches}

# By default, we build a slowdebug build during main build on JIT architectures
%if %{with slowdebug}
%ifarch %{debug_arches}
%global include_debug_build 1
%else
%global include_debug_build 0
%endif
%else
%global include_debug_build 0
%endif

# On certain architectures, we compile the Shenandoah GC
%ifarch %{shenandoah_arches}
%global use_shenandoah_hotspot 1
%else
%global use_shenandoah_hotspot 0
%endif

# By default, we build a fastdebug build during main build only on fastdebug architectures
%if %{with fastdebug}
%ifarch %{fastdebug_arches}
%global include_fastdebug_build 1
%else
%global include_fastdebug_build 0
%endif
%else
%global include_fastdebug_build 0
%endif

%if %{include_debug_build}
%global slowdebug_build %{debug_suffix}
%else
%global slowdebug_build %{nil}
%endif

%if %{include_fastdebug_build}
%global fastdebug_build %{fastdebug_suffix}
%else
%global fastdebug_build %{nil}
%endif

# If you disable all builds, then the build fails
# Build and test slowdebug first as it provides the best diagnostics
%global build_loop %{slowdebug_build} %{fastdebug_build} %{normal_build}

%if 0%{?flatpak}
%global bootstrap_build false
%else
%ifarch %{bootstrap_arches}
%global bootstrap_build true
%else
%global bootstrap_build false
%endif
%endif

%global bootstrap_targets images
%global release_targets images docs-zip
# No docs nor bootcycle for debug builds
%global debug_targets images
# Target to use to just build HotSpot
%global hotspot_target hotspot

# Disable LTO as this causes build failures at the moment.
# See RHBZ#1861401
%define _lto_cflags %{nil}

# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -O flags so that the optimization of HotSpot is not lowered from O3 to O2
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We replace it with -Wformat (required by -Werror=format-security) and -Wno-cpp to avoid FORTIFY_SOURCE warnings
# We filter out -fexceptions as the HotSpot build explicitly does -fno-exceptions and it's otherwise the default for C++
%global ourflags %(echo %optflags | sed -e 's|-Wall|-Wformat -Wno-cpp|' | sed -r -e 's|-O[0-9]*||')
%global ourcppflags %(echo %ourflags | sed -e 's|-fexceptions||')
%global ourldflags %{__global_ldflags}

# With disabled nss is NSS deactivated, so NSS_LIBDIR can contain the wrong path
# the initialization must be here. Later the pkg-config have buggy behavior
# looks like openjdk RPM specific bug
# Always set this so the nss.cfg file is not broken
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
%global NSS_LIBS %(pkg-config --libs nss)
%global NSS_CFLAGS %(pkg-config --cflags nss-softokn)
# see https://bugzilla.redhat.com/show_bug.cgi?id=1332456
%global NSSSOFTOKN_BUILDTIME_NUMBER %(pkg-config --modversion nss-softokn || : )
%global NSS_BUILDTIME_NUMBER %(pkg-config --modversion nss || : )
# this is workaround for processing of requires during srpm creation
%global NSSSOFTOKN_BUILDTIME_VERSION %(if [ "x%{NSSSOFTOKN_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSSSOFTOKN_BUILDTIME_NUMBER}" ;fi)
%global NSS_BUILDTIME_VERSION %(if [ "x%{NSS_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSS_BUILDTIME_NUMBER}" ;fi)

# In some cases, the arch used by the JDK does
# not match _arch.
# Also, in some cases, the machine name used by SystemTap
# does not match that given by _target_cpu
%ifarch x86_64
%global archinstall amd64
%global stapinstall x86_64
%endif
%ifarch ppc
%global archinstall ppc
%global stapinstall powerpc
%endif
%ifarch %{ppc64be}
%global archinstall ppc64
%global stapinstall powerpc
%endif
%ifarch %{ppc64le}
%global archinstall ppc64le
%global stapinstall powerpc
%endif
%ifarch %{ix86}
%global archinstall i386
%global stapinstall i386
%endif
%ifarch ia64
%global archinstall ia64
%global stapinstall ia64
%endif
%ifarch s390
%global archinstall s390
%global stapinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%global stapinstall s390
%endif
%ifarch %{arm}
%global archinstall arm
%global stapinstall arm
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%global stapinstall arm64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%global stapinstall %{_target_cpu}
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%global stapinstall %{_target_cpu}
%endif
# riscv64
%ifarch riscv64
%global archinstall riscv64
%global stapinstall %{nil}
%endif
# Need to support noarch for srpm build
%ifarch noarch
%global archinstall %{nil}
%global stapinstall %{nil}
%endif

# Always off in portables
%ifarch %{systemtap_arches}
%global with_systemtap 0
%else
%global with_systemtap 0
%endif

# New Version-String scheme-style defines
%global featurever 1.8.0
%global majorver 8
# Define version of OpenJDK 8 used
%global project openjdk
%global repo shenandoah-jdk8u
%global openjdk_revision jdk8u432-b06
%global shenandoah_revision shenandoah-%{openjdk_revision}
# Define IcedTea version used for SystemTap tapsets and desktop file
# Define current Git revision for the FIPS support patches
%global fipsver 6d1aade0648
# Define current Git revision for the cacerts patch
%global cacertsver 8139f2361c2

# Standard JPackage naming and versioning defines
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{shenandoah_revision}

# Settings for local security configuration
%global security_file %{top_level_dir_name}/jdk/src/share/lib/security/java.security-%{_target_os}
%global cacerts_file /etc/pki/java/cacerts
# JDK to use for bootstrapping
# Use OpenJDK 7 where available (on RHEL) to avoid
# having to use the rhel-7.x-java-unsafe-candidate hack
%if ! 0%{?fedora} && 0%{?rhel} <= 7
%global buildjdkver 1.7.0
%else
%global buildjdkver 1.8.0
%endif
# JDK to use for bootstrapping
%global bootjdk /usr/lib/jvm/java-%{buildjdkver}-openjdk
# Define whether to use the bootstrap JDK directly or with a fresh libjvm.so
# This will only work where the bootstrap JDK is the same major version
# as the JDK being built
%if %{with fresh_libjvm} && "%{buildjdkver}" == "%{featurever}"
%global build_hotspot_first 1
%else
%global build_hotspot_first 0
%endif

# Define vendor information used by OpenJDK
%global oj_vendor Red Hat, Inc.
%global oj_vendor_url https://www.redhat.com/
# Define what url should JVM offer in case of a crash report
# order may be important, epel may have rhel declared
%if 0%{?epel}
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL&component=%{component}&version=epel%{epel}
%else
%if 0%{?fedora}
# Does not work for rawhide, keeps the version field empty
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&component=%{component}&version=%{fedora}
%else
%if 0%{?rhel}
%global oj_vendor_bug_url https://access.redhat.com/support/cases/
%else
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi
%endif
%endif
%endif
%global oj_vendor_version (Red_Hat-%{version}-%{rpmrelease})

%global javaver         1.%{majorver}.0
# e.g. aarch64-shenandoah-jdk8u212-b04-shenandoah-merge-2019-04-30 -> aarch64-shenandoah-jdk8u212-b04
%global version_tag     %(VERSION=%{shenandoah_revision}; echo ${VERSION%%-shenandoah-merge*})
# eg # jdk8u60-b27 -> jdk8u60 or # aarch64-jdk8u60-b27 -> aarch64-jdk8u60  (dont forget spec escape % by %%)
%global whole_update    %(VERSION=%{version_tag}; echo ${VERSION%%-*})
# eg  jdk8u60 -> 60 or aarch64-jdk8u60 -> 60
%global updatever       %(VERSION=%{whole_update}; echo ${VERSION##*u})
# eg jdk8u60-b27 -> b27
%global buildver        %(VERSION=%{version_tag}; echo ${VERSION##*-})
%global rpmrelease      %(echo "%autorelease" | sed 's;%{?dist};;')
# priority must be 7 digits in total; up to openjdk 1.8
%if %is_system_jdk
%global priority        1800%{updatever}
%else
# for techpreview, using 1, so slowdebugs can have 0
%global priority        0000001
%endif
# Define milestone (EA for pre-releases, GA ("fcs") for releases)
# Release will be (where N is usually a number starting at 1):
# - 0.N%%{?extraver}%%{?dist} for EA releases,
# - N%%{?extraver}{?dist} for GA releases
%global is_ga           1
%if %{is_ga}
%global milestone          fcs
%global milestone_version  %{nil}
%global extraver %{nil}
%global eaprefix %{nil}
%else
%global milestone          ea
%global milestone_version  "-ea"
%global extraver .%{milestone}
%global eaprefix 0.
%endif

# parametrized macros are order-sensitive
%global compatiblename  java-%{javaver}-%{origin}
%global fullversion     %{compatiblename}-%{version}-%{release}
# images directories from upstream build
%global jdkimage       j2sdk-image
%global jreimage       j2re-image
# output dir stub
%define buildoutputdir() %{expand:build/jdk8.build%{?1}}
%define installoutputdir() %{expand:install/jdk8.install%{?1}}
%define packageoutputdir() %{expand:packages/jdk8.packages%{?1}}
# we can copy the javadoc to not arched dir, or make it not noarch
%define uniquejavadocdir()    %{expand:%{fullversion}%{?1}}
# main id and dir of this jdk
%define uniquesuffix()        %{expand:%{fullversion}.%{_arch}%{?1}}
%define jreportablenameimpl() %(echo %{uniquesuffix ""} | sed "s;%{version}-%{release};\\0.portable%{1}.jre;g" | sed "s;openjdkportable;el;g")
%define jdkportablenameimpl() %(echo %{uniquesuffix ""} | sed "s;%{version}-%{release};\\0.portable%{1}.jdk;g" | sed "s;openjdkportable;el;g")
%define jdkportablesourcesnameimpl() %(echo %{uniquesuffix ""} | sed "s;%{version}-%{release};\\0.portable%{1}.sources;g" | sed "s;openjdkportable;el;g" | sed "s;.%{_arch};.noarch;g")
%define staticlibsportablenameimpl() %(echo %{uniquesuffix ""} | sed "s;%{version}-%{release};\\0.portable%{1}.static-libs;g" | sed "s;openjdkportable;el;g")
%define jreportablearchive()  %{expand:%{jreportablenameimpl -- %%{1}}.tar.xz}
%define jdkportablearchive()  %{expand:%{jdkportablenameimpl -- %%{1}}.tar.xz}
%define jdkportablesourcesarchive()  %{expand:%{jdkportablesourcesnameimpl -- %%{1}}.tar.xz}
%define jreportablename()     %{expand:%{jreportablenameimpl -- %%{1}}}
%define jdkportablename()     %{expand:%{jdkportablenameimpl -- %%{1}}}
%define jdkportablesourcesname()     %{expand:%{jdkportablesourcesnameimpl -- %%{1}}}
%define docportablename() %(echo %{uniquesuffix ""} | sed "s;%{version}-%{release};\\0.portable.docs;g" | sed "s;openjdkportable;el;g")
%define docportablearchive()  %{docportablename}.tar.xz
%define miscportablename() %(echo %{uniquesuffix ""} | sed "s;%{version}-%{release};\\0.portable.misc;g" | sed "s;openjdkportable;el;g")
%define miscportablearchive()  %{miscportablename}.tar.xz

# RPM 4.19 no longer accept our double percentaged %%{nil} passed to %%{1}
# so we have to pass in "" but evaluate it, otherwise files record will include it
%define jreportablearchiveForFiles()  %(echo %{jreportablearchive -- ""})
%define jdkportablearchiveForFiles()  %(echo %{jdkportablearchive -- ""})
%define jdkportablesourcesarchiveForFiles()  %(echo %{jdkportablesourcesarchive -- ""})
%define jdkportablesourcesnameForFiles()  %(echo %{jdkportablesourcesname -- ""})

# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349.
# See also https://bugzilla.redhat.com/show_bug.cgi?id=1590796
# as to why some libraries *cannot* be excluded. In particular,
# these are:
# libjsig.so, libjava.so, libjawt.so, libjvm.so and libverify.so
%global _privatelibs libatk-wrapper[.]so.*|libattach[.]so.*|libawt_headless[.]so.*|libawt[.]so.*|libawt_xawt[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libhprof[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas_unix[.]so.*|libjava_crw_demo[.]so.*%{jpeg_lib}|libjdwp[.]so.*|libjli[.]so.*|libjsdt[.]so.*|libjsoundalsa[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libnpt[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsplashscreen[.]so.*|libsunec[.]so.*|libsystemconf[.]so.*|libunpack[.]so.*|libzip[.]so.*|lib[.]so\\(SUNWprivate_.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$


# Standard JPackage directories and symbolic links.
%global sdkdir()        %{expand:%{uniquesuffix -- %{?1}}}
%global jrelnk()        %{expand:jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}%1}

%global jredir()        %{expand:%{sdkdir -- %{?1}}/jre}
%global sdkbindir()     %{expand:%{_jvmdir}/%{sdkdir -- %{?1}}/bin}
%global jrebindir()     %{expand:%{_jvmdir}/%{jredir -- %{?1}}/bin}
%global alt_java_name     alt-java
%global jvmjardir()     %{expand:%{_jvmjardir}/%{uniquesuffix %%1}}

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/

# For flatpack builds hard-code /usr/sbin/alternatives,
# otherwise use %%{_sbindir} relative path.
%if 0%{?flatpak}
%global alternatives_requires /usr/sbin/alternatives
%else
%global alternatives_requires %{_sbindir}/alternatives
%endif

# x86 is no longer supported
%if 0%{?java_arches:1}
ExclusiveArch:  %{java_arches}
%else
ExcludeArch: %{ix86}
%endif

# Prevent brp-java-repack-jars from being run
%global __jar_repack 0

# portables have grown out of its component, moving back to java-x-vendor
# this expression, when declared as global, filled component with java-x-vendor portable
%define component %(echo %{name} | sed "s;-portable;;g")

Name:    java-%{javaver}-%{origin}-portable
Version: %{javaver}.%{updatever}.b06
Release: %{?eaprefix}%{rpmrelease}%{?extraver}%{?dist}
# java-1.5.0-ibm from jpackage.org set Epoch to 1 for unknown reasons
# and this change was brought into RHEL-4. java-1.5.0-ibm packages
# also included the epoch in their virtual provides. This created a
# situation where in-the-wild java-1.5.0-ibm packages provided "java =
# 1:1.5.0". In RPM terms, "1.6.0 < 1:1.5.0" since 1.6.0 is
# interpreted as 0:1.6.0. So the "java >= 1.6.0" requirement would be
# satisfied by the 1:1.5.0 packages. Thus we need to set the epoch in
# JDK package >= 1.6.0 to 1, and packages referring to JDK virtual
# provides >= 1.6.0 must specify the epoch, "java >= 1:1.6.0".

Epoch:   1
Summary: %{origin_nice} %{majorver} Runtime Environment portable edition
# Groups are only used up to RHEL 8 and on Fedora versions prior to F30
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

# HotSpot code is licensed under GPLv2
# JDK library code is licensed under GPLv2 with the Classpath exception
# The Apache license is used in code taken from Apache projects (primarily JAXP & JAXWS)
# DOM levels 2 & 3 and the XML digital signature schemas are licensed under the W3C Software License
# The JSR166 concurrency code is in the public domain
# The BSD and MIT licenses are used for a number of third-party libraries (see THIRD_PARTY_README)
# The OpenJDK source tree includes the JPEG library (IJG), zlib & libpng (zlib), giflib and LCMS (MIT)
# The test code includes copies of NSS under the Mozilla Public License v2.0
# The PCSClite headers are under a BSD with advertising license
# The elliptic curve cryptography (ECC) source code is licensed under the LGPLv2.1 or any later version
License:  ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib
URL:      http://openjdk.java.net/

# Shenandoah HotSpot
# aarch64-port/jdk8u-shenandoah contains an integration forest of
# OpenJDK 8u, the aarch64 port and Shenandoah
# To regenerate, use:
# VERSION=%%{shenandoah_revision}
# FILE_NAME_ROOT=%%{project}-%%{repo}-${VERSION}
# REPO_ROOT=<path to checked-out repository> generate_source_tarball.sh
# where the source is obtained from http://github.com/%%{project}/%%{repo}
Source0: gnu-andrew-%{shenandoah_revision}.tar.xz

# Custom README for -src subpackage
Source2:  README.md


# Use 'icedtea_sync.sh' to update the following
# They are based on code contained in the IcedTea project (3.x).
# Systemtap tapsets. Zipped up to keep it small.
# Disabled in portables
#Source8: tapsets-icedtea-%%{icedteaver}.tar.xz

# Desktop files. Adapted from IcedTea
# Disabled in portables
#Source9: jconsole.desktop.in

# Release notes
Source10: NEWS

# nss configuration file
Source11: nss.cfg.in

# Removed libraries that we link instead
Source12: remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

# Verify system crypto (policy) can be disabled via a property
Source15: TestSecurityProperties.java

# Ensure vendor settings are correct
Source16: CheckVendor.java

# nss fips configuration file
Source17: nss.fips.cfg.in

# Ensure translations are available for new timezones
Source18: TestTranslations.java

# Disabled in portables
#Source20: repackReproduciblePolycies.sh

# New versions of config files with aarch64 support. This is not upstream yet.
Source100: config.guess
Source101: config.sub

############################################
#
# RPM/distribution specific patches
#
# This section includes patches specific to
# Fedora/RHEL which can not be upstreamed
# either in their current form or at all.
############################################

# Accessibility patches
# Ignore AWTError when assistive technologies are loaded
Patch1:   rh1648242-accessible_toolkit_crash_do_not_break_jvm.patch
# Turn on AssumeMP by default on RHEL systems
Patch534: rh1648246-always_instruct_vm_to_assume_multiple_processors_are_available.patch
# RH1648249: Add PKCS11 provider to java.security
Patch1000: rh1648249-add_commented_out_nss_cfg_provider_to_java_security.patch
# RH1582504: Use RSA as default for keytool, as DSA is disabled in all crypto policies except LEGACY
Patch1003: rh1582504-rsa_default_for_keytool.patch

# Crypto policy and FIPS support patches
# Patch is generated from the fips tree at https://github.com/rh-openjdk/jdk8u/tree/fips
# as follows: git diff %%{openjdk_revision} common jdk > fips-8u-$(git show -s --format=%h HEAD).patch
# Diff is limited to src and make subdirectories to exclude .github changes
# Fixes currently included:
# PR3183, RH1340845: Support Fedora/RHEL8 system crypto policy
# PR3655: Allow use of system crypto policy to be disabled by the user
# RH1655466: Support RHEL FIPS mode using SunPKCS11 provider
# RH1760838: No ciphersuites available for SSLSocket in FIPS mode
# RH1860986: Disable TLSv1.3 with the NSS-FIPS provider until PKCS#11 v3.0 support is available
# RH1906862: Always initialise JavaSecuritySystemConfiguratorAccess
# RH1929465: Improve system FIPS detection
# RH1996182: Login to the NSS software token in FIPS mode
# RH1991003: Allow plain key import unless com.redhat.fips.plainKeySupport is set to false
# RH2021263: Resolve outstanding FIPS issues
# RH2052819: Fix FIPS reliance on crypto policies
# RH2052829: Detect NSS at Runtime for FIPS detection
# RH2036462: sun.security.pkcs11.wrapper.PKCS11.getInstance breakage
# RH2090378: Revert to disabling system security properties and FIPS mode support together
Patch1001: fips-8u-%{fipsver}.patch

#############################################
#
# Upstreamable patches
#
# This section includes patches which need to
# be reviewed & pushed to the current development
# tree of OpenJDK.
#############################################
# PR2737: Allow multiple initialization of PKCS11 libraries
Patch5: pr2737-allow_multiple_pkcs11_library_initialisation_to_be_a_non_critical_error.patch
# Turn off strict overflow on IndicRearrangementProcessor{,2}.cpp following 8140543: Arrange font actions
Patch512: rh1649664-awt2dlibraries_compiled_with_no_strict_overflow.patch
# RH1337583, PR2974: PKCS#10 certificate requests now use CRLF line endings rather than system line endings
Patch523: pr2974-rh1337583-add_systemlineendings_option_to_keytool_and_use_line_separator_instead_of_crlf_in_pkcs10.patch
# PR3083, RH1346460: Regression in SSL debug output without an ECC provider
Patch528: pr3083-rh1346460-for_ssl_debug_return_null_instead_of_exception_when_theres_no_ecc_provider.patch
# PR2888: OpenJDK should check for system cacerts database (e.g. /etc/pki/java/cacerts)
# PR3575, RH1567204: System cacerts database handling should not affect jssecacerts
# RH2055274: Revert default keystore to JAVA_HOME/jre/lib/security/cacerts in portable builds
# Must be applied after the FIPS patch as it also changes java.security
# Patch is generated from the cacerts tree at https://github.com/rh-openjdk/jdk8u/tree/cacerts
# as follows: git diff fips > pr2888-rh2055274-support_system_cacerts-$(git show -s --format=%h HEAD).patch
Patch539: pr2888-rh2055274-support_system_cacerts-%{cacertsver}.patch
Patch541: rh1684077-openjdk_should_depend_on_pcsc-lite-libs_instead_of_pcsc-lite-devel.patch
# RH1750419: Enable build of speculative store bypass hardened alt-java (CVE-2018-3639)
Patch600: rh1750419-redhat_alt_java.patch

#############################################
#
# Arch-specific upstreamable patches
#
# This section includes patches which need to
# be reviewed & pushed upstream and are specific
# to certain architectures. This usually means the
# current OpenJDK development branch, but may also
# include other trees e.g. for the AArch64 port for
# OpenJDK 8u.
#############################################
# s390: PR3593: Use "%z" for size_t on s390 as size_t != intptr_t
Patch103: pr3593-s390_use_z_format_specifier_for_size_t_arguments_as_size_t_not_equals_to_int.patch
# x86: S8199936, PR3533: HotSpot generates code with unaligned stack, crashes on SSE operations (-mstackrealign workaround)
Patch105: jdk8199936-pr3533-enable_mstackrealign_on_x86_linux_as_well_as_x86_mac_os_x.patch
# S390 ambiguous log2_intptr calls
Patch107: s390-8214206_fix.patch

# Add support for RISC-V (riscv64)
#Patch130: java-1.8.0-riscv-1.patch


#############################################
#
# Patches which need backporting to 8u
#
# This section includes patches which have
# been pushed upstream to the latest OpenJDK
# development tree, but need to be backported
# to OpenJDK 8u.
#############################################
# S8074839, PR2462: Resolve disabled warnings for libunpack and the unpack200 binary
# This fixes printf warnings that lead to build failure with -Werror=format-security from optflags
Patch502: pr2462-resolve_disabled_warnings_for_libunpack_and_the_unpack200_binary.patch
# PR3591: Fix for bug 3533 doesn't add -mstackrealign to JDK code
Patch571: jdk8199936-pr3591-enable_mstackrealign_on_x86_linux_as_well_as_x86_mac_os_x_jdk.patch
# 8143245, PR3548: Zero build requires disabled warnings
Patch574: jdk8143245-pr3548-zero_build_requires_disabled_warnings.patch
# s390: JDK-8203030, Type fixing for s390
Patch102: jdk8203030-zero_s390_31_bit_size_t_type_conflicts_in_shared_code.patch
# 8035341: Allow using a system installed libpng
Patch202: jdk8035341-allow_using_system_installed_libpng.patch
# 8042159: Allow using a system-installed lcms2
Patch203: jdk8042159-allow_using_system_installed_lcms2-root.patch
Patch204: jdk8042159-allow_using_system_installed_lcms2-jdk.patch
# JDK-8257794: Zero: assert(istate->_stack_limit == istate->_thread->last_Java_sp() + 1) failed: wrong on Linux/x86_32
Patch581: jdk8257794-remove_broken_assert.patch
# JDK-8186464, RH1433262: ZipFile cannot read some InfoZip ZIP64 zip files
Patch12: jdk8186464-rh1433262-zip64_failure.patch

#############################################
#
# Patches appearing in 8u401
#
# This section includes patches which are present
# in the listed OpenJDK 8u release and should be
# able to be removed once that release is out
# and used by this RPM.
#############################################

#############################################
#
# Patches ineligible for 8u
#
# This section includes patches which are present
# upstream, but ineligible for upstream 8u backport.
#############################################
# 8043805: Allow using a system-installed libjpeg
Patch201: jdk8043805-allow_using_system_installed_libjpeg.patch

#############################################
#
# Shenandoah fixes
#
# This section includes patches which are
# specific to the Shenandoah garbage collector
# and should be upstreamed to the appropriate
# trees.
#############################################

#############################################
#
# Non-OpenJDK fixes
#
# This section includes patches to code other
# that from OpenJDK.
#############################################

#############################################
#
# Dependencies
#
#############################################
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: alsa-lib-devel
BuildRequires: binutils
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
# elfutils only are OK for build without AOT
BuildRequires: elfutils-devel
BuildRequires: file
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: gdb
%if (0%{?rhel} > 0 && 0%{?rhel} < 8)
# rhel7 only, portables only. Rhel8 have gtk3, rpms have runtime recommends of gtk
BuildRequires: gtk2-devel
%endif
BuildRequires: libxslt
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
# Requirement for setting up nss.cfg and nss.fips.cfg
BuildRequires: nss-devel
# Requirement for system security property test
# N/A for portable. RHEL7 doesn't provide them
#BuildRequires: crypto-policies
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: zip
BuildRequires: tar
BuildRequires: unzip
# Require a boot JDK which doesn't fail due to RH1482244
BuildRequires: java-%{buildjdkver}-openjdk-devel >= 1.7.0.151-2.6.11.3
# Zero-assembler build requirement
%ifarch %{zero_arches}
BuildRequires: libffi-devel
%endif
# 2023c required as of JDK-8305113
BuildRequires: tzdata-java >= 2023c
# cacerts build requirement in portable mode
BuildRequires: ca-certificates
# Earlier versions have a bug in tree vectorization on PPC
BuildRequires: gcc >= 4.8.3-8

%if %{with_systemtap}
BuildRequires: systemtap-sdt-devel
%endif

%if %{system_libs}
BuildRequires: giflib-devel
BuildRequires: lcms2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
%else
# Version in jdk/src/share/native/java/util/zip/zlib/zlib.h
Provides: bundled(zlib) = 1.2.13
# Version in jdk/src/share/native/sun/awt/giflib/gif_lib.h
Provides: bundled(giflib) = 5.2.1
# Version in jdk/src/share/native/sun/java2d/cmm/lcms/lcms2.h
Provides: bundled(lcms2) = 2.10.0
# Version in jdk/src/share/native/sun/awt/image/jpeg/jpeglib.h
Provides: bundled(libjpeg) = 6b
# Version in jdk/src/share/native/sun/awt/libpng/png.h
Provides: bundled(libpng) = 1.6.39
# We link statically against libstdc++ to increase portability
BuildRequires: libstdc++-static
%endif

%description
The %{origin_nice} %{majorver} runtime environment - portable edition

%if %{include_normal_build}
%package devel
Summary: %{origin_nice} %{majorver} Development Environment portable edition
Group:   Development/Tools
%description devel
The %{origin_nice} %{majorver} development tools - portable edition
%endif

%if %{include_debug_build}
%package slowdebug
Summary: %{origin_nice} %{majorver} Runtime Environment portable edition %{debug_on}
Group:   Development/Languages
%description slowdebug
The %{origin_nice} %{majorver} runtime environment - portable edition
%{debug_warning}

%package devel-slowdebug
Summary: %{origin_nice} %{majorver} Development Environment portable edition %{debug_on}
Group:   Development/Tools
%description devel-slowdebug
The %{origin_nice} %{majorver} development tools - portable edition
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package fastdebug
Summary: %{origin_nice} %{majorver} Runtime Environment portable edition %{fastdebug_on}
Group:   Development/Languages
%description fastdebug
The %{origin_nice} %{majorver} runtime environment - portable edition
%{fastdebug_warning}

%package devel-fastdebug
Summary: %{origin_nice} %{majorver} Development Environment portable edition %{fastdebug_on}
Group:   Development/Tools
%description devel-fastdebug
The %{origin_nice} %{majorver} development tools - portable edition
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package unstripped
Summary: The %{origin_nice} %{majorver} runtime environment, unstripped.
Group:   Development/Languages
%description unstripped
The %{origin_nice} %{majorver} runtime environment, unstripped.
%endif

%if %{include_normal_build}
%package docs
Summary: %{origin_nice} %{majorver} API documentation
Group:   Development/Languages
%description docs
The %{origin_nice} %{majorver} API documentation.
%endif

%package misc
Summary: %{origin_nice} %{majorver} miscellany
Group:   Development/Languages
%description misc
The %{origin_nice} %{majorver} miscellany.
%package sources
Summary: %{origin_nice} %{majorver} full patched sources of portable JDK

%description sources
The %{origin_nice} %{majorver} full patched sources of portable JDK to build, attach to debuggers or for debuginfo
%prep

echo "Preparing %{oj_vendor_version}"

if [ %{include_normal_build} -eq 0 -o  %{include_normal_build} -eq 1 ] ; then
  echo "include_normal_build is %{include_normal_build}"
else
  echo "include_normal_build is %{include_normal_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 11
fi
if [ %{include_debug_build} -eq 0 -o  %{include_debug_build} -eq 1 ] ; then
  echo "include_debug_build is %{include_debug_build}"
else
  echo "include_debug_build is %{include_debug_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 12
fi
if [ %{include_fastdebug_build} -eq 0 -o  %{include_fastdebug_build} -eq 1 ] ; then
  echo "include_fastdebug_build is %{include_fastdebug_build}"
else
  echo "include_fastdebug_build is %{include_fastdebug_build}, that is invalid. Use 1 for yes or 0 for no"
  exit 13
fi
if [ %{include_debug_build} -eq 0 -a  %{include_normal_build} -eq 0 -a  %{include_fastdebug_build} -eq 0 ] ; then
  echo "You have disabled all builds (normal,fastdebug,slowdebug). That is a no go."
  exit 14
fi

%if %{with fresh_libjvm} && ! %{build_hotspot_first}
echo "WARNING: The build of a fresh libjvm has been disabled due to a JDK version mismatch"
echo "Build JDK version is %{buildjdkver}, feature JDK version is %{featurever}"
%endif

echo "Update version: %{updatever}"
echo "Build number: %{buildver}"
echo "Milestone: %{milestone}"

%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 7 ] ; then
 echo "priority must be 7 digits in total, violated"
 exit 14
fi
# For old patches
ln -s %{top_level_dir_name} jdk8
ln -s %{top_level_dir_name} openjdk

cp %{SOURCE2} .

# replace outdated configure guess script
#
# the configure macro will do this too, but it also passes a few flags not
# supported by openjdk configure script
cp %{SOURCE100} %{top_level_dir_name}/common/autoconf/build-aux/
cp %{SOURCE101} %{top_level_dir_name}/common/autoconf/build-aux/

# OpenJDK patches
%if %{system_libs}
# Remove libraries that are linked
sh %{SOURCE12}
%endif

# Patch the JDK
# -P N: apply patch number N, same as passing N as a positional argument on rpm >= 4.18
# -p N: strip N leading slashes from paths
# Do not enable them with system_libs, they do not work properly with bundled option
# System library fixes
%if %{system_libs}
%patch -P201
%patch -P 202
%patch -P 203
%patch -P204
%endif

%patch -P1
%patch -P5

# s390 build fixes
%patch -P102
%patch -P103
%patch -P107

# AArch64 fixes

# RISC-V (riscv64) fixes
#%patch -P130

# x86 fixes
pushd %{top_level_dir_name}
%patch -P105 -p1
popd

# Upstreamable fixes
%patch -P512
%patch -P523
%patch -P528
%patch -P571
%patch -P574
%patch -P581
%patch -P541
%patch -P12
pushd %{top_level_dir_name}
%patch -P502 -p1
popd

pushd %{top_level_dir_name}
# Add crypto policy and FIPS support
%patch -P1001 -p1
# nss.cfg PKCS11 support; must come last as it also alters java.security
%patch -P1000 -p1
# system cacerts support
%patch -P539 -p1
popd

# RPM-only fixes
%patch -P600
%patch -P1003

# RHEL-only patches
%if ! 0%{?fedora} && 0%{?rhel} <= 7
%patch -P534
%endif

pushd %{top_level_dir_name}

popd

# Shenandoah patches

# Prepare desktop files
# Portables do not have desktop integration

# Setup nss.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE11} > nss.cfg

# Setup nss.fips.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE17} > nss.fips.cfg

# Setup security policy
#Commented because NA to portable
#sed -i -e "s:^security.systemCACerts=.*:security.systemCACerts=%{cacerts_file}:" %{security_file}

%ifarch riscv64
find %{top_level_dir_name} -name 'config.guess' -exec cp -f /usr/lib/rpm/%{_vendor}/config.guess {} \;
find %{top_level_dir_name} -name 'config.sub' -exec cp -f /usr/lib/rpm/%{_vendor}/config.sub {} \;
%endif

%build

# How many CPU's do we have?
export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
export NUM_PROC=${NUM_PROC:-1}
%if 0%{?_smp_ncpus_max}
# Honor %%_smp_ncpus_max
[ ${NUM_PROC} -gt %{?_smp_ncpus_max} ] && export NUM_PROC=%{?_smp_ncpus_max}
%endif

%ifarch s390x sparc64 alpha %{power64} %{aarch64} riscv64
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

# We use ourcppflags because the OpenJDK build seems to
# pass EXTRA_CFLAGS to the HotSpot C++ compiler...
EXTRA_CFLAGS="%ourcppflags -Wno-error"
EXTRA_CPP_FLAGS="%ourcppflags"

%ifarch %{power64} ppc
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-tree-vectorize"
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
EXTRA_ASFLAGS="${EXTRA_CFLAGS} -Wa,--generate-missing-build-notes=yes"
export EXTRA_CFLAGS EXTRA_ASFLAGS

(cd %{top_level_dir_name}/common/autoconf
 bash ./autogen.sh
)

function buildjdk() {
    local outputdir=${1}
    local buildjdk=${2}
    local maketargets="${3}"
    local debuglevel=${4}
    local link_opt=${5}
    local debug_symbols=${6}

    local top_srcdir_abs_path=$(pwd)/%{top_level_dir_name}
    # Variable used in hs_err hook on build failures
    local top_builddir_abs_path=$(pwd)/${outputdir}

    echo "Using output directory: ${outputdir}";

    if [ "x${link_opt}" = "xbundled" ] ; then
        libc_link_opt="static";
    else
        libc_link_opt="dynamic";
    fi

    echo "Using output directory: ${outputdir}";
    echo "Checking build JDK ${buildjdk} is operational..."
    ${buildjdk}/bin/java -version
    echo "Using make targets: ${maketargets}"
    echo "Using debuglevel: ${debuglevel}"
    echo "Using link_opt: ${link_opt}"
    echo "Using debug_symbols: ${debug_symbols}"
    echo "Building 8u%{updatever}-%{buildver}, milestone %{milestone}"

    mkdir -p ${outputdir}
    pushd ${outputdir}

    bash ${top_srcdir_abs_path}/configure \
%ifarch %{jfr_arches}
    --enable-jfr \
%else
    --disable-jfr \
%endif
%ifarch %{zero_arches}
    --with-jvm-variants=zero \
%endif
    --with-native-debug-symbols=${debug_symbols} \
    --with-milestone=%{milestone} \
    --with-update-version=%{updatever} \
    --with-build-number=%{buildver} \
    --with-vendor-name="%{oj_vendor}" \
    --with-vendor-url="%{oj_vendor_url}" \
    --with-vendor-bug-url="%{oj_vendor_bug_url}" \
    --with-vendor-vm-bug-url="%{oj_vendor_bug_url}" \
    --with-boot-jdk=${buildjdk} \
    --with-debug-level=${debuglevel} \
    --disable-sysconf-nss \
    --enable-unlimited-crypto \
    --with-zlib=${link_opt} \
    --with-giflib=${link_opt} \
%if %{with system_libs}
    --with-libjpeg=${link_opt} \
    --with-libpng=${link_opt} \
    --with-lcms=${link_opt} \
%endif
    --with-stdc++lib=${libc_link_opt} \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-asflags="$EXTRA_ASFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC"

    cat spec.gmk
    cat hotspot-spec.gmk

    make \
      JAVAC_FLAGS=-g \
      LOG=trace \
      SCTP_WERROR= \
      $maketargets || ( pwd; find ${top_srcdir_abs_path} ${top_builddir_abs_path} -name "hs_err_pid*.log" | xargs cat && false )

    popd
}

function installjdk() {
    local outputdir=${1}
    local installdir=${2}
    local jdkimagepath=${installdir}/images/%{jdkimage}
    local jreimagepath=${installdir}/images/%{jreimage}

    echo "Installing build from ${outputdir} to ${installdir}..."
    mkdir -p ${installdir}
    echo "Installing images..."
    mv ${outputdir}/images ${installdir}
    if [ -d ${outputdir}/bundles ] ; then
        echo "Installing bundles...";
        mv ${outputdir}/bundles ${installdir} ;
    fi
    # On 8u, docs ends up at the top-level, not in images
    if [ -d ${outputdir}/docs ] ; then
        echo "Installing docs...";
        mv ${outputdir}/docs ${installdir} ;
    fi

%if !%{with artifacts}
    echo "Removing output directory...";
    rm -rf ${outputdir}
%endif

    for imagepath in ${jdkimagepath} ${jreimagepath} ; do

        if [ -d ${imagepath} ] ; then
            # the build (erroneously) removes read permissions from some jars
            # this is a regression in OpenJDK 7 (our compiler):
            # http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
            find ${imagepath} -iname '*.jar' -exec chmod ugo+r {} \;

            # Build screws up permissions on binaries
            # https://bugs.openjdk.java.net/browse/JDK-8173610
            find ${imagepath} -iname '*.so' -exec chmod +x {} \;
            find ${imagepath}/bin/ -exec chmod +x {} \;

            # Install local files which are distributed with the JDK
            install -m 644 %{SOURCE10} ${imagepath}

            # Create fake alt-java as a placeholder for future alt-java
            pushd ${imagepath}
            # add alt-java man page
            echo "Hardened java binary recommended for launching untrusted code from the Web e.g. javaws" > man/man1/%{alt_java_name}.1
            cat man/man1/java.1 >> man/man1/%{alt_java_name}.1
            popd

            # Print release information
            cat ${imagepath}/release
        fi
    done

    # Handle these outside the loop as install path differs between JDK and JRE image
    install -m 644 nss.cfg ${jdkimagepath}/jre/lib/security/
    install -m 644 nss.cfg ${jreimagepath}/lib/security/
    # Install nss.fips.cfg: NSS configuration for global FIPS mode (crypto-policies)
    install -m 644 nss.fips.cfg ${jdkimagepath}/jre/lib/security/
    install -m 644 nss.fips.cfg ${jreimagepath}/lib/security/
}

tar -cJf  ../%{jdkportablesourcesarchive -- ""} --transform "s|^|%{jdkportablesourcesname -- ""}/|" %{top_level_dir_name} nss*
sha256sum ../%{jdkportablesourcesarchive -- ""} > ../%{jdkportablesourcesarchive -- ""}.sha256sum

function genchecksum() {
    local checkedfile=${1}

    checkdir=$(dirname ${1})
    checkfile=$(basename ${1})

    echo "Generating checksum for ${checkfile} in ${checkdir}..."
    pushd ${checkdir}
    sha256sum ${checkfile} > ${checkfile}.sha256sum
    sha256sum --check ${checkfile}.sha256sum
    popd
}

function packagejdk() {
    local imagesdir=$(pwd)/${1}/images
    local docdir=$(pwd)/${1}/docs
    local bundledir=$(pwd)/${1}/bundles
    local packagesdir=$(pwd)/${2}
    local srcdir=$(pwd)/%{top_level_dir_name}
    local tapsetdir=$(pwd)/tapset

    echo "Packaging build from ${imagesdir} to ${packagesdir}..."
    mkdir -p ${packagesdir}
    pushd ${imagesdir}

    if [ "x$suffix" = "x" ] ; then
        nameSuffix=""
    else
        nameSuffix=`echo "$suffix"| sed s/-/./`
    fi

    jdkname=%{jdkportablename -- "$nameSuffix"}
    jdkarchive=${packagesdir}/%{jdkportablearchive -- "$nameSuffix"}
    jrename=%{jreportablename -- "$nameSuffix"}
    jrearchive=${packagesdir}/%{jreportablearchive -- "$nameSuffix"}
    debugjdkarchive=${packagesdir}/%{jdkportablearchive -- "${nameSuffix}.debuginfo"}
    debugjrearchive=${packagesdir}/%{jreportablearchive -- "${nameSuffix}.debuginfo"}
    unstrippedarchive=${packagesdir}/%{jdkportablearchive -- "${nameSuffix}.unstripped"}
    # We only use docs for the release build
    docname=%{docportablename}
    docarchive=${packagesdir}/%{docportablearchive}
    built_doc_archive=jdk-%{javaver}_%{updatever}%{milestone_version}$suffix-%{buildver}-docs.zip
    # These are from the source tree so no debug variants
    miscname=%{miscportablename}
    miscarchive=${packagesdir}/%{miscportablearchive}

    # Rename directories for packaging
    mv %{jdkimage} ${jdkname}
    mv %{jreimage} ${jrename}

    # Release images have external debug symbols
    if [ "x$suffix" = "x" ] ; then
        # Keep the unstripped version for consumption by RHEL RPMs
        tar -cJf ${unstrippedarchive} ${jdkname}
        genchecksum ${unstrippedarchive}

        # Strip the files
        for file in $(find ${jdkname} ${jrename} -type f) ; do
            if file ${file} | grep -q 'ELF'; then
                noextfile=${file/.so/};
                objcopy --only-keep-debug ${file} ${noextfile}.debuginfo;
                objcopy --add-gnu-debuglink=${noextfile}.debuginfo ${file};
                strip -g ${file};
            fi
        done

        tar -cJf ${debugjdkarchive} $(find ${jdkname} -name \*.debuginfo)
        genchecksum ${debugjdkarchive}
        tar -cJf ${debugjrearchive} $(find ${jrename} -name \*.debuginfo)
        genchecksum ${debugjrearchive}

	mkdir ${docname}
	mv ${docdir} ${docname}
	mv ${bundledir}/${built_doc_archive} ${docname}
	tar -cJf ${docarchive} ${docname}
	genchecksum ${docarchive}

	mkdir ${miscname}
	for s in 16 24 32 48 ; do
	    cp -av ${srcdir}/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png ${miscname}
	done
%if %{with_systemtap}
        cp -a ${tapsetdir}* ${miscname}
%endif
	tar -cJf ${miscarchive} ${miscname}
	genchecksum ${miscarchive}
    fi

    tar -cJf ${jdkarchive} --exclude='**.debuginfo' ${jdkname}
    genchecksum ${jdkarchive}

    tar -cJf ${jrearchive}  --exclude='**.debuginfo' ${jrename}
    genchecksum ${jrearchive}

    # Revert directory renaming so testing will run
    # TODO: testing should run on the packaged JDK
    mv ${jdkname} %{jdkimage}
    mv ${jrename} %{jreimage}

    popd #images

}

%if %{build_hotspot_first}
  # Build a fresh libjvm.so first and use it to bootstrap
  cp -LR --preserve=mode,timestamps %{bootjdk} newboot
  systemjdk=$(pwd)/newboot
  buildjdk build/newboot ${systemjdk} %{hotspot_target} "release" "bundled" "internal"
  mv build/newboot/hotspot/dist/jre/lib/%{archinstall}/server/libjvm.so newboot/jre/lib/%{archinstall}/server
%else
  systemjdk=%{bootjdk}
%endif

for suffix in %{build_loop} ; do
  if [ "x$suffix" = "x" ] ; then
      debugbuild=release
  else
      # change --something to something
      debugbuild=`echo $suffix  | sed "s/-//g"`
  fi
  # We build with internal debug symbols and do
  # our own stripping for one version of the
  # release build
  debug_symbols=internal

  builddir=%{buildoutputdir -- ${suffix}}
  bootbuilddir=boot${builddir}
  installdir=%{installoutputdir -- ${suffix}}
  bootinstalldir=boot${installdir}
  packagesdir=%{packageoutputdir -- ${suffix}}

  link_opt="%{link_type}"
%if %{system_libs}
  # Copy the source tree so we can remove all in-tree libraries
  cp -a %{top_level_dir_name} %{top_level_dir_name_backup}
  # Remove all libraries that are linked
  sh %{SOURCE12} %{top_level_dir_name} full
%endif
  # Debug builds don't need same targets as release for
  # build speed-up. We also avoid bootstrapping these
  # slower builds.
  if echo $debugbuild | grep -q "debug" ; then
      maketargets="%{debug_targets}"
      run_bootstrap=false
  else
      maketargets="%{release_targets}"
      run_bootstrap=%{bootstrap_build}
  fi
  if ${run_bootstrap} ; then
      buildjdk ${bootbuilddir} ${systemjdk} "%{bootstrap_targets}" ${debugbuild} ${link_opt} ${debug_symbols}
      installjdk ${bootbuilddir} ${bootinstalldir}
      buildjdk ${builddir} $(pwd)/${bootinstalldir}/images/%{jdkimage} "${maketargets}" ${debugbuild} ${link_opt} ${debug_symbols}
      installjdk ${builddir} ${installdir}
      %{!?with_artifacts:rm -rf ${bootinstalldir}}
  else
      buildjdk ${builddir} ${systemjdk} "${maketargets}" ${debugbuild} ${link_opt} ${debug_symbols}
      installjdk ${builddir} ${installdir}
  fi
  packagejdk ${installdir} ${packagesdir}

%if %{system_libs}
  # Restore original source tree we modified by removing full in-tree sources
  rm -rf %{top_level_dir_name}
  mv %{top_level_dir_name_backup} %{top_level_dir_name}
%endif

# build cycles
done # end of release / debug cycle loop

%check

# We test debug first as it will give better diagnostics on a crash
for suffix in %{build_loop} ; do

export JAVA_HOME=$(pwd)/%{installoutputdir -- $suffix}/images/%{jdkimage}

# Check Shenandoah is enabled
%if %{use_shenandoah_hotspot}
$JAVA_HOME/bin/java -XX:+UseShenandoahGC -version
%endif

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java TestCryptoLevel

# Check ECC is working
$JAVA_HOME/bin/javac -d . %{SOURCE14}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||")

# Check system crypto (policy) is active and can be disabled
# Test takes a single argument - true or false - to state whether system
# security properties are enabled or not.
$JAVA_HOME/bin/javac -d . %{SOURCE15}
export PROG=$(echo $(basename %{SOURCE15})|sed "s|\.java||")
export SEC_DEBUG="-Djava.security.debug=properties"
# Specific to portable:System security properties to be off by default
$JAVA_HOME/bin/java ${SEC_DEBUG} ${PROG} false
$JAVA_HOME/bin/java ${SEC_DEBUG} -Djava.security.disableSystemPropertiesFile=true ${PROG} false

# Check correct vendor values have been set
$JAVA_HOME/bin/javac -d . %{SOURCE16}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE16})|sed "s|\.java||") "%{oj_vendor}" "%{oj_vendor_url}" "%{oj_vendor_bug_url}"

# Check java launcher has no SSB mitigation
if ! nm $JAVA_HOME/bin/java | grep set_speculation ; then true ; else false; fi

# Check alt-java launcher has SSB mitigation on supported architectures
%ifarch %{ssbd_arches}
nm $JAVA_HOME/bin/%{alt_java_name} | grep set_speculation
%else
if ! nm $JAVA_HOME/bin/%{alt_java_name} | grep set_speculation ; then true ; else false; fi
%endif

# Check translations are available for new timezones
$JAVA_HOME/bin/javac -d . %{SOURCE18}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE18})|sed "s|\.java||") JRE

# Release builds strip the debug symbols into external .debuginfo files
if [ "x$suffix" = "x" ] ; then
  so_suffix="debuginfo"
else
  so_suffix="so"
fi
# Check debug symbols are present and can identify code
find "$JAVA_HOME" -iname "*.$so_suffix" -print0 | while read -d $'\0' lib
do
  if [ -f "$lib" ] ; then
    echo "Testing $lib for debug symbols"
    # All these tests rely on RPM failing the build if the exit code of any set
    # of piped commands is non-zero.

    # Test for .debug_* sections in the shared object. This is the main test
    # Stripped objects will not contain these
    eu-readelf -S "$lib" | grep "] .debug_"
    test $(eu-readelf -S "$lib" | grep -E "\]\ .debug_(info|abbrev)" | wc --lines) == 2

    # Test FILE symbols. These will most likely be removed by anything that
    # manipulates symbol tables because it's generally useless. So a nice test
    # that nothing has messed with symbols
    old_IFS="$IFS"
    IFS=$'\n'
    for line in $(eu-readelf -s "$lib" | grep "00000000      0 FILE    LOCAL  DEFAULT")
    do
     # We expect to see .cpp and .S files, except for architectures like aarch64 and
     # s390 where we expect .o and .oS files
      echo "$line" | grep -E "ABS ((.*/)?[-_a-zA-Z0-9]+\.(c|cc|cpp|cxx|o|S|oS))?$"
    done
    IFS="$old_IFS"

    # If this is the JVM, look for javaCalls.(cpp|o) in FILEs, for extra sanity checking
    if [ "`basename $lib`" = "libjvm.so" ]; then
      eu-readelf -s "$lib" | \
        grep -E "00000000      0 FILE    LOCAL  DEFAULT      ABS javaCalls.(cpp|o)$"
    fi

    # Test that there are no .gnu_debuglink sections pointing to another
    # debuginfo file. There shouldn't be any debuginfo files, so the link makes
    # no sense either
    eu-readelf -S "$lib" | grep 'gnu'
    if eu-readelf -S "$lib" | grep '] .gnu_debuglink' | grep PROGBITS; then
      echo "bad .gnu_debuglink section."
      eu-readelf -x .gnu_debuglink "$lib"
      false
    fi
  fi
done

%ifnarch riscv64
# Make sure gdb can do a backtrace based on line numbers on libjvm.so
# javaCalls.cpp:58 should map to:
# http://hg.openjdk.java.net/jdk8u/jdk8u/hotspot/file/ff3b27e6bcc2/src/share/vm/runtime/javaCalls.cpp#l58
# Using line number 1 might cause build problems. See:
# https://bugzilla.redhat.com/show_bug.cgi?id=1539664
# https://bugzilla.redhat.com/show_bug.cgi?id=1538767
gdb -q "$JAVA_HOME/bin/java" <<EOF | tee gdb.out
handle SIGSEGV pass nostop noprint
handle SIGILL pass nostop noprint
set breakpoint pending on
break javaCalls.cpp:58
commands 1
backtrace
quit
end
run -version
EOF
%ifarch %{gdb_arches}
grep 'JavaCallWrapper::JavaCallWrapper' gdb.out
%endif
%endif

# Check src.zip has all sources. See RHBZ#1130490
$JAVA_HOME/bin/jar -tf $JAVA_HOME/src.zip | grep 'sun.misc.Unsafe'

# Check class files include useful debugging information
$JAVA_HOME/bin/javap -l java.lang.Object | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.lang.Object | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.lang.Object | grep LocalVariableTable

# Check generated class files include useful debugging information
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LocalVariableTable

# build cycles check
done

%install

 mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
 mv ../%{jdkportablesourcesarchive -- ""} $RPM_BUILD_ROOT%{_jvmdir}/ 
 mv ../%{jdkportablesourcesarchive -- ""}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/


for suffix in %{build_loop} ; do

    packagesdir=%{packageoutputdir -- ${suffix}}

    if [ "x$suffix" == "x" ] ; then
        nameSuffix=""
    else
        nameSuffix=`echo "$suffix"| sed s/-/./`
    fi

    # These definitions should match those in installjdk
    jdkarchive=${packagesdir}/%{jdkportablearchive -- "$nameSuffix"}
    jrearchive=${packagesdir}/%{jreportablearchive -- "$nameSuffix"}
    debugjdkarchive=${packagesdir}/%{jdkportablearchive -- "${nameSuffix}.debuginfo"}
    debugjrearchive=${packagesdir}/%{jreportablearchive -- "${nameSuffix}.debuginfo"}
    unstrippedarchive=${packagesdir}/%{jdkportablearchive -- "${nameSuffix}.unstripped"}

    mv ${jdkarchive} $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jdkarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jrearchive} $RPM_BUILD_ROOT%{_jvmdir}/
    mv ${jrearchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/

    if [ "x$suffix" = "x" ] ; then
        mv ${debugjdkarchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${debugjdkarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${debugjrearchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${debugjrearchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${unstrippedarchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${unstrippedarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
    fi
done

    if [ "x$suffix" = "x" ] ; then
        # These definitions should match those in installjdk
        # Install outside the loop as there are no debug variants
        docarchive=${packagesdir}/%{docportablearchive}
        miscarchive=${packagesdir}/%{miscportablearchive}
        mv ${docarchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${docarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${miscarchive} $RPM_BUILD_ROOT%{_jvmdir}/
        mv ${miscarchive}.sha256sum $RPM_BUILD_ROOT%{_jvmdir}/
   fi

# To show sha in the build log
for file in `ls $RPM_BUILD_ROOT%{_jvmdir}/*.sha256sum` ; do
    ls -l $file ;
    cat $file ;
done

%if %{include_normal_build}
%files
# main package builds always
%{_jvmdir}/%{jreportablearchiveForFiles}
%{_jvmdir}/%{jreportablearchive -- .debuginfo}
%{_jvmdir}/%{jreportablearchiveForFiles}.sha256sum
%{_jvmdir}/%{jreportablearchive -- .debuginfo}.sha256sum
%else
%files
# placeholder
%endif

%if %{include_normal_build}
%files devel
%{_jvmdir}/%{jdkportablearchiveForFiles}
%{_jvmdir}/%{jdkportablearchive -- .debuginfo}
%{_jvmdir}/%{jdkportablearchiveForFiles}.sha256sum
%{_jvmdir}/%{jdkportablearchive -- .debuginfo}.sha256sum
%endif

%files unstripped
%{_jvmdir}/%{jdkportablearchive -- .unstripped}
%{_jvmdir}/%{jdkportablearchive -- .unstripped}.sha256sum

%if %{include_debug_build}
%files slowdebug
%{_jvmdir}/%{jreportablearchive -- .slowdebug}
%{_jvmdir}/%{jreportablearchive -- .slowdebug}.sha256sum

%files devel-slowdebug
%{_jvmdir}/%{jdkportablearchive -- .slowdebug}
%{_jvmdir}/%{jdkportablearchive -- .slowdebug}.sha256sum
%endif
%if %{include_fastdebug_build}
%files fastdebug
%{_jvmdir}/%{jreportablearchive -- .fastdebug}
%{_jvmdir}/%{jreportablearchive -- .fastdebug}.sha256sum

%files devel-fastdebug
%{_jvmdir}/%{jdkportablearchive -- .fastdebug}
%{_jvmdir}/%{jdkportablearchive -- .fastdebug}.sha256sum
%endif

%files sources
%{_jvmdir}/%{jdkportablesourcesarchiveForFiles}
%{_jvmdir}/%{jdkportablesourcesarchiveForFiles}.sha256sum

%if %{include_normal_build}
%files docs
%{_jvmdir}/%{docportablearchive}
%{_jvmdir}/%{docportablearchive}.sha256sum

%files misc
%{_jvmdir}/%{miscportablearchive}
%{_jvmdir}/%{miscportablearchive}.sha256sum
%endif

%changelog
%autochangelog
