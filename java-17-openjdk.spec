# RPM conditionals so as to be able to dynamically produce
# slowdebug/release builds. See:
# http://rpm.org/user_doc/conditional_builds.html
#
# Examples:
#
# Produce release, fastdebug *and* slowdebug builds on x86_64 (default):
# $ rpmbuild -ba java-17-openjdk.spec
#
# Produce only release builds (no debug builds) on x86_64:
# $ rpmbuild -ba java-17-openjdk.spec --without slowdebug --without fastdebug
#
# Only produce a release build on x86_64:
# $ fedpkg mockbuild --without slowdebug --without fastdebug

# Enable fastdebug builds by default on relevant arches.
%bcond_without fastdebug
# Enable slowdebug builds by default on relevant arches.
%bcond_without slowdebug
# Enable release builds by default on relevant arches.
%bcond_without release
# Enable static library builds by default.
%bcond_without staticlibs
# Build a fresh libjvm.so for use in a copy of the bootstrap JDK
%bcond_without fresh_libjvm
# Build with system libraries
%bcond_with system_libs

# Workaround for stripping of debug symbols from static libraries
%if %{with staticlibs}
%define __brp_strip_static_archive %{nil}
%global include_staticlibs 1
%else
%global include_staticlibs 0
%endif

# Define whether to use the bootstrap JDK directly or with a fresh libjvm.so
%if %{with fresh_libjvm}
%global build_hotspot_first 1
%else
%global build_hotspot_first 0
%endif

%if %{with system_libs}
%global system_libs 1
%global link_type system
%global freetype_lib %{nil}
%else
%global system_libs 0
%global link_type bundled
%global freetype_lib |libfreetype[.]so.*
%endif

# The -g flag says to use strip -g instead of full strip on DSOs or EXEs.
# This fixes detailed NMT and other tools which need minimal debug info.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1520879
%global _find_debuginfo_opts -g

# With LTO flags enabled, debuginfo checks fail for some reason. Disable
# LTO for a passing build. This really needs to be looked at.
%define _lto_cflags %{nil}

# note: parametrized macros are order-sensitive (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter to other macros. If not macro, then it is considered a switch
# see the difference between global and define:
# See https://github.com/rpm-software-management/rpm/issues/127 to comments at  "pmatilai commented on Aug 18, 2017"
# (initiated in https://bugzilla.redhat.com/show_bug.cgi?id=1482192)
%global debug_suffix_unquoted -slowdebug
%global fastdebug_suffix_unquoted -fastdebug
%global main_suffix_unquoted -main
%global staticlibs_suffix_unquoted -staticlibs
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global fastdebug_suffix "%{fastdebug_suffix_unquoted}"
%global normal_suffix ""
%global main_suffix "%{main_suffix_unquoted}"
%global staticlibs_suffix "%{staticlibs_suffix_unquoted}"

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

# We have hardcoded list of files, which  is appearing in alternatives, and in files
# in alternatives those are slaves and master, very often triplicated by man pages
# in files all masters and slaves are ghosted
# the ghosts are here to allow installation via query like `dnf install /usr/bin/java`
# you can list those files, with appropriate sections: cat *.spec | grep -e --install -e --slave -e post_ -e alternatives
# TODO - fix those hardcoded lists via single list
# Those files must *NOT* be ghosted for *slowdebug* packages
# FIXME - if you are moving jshell or jlink or similar, always modify all three sections
# you can check via headless and devels:
#    rpm -ql --noghost java-11-openjdk-headless-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# == rpm -ql           java-11-openjdk-headless-slowdebug-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# != rpm -ql           java-11-openjdk-headless-11.0.1.13-8.fc29.x86_64.rpm  | grep bin
# similarly for other %%{_jvmdir}/{jre,java} and %%{_javadocdir}/{java,java-zip}
%define is_release_build() %( if [ "%{?1}" == "%{debug_suffix_unquoted}" -o "%{?1}" == "%{fastdebug_suffix_unquoted}" ]; then echo "0" ; else echo "1"; fi )

# while JDK is a techpreview(is_system_jdk=0), some provides are turned off. Once jdk stops to be an techpreview, move it to 1
# as sytem JDK, we mean any JDK which can run whole system java stack without issues (like bytecode issues, module issues, dependencies...)
%global is_system_jdk 1

%global aarch64         aarch64 arm64 armv8
# we need to distinguish between big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
# Set of architectures which support multiple ABIs
%global multilib_arches %{power64} sparc64 x86_64
# Set of architectures for which we build slowdebug builds
%global debug_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} s390x
# Set of architectures for which we build fastdebug builds
%global fastdebug_arches x86_64 ppc64le aarch64
# Set of architectures with a Just-In-Time (JIT) compiler
%global jit_arches      %{arm} %{aarch64} %{ix86} %{power64} s390x sparcv9 sparc64 x86_64
# Set of architectures which use the Zero assembler port (!jit_arches)
%global zero_arches ppc s390
# Set of architectures which run a full bootstrap cycle
%global bootstrap_arches %{jit_arches}
# Set of architectures which support SystemTap tapsets
%global systemtap_arches %{jit_arches}
# Set of architectures with a Ahead-Of-Time (AOT) compiler
%global aot_arches      x86_64 %{aarch64}
# Set of architectures which support the serviceability agent
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm}
# Set of architectures which support class data sharing
# See https://bugzilla.redhat.com/show_bug.cgi?id=513605
# MetaspaceShared::generate_vtable_methods is not implemented for the PPC JIT
%global share_arches    %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{arm} s390x
# Set of architectures for which we build the Shenandoah garbage collector
%global shenandoah_arches x86_64 %{aarch64}
# Set of architectures for which we build the Z garbage collector
%global zgc_arches x86_64
# Set of architectures for which alt-java has SSB mitigation
%global ssbd_arches x86_64
# Set of architectures for which java has short vector math library (libsvml.so)
%global svml_arches x86_64
# Set of architectures where we verify backtraces with gdb
%global gdb_arches %{jit_arches} %{zero_arches}

# By default, we build a debug build during main build on JIT architectures
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

%if %{include_staticlibs}
%global staticlibs_loop %{staticlibs_suffix}
%else
%global staticlibs_loop %{nil}
%endif

%if 0%{?flatpak}
%global bootstrap_build false
%else
%ifarch %{bootstrap_arches}
%global bootstrap_build true
%else
%global bootstrap_build false
%endif
%endif

%if %{include_staticlibs}
# Extra target for producing the static-libraries. Separate from
# other targets since this target is configured to use in-tree
# AWT dependencies: lcms, libjpeg, libpng, libharfbuzz, giflib
# and possibly others
%global static_libs_target static-libs-image
%else
%global static_libs_target %{nil}
%endif

# RPM JDK builds keep the debug symbols internal, to be later stripped by RPM
%global debug_symbols internal

# unlike portables,the rpms have to use static_libs_target very dynamically
%global bootstrap_targets images
%global release_targets images docs-zip
# No docs nor bootcycle for debug builds
%global debug_targets images
# Target to use to just build HotSpot
%global hotspot_target hotspot

# JDK to use for bootstrapping
%global bootjdk /usr/lib/jvm/java-%{buildjdkver}-openjdk


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
%global archinstall i686
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
# Need to support noarch for srpm build
%ifarch noarch
%global archinstall %{nil}
%global stapinstall %{nil}
%endif

%ifarch %{systemtap_arches}
%global with_systemtap 1
%else
%global with_systemtap 0
%endif

# New Version-String scheme-style defines
%global featurever 17
%global interimver 0
%global updatever 5
%global patchver 0
# buildjdkver is usually same as %%{featurever},
# but in time of bootstrap of next jdk, it is featurever-1,
# and this it is better to change it here, on single place
%global buildjdkver %{featurever}
# We don't add any LTS designator for STS packages (Fedora and EPEL).
# We need to explicitly exclude EPEL as it would have the %%{rhel} macro defined.
%if 0%{?rhel} && !0%{?epel}
  %global lts_designator "LTS"
  %global lts_designator_zip -%{lts_designator}
%else
 %global lts_designator ""
 %global lts_designator_zip ""
%endif

# Define vendor information used by OpenJDK
%global oj_vendor Red Hat, Inc.
%global oj_vendor_url https://www.redhat.com/
# Define what url should JVM offer in case of a crash report
# order may be important, epel may have rhel declared
%if 0%{?epel}
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL&component=%{name}&version=epel%{epel}
%else
%if 0%{?fedora}
# Does not work for rawhide, keeps the version field empty
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&component=%{name}&version=%{fedora}
%else
%if 0%{?rhel}
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi?product=Red%20Hat%20Enterprise%20Linux%20%{rhel}&component=%{name}
%else
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi
%endif
%endif
%endif
%global oj_vendor_version (Red_Hat-%{version}-%{release})

# Define IcedTea version used for SystemTap tapsets and desktop file
%global icedteaver      6.0.0pre00-c848b93a8598
# Define current Git revision for the FIPS support patches
%global fipsver 0bd5ca9ccc5

# Standard JPackage naming and versioning defines
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{origin}
%global top_level_dir_name_backup %{top_level_dir_name}-backup
%global buildver        7
%global rpmrelease      1
# Priority must be 8 digits in total; up to openjdk 1.8, we were using 18..... so when we moved to 11, we had to add another digit
%if %is_system_jdk
# Using 10 digits may overflow the int used for priority, so we combine the patch and build versions
# It is very unlikely we will ever have a patch version > 4 or a build version > 20, so we combine as (patch * 20) + build.
# This means 11.0.9.0+11 would have had a priority of 11000911 as before
# A 11.0.9.1+1 would have had a priority of 11000921 (20 * 1 + 1), thus ensuring it is bigger than 11.0.9.0+11
%global combiver $( expr 20 '*' %{patchver} + %{buildver} )
%global priority %( printf '%02d%02d%02d%02d' %{featurever} %{interimver} %{updatever} %{combiver} )
%else
# for techpreview, using 1, so slowdebugs can have 0
%global priority %( printf '%08d' 1 )
%endif
%global newjavaver %{featurever}.%{interimver}.%{updatever}.%{patchver}
%global javaver         %{featurever}

# Strip up to 6 trailing zeros in newjavaver, as the JDK does, to get the correct version used in filenames
%global filever %(svn=%{newjavaver}; for i in 1 2 3 4 5 6 ; do svn=${svn%%.0} ; done; echo ${svn})

# The tag used to create the OpenJDK tarball
%global vcstag jdk-%{filever}+%{buildver}%{?tagsuffix:-%{tagsuffix}}

# Define milestone (EA for pre-releases, GA for releases)
# Release will be (where N is usually a number starting at 1):
# - 0.N%%{?extraver}%%{?dist} for EA releases,
# - N%%{?extraver}{?dist} for GA releases
%global is_ga           0
%if %{is_ga}
%global build_type GA
%global ea_designator ""
%global ea_designator_zip ""
%global extraver %{nil}
%global eaprefix %{nil}
%else
%global build_type EA
%global ea_designator ea
%global ea_designator_zip -%{ea_designator}
%global extraver .%{ea_designator}
%global eaprefix 0.
%endif

# parametrized macros are order-sensitive
%global compatiblename  java-%{featurever}-%{origin}
%global fullversion     %{compatiblename}-%{version}-%{release}
# images directories from upstream build
%global jdkimage                jdk
%global static_libs_image       static-libs
# installation directory for static libraries
%global static_libs_root        lib/static
%global static_libs_arch_dir    %{static_libs_root}/linux-%{archinstall}
%global static_libs_install_dir %{static_libs_arch_dir}/glibc
# output dir stub
%define buildoutputdir() %{expand:build/jdk%{featurever}.build%{?1}}
# we can copy the javadoc to not arched dir, or make it not noarch
%define uniquejavadocdir()    %{expand:%{fullversion}.%{_arch}%{?1}}
# main id and dir of this jdk
%define uniquesuffix()        %{expand:%{fullversion}.%{_arch}%{?1}}

#################################################################
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349
#         https://bugzilla.redhat.com/show_bug.cgi?id=1590796#c14
#         https://bugzilla.redhat.com/show_bug.cgi?id=1655938
%global _privatelibs libsplashscreen[.]so.*|libawt_xawt[.]so.*|libjli[.]so.*|libattach[.]so.*|libawt[.]so.*|libextnet[.]so.*|libawt_headless[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjimage[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmanagement_agent[.]so.*|libmanagement_ext[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libprefs[.]so.*|librmi[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsystemconf[.]so.*|libzip[.]so.*%{freetype_lib}
%global _publiclibs libjawt[.]so.*|libjava[.]so.*|libjvm[.]so.*|libverify[.]so.*|libjsig[.]so.*
%if %is_system_jdk
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
# Never generate lib-style provides/requires for any debug packages
%global __provides_exclude_from ^.*/%{uniquesuffix -- %{debug_suffix_unquoted}}/.*$
%global __requires_exclude_from ^.*/%{uniquesuffix -- %{debug_suffix_unquoted}}/.*$
%global __provides_exclude_from ^.*/%{uniquesuffix -- %{fastdebug_suffix_unquoted}}/.*$
%global __requires_exclude_from ^.*/%{uniquesuffix -- %{fastdebug_suffix_unquoted}}/.*$
%else
# Don't generate provides/requires for JDK provided shared libraries at all.
%global __provides_exclude ^(%{_privatelibs}|%{_publiclibs})$
%global __requires_exclude ^(%{_privatelibs}|%{_publiclibs})$
%endif


%global etcjavasubdir     %{_sysconfdir}/java/java-%{javaver}-%{origin}
%define etcjavadir()      %{expand:%{etcjavasubdir}/%{uniquesuffix -- %{?1}}}
# Standard JPackage directories and symbolic links.
%define sdkdir()        %{expand:%{uniquesuffix -- %{?1}}}
%define jrelnk()        %{expand:jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}%{?1}}

%define sdkbindir()     %{expand:%{_jvmdir}/%{sdkdir -- %{?1}}/bin}
%define jrebindir()     %{expand:%{_jvmdir}/%{sdkdir -- %{?1}}/bin}

%global alt_java_name     alt-java

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/

# For flatpack builds hard-code /usr/sbin/alternatives,
# otherwise use %%{_sbindir} relative path.
%if 0%{?flatpak}
%global alternatives_requires /usr/sbin/alternatives
%else
%global alternatives_requires %{_sbindir}/alternatives
%endif

%global family %{name}.%{_arch}
%global family_noarch  %{name}

%if %{with_systemtap}
# Where to install systemtap tapset (links)
# We would like these to be in a package specific sub-dir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinguish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka target_cpu as architecture specific directory name.
%global tapsetroot /usr/share/systemtap
%global tapsetdirttapset %{tapsetroot}/tapset/
%global tapsetdir %{tapsetdirttapset}/%{stapinstall}
%endif

# x86 is no longer supported
%if 0%{?java_arches:1}
ExclusiveArch:  %{java_arches}
%else
ExcludeArch: %{ix86}
%endif

# not-duplicated scriptlets for normal/debug packages
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%define save_alternatives() %{expand:
  # warning! alternatives are localised!
  # LANG=cs_CZ.UTF-8  alternatives --display java | head
  # LANG=en_US.UTF-8  alternatives --display java | head
  function nonLocalisedAlternativesDisplayOfMaster() {
    LANG=en_US.UTF-8 alternatives --display "$MASTER"
  }
  function headOfAbove() {
    nonLocalisedAlternativesDisplayOfMaster | head -n $1
  }
  MASTER="%{?1}"
  LOCAL_LINK="%{?2}"
  FAMILY="%{?3}"
  rm -f %{_localstatedir}/lib/rpm-state/"$MASTER"_$FAMILY > /dev/null
  if nonLocalisedAlternativesDisplayOfMaster > /dev/null ; then
      if headOfAbove 1 | grep -q manual ; then
        if headOfAbove 2 | tail -n 1 | grep -q %{compatiblename} ; then
           headOfAbove 2  > %{_localstatedir}/lib/rpm-state/"$MASTER"_"$FAMILY"
        fi
      fi
  fi
}

%define save_and_remove_alternatives() %{expand:
  if [ "x$debug"  == "xtrue" ] ; then
    set -x
  fi
  upgrade1_uninstal0=%{?3}
  if [ "0$upgrade1_uninstal0" -gt 0 ] ; then # removal of this condition will cause persistence between uninstall
    %{save_alternatives %{?1} %{?2} %{?4}}
  fi
  alternatives --remove  "%{?1}" "%{?2}"
}

%define set_if_needed_alternatives() %{expand:
  MASTER="%{?1}"
  FAMILY="%{?2}"
  ALTERNATIVES_FILE="%{_localstatedir}/lib/rpm-state/$MASTER"_"$FAMILY"
  if [ -e  "$ALTERNATIVES_FILE" ] ; then
    rm "$ALTERNATIVES_FILE"
    alternatives --set $MASTER $FAMILY
  fi
}


%define post_script() %{expand:
update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
exit 0
}

%define alternatives_java_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
PRIORITY=%{priority}
if [ "%{?1}" == %{debug_suffix} ]; then
  let PRIORITY=PRIORITY-1
fi

ext=.gz
key=java
alternatives \\
  --install %{_bindir}/java $key %{jrebindir -- %{?1}}/java $PRIORITY  --family %{family} \\
  --slave %{_jvmdir}/jre jre %{_jvmdir}/%{sdkdir -- %{?1}} \\
  --slave %{_bindir}/%{alt_java_name} %{alt_java_name} %{jrebindir -- %{?1}}/%{alt_java_name} \\
  --slave %{_bindir}/keytool keytool %{jrebindir -- %{?1}}/keytool \\
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir -- %{?1}}/rmiregistry \\
  --slave %{_mandir}/man1/java.1$ext java.1$ext \\
  %{_mandir}/man1/java-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/%{alt_java_name}.1$ext %{alt_java_name}.1$ext \\
  %{_mandir}/man1/%{alt_java_name}-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/keytool.1$ext keytool.1$ext \\
  %{_mandir}/man1/keytool-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/rmiregistry.1$ext rmiregistry.1$ext \\
  %{_mandir}/man1/rmiregistry-%{uniquesuffix -- %{?1}}.1$ext

%{set_if_needed_alternatives $key %{family}}

for X in %{origin} %{javaver} ; do
  key=jre_"$X"
  alternatives --install %{_jvmdir}/jre-"$X" $key %{_jvmdir}/%{sdkdir -- %{?1}} $PRIORITY --family %{family}
  %{set_if_needed_alternatives $key %{family}}
done

key=jre_%{javaver}_%{origin}
alternatives --install %{_jvmdir}/jre-%{javaver}-%{origin} $key %{_jvmdir}/%{jrelnk -- %{?1}} $PRIORITY  --family %{family}
%{set_if_needed_alternatives $key %{family}}
}

%define post_headless() %{expand:
%ifarch %{share_arches}
%{jrebindir -- %{?1}}/java -Xshare:dump >/dev/null 2>/dev/null
%endif

update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

# see pretrans where this file is declared
# also see that pretrans is only for non-debug
if [ ! "%{?1}" == %{debug_suffix} ]; then
  if [ -f %{_libexecdir}/copy_jdk_configs_fixFiles.sh ] ; then
    sh  %{_libexecdir}/copy_jdk_configs_fixFiles.sh %{rpm_state_dir}/%{name}.%{_arch}  %{_jvmdir}/%{sdkdir -- %{?1}}
  fi
fi

exit 0
}

%define postun_script() %{expand:
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{update_desktop_icons}
fi
exit 0
}


%define postun_headless() %{expand:
  if [ "x$debug"  == "xtrue" ] ; then
    set -x
  fi
  post_state=$1 # from postun, https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_syntax
  %{save_and_remove_alternatives  java  %{jrebindir -- %{?1}}/java $post_state %{family}}
  %{save_and_remove_alternatives  jre_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}} $post_state %{family}}
  %{save_and_remove_alternatives  jre_%{javaver} %{_jvmdir}/%{sdkdir -- %{?1}} $post_state %{family}}
  %{save_and_remove_alternatives  jre_%{javaver}_%{origin} %{_jvmdir}/%{jrelnk -- %{?1}} $post_state %{family}}
}

%define posttrans_script() %{expand:
%{update_desktop_icons}
}


%define alternatives_javac_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
PRIORITY=%{priority}
if [ "%{?1}" == %{debug_suffix} ]; then
  let PRIORITY=PRIORITY-1
fi

ext=.gz
key=javac
alternatives \\
  --install %{_bindir}/javac $key %{sdkbindir -- %{?1}}/javac $PRIORITY  --family %{family} \\
  --slave %{_jvmdir}/java java_sdk %{_jvmdir}/%{sdkdir -- %{?1}} \\
  --slave %{_bindir}/jlink jlink %{sdkbindir -- %{?1}}/jlink \\
  --slave %{_bindir}/jmod jmod %{sdkbindir -- %{?1}}/jmod \\
%ifarch %{sa_arches}
%ifnarch %{zero_arches}
  --slave %{_bindir}/jhsdb jhsdb %{sdkbindir -- %{?1}}/jhsdb \\
%endif
%endif
  --slave %{_bindir}/jar jar %{sdkbindir -- %{?1}}/jar \\
  --slave %{_bindir}/jarsigner jarsigner %{sdkbindir -- %{?1}}/jarsigner \\
  --slave %{_bindir}/javadoc javadoc %{sdkbindir -- %{?1}}/javadoc \\
  --slave %{_bindir}/javap javap %{sdkbindir -- %{?1}}/javap \\
  --slave %{_bindir}/jcmd jcmd %{sdkbindir -- %{?1}}/jcmd \\
  --slave %{_bindir}/jconsole jconsole %{sdkbindir -- %{?1}}/jconsole \\
  --slave %{_bindir}/jdb jdb %{sdkbindir -- %{?1}}/jdb \\
  --slave %{_bindir}/jdeps jdeps %{sdkbindir -- %{?1}}/jdeps \\
  --slave %{_bindir}/jdeprscan jdeprscan %{sdkbindir -- %{?1}}/jdeprscan \\
  --slave %{_bindir}/jfr jfr %{sdkbindir -- %{?1}}/jfr \\
  --slave %{_bindir}/jimage jimage %{sdkbindir -- %{?1}}/jimage \\
  --slave %{_bindir}/jinfo jinfo %{sdkbindir -- %{?1}}/jinfo \\
  --slave %{_bindir}/jmap jmap %{sdkbindir -- %{?1}}/jmap \\
  --slave %{_bindir}/jps jps %{sdkbindir -- %{?1}}/jps \\
  --slave %{_bindir}/jpackage jpackage %{sdkbindir -- %{?1}}/jpackage \\
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir -- %{?1}}/jrunscript \\
  --slave %{_bindir}/jshell jshell %{sdkbindir -- %{?1}}/jshell \\
  --slave %{_bindir}/jstack jstack %{sdkbindir -- %{?1}}/jstack \\
  --slave %{_bindir}/jstat jstat %{sdkbindir -- %{?1}}/jstat \\
  --slave %{_bindir}/jstatd jstatd %{sdkbindir -- %{?1}}/jstatd \\
  --slave %{_bindir}/serialver serialver %{sdkbindir -- %{?1}}/serialver \\
  --slave %{_mandir}/man1/jar.1$ext jar.1$ext \\
  %{_mandir}/man1/jar-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jarsigner.1$ext jarsigner.1$ext \\
  %{_mandir}/man1/jarsigner-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/javac.1$ext javac.1$ext \\
  %{_mandir}/man1/javac-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/javadoc.1$ext javadoc.1$ext \\
  %{_mandir}/man1/javadoc-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/javap.1$ext javap.1$ext \\
  %{_mandir}/man1/javap-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jcmd.1$ext jcmd.1$ext \\
  %{_mandir}/man1/jcmd-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jconsole.1$ext jconsole.1$ext \\
  %{_mandir}/man1/jconsole-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jdb.1$ext jdb.1$ext \\
  %{_mandir}/man1/jdb-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jdeps.1$ext jdeps.1$ext \\
  %{_mandir}/man1/jdeps-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jinfo.1$ext jinfo.1$ext \\
  %{_mandir}/man1/jinfo-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jmap.1$ext jmap.1$ext \\
  %{_mandir}/man1/jmap-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jps.1$ext jps.1$ext \\
  %{_mandir}/man1/jps-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jpackage.1$ext jpackage.1$ext \\
  %{_mandir}/man1/jpackage-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \\
  %{_mandir}/man1/jrunscript-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \\
  %{_mandir}/man1/jstack-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \\
  %{_mandir}/man1/jstat-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstatd.1$ext jstatd.1$ext \\
  %{_mandir}/man1/jstatd-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/serialver.1$ext serialver.1$ext \\
  %{_mandir}/man1/serialver-%{uniquesuffix -- %{?1}}.1$ext

%{set_if_needed_alternatives  $key %{family}}

for X in %{origin} %{javaver} ; do
  key=java_sdk_"$X"
  alternatives --install %{_jvmdir}/java-"$X" $key %{_jvmdir}/%{sdkdir -- %{?1}} $PRIORITY  --family %{family}
  %{set_if_needed_alternatives  $key %{family}}
done

key=java_sdk_%{javaver}_%{origin}
alternatives --install %{_jvmdir}/java-%{javaver}-%{origin} $key %{_jvmdir}/%{sdkdir -- %{?1}} $PRIORITY  --family %{family}
%{set_if_needed_alternatives  $key %{family}}
}

%define post_devel() %{expand:
update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

exit 0
}

%define postun_devel() %{expand:
  if [ "x$debug"  == "xtrue" ] ; then
    set -x
  fi
  post_state=$1 # from postun, https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_syntax
  %{save_and_remove_alternatives  javac %{sdkbindir -- %{?1}}/javac $post_state %{family}}
  %{save_and_remove_alternatives  java_sdk_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}} $post_state %{family}}
  %{save_and_remove_alternatives  java_sdk_%{javaver} %{_jvmdir}/%{sdkdir -- %{?1}} $post_state %{family}}
  %{save_and_remove_alternatives  java_sdk_%{javaver}_%{origin} %{_jvmdir}/%{sdkdir -- %{?1}} $post_state %{family}}

update-desktop-database %{_datadir}/applications &> /dev/null || :

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{update_desktop_icons}
fi
exit 0
}

%define posttrans_devel() %{expand:
%{alternatives_javac_install --  %{?1}}
%{update_desktop_icons}
}

%define alternatives_javadoc_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
PRIORITY=%{priority}
if [ "%{?1}" == %{debug_suffix} ]; then
  let PRIORITY=PRIORITY-1
fi
  for X in %{origin} %{javaver} ; do
    key=javadocdir_"$X"
    alternatives --install %{_javadocdir}/java-"$X" $key %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api $PRIORITY --family %{family_noarch}
    %{set_if_needed_alternatives $key %{family_noarch}}
  done

  key=javadocdir_%{javaver}_%{origin}
  alternatives --install %{_javadocdir}/java-%{javaver}-%{origin} $key %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api $PRIORITY --family %{family_noarch}
  %{set_if_needed_alternatives  $key %{family_noarch}}

  key=javadocdir
  alternatives --install %{_javadocdir}/java $key %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api $PRIORITY --family %{family_noarch}
  %{set_if_needed_alternatives  $key %{family_noarch}}
exit 0
}

%define postun_javadoc() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
  post_state=$1 # from postun, https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_syntax
  %{save_and_remove_alternatives  javadocdir  %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api $post_state %{family_noarch}}
  %{save_and_remove_alternatives  javadocdir_%{origin} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api $post_state %{family_noarch}}
  %{save_and_remove_alternatives  javadocdir_%{javaver} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api $post_state %{family_noarch}}
  %{save_and_remove_alternatives  javadocdir_%{javaver}_%{origin} %{_javadocdir}/%{uniquejavadocdir -- %{?1}}/api $post_state %{family_noarch}}
exit 0
}

%define alternatives_javadoczip_install() %{expand:
if [ "x$debug"  == "xtrue" ] ; then
  set -x
fi
PRIORITY=%{priority}
if [ "%{?1}" == %{debug_suffix} ]; then
  let PRIORITY=PRIORITY-1
fi
  for X in %{origin} %{javaver} ; do
    key=javadoczip_"$X"
    alternatives --install %{_javadocdir}/java-"$X".zip $key %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip $PRIORITY --family %{family_noarch}
    %{set_if_needed_alternatives $key %{family_noarch}}
  done

  key=javadoczip_%{javaver}_%{origin}
  alternatives --install %{_javadocdir}/java-%{javaver}-%{origin}.zip $key %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip $PRIORITY --family %{family_noarch}
  %{set_if_needed_alternatives  $key %{family_noarch}}

  # Weird legacy filename for backwards-compatibility
  key=javadoczip
  alternatives --install %{_javadocdir}/java-zip $key %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip $PRIORITY  --family %{family_noarch}
  %{set_if_needed_alternatives  $key %{family_noarch}}
exit 0
}

%define postun_javadoc_zip() %{expand:
  if [ "x$debug"  == "xtrue" ] ; then
    set -x
  fi
  post_state=$1 # from postun, https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_syntax
  %{save_and_remove_alternatives  javadoczip  %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip $post_state %{family_noarch}}
  %{save_and_remove_alternatives  javadoczip_%{origin}  %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip $post_state %{family_noarch}}
  %{save_and_remove_alternatives  javadoczip_%{javaver}  %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip $post_state %{family_noarch}}
  %{save_and_remove_alternatives  javadoczip_%{javaver}_%{origin}  %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip $post_state %{family_noarch}}
exit 0
}

%define files_jre() %{expand:
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-%{origin}.png
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsplashscreen.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt_xawt.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjawt.so
}


%define files_jre_headless() %{expand:
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%doc %{_defaultdocdir}/%{uniquejavadocdir -- %{?1}}/NEWS
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%dir %{_jvmdir}/%{sdkdir -- %{?1}}
%{_jvmdir}/%{sdkdir -- %{?1}}/release
%{_jvmdir}/%{jrelnk -- %{?1}}
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/bin
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/java
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/%{alt_java_name}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/keytool
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/rmiregistry
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib
%ifarch %{jit_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/classlist
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jexec
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jspawnhelper
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jrt-fs.jar
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/modules
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/psfont.properties.ja
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/psfontj2d.properties
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/tzdb.dat
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/tzdb.dat.upstream
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjli.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jvm.cfg
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libattach.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libextnet.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjsig.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt_headless.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libdt_socket.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libfontmanager.so
%if ! %{system_libs}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libfreetype.so
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libinstrument.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libj2gss.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libj2pcsc.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libj2pkcs11.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjaas.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjava.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjavajpeg.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjdwp.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjimage.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjsound.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/liblcms.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmanagement.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmanagement_agent.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmanagement_ext.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libmlib_image.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libnet.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libnio.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libprefs.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/librmi.so
# Some architectures don't have the serviceability agent
%ifarch %{sa_arches}
%ifnarch %{zero_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsaproc.so
%endif
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsctp.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsystemconf.so
%ifarch %{svml_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjsvml.so
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsyslookup.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libverify.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libzip.so
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr/default.jfc
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr/profile.jfc
%{_mandir}/man1/java-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/%{alt_java_name}-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/keytool-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/rmiregistry-%{uniquesuffix -- %{?1}}.1*
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/server/
%ifarch %{share_arches}
%attr(444, root, root) %ghost %{_jvmdir}/%{sdkdir -- %{?1}}/lib/server/classes.jsa
%endif
%dir %{etcjavasubdir}
%dir %{etcjavadir -- %{?1}}
%dir %{etcjavadir -- %{?1}}/lib
%dir %{etcjavadir -- %{?1}}/lib/security
%{etcjavadir -- %{?1}}/lib/security/cacerts
%{etcjavadir -- %{?1}}/lib/security/cacerts.upstream
%dir %{etcjavadir -- %{?1}}/conf
%dir %{etcjavadir -- %{?1}}/conf/sdp
%dir %{etcjavadir -- %{?1}}/conf/management
%dir %{etcjavadir -- %{?1}}/conf/security
%dir %{etcjavadir -- %{?1}}/conf/security/policy
%dir %{etcjavadir -- %{?1}}/conf/security/policy/limited
%dir %{etcjavadir -- %{?1}}/conf/security/policy/unlimited
%config(noreplace) %{etcjavadir -- %{?1}}/lib/security/default.policy
%config(noreplace) %{etcjavadir -- %{?1}}/lib/security/blocked.certs
%config(noreplace) %{etcjavadir -- %{?1}}/lib/security/public_suffix_list.dat
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/limited/exempt_local.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/limited/default_local.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/limited/default_US_export.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/unlimited/default_local.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/policy/unlimited/default_US_export.policy
 %{etcjavadir -- %{?1}}/conf/security/policy/README.txt
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/java.policy
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/java.security
%config(noreplace) %{etcjavadir -- %{?1}}/conf/logging.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/nss.cfg
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/nss.fips.cfg
%config(noreplace) %{etcjavadir -- %{?1}}/conf/management/jmxremote.access
# This is a config template, thus not config-noreplace
%config  %{etcjavadir -- %{?1}}/conf/management/jmxremote.password.template
%config  %{etcjavadir -- %{?1}}/conf/sdp/sdp.conf.template
%config(noreplace) %{etcjavadir -- %{?1}}/conf/management/management.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/net.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/sound.properties
%{_jvmdir}/%{sdkdir -- %{?1}}/conf
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/security
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_bindir}/java
%ghost %{_bindir}/%{alt_java_name}
%ghost %{_jvmdir}/jre
%ghost %{_bindir}/keytool
%ghost %{_bindir}/pack200
%ghost %{_bindir}/rmid
%ghost %{_bindir}/rmiregistry
%ghost %{_bindir}/unpack200
%ghost %{_jvmdir}/jre-%{origin}
%ghost %{_jvmdir}/jre-%{javaver}
%ghost %{_jvmdir}/jre-%{javaver}-%{origin}
%endif
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=1820172
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
%ghost %{_jvmdir}/%{sdkdir -- %{?1}}/conf.rpmmoved
%ghost %{_jvmdir}/%{sdkdir -- %{?1}}/lib/security.rpmmoved
}

%define files_devel() %{expand:
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/bin
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jar
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jarsigner
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javac
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javadoc
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javap
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jconsole
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jcmd
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdb
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdeps
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdeprscan
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jfr
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jimage
# Some architectures don't have the serviceability agent
%ifarch %{sa_arches}
%ifnarch %{zero_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jhsdb
%{_mandir}/man1/jhsdb-%{uniquesuffix -- %{?1}}.1*
%endif
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jinfo
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jlink
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jmap
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jmod
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jps
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jpackage
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jrunscript
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jshell
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstack
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstat
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstatd
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/serialver
%{_jvmdir}/%{sdkdir -- %{?1}}/include
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/ct.sym
%if %{with_systemtap}
%{_jvmdir}/%{sdkdir -- %{?1}}/tapset
%endif
%{_datadir}/applications/*jconsole%{?1}.desktop
%{_mandir}/man1/jar-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jarsigner-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/javac-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/javadoc-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/javap-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jconsole-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jcmd-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jdb-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jdeps-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jinfo-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jmap-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jps-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jpackage-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jrunscript-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jstack-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jstat-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jstatd-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/serialver-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jdeprscan-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jlink-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jmod-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jshell-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jfr-%{uniquesuffix -- %{?1}}.1*

%if %{with_systemtap}
%dir %{tapsetroot}
%dir %{tapsetdirttapset}
%dir %{tapsetdir}
%{tapsetdir}/*%{_arch}%{?1}.stp
%endif
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_bindir}/javac
%ghost %{_jvmdir}/java
%ghost %{_jvmdir}/%{alt_java_name}
%ghost %{_bindir}/jlink
%ghost %{_bindir}/jmod
%ghost %{_bindir}/jhsdb
%ghost %{_bindir}/jar
%ghost %{_bindir}/jarsigner
%ghost %{_bindir}/javadoc
%ghost %{_bindir}/javap
%ghost %{_bindir}/jcmd
%ghost %{_bindir}/jconsole
%ghost %{_bindir}/jdb
%ghost %{_bindir}/jdeps
%ghost %{_bindir}/jdeprscan
%ghost %{_bindir}/jimage
%ghost %{_bindir}/jinfo
%ghost %{_bindir}/jmap
%ghost %{_bindir}/jps
%ghost %{_bindir}/jrunscript
%ghost %{_bindir}/jshell
%ghost %{_bindir}/jstack
%ghost %{_bindir}/jstat
%ghost %{_bindir}/jstatd
%ghost %{_bindir}/serialver
%ghost %{_jvmdir}/java-%{origin}
%ghost %{_jvmdir}/java-%{javaver}
%ghost %{_jvmdir}/java-%{javaver}-%{origin}
%endif
%endif
}

%define files_jmods() %{expand:
%{_jvmdir}/%{sdkdir -- %{?1}}/jmods
}

%define files_demo() %{expand:
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%{_jvmdir}/%{sdkdir -- %{?1}}/demo
%{_jvmdir}/%{sdkdir -- %{?1}}/sample
}

%define files_src() %{expand:
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/src.zip
}

%define files_static_libs() %{expand:
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_root}
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_arch_dir}
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_install_dir}
%{_jvmdir}/%{sdkdir -- %{?1}}/%{static_libs_install_dir}/lib*.a
}

%define files_javadoc() %{expand:
%doc %{_javadocdir}/%{uniquejavadocdir -- %{?1}}
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_javadocdir}/java
%ghost %{_javadocdir}/java-%{origin}
%ghost %{_javadocdir}/java-%{javaver}
%ghost %{_javadocdir}/java-%{javaver}-%{origin}
%endif
%endif
}

%define files_javadoc_zip() %{expand:
%doc %{_javadocdir}/%{uniquejavadocdir -- %{?1}}.zip
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_javadocdir}/java-zip
%ghost %{_javadocdir}/java-%{origin}.zip
%ghost %{_javadocdir}/java-%{javaver}.zip
%ghost %{_javadocdir}/java-%{javaver}-%{origin}.zip
%endif
%endif
}

# not-duplicated requires/provides/obsoletes for normal/debug packages
%define java_rpo() %{expand:
Requires: fontconfig%{?_isa}
Requires: xorg-x11-fonts-Type1
# Require libXcomposite explicitly since it's only dynamically loaded
# at runtime. Fixes screenshot issues. See JDK-8150954.
Requires: libXcomposite%{?_isa}
# Requires rest of java
Requires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
# for java-X-openjdk package's desktop binding
# Where recommendations are available, recommend Gtk+ for the Swing look and feel
%if 0%{?rhel} >= 8 || 0%{?fedora} > 0
Recommends: gtk3%{?_isa}
%endif

Provides: java-%{javaver}-%{origin}%{?1} = %{epoch}:%{version}-%{release}

# Standard JPackage base provides
Provides: jre-%{javaver}%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java%{?1} = %{epoch}:%{version}-%{release}
Provides: jre%{?1} = %{epoch}:%{version}-%{release}
%endif
}

%define java_headless_rpo() %{expand:
# Require /etc/pki/java/cacerts
Requires: ca-certificates
# Require javapackages-filesystem for ownership of /usr/lib/jvm/ and macros
Requires: javapackages-filesystem
# Require zone-info data provided by tzdata-java sub-package
# 2022a required as of JDK-8283350 in 17.0.4
Requires: tzdata-java >= 2022a
# for support of kernel stream control
# libsctp.so.1 is being `dlopen`ed on demand
Requires: lksctp-tools%{?_isa}
%if ! 0%{?flatpak}
# tool to copy jdk's configs - should be Recommends only, but then only dnf/yum enforce it,
# not rpm transaction and so no configs are persisted when pure rpm -u is run. It may be
# considered as regression
Requires: copy-jdk-configs >= 4.0
OrderWithRequires: copy-jdk-configs
%endif
# for printing support
Requires: cups-libs
# for system security properties
Requires: crypto-policies
# for FIPS PKCS11 provider
Requires: nss
# Post requires alternatives to install tool alternatives
Requires(post):   %{alternatives_requires}
# Postun requires alternatives to uninstall tool alternatives
Requires(postun): %{alternatives_requires}
# Where suggestions are available, recommend the sctp and pcsc libraries
# for optional support of kernel stream control and card reader
%if 0%{?rhel} >= 8 || 0%{?fedora} > 0
Suggests: lksctp-tools%{?_isa}, pcsc-lite-libs%{?_isa}
%endif

# Standard JPackage base provides
Provides: jre-%{javaver}-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: jre-headless%{?1} = %{epoch}:%{version}-%{release}
Provides: java-headless%{?1} = %{epoch}:%{version}-%{release}
%endif
}

%define java_devel_rpo() %{expand:
# Requires base package
Requires:         %{name}%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives
Requires(post):   %{alternatives_requires}
# Postun requires alternatives to uninstall tool alternatives
Requires(postun): %{alternatives_requires}

# Standard JPackage devel provides
Provides: java-sdk-%{javaver}-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-sdk-%{javaver}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-devel%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-devel%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-devel-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-sdk-%{origin}%{?1} = %{epoch}:%{version}-%{release}
Provides: java-devel%{?1} = %{epoch}:%{version}-%{release}
Provides: java-sdk%{?1} = %{epoch}:%{version}-%{release}
%endif
}

%define java_static_libs_rpo() %{expand:
Requires:         %{name}-devel%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
}

%define java_jmods_rpo() %{expand:
# Requires devel package
# as jmods are bytecode, they should be OK without any _isa
Requires:         %{name}-devel%{?1} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1} = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-jmods%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-jmods%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-jmods%{?1} = %{epoch}:%{version}-%{release}
%endif
}

%define java_demo_rpo() %{expand:
Requires: %{name}%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}

Provides: java-%{javaver}-demo%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-demo%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-demo%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-demo%{?1} = %{epoch}:%{version}-%{release}
%endif
}

%define java_javadoc_rpo() %{expand:
OrderWithRequires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}
# Post requires alternatives to install javadoc alternative
Requires(post):   %{alternatives_requires}
# Postun requires alternatives to uninstall javadoc alternative
Requires(postun): %{alternatives_requires}

# Standard JPackage javadoc provides
Provides: java-%{javaver}-javadoc%{?1}%{?2} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-javadoc%{?1}%{?2} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-javadoc%{?1}%{?2} = %{epoch}:%{version}-%{release}
%endif
}

%define java_src_rpo() %{expand:
Requires: %{name}-headless%{?1}%{?_isa} = %{epoch}:%{version}-%{release}

# Standard JPackage sources provides
Provides: java-%{javaver}-src%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-%{origin}-src%{?1} = %{epoch}:%{version}-%{release}
%if %is_system_jdk
Provides: java-src%{?1} = %{epoch}:%{version}-%{release}
Provides: java-%{origin}-src%{?1} = %{epoch}:%{version}-%{release}
%endif
}

# Prevent brp-java-repack-jars from being run
%global __jar_repack 0

Name:    java-17-%{origin}
Version: %{newjavaver}.%{buildver}
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
Summary: %{origin_nice} %{featurever} Runtime Environment
# Groups are only used up to RHEL 8 and on Fedora versions prior to F30
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

# HotSpot code is licensed under GPLv2
# JDK library code is licensed under GPLv2 with the Classpath exception
# The Apache license is used in code taken from Apache projects (primarily xalan & xerces)
# DOM levels 2 & 3 and the XML digital signature schemas are licensed under the W3C Software License
# The JSR166 concurrency code is in the public domain
# The BSD and MIT licenses are used for a number of third-party libraries (see ADDITIONAL_LICENSE_INFO)
# The OpenJDK source tree includes:
# - JPEG library (IJG), zlib & libpng (zlib), giflib (MIT), harfbuzz (ISC),
# - freetype (FTL), jline (BSD) and LCMS (MIT)
# - jquery (MIT), jdk.crypto.cryptoki PKCS 11 wrapper (RSA)
# - public_suffix_list.dat from publicsuffix.org (MPLv2.0)
# The test code includes copies of NSS under the Mozilla Public License v2.0
# The PCSClite headers are under a BSD with advertising license
# The elliptic curve cryptography (ECC) source code is licensed under the LGPLv2.1 or any later version
License:  ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib and ISC and FTL and RSA
URL:      http://openjdk.java.net/


# The source tarball, generated using generate_source_tarball.sh
Source0: openjdk-jdk%{featurever}u-%{vcstag}.tar.xz

# Use 'icedtea_sync.sh' to update the following
# They are based on code contained in the IcedTea project (6.x).
# Systemtap tapsets. Zipped up to keep it small.
Source8: tapsets-icedtea-%{icedteaver}.tar.xz

# Desktop files. Adapted from IcedTea
Source9: jconsole.desktop.in

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

############################################
#
# RPM/distribution specific patches
#
############################################

# NSS via SunPKCS11 Provider (disabled comment
# due to memory leak).
Patch1000: rh1648249-add_commented_out_nss_cfg_provider_to_java_security.patch
# RH1750419: enable build of speculative store bypass hardened alt-java (CVE-2018-3639)
Patch600: rh1750419-redhat_alt_java.patch

# Ignore AWTError when assistive technologies are loaded
Patch1:    rh1648242-accessible_toolkit_crash_do_not_break_jvm.patch
# Restrict access to java-atk-wrapper classes
Patch2:    rh1648644-java_access_bridge_privileged_security.patch
Patch3:    rh649512-remove_uses_of_far_in_jpeg_libjpeg_turbo_1_4_compat_for_jdk10_and_up.patch
# Depend on pcsc-lite-libs instead of pcsc-lite-devel as this is only in optional repo
Patch6: rh1684077-openjdk_should_depend_on_pcsc-lite-libs_instead_of_pcsc-lite-devel.patch
# Add translations for Europe/Kyiv locally until upstream is fully updated for tzdata2022b
Patch7: jdk8292223-tzdata2022b-kyiv.patch

# Crypto policy and FIPS support patches
# Patch is generated from the fips-17u tree at https://github.com/rh-openjdk/jdk/tree/fips-17u
# as follows: git diff %%{vcstag} src make > fips-17u-$(git show -s --format=%h HEAD).patch
# Diff is limited to src and make subdirectories to exclude .github changes
# Fixes currently included:
# PR3183, RH1340845: Follow system wide crypto policy
# PR3695: Allow use of system crypto policy to be disabled by the user
# RH1655466: Support RHEL FIPS mode using SunPKCS11 provider
# RH1818909: No ciphersuites availale for SSLSocket in FIPS mode
# RH1860986: Disable TLSv1.3 with the NSS-FIPS provider until PKCS#11 v3.0 support is available
# RH1915071: Always initialise JavaSecuritySystemConfiguratorAccess
# RH1929465: Improve system FIPS detection
# RH1995150: Disable non-FIPS crypto in SUN and SunEC security providers
# RH1996182: Login to the NSS software token in FIPS mode
# RH1991003: Allow plain key import unless com.redhat.fips.plainKeySupport is set to false
# RH2021263: Resolve outstanding FIPS issues
# RH2052819: Fix FIPS reliance on crypto policies
# RH2052829: Detect NSS at Runtime for FIPS detection
# RH2052070: Enable AlgorithmParameters and AlgorithmParameterGenerator services in FIPS mode
# RH2023467: Enable FIPS keys export
# RH2094027: SunEC runtime permission for FIPS
# RH2036462: sun.security.pkcs11.wrapper.PKCS11.getInstance breakage
# RH2090378: Revert to disabling system security properties and FIPS mode support together
# RH2104724: Avoid import/export of DH private keys
# RH2092507: P11Key.getEncoded does not work for DH keys in FIPS mode
# Build the systemconf library on all platforms
# RH2048582: Support PKCS#12 keystores
# RH2020290: Support TLS 1.3 in FIPS mode
Patch1001: fips-17u-%{fipsver}.patch

#############################################
#
# OpenJDK patches in need of upstreaming
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
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: gdb
BuildRequires: libxslt
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
# Requirement for setting up nss.cfg and nss.fips.cfg
BuildRequires: nss-devel
# Requirement for system security property test
BuildRequires: crypto-policies
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: zip
BuildRequires: javapackages-filesystem
BuildRequires: java-%{buildjdkver}-openjdk-devel
# Zero-assembler build requirement
%ifarch %{zero_arches}
BuildRequires: libffi-devel
%endif
# 2022a required as of JDK-8283350 in 17.0.4
BuildRequires: tzdata-java >= 2022a
# Earlier versions have a bug in tree vectorization on PPC
BuildRequires: gcc >= 4.8.3-8

%if %{with_systemtap}
BuildRequires: systemtap-sdt-devel
%endif
BuildRequires: make

%if %{system_libs}
BuildRequires: freetype-devel
BuildRequires: giflib-devel
BuildRequires: harfbuzz-devel
BuildRequires: lcms2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
%else
# Version in src/java.desktop/share/native/libfreetype/include/freetype/freetype.h
Provides: bundled(freetype) = 2.12.1
# Version in src/java.desktop/share/native/libsplashscreen/giflib/gif_lib.h
Provides: bundled(giflib) = 5.2.1
# Version in src/java.desktop/share/native/libharfbuzz/hb-version.h
Provides: bundled(harfbuzz) = 4.4.1
# Version in src/java.desktop/share/native/liblcms/lcms2.h
Provides: bundled(lcms2) = 2.12.0
# Version in src/java.desktop/share/native/libjavajpeg/jpeglib.h
Provides: bundled(libjpeg) = 6b
# Version in src/java.desktop/share/native/libsplashscreen/libpng/png.h
Provides: bundled(libpng) = 1.6.37
# We link statically against libstdc++ to increase portability
BuildRequires: libstdc++-static
%endif

# this is always built, also during debug-only build
# when it is built in debug-only this package is just placeholder
%{java_rpo %{nil}}

%description
The %{origin_nice} %{featurever} runtime environment.

%if %{include_debug_build}
%package slowdebug
Summary: %{origin_nice} %{featurever} Runtime Environment %{debug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_rpo -- %{debug_suffix_unquoted}}
%description slowdebug
The %{origin_nice} %{featurever} runtime environment.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package fastdebug
Summary: %{origin_nice} %{featurever} Runtime Environment %{fastdebug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_rpo -- %{fastdebug_suffix_unquoted}}
%description fastdebug
The %{origin_nice} %{featurever} runtime environment.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package headless
Summary: %{origin_nice} %{featurever} Headless Runtime Environment
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_headless_rpo %{nil}}

%description headless
The %{origin_nice} %{featurever} runtime environment without audio and video support.
%endif

%if %{include_debug_build}
%package headless-slowdebug
Summary: %{origin_nice} %{featurever} Runtime Environment %{debug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_headless_rpo -- %{debug_suffix_unquoted}}

%description headless-slowdebug
The %{origin_nice} %{featurever} runtime environment without audio and video support.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package headless-fastdebug
Summary: %{origin_nice} %{featurever} Runtime Environment %{fastdebug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_headless_rpo -- %{fastdebug_suffix_unquoted}}

%description headless-fastdebug
The %{origin_nice} %{featurever} runtime environment without audio and video support.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package devel
Summary: %{origin_nice} %{featurever} Development Environment
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_devel_rpo %{nil}}

%description devel
The %{origin_nice} %{featurever} development tools.
%endif

%if %{include_debug_build}
%package devel-slowdebug
Summary: %{origin_nice} %{featurever} Development Environment %{debug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_devel_rpo -- %{debug_suffix_unquoted}}

%description devel-slowdebug
The %{origin_nice} %{featurever} development tools.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package devel-fastdebug
Summary: %{origin_nice} %{featurever} Development Environment %{fastdebug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Tools
%endif

%{java_devel_rpo -- %{fastdebug_suffix_unquoted}}

%description devel-fastdebug
The %{origin_nice} %{featurever} development tools              .
%{fastdebug_warning}
%endif

%if %{include_staticlibs}

%if %{include_normal_build}
%package static-libs
Summary: %{origin_nice} %{featurever} libraries for static linking

%{java_static_libs_rpo %{nil}}

%description static-libs
The %{origin_nice} %{featurever} libraries for static linking.
%endif

%if %{include_debug_build}
%package static-libs-slowdebug
Summary: %{origin_nice} %{featurever} libraries for static linking %{debug_on}

%{java_static_libs_rpo -- %{debug_suffix_unquoted}}

%description static-libs-slowdebug
The %{origin_nice} %{featurever} libraries for static linking.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package static-libs-fastdebug
Summary: %{origin_nice} %{featurever} libraries for static linking %{fastdebug_on}

%{java_static_libs_rpo -- %{fastdebug_suffix_unquoted}}

%description static-libs-fastdebug
The %{origin_nice} %{featurever} libraries for static linking.
%{fastdebug_warning}
%endif

# staticlibs
%endif

%if %{include_normal_build}
%package jmods
Summary: JMods for %{origin_nice} %{featurever}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_jmods_rpo %{nil}}

%description jmods
The JMods for %{origin_nice} %{featurever}.
%endif

%if %{include_debug_build}
%package jmods-slowdebug
Summary: JMods for %{origin_nice} %{featurever} %{debug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_jmods_rpo -- %{debug_suffix_unquoted}}

%description jmods-slowdebug
The JMods for %{origin_nice} %{featurever}.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package jmods-fastdebug
Summary: JMods for %{origin_nice} %{featurever} %{fastdebug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Tools
%endif

%{java_jmods_rpo -- %{fastdebug_suffix_unquoted}}

%description jmods-fastdebug
The JMods for %{origin_nice} %{featurever}.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package demo
Summary: %{origin_nice} %{featurever} Demos
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_demo_rpo %{nil}}

%description demo
The %{origin_nice} %{featurever} demos.
%endif

%if %{include_debug_build}
%package demo-slowdebug
Summary: %{origin_nice} %{featurever} Demos %{debug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_demo_rpo -- %{debug_suffix_unquoted}}

%description demo-slowdebug
The %{origin_nice} %{featurever} demos.
%{debug_warning}
%endif

%if %{include_fastdebug_build}
%package demo-fastdebug
Summary: %{origin_nice} %{featurever} Demos %{fastdebug_on}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_demo_rpo -- %{fastdebug_suffix_unquoted}}

%description demo-fastdebug
The %{origin_nice} %{featurever} demos.
%{fastdebug_warning}
%endif

%if %{include_normal_build}
%package src
Summary: %{origin_nice} %{featurever} Source Bundle
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_src_rpo %{nil}}

%description src
The %{compatiblename}-src sub-package contains the complete %{origin_nice} %{featurever}
class library source code for use by IDE indexers and debuggers.
%endif

%if %{include_debug_build}
%package src-slowdebug
Summary: %{origin_nice} %{featurever} Source Bundle %{for_debug}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_src_rpo -- %{debug_suffix_unquoted}}

%description src-slowdebug
The %{compatiblename}-src-slowdebug sub-package contains the complete %{origin_nice} %{featurever}
 class library source code for use by IDE indexers and debuggers, %{for_debug}.
%endif

%if %{include_fastdebug_build}
%package src-fastdebug
Summary: %{origin_nice} %{featurever} Source Bundle %{for_fastdebug}
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Development/Languages
%endif

%{java_src_rpo -- %{fastdebug_suffix_unquoted}}

%description src-fastdebug
The %{compatiblename}-src-fastdebug sub-package contains the complete %{origin_nice} %{featurever}
 class library source code for use by IDE indexers and debuggers, %{for_fastdebug}.
%endif

%if %{include_normal_build}
%package javadoc
Summary: %{origin_nice} %{featurever} API documentation
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Documentation
%endif
Requires: javapackages-filesystem
Obsoletes: javadoc-slowdebug < 1:13.0.0.33-1.rolling

%{java_javadoc_rpo -- %{nil} %{nil}}

%description javadoc
The %{origin_nice} %{featurever} API documentation.
%endif

%if %{include_normal_build}
%package javadoc-zip
Summary: %{origin_nice} %{featurever} API documentation compressed in a single archive
%if (0%{?rhel} > 0 && 0%{?rhel} <= 8) || (0%{?fedora} >= 0 && 0%{?fedora} < 30)
Group:   Documentation
%endif
Requires: javapackages-filesystem
Obsoletes: javadoc-zip-slowdebug < 1:13.0.0.33-1.rolling

%{java_javadoc_rpo -- %{nil} -zip}
%{java_javadoc_rpo -- %{nil} %{nil}}

%description javadoc-zip
The %{origin_nice} %{featurever} API documentation compressed in a single archive.
%endif

%prep

echo "Preparing %{oj_vendor_version}"

# Using the echo macro breaks rpmdev-bumpspec, as it parses the first line of stdout :-(
%if 0%{?stapinstall:1}
  echo "CPU: %{_target_cpu}, arch install directory: %{archinstall}, SystemTap install directory: %{stapinstall}"
%else
  %{error:Unrecognised architecture %{_target_cpu}}
%endif

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
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 8 ] ; then
 echo "priority must be 8 digits in total, violated"
 exit 14
fi

# OpenJDK patches

%if %{system_libs}
# Remove libraries that are linked by both static and dynamic builds
sh %{SOURCE12} %{top_level_dir_name}
%endif

# Patch the JDK
pushd %{top_level_dir_name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch6 -p1
%patch7 -p1
# Add crypto policy and FIPS support
%patch1001 -p1
# nss.cfg PKCS11 support; must come last as it also alters java.security
%patch1000 -p1
popd # openjdk

%patch600

# The OpenJDK version file includes the current
# upstream version information. For some reason,
# configure does not automatically use the
# default pre-version supplied there (despite
# what the file claims), so we pass it manually
# to configure
VERSION_FILE=$(pwd)/%{top_level_dir_name}/make/conf/version-numbers.conf
if [ -f ${VERSION_FILE} ] ; then
    UPSTREAM_EA_DESIGNATOR=$(grep '^DEFAULT_PROMOTED_VERSION_PRE' ${VERSION_FILE} | cut -d '=' -f 2)
else
    echo "Could not find OpenJDK version file.";
    exit 16
fi
if [ "x${UPSTREAM_EA_DESIGNATOR}" != "x%{ea_designator}" ] ; then
    echo "WARNING: Designator mismatch";
    echo "Spec file is configured for a %{build_type} build with designator '%{ea_designator}'"
    echo "Upstream version-pre setting is '${UPSTREAM_EA_DESIGNATOR}'";
    # Don't fail at present as upstream are not maintaining the value correctly
    #exit 17
fi

# Extract systemtap tapsets
%if %{with_systemtap}
tar --strip-components=1 -x -I xz -f %{SOURCE8}
%if %{include_debug_build}
cp -r tapset tapset%{debug_suffix}
%endif
%if %{include_fastdebug_build}
cp -r tapset tapset%{fastdebug_suffix}
%endif

for suffix in %{build_loop} ; do
  for file in "tapset"$suffix/*.in; do
    OUTPUT_FILE=`echo $file | sed -e "s:\.stp\.in$:-%{version}-%{release}.%{_arch}.stp:g"`
    sed -e "s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir -- $suffix}/lib/server/libjvm.so:g" $file > $file.1
    sed -e "s:@JAVA_SPEC_VER@:%{javaver}:g" $file.1 > $file.2
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e "s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir -- $suffix}/lib/client/libjvm.so:g" $file.2 > $OUTPUT_FILE
%else
    sed -e "/@ABS_CLIENT_LIBJVM_SO@/d" $file.2 > $OUTPUT_FILE
%endif
    sed -i -e "s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir -- $suffix}:g" $OUTPUT_FILE
    sed -i -e "s:@INSTALL_ARCH_DIR@:%{archinstall}:g" $OUTPUT_FILE
    sed -i -e "s:@prefix@:%{_jvmdir}/%{sdkdir -- $suffix}/:g" $OUTPUT_FILE
  done
done
# systemtap tapsets ends
%endif

# Prepare desktop files
# The _X_ syntax indicates variables that are replaced by make upstream
# The @X@ syntax indicates variables that are replaced by configure upstream
for suffix in %{build_loop} ; do
for file in %{SOURCE9}; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed    -e  "s:_SDKBINDIR_:%{sdkbindir -- $suffix}:g" $file > $OUTPUT_FILE
    sed -i -e  "s:@target_cpu@:%{_arch}:g" $OUTPUT_FILE
    sed -i -e  "s:@OPENJDK_VER@:%{version}-%{release}.%{_arch}$suffix:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VER@:%{javaver}:g" $OUTPUT_FILE
    sed -i -e  "s:@JAVA_VENDOR@:%{origin}:g" $OUTPUT_FILE
done
done

# Setup nss.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE11} > nss.cfg

# Setup nss.fips.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE17} > nss.fips.cfg

%build

# How many CPU's do we have?
export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
export NUM_PROC=${NUM_PROC:-1}
%if 0%{?_smp_ncpus_max}
# Honor %%_smp_ncpus_max
[ ${NUM_PROC} -gt %{?_smp_ncpus_max} ] && export NUM_PROC=%{?_smp_ncpus_max}
%endif

%ifarch s390x sparc64 alpha %{power64} %{aarch64}
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

# We use ourcppflags because the OpenJDK build seems to
# pass EXTRA_CFLAGS to the HotSpot C++ compiler...
# Explicitly set the C++ standard as the default has changed on GCC >= 6
EXTRA_CFLAGS="%ourcppflags"
EXTRA_CPP_FLAGS="%ourcppflags"

%ifarch %{power64} ppc
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
%ifarch %{ix86}
# Align stack boundary on x86_32
EXTRA_CFLAGS="$(echo ${EXTRA_CFLAGS} | sed -e 's|-mstackrealign|-mincoming-stack-boundary=2 -mpreferred-stack-boundary=4|')"
EXTRA_CPP_FLAGS="$(echo ${EXTRA_CPP_FLAGS} | sed -e 's|-mstackrealign|-mincoming-stack-boundary=2 -mpreferred-stack-boundary=4|')"
%endif
export EXTRA_CFLAGS EXTRA_CPP_FLAGS

function buildjdk() {
    local outputdir=${1}
    local buildjdk=${2}
    local maketargets="${3}"
    local debuglevel=${4}
    local link_opt=${5}

    local top_dir_abs_src_path=$(pwd)/%{top_level_dir_name}
    local top_dir_abs_build_path=$(pwd)/${outputdir}

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
    echo "Building %{newjavaver}-%{buildver}, pre=%{ea_designator}, opt=%{lts_designator}"

    mkdir -p ${outputdir}
    pushd ${outputdir}

    bash ${top_dir_abs_src_path}/configure \
%ifarch %{zero_arches}
    --with-jvm-variants=zero \
%endif
%ifarch %{ppc64le}
    --with-jobs=1 \
%endif
    --with-version-build=%{buildver} \
    --with-version-pre="%{ea_designator}" \
    --with-version-opt=%{lts_designator} \
    --with-vendor-version-string="%{oj_vendor_version}" \
    --with-vendor-name="%{oj_vendor}" \
    --with-vendor-url="%{oj_vendor_url}" \
    --with-vendor-bug-url="%{oj_vendor_bug_url}" \
    --with-vendor-vm-bug-url="%{oj_vendor_bug_url}" \
    --with-boot-jdk=${buildjdk} \
    --with-debug-level=${debuglevel} \
    --with-native-debug-symbols="%{debug_symbols}" \
    --disable-sysconf-nss \
    --enable-unlimited-crypto \
    --with-zlib=${link_opt} \
    --with-freetype=${link_opt} \
    --with-libjpeg=${link_opt} \
    --with-giflib=${link_opt} \
    --with-libpng=${link_opt} \
    --with-lcms=${link_opt} \
    --with-harfbuzz=${link_opt} \
    --with-stdc++lib=${libc_link_opt} \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC" \
    --with-source-date="${SOURCE_DATE_EPOCH}" \
    --disable-javac-server \
%ifarch %{zgc_arches}
    --with-jvm-features=zgc \
%endif
    --disable-warnings-as-errors

    cat spec.gmk

    make \
      LOG=trace \
      WARNINGS_ARE_ERRORS="-Wno-error" \
      CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
      $maketargets || ( pwd; find ${top_dir_abs_src_path} ${top_dir_abs_build_path} -name "hs_err_pid*.log" | xargs cat && false )

    popd
}

function installjdk() {
    local imagepath=${1}

    if [ -d ${imagepath} ] ; then
        # the build (erroneously) removes read permissions from some jars
        # this is a regression in OpenJDK 7 (our compiler):
        # http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
        find ${imagepath} -iname '*.jar' -exec chmod ugo+r {} \;

        # Build screws up permissions on binaries
        # https://bugs.openjdk.java.net/browse/JDK-8173610
        find ${imagepath} -iname '*.so' -exec chmod +x {} \;
        find ${imagepath}/bin/ -exec chmod +x {} \;

        # Install nss.cfg right away as we will be using the JRE above
        install -m 644 nss.cfg ${imagepath}/conf/security/

        # Install nss.fips.cfg: NSS configuration for global FIPS mode (crypto-policies)
        install -m 644 nss.fips.cfg ${imagepath}/conf/security/

        # Turn on system security properties
        sed -i -e "s:^security.useSystemPropertiesFile=.*:security.useSystemPropertiesFile=true:" \
            ${imagepath}/conf/security/java.security

        # Use system-wide tzdata
        mv ${imagepath}/lib/tzdb.dat{,.upstream}
        ln -sv %{_datadir}/javazi-1.8/tzdb.dat ${imagepath}/lib/tzdb.dat

        # Rename OpenJDK cacerts database
        mv ${imagepath}/lib/security/cacerts{,.upstream}
        # Install cacerts symlink needed by some apps which hard-code the path
        ln -sv /etc/pki/java/cacerts ${imagepath}/lib/security

        # Create fake alt-java as a placeholder for future alt-java
        pushd ${imagepath}
        # add alt-java man page
        echo "Hardened java binary recommended for launching untrusted code from the Web e.g. javaws" > man/man1/%{alt_java_name}.1
        cat man/man1/java.1 >> man/man1/%{alt_java_name}.1
        popd
    fi
}

# Checks on debuginfo must be performed before the files are stripped
# by the RPM installation stage
function debugcheckjdk() {
    local imagepath=${1}

    if [ -d ${imagepath} ] ; then

        so_suffix="so"
        # Check debug symbols are present and can identify code
        find "${imagepath}" -iname "*.$so_suffix" -print0 | while read -d $'\0' lib
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
                if eu-readelf -S "$lib" | grep "\] .gnu_debuglink" | grep PROGBITS; then
                   echo "bad .gnu_debuglink section."
                   eu-readelf -x .gnu_debuglink "$lib"
                   false
                fi
            fi
        done

        # Make sure gdb can do a backtrace based on line numbers on libjvm.so
        # javaCalls.cpp:58 should map to:
        # http://hg.openjdk.java.net/jdk8u/jdk8u/hotspot/file/ff3b27e6bcc2/src/share/vm/runtime/javaCalls.cpp#l58
        # Using line number 1 might cause build problems. See:
        # https://bugzilla.redhat.com/show_bug.cgi?id=1539664
        # https://bugzilla.redhat.com/show_bug.cgi?id=1538767
        gdb -q "${imagepath}/bin/java" <<EOF | tee gdb.out
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

    fi
}

%if %{build_hotspot_first}
  # Build a fresh libjvm.so first and use it to bootstrap
  cp -LR --preserve=mode,timestamps %{bootjdk} newboot
  systemjdk=$(pwd)/newboot
  buildjdk build/newboot ${systemjdk} %{hotspot_target} "release" "bundled"
  mv build/newboot/jdk/lib/server/libjvm.so newboot/lib/server
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


  for loop in %{main_suffix} %{staticlibs_loop} ; do

    builddir=%{buildoutputdir -- ${suffix}${loop}}
    bootbuilddir=boot${builddir}

    if test "x${loop}" = "x%{main_suffix}" ; then
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
        buildjdk ${bootbuilddir} ${systemjdk} "%{bootstrap_targets}" ${debugbuild} ${link_opt}
        buildjdk ${builddir} $(pwd)/${bootbuilddir}/images/%{jdkimage} "${maketargets}" ${debugbuild} ${link_opt}
        rm -rf ${bootbuilddir}
      else
        buildjdk ${builddir} ${systemjdk} "${maketargets}" ${debugbuild} ${link_opt}
      fi
%if %{system_libs}
      # Restore original source tree we modified by removing full in-tree sources
      rm -rf %{top_level_dir_name}
      mv %{top_level_dir_name_backup} %{top_level_dir_name}
%endif
    else
      # Use bundled libraries for building statically
      link_opt="bundled"
      # Static library cycle only builds the static libraries
      maketargets="%{static_libs_target}"
      # Always just do the one build for the static libraries
      buildjdk ${builddir} ${systemjdk} "${maketargets}" ${debugbuild} ${link_opt}
    fi

  done # end of main / staticlibs loop

  # Final setup on the main image
  top_dir_abs_main_build_path=$(pwd)/%{buildoutputdir -- ${suffix}%{main_suffix}}
  installjdk ${top_dir_abs_main_build_path}/images/%{jdkimage}
  # Check debug symbols were built into the dynamic libraries
  debugcheckjdk ${top_dir_abs_main_build_path}/images/%{jdkimage}

  # Print release information
  cat ${top_dir_abs_main_build_path}/images/%{jdkimage}/release

# build cycles
done # end of release / debug cycle loop

%install
STRIP_KEEP_SYMTAB=libjvm*

for suffix in %{build_loop} ; do

top_dir_abs_main_build_path=$(pwd)/%{buildoutputdir -- ${suffix}%{main_suffix}}
%if %{include_staticlibs}
top_dir_abs_staticlibs_build_path=$(pwd)/%{buildoutputdir -- ${suffix}%{staticlibs_loop}}
%endif
jdk_image=${top_dir_abs_main_build_path}/images/%{jdkimage}

# Install the jdk
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}
cp -a ${jdk_image} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}

pushd ${jdk_image}

%if %{with_systemtap}
  # Install systemtap support files
  install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/tapset
  # note, that uniquesuffix  is in BUILD dir in this case
  cp -a $RPM_BUILD_DIR/%{uniquesuffix ""}/tapset$suffix/*.stp $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/tapset/
  pushd  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/tapset/
   tapsetFiles=`ls *.stp`
  popd
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  for name in $tapsetFiles ; do
    targetName=`echo $name | sed "s/.stp/$suffix.stp/"`
    ln -srvf $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/tapset/$name $RPM_BUILD_ROOT%{tapsetdir}/$targetName
  done
%endif

  # Install version-ed symlinks
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{sdkdir -- $suffix} %{jrelnk -- $suffix}
  popd

  # Install man pages
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)-%{uniquesuffix -- $suffix}.1
  done
  # Remove man pages from jdk image
  rm -rf $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/man

popd

# Install static libs artefacts
%if %{include_staticlibs}
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/%{static_libs_install_dir}
cp -a ${top_dir_abs_staticlibs_build_path}/images/%{static_libs_image}/lib/*.a \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/%{static_libs_install_dir}
%endif

if ! echo $suffix | grep -q "debug" ; then
  # Install Javadoc documentation
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
  cp -a ${top_dir_abs_main_build_path}/images/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}
  built_doc_archive=jdk-%{filever}%{ea_designator_zip}+%{buildver}%{lts_designator_zip}-docs.zip
  cp -a ${top_dir_abs_main_build_path}/bundles/${built_doc_archive} \
     $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}.zip || ls -l ${top_dir_abs_main_build_path}/bundles/
fi

# Install release notes
commondocdir=${RPM_BUILD_ROOT}%{_defaultdocdir}/%{uniquejavadocdir -- $suffix}
install -d -m 755 ${commondocdir}
cp -a %{SOURCE10} ${commondocdir}

# Install icons and menu entries
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    %{top_level_dir_name}/src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-%{origin}.png
done

# Install desktop files
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix -- $suffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# copy samples next to demos; samples are mostly js files
cp -r %{top_level_dir_name}/src/sample  $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/


# moving config files to /etc
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mkdir -p $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/conf/  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}
mv $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/lib/security  $RPM_BUILD_ROOT/%{etcjavadir -- $suffix}/lib
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}
  ln -srv $RPM_BUILD_ROOT%{etcjavadir -- $suffix}/conf  ./conf
popd
pushd $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/lib
  ln -srv $RPM_BUILD_ROOT%{etcjavadir -- $suffix}/lib/security  ./security
popd
# end moving files to /etc

# stabilize permissions
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/ -name "*.so" -exec chmod 755 {} \; ;
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/ -type d -exec chmod 755 {} \; ;
find $RPM_BUILD_ROOT/%{_jvmdir}/%{sdkdir -- $suffix}/legal -type f -exec chmod 644 {} \; ;

# end, dual install
done

%check

# We test debug first as it will give better diagnostics on a crash
for suffix in %{build_loop} ; do

# Tests in the check stage are performed on the installed image
# rpmbuild operates as follows: build -> install -> test
export JAVA_HOME=${RPM_BUILD_ROOT}%{_jvmdir}/%{sdkdir -- $suffix}

#check Shenandoah is enabled
%if %{use_shenandoah_hotspot}
$JAVA_HOME/bin/java -XX:+UnlockExperimentalVMOptions -XX:+UseShenandoahGC -version
%endif

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel

# Check ECC is working
$JAVA_HOME/bin/javac -d . %{SOURCE14}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE14})|sed "s|\.java||")

# Check system crypto (policy) is active and can be disabled
# Test takes a single argument - true or false - to state whether system
# security properties are enabled or not.
$JAVA_HOME/bin/javac -d . %{SOURCE15}
export PROG=$(echo $(basename %{SOURCE15})|sed "s|\.java||")
export SEC_DEBUG="-Djava.security.debug=properties"
$JAVA_HOME/bin/java ${SEC_DEBUG} ${PROG} true
$JAVA_HOME/bin/java ${SEC_DEBUG} -Djava.security.disableSystemPropertiesFile=true ${PROG} false

# Check java launcher has no SSB mitigation
if ! nm $JAVA_HOME/bin/java | grep set_speculation ; then true ; else false; fi

# Check alt-java launcher has SSB mitigation on supported architectures
%ifarch %{ssbd_arches}
nm $JAVA_HOME/bin/%{alt_java_name} | grep set_speculation
%else
if ! nm $JAVA_HOME/bin/%{alt_java_name} | grep set_speculation ; then true ; else false; fi
%endif

# Check correct vendor values have been set
$JAVA_HOME/bin/javac -d . %{SOURCE16}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE16})|sed "s|\.java||") "%{oj_vendor}" "%{oj_vendor_url}" "%{oj_vendor_bug_url}" "%{oj_vendor_version}"

# Check translations are available for new timezones
$JAVA_HOME/bin/javac --add-exports java.base/sun.util.resources=ALL-UNNAMED \
                     --add-exports java.base/sun.util.locale.provider=ALL-UNNAMED \
                     -d . %{SOURCE18}
$JAVA_HOME/bin/java --add-exports java.base/sun.util.resources=ALL-UNNAMED \
                    --add-exports java.base/sun.util.locale.provider=ALL-UNNAMED \
                    $(echo $(basename %{SOURCE18})|sed "s|\.java||") "Europe/Kiev" "Europe/Kyiv"

%if %{include_staticlibs}
# Check debug symbols in static libraries (smoke test)
export STATIC_LIBS_HOME=${JAVA_HOME}/%{static_libs_install_dir}
readelf --debug-dump $STATIC_LIBS_HOME/libfdlibm.a | grep w_remainder.c
readelf --debug-dump $STATIC_LIBS_HOME/libfdlibm.a | grep e_remainder.c
%endif

# Check src.zip has all sources. See RHBZ#1130490
$JAVA_HOME/bin/jar -tf $JAVA_HOME/lib/src.zip | grep 'sun.misc.Unsafe'

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

%if %{include_normal_build}
# intentionally only for non-debug
%pretrans headless -p <lua>
-- see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue
-- see https://bugzilla.redhat.com/show_bug.cgi?id=1290388 for pretrans over pre
-- if copy-jdk-configs is in transaction, it installs in pretrans to temp
-- if copy_jdk_configs is in temp, then it means that copy-jdk-configs is in transaction  and so is
-- preferred over one in %%{_libexecdir}. If it is not in transaction, then depends
-- whether copy-jdk-configs is installed or not. If so, then configs are copied
-- (copy_jdk_configs from %%{_libexecdir} used) or not copied at all
local posix = require "posix"

if (os.getenv("debug") == "true") then
  debug = true;
  print("cjc: in spec debug is on")
else
  debug = false;
end

SOURCE1 = "%{rpm_state_dir}/copy_jdk_configs.lua"
SOURCE2 = "%{_libexecdir}/copy_jdk_configs.lua"

local stat1 = posix.stat(SOURCE1, "type");
local stat2 = posix.stat(SOURCE2, "type");

  if (stat1 ~= nil) then
  if (debug) then
    print(SOURCE1 .." exists - copy-jdk-configs in transaction, using this one.")
  end;
  package.path = package.path .. ";" .. SOURCE1
else
  if (stat2 ~= nil) then
  if (debug) then
    print(SOURCE2 .." exists - copy-jdk-configs already installed and NOT in transaction. Using.")
  end;
  package.path = package.path .. ";" .. SOURCE2
  else
    if (debug) then
      print(SOURCE1 .." does NOT exists")
      print(SOURCE2 .." does NOT exists")
      print("No config files will be copied")
    end
  return
  end
end
arg = nil ;  -- it is better to null the arg up, no meter if they exists or not, and use cjc as module in unified way, instead of relaying on "main" method during require "copy_jdk_configs.lua"
cjc = require "copy_jdk_configs.lua"
args = {"--currentjvm", "%{uniquesuffix %{nil}}", "--jvmdir", "%{_jvmdir %{nil}}", "--origname", "%{name}", "--origjavaver", "%{javaver}", "--arch", "%{_arch}", "--temp", "%{rpm_state_dir}/%{name}.%{_arch}"}
cjc.mainProgram(args)

%post
%{post_script %{nil}}

%post headless
%{post_headless %{nil}}

%postun
%{postun_script %{nil}}

%postun headless
%{postun_headless %{nil}}

%posttrans
%{posttrans_script %{nil}}

%posttrans headless
%{alternatives_java_install %{nil}}

%post devel
%{post_devel %{nil}}

%postun devel
%{postun_devel %{nil}}

%posttrans  devel
%{posttrans_devel %{nil}}

%posttrans javadoc
%{alternatives_javadoc_install %{nil}}

%postun javadoc
%{postun_javadoc %{nil}}

%posttrans javadoc-zip
%{alternatives_javadoczip_install %{nil}}

%postun javadoc-zip
%{postun_javadoc_zip %{nil}}
%endif

%if %{include_debug_build}
%post slowdebug
%{post_script -- %{debug_suffix_unquoted}}

%post headless-slowdebug
%{post_headless -- %{debug_suffix_unquoted}}

%posttrans headless-slowdebug
%{alternatives_java_install -- %{debug_suffix_unquoted}}

%postun slowdebug
%{postun_script -- %{debug_suffix_unquoted}}

%postun headless-slowdebug
%{postun_headless -- %{debug_suffix_unquoted}}

%posttrans slowdebug
%{posttrans_script -- %{debug_suffix_unquoted}}

%post devel-slowdebug
%{post_devel -- %{debug_suffix_unquoted}}

%postun devel-slowdebug
%{postun_devel -- %{debug_suffix_unquoted}}

%posttrans  devel-slowdebug
%{posttrans_devel -- %{debug_suffix_unquoted}}
%endif

%if %{include_fastdebug_build}
%post fastdebug
%{post_script -- %{fastdebug_suffix_unquoted}}

%post headless-fastdebug
%{post_headless -- %{fastdebug_suffix_unquoted}}

%postun fastdebug
%{postun_script -- %{fastdebug_suffix_unquoted}}

%postun headless-fastdebug
%{postun_headless -- %{fastdebug_suffix_unquoted}}

%posttrans fastdebug
%{posttrans_script -- %{fastdebug_suffix_unquoted}}

%posttrans headless-fastdebug
%{alternatives_java_install -- %{fastdebug_suffix_unquoted}}

%post devel-fastdebug
%{post_devel -- %{fastdebug_suffix_unquoted}}

%postun devel-fastdebug
%{postun_devel -- %{fastdebug_suffix_unquoted}}

%posttrans  devel-fastdebug
%{posttrans_devel -- %{fastdebug_suffix_unquoted}}

%endif

%if %{include_normal_build}
%files
# main package builds always
%{files_jre %{nil}}
%else
%files
# placeholder
%endif


%if %{include_normal_build}
%files headless
# important note, see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue
# all config/noreplace files (and more) have to be declared in pretrans. See pretrans
%{files_jre_headless %{nil}}

%files devel
%{files_devel %{nil}}

%if %{include_staticlibs}
%files static-libs
%{files_static_libs %{nil}}
%endif

%files jmods
%{files_jmods %{nil}}

%files demo
%{files_demo %{nil}}

%files src
%{files_src %{nil}}

%files javadoc
%{files_javadoc %{nil}}

# This puts a huge documentation file in /usr/share
# It is now architecture-dependent, as eg. AOT and Graal are now x86_64 only
# same for debug variant
%files javadoc-zip
%{files_javadoc_zip %{nil}}
%endif

%if %{include_debug_build}
%files slowdebug
%{files_jre -- %{debug_suffix_unquoted}}

%files headless-slowdebug
%{files_jre_headless -- %{debug_suffix_unquoted}}

%files devel-slowdebug
%{files_devel -- %{debug_suffix_unquoted}}

%if %{include_staticlibs}
%files static-libs-slowdebug
%{files_static_libs -- %{debug_suffix_unquoted}}
%endif

%files jmods-slowdebug
%{files_jmods -- %{debug_suffix_unquoted}}

%files demo-slowdebug
%{files_demo -- %{debug_suffix_unquoted}}

%files src-slowdebug
%{files_src -- %{debug_suffix_unquoted}}
%endif

%if %{include_fastdebug_build}
%files fastdebug
%{files_jre -- %{fastdebug_suffix_unquoted}}

%files headless-fastdebug
%{files_jre_headless -- %{fastdebug_suffix_unquoted}}

%files devel-fastdebug
%{files_devel -- %{fastdebug_suffix_unquoted}}

%if %{include_staticlibs}
%files static-libs-fastdebug
%{files_static_libs -- %{fastdebug_suffix_unquoted}}
%endif

%files jmods-fastdebug
%{files_jmods -- %{fastdebug_suffix_unquoted}}

%files demo-fastdebug
%{files_demo -- %{fastdebug_suffix_unquoted}}

%files src-fastdebug
%{files_src -- %{fastdebug_suffix_unquoted}}

%endif

%changelog
* Tue Oct 04 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.5.0.7-0.1.ea
- Update to jdk-17.0.5+7
- Update release notes to 17.0.5+7

* Mon Oct 03 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.5.0.1-0.1.ea
- Update to jdk-17.0.5+1
- Update release notes to 17.0.5+1
- Switch to EA mode for 17.0.5 pre-release builds.
- Bump HarfBuzz bundled version to 4.4.1 following JDK-8289853
- Bump FreeType bundled version to 2.12.1 following JDK-8290334

* Tue Aug 30 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.1.1-3
- Switch to static builds, reducing system dependencies and making build more portable

* Mon Aug 29 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.1.1-2
- Update FIPS support to bring in latest changes
- * RH2048582: Support PKCS#12 keystores
- * RH2020290: Support TLS 1.3 in FIPS mode

* Sun Aug 21 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.1.1-1
- Update to jdk-17.0.4.1+1
- Update release notes to 17.0.4.1+1
- Add patch to provide translations for Europe/Kyiv added in tzdata2022b
- Add test to ensure timezones can be translated

* Mon Aug 15 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.0.8-2
- Update FIPS support to bring in latest changes
- * RH2104724: Avoid import/export of DH private keys
- * RH2092507: P11Key.getEncoded does not work for DH keys in FIPS mode
- * Build the systemconf library on all platforms

* Fri Jul 22 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.0.8-1
- Update to jdk-17.0.4.0+8
- Update release notes to 17.0.4.0+8
- Switch to GA mode for release
- Exclude x86 where java_arches is undefined, in order to unbreak build

* Fri Jul 22 2022 Jiri Vanek <gnu.andrew@redhat.com> - 1:17.0.4.0.7-0.3.ea
- moved to build only on %%{java_arches}
-- https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
- reverted :
-- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild (always mess up release)
-- Try to build on x86 again by creating a husk of a JDK which does not depend on itself
-- Exclude x86 from builds as the bootstrap JDK is now completely broken and unusable
-- Replaced binaries and .so files with bash-stubs on i686
- added ExclusiveArch:  %%{java_arches}
-- this now excludes i686
-- this is safely backport-able to older fedoras, as the macro was  backported proeprly (with i686 included)
- https://bugzilla.redhat.com/show_bug.cgi?id=2104128

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.0.4.0.7-0.2.ea.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.0.7-0.2.ea
- Try to build on x86 again by creating a husk of a JDK which does not depend on itself

* Sat Jul 16 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.0.7-0.1.ea
- Update to jdk-17.0.3.0+7
- Update release notes to 17.0.3.0+7
- Exclude x86 from builds as the bootstrap JDK is now completely broken and unusable
- Need to include the '.S' suffix in debuginfo checks after JDK-8284661

* Thu Jul 14 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.0.1-0.5.ea
- Explicitly require crypto-policies during build and runtime for system security properties

* Thu Jul 14 2022 Jiri Vanek <jvanek@redhat.com> - 1:17.0.4.0.1-0.4.ea
- Replaced binaries and .so files with bash-stubs on i686 in preparation of the removal on that architecture:
- https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs

* Thu Jul 14 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1:17.0.4.0.1-0.3.ea
- Add javaver- and origin-specific javadoc and javadoczip alternatives.

* Thu Jul 14 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.0.1-0.2.ea
- Make use of the vendor version string to store our version & release rather than an upstream release date
- Include a test in the RPM to check the build has the correct vendor information.

* Thu Jul 14 2022 Jayashree Huttanagoudar <jhuttana@redhat.com> - 1:17.0.4.0.1-0.2.ea
- Fix issue where CheckVendor.java test erroneously passes when it should fail.
- Add proper quoting so '&' is not treated as a special character by the shell.

* Mon Jul 11 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.4.0.1-0.1.ea
- Update to jdk-17.0.4.0+1
- Update release notes to 17.0.4.0+1
- Switch to EA mode for 17.0.4 pre-release builds.
- Drop JDK-8282004 patch which is now upstreamed under JDK-8282231
- Print release file during build, which should now include a correct SOURCE value from .src-rev
- Update tarball script with IcedTea GitHub URL and .src-rev generation
- Include script to generate bug list for release notes
- Update tzdata requirement to 2022a to match JDK-8283350
- Move EA designator check to prep so failures can be caught earlier
- Make EA designator check non-fatal while upstream is not maintaining it

* Thu Jul 07 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.7-7
- Fix whitespace in spec file

* Thu Jul 07 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.7-7
- Sequence spec file sections as they are run by rpmbuild (build, install then test)

* Tue Jul 05 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.7-7
- Turn on system security properties as part of the build's install section
- Move cacerts replacement to install section and retain original of this and tzdb.dat
- Run tests on the installed image, rather than the build image
- Introduce variables to refer to the static library installation directories
- Use relative symlinks so they work within the image
- Run debug symbols check during build stage, before the install strips them

* Fri Jul 01 2022 Stephan Bergmann <sbergman@redhat.com> - 1:17.0.3.0.7-6
- Fix flatpak builds by exempting them from bootstrap

* Thu Jun 30 2022 Francisco Ferrari Bihurriet <fferrari@redhat.com> - 1:17.0.3.0.7-5
- RH2007331: SecretKey generate/import operations don't add the CKA_SIGN attribute in FIPS mode

* Mon Jun 27 2022 Stephan Bergmann <sbergman@redhat.com> - 1:17.0.3.0.7-4
- Fix flatpak builds (catering for their uncompressed manual pages)

* Wed Jun 22 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.7-3
- Update FIPS support to bring in latest changes
- * RH2036462: sun.security.pkcs11.wrapper.PKCS11.getInstance breakage
- * RH2090378: Revert to disabling system security properties and FIPS mode support together
- Rebase RH1648249 nss.cfg patch so it applies after the FIPS patch
- Enable system security properties in the RPM (now disabled by default in the FIPS repo)
- Improve security properties test to check both enabled and disabled behaviour
- Run security properties test with property debugging on

* Sun Jun 12 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.7-2
- Rebase FIPS patches from fips-17u branch and simplify by using a single patch from that repository
- Rebase RH1648249 nss.cfg patch so it applies after the FIPS patch
- RH2023467: Enable FIPS keys export
- RH2094027: SunEC runtime permission for FIPS

* Sun Apr 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.7-1
- April 2022 security update to jdk 17.0.3+7
- Update release notes to 17.0.3.0+7
- Update README.md and generate_source_tarball.sh to match CentOS
- Switch to GA mode for release
- JDK-8283911 patch no longer needed now we're GA...

* Wed Apr 13 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.5-0.1.ea
- Update to jdk-17.0.3.0+5
- Update release notes to 17.0.3.0+5

* Fri Apr 08 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.3.0.1-0.1.ea
- Update to jdk-17.0.3.0+1
- Update release notes to 17.0.3.0+1
- Switch to EA mode for 17.0.3 pre-release builds.
- Add JDK-8283911 to fix bad DEFAULT_PROMOTED_VERSION_PRE value

* Wed Apr 06 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-9
- Enable AlgorithmParameters and AlgorithmParameterGenerator services in FIPS mode

* Wed Mar 30 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-8
- java-17-openjdk should depend on itself to build, not java-latest-openjdk which is now OpenJDK 18

* Wed Feb 23 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-8
- Detect NSS at runtime for FIPS detection
- Turn off build-time NSS linking and go back to an explicit Requires on NSS

* Tue Feb 08 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-7
- Reinstate JIT builds on x86_32.
- Add JDK-8282004 to fix missing CALL effects on x86_32.

* Mon Feb 07 2022 Severin Gehwolf <sgehwolf@redhat.com> - 1:17.0.2.0.8-6
- Re-enable gdb backtrace check.

* Mon Feb 07 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-5
- Introduce stapinstall variable to set SystemTap arch directory correctly (e.g. arm64 on aarch64)
- Need to support noarch for creating source RPMs for non-scratch builds.

* Fri Feb 04 2022 Jiri Vanek <jvanek@redhat.com> - 1:17.0.2.0.8-4
- moved to become system jdk

* Fri Feb 04 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-2
- Temporarily move x86 to use Zero in order to get a working build
- Replace -mstackrealign with -mincoming-stack-boundary=2 -mpreferred-stack-boundary=4 on x86_32 for stack alignment
- Support a HotSpot-only build so a freshly built libjvm.so can then be used in the bootstrap JDK.
- Explicitly list JIT architectures rather than relying on those with slowdebug builds
- Disable the serviceability agent on Zero architectures even when the architecture itself is supported

* Mon Jan 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-1.rolling
- January 2022 security update to jdk 17.0.2+8
- Extend LTS check to exclude EPEL.
- Rename libsvml.so to libjsvml.so following JDK-8276025
- Remove JDK-8276572 patch which is now upstream.
- Rebase RH1995150 & RH1996182 patches following JDK-8275863 addition to module-info.java

* Mon Jan 24 2022 Severin Gehwolf <sgehwolf@redhat.com> - 1:17.0.2.0.8-1.rolling
- Set LTS designator.

* Mon Jan 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-16.rolling
- Separate crypto policy initialisation from FIPS initialisation, now they are no longer interdependent

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.0.1.0.12-15.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-15.rolling
- Sync gdb test with java-1.8.0-openjdk and improve architecture restrictions.
- Disable on x86, x86_64, ppc64le & s390x while these are broken in rawhide.

* Thu Jan 13 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-14.rolling
- Fix FIPS issues in native code and with initialisation of java.security.Security

* Thu Dec 09 2021 Jiri Vanek <jvanek@redhat.com> - 1:17.0.1.0.12-13.rolling
- Storing and restoring alterntives during update manually
- Fixing Bug 2001567 - update of JDK/JRE is removing its manually selected alterantives and select (as auto) system JDK/JRE
-- The move of alternatives creation to posttrans to fix:
-- Bug 1200302 - dnf reinstall breaks alternatives
-- Had caused the alternatives to be removed, and then created again,
-- instead of being added, and then removing the old, and thus persisting
-- the selection in family
-- Thus this fix, is storing the family of manually selected master, and if
-- stored, then it is restoring the family of the master

* Thu Dec 09 2021 Jiri Vanek <jvanek@redhat.com> - 1:17.0.1.0.12-12.rolling
- Family extracted to globals

* Thu Dec 09 2021 Jiri Vanek <jvanek@redhat.com> - 1:17.0.1.0.12-11.rolling
- javadoc-zip got its own provides next to plain javadoc ones

* Thu Dec 09 2021 Jiri Vanek <jvanek@redhat.com> - 1:17.0.1.0.12-10.rolling
- replaced tabs by sets of spaces to make rpmlint happy

* Mon Nov 29 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-9.rolling
- Handle Fedora in distro conditionals that currently only pertain to RHEL.

* Thu Nov 18 2021 Jiri Vanek <jvanek@redhat.com> - 1:17.0.0.0.35-8
-- inital import
