# RPM conditionals so as to be able to dynamically produce
# slowdebug/release builds. See:
# http://rpm.org/user_doc/conditional_builds.html
#
# Examples:
#
# Produce release, fastdebug *and* slowdebug builds on x86_64 (default):
# $ rpmbuild -ba java-11-openjdk.spec
#
# Produce only release builds (no slowdebug builds) on x86_64:
# $ rpmbuild -ba java-11-openjdk.spec --without slowdebug --without fastdebug
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

# Workaround for stripping of debug symbols from static libraries
%if %{with staticlibs}
%define __brp_strip_static_archive %{nil}
%global include_staticlibs 1
%else
%global include_staticlibs 0
%endif

#placeholder - used in regexes, otherwise for no use in portables
%global freetype_lib |libfreetype[.]so.*

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
%global is_system_jdk 0

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
%global jit_arches      %{arm} %{aarch64} %{ix86} %{power64} s390x sparcv9 sparc64 x86_64 riscv64
# Set of architectures which use the Zero assembler port (!jit_arches)
%global zero_arches ppc s390
# Set of architectures which support SystemTap tapsets
%global systemtap_arches %{jit_arches}
# Set of architectures with a Ahead-Of-Time (AOT) compiler
%global aot_arches      x86_64 %{aarch64}
# Set of architectures which support the serviceability agent
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm}
# As of JDK-8005165 in OpenJDK 10, class sharing is not arch-specific
# However, it does segfault on the Zero assembler port, so currently JIT only
%global share_arches    %{jit_arches}
# Set of architectures for which we build the Shenandoah garbage collector
%global shenandoah_arches x86_64 %{aarch64}
# Set of architectures for which we build the Z garbage collector
%global zgc_arches x86_64
# Set of architectures for which alt-java has SSB mitigation
%global ssbd_arches x86_64
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

# VM variant being built
%ifarch %{zero_arches}
%global vm_variant zero
%else
%global vm_variant server
%endif

# debugedit tool for rewriting ELF file paths
%global debugedit %( if [ -f "%{_rpmconfigdir}/debugedit"  ]; then echo "%{_rpmconfigdir}/debugedit" ; else echo "/usr/bin/debugedit"; fi )

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
%ifarch riscv64
%global archinstall riscv64
%global stapinstall riscv64
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
%global featurever 11
%global interimver 0
%global updatever 24
%global patchver 0

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
%global oj_vendor_bug_url https://access.redhat.com/support/cases/
%else
%global oj_vendor_bug_url  https://bugzilla.redhat.com/enter_bug.cgi
%endif
%endif
%endif
%global oj_vendor_version (Red_Hat-%{version}-%{release})

# Define IcedTea version used for SystemTap tapsets and desktop file
%global icedteaver      6.0.0pre00-c848b93a8598
# Define JDK versions
%global newjavaver %{featurever}.%{interimver}.%{updatever}.%{patchver}
%global javaver         %{featurever}
# Strip up to 6 trailing zeros in newjavaver, as the JDK does, to get the correct version used in filenames
%global filever %(svn=%{newjavaver}; for i in 1 2 3 4 5 6 ; do svn=${svn%%.0} ; done; echo ${svn})
# The tag used to create the OpenJDK tarball
%global vcstag jdk-%{filever}+%{buildver}%{?tagsuffix:-%{tagsuffix}}

# Standard JPackage naming and versioning defines
%global origin          openjdk
%global origin_nice     OpenJDK
%global top_level_dir_name   %{vcstag}
%global top_level_dir_name_backup %{top_level_dir_name}-backup
%global buildver        8
%global rpmrelease      2
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

# Define milestone (EA for pre-releases, GA for releases)
# Release will be (where N is usually a number starting at 1):
# - 0.N%%{?extraver}%%{?dist} for EA releases,
# - N%%{?extraver}{?dist} for GA releases
%global is_ga           1
%if %{is_ga}
%global build_type GA
%global ea_designator ""
%global ea_designator_zip %{nil}
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

# we can copy the javadoc to not arched dir, or make it not noarch
%define uniquejavadocdir()    %{expand:%{fullversion}.%{_arch}%{?1}}
# main id and dir of this jdk
%define uniquesuffix()        %{expand:%{fullversion}.%{_arch}%{?1}}

#################################################################
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349
#         https://bugzilla.redhat.com/show_bug.cgi?id=1590796#c14
#         https://bugzilla.redhat.com/show_bug.cgi?id=1655938
%global _privatelibs libsplashscreen[.]so.*|libawt_xawt[.]so.*|libjli[.]so.*|libattach[.]so.*|libawt[.]so.*|libextnet[.]so.*|libawt_headless[.]so.*|libdt_socket[.]so.*|libfontmanager[.]so.*|libinstrument[.]so.*|libj2gss[.]so.*|libj2pcsc[.]so.*|libj2pkcs11[.]so.*|libjaas[.]so.*|libjavajpeg[.]so.*|libjdwp[.]so.*|libjimage[.]so.*|libjsound[.]so.*|liblcms[.]so.*|libmanagement[.]so.*|libmanagement_agent[.]so.*|libmanagement_ext[.]so.*|libmlib_image[.]so.*|libnet[.]so.*|libnio[.]so.*|libprefs[.]so.*|librmi[.]so.*|libsaproc[.]so.*|libsctp[.]so.*|libsunec[.]so.*|libsystemconf[.]so.*|libunpack[.]so.*|libzip[.]so.*%{freetype_lib}
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
%global generated_sources_name     generated_sources

%global rpm_state_dir %{_localstatedir}/lib/rpm-state/
%global repack_file repack.info

# For flatpack builds hard-code dependency paths,
# otherwise use relative paths.
%if 0%{?flatpak}
%global alternatives_requires /usr/sbin/alternatives
%global javazidir /usr/share/javazi-1.8
%global portablejvmdir /usr/lib/jvm
%else
%global alternatives_requires %{_sbindir}/alternatives
%global javazidir %{_datadir}/javazi-1.8
%global portablejvmdir %{_jvmdir}
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
  --slave %{_bindir}/jcmd jcmd %{sdkbindir -- %{?1}}/jcmd \\
  --slave %{_bindir}/jjs jjs %{jrebindir -- %{?1}}/jjs \\
  --slave %{_bindir}/keytool keytool %{jrebindir -- %{?1}}/keytool \\
  --slave %{_bindir}/pack200 pack200 %{jrebindir -- %{?1}}/pack200 \\
  --slave %{_bindir}/rmid rmid %{jrebindir -- %{?1}}/rmid \\
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir -- %{?1}}/rmiregistry \\
  --slave %{_bindir}/unpack200 unpack200 %{jrebindir -- %{?1}}/unpack200 \\
  --slave %{_mandir}/man1/java.1$ext java.1$ext \\
  %{_mandir}/man1/java-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/%{alt_java_name}.1$ext %{alt_java_name}.1$ext \\
  %{_mandir}/man1/%{alt_java_name}-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jjs.1$ext jjs.1$ext \\
  %{_mandir}/man1/jjs-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jcmd.1$ext jcmd.1$ext \\
  %{_mandir}/man1/jcmd-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/keytool.1$ext keytool.1$ext \\
  %{_mandir}/man1/keytool-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/pack200.1$ext pack200.1$ext \\
  %{_mandir}/man1/pack200-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/rmid.1$ext rmid.1$ext \\
  %{_mandir}/man1/rmid-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/rmiregistry.1$ext rmiregistry.1$ext \\
  %{_mandir}/man1/rmiregistry-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/unpack200.1$ext unpack200.1$ext \\
  %{_mandir}/man1/unpack200-%{uniquesuffix -- %{?1}}.1$ext

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
%ifarch %{aot_arches}
  --slave %{_bindir}/jaotc jaotc %{sdkbindir -- %{?1}}/jaotc \\
%endif
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
  --slave %{_bindir}/jconsole jconsole %{sdkbindir -- %{?1}}/jconsole \\
  --slave %{_bindir}/jdb jdb %{sdkbindir -- %{?1}}/jdb \\
  --slave %{_bindir}/jdeps jdeps %{sdkbindir -- %{?1}}/jdeps \\
  --slave %{_bindir}/jdeprscan jdeprscan %{sdkbindir -- %{?1}}/jdeprscan \\
  --slave %{_bindir}/jfr jfr %{sdkbindir -- %{?1}}/jfr \\
  --slave %{_bindir}/jimage jimage %{sdkbindir -- %{?1}}/jimage \\
  --slave %{_bindir}/jinfo jinfo %{sdkbindir -- %{?1}}/jinfo \\
  --slave %{_bindir}/jmap jmap %{sdkbindir -- %{?1}}/jmap \\
  --slave %{_bindir}/jps jps %{sdkbindir -- %{?1}}/jps \\
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir -- %{?1}}/jrunscript \\
  --slave %{_bindir}/jshell jshell %{sdkbindir -- %{?1}}/jshell \\
  --slave %{_bindir}/jstack jstack %{sdkbindir -- %{?1}}/jstack \\
  --slave %{_bindir}/jstat jstat %{sdkbindir -- %{?1}}/jstat \\
  --slave %{_bindir}/jstatd jstatd %{sdkbindir -- %{?1}}/jstatd \\
  --slave %{_bindir}/rmic rmic %{sdkbindir -- %{?1}}/rmic \\
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
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \\
  %{_mandir}/man1/jrunscript-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \\
  %{_mandir}/man1/jstack-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \\
  %{_mandir}/man1/jstat-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstatd.1$ext jstatd.1$ext \\
  %{_mandir}/man1/jstatd-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/rmic.1$ext rmic.1$ext \\
  %{_mandir}/man1/rmic-%{uniquesuffix -- %{?1}}.1$ext \\
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
%{_jvmdir}/%{sdkdir -- %{?1}}/NEWS
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%dir %{_jvmdir}/%{sdkdir -- %{?1}}
%{_jvmdir}/%{sdkdir -- %{?1}}/release
%{_jvmdir}/%{jrelnk -- %{?1}}
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/bin
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/java
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/%{alt_java_name}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jjs
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jcmd
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/keytool
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/pack200
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/rmid
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/rmiregistry
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/unpack200
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
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib/jli
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jli/libjli.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jvm.cfg
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libattach.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libextnet.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libjsig.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libawt_headless.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libdt_socket.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libfontmanager.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libfreetype.so
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
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsunec.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libsystemconf.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libunpack.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libverify.so
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/libzip.so
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr/default.jfc
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/jfr/profile.jfc
%{_mandir}/man1/java-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/%{alt_java_name}-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jcmd-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jjs-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/keytool-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/pack200-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/rmid-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/rmiregistry-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/unpack200-%{uniquesuffix -- %{?1}}.1*
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
%config(noreplace) %{etcjavadir -- %{?1}}/conf/management/management.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/net.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/sound.properties
%{_jvmdir}/%{sdkdir -- %{?1}}/conf
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/security
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_bindir}/java
%ghost %{_jvmdir}/jre
%ghost %{_bindir}/%{alt_java_name}
%ghost %{_bindir}/jcmd
# https://bugzilla.redhat.com/show_bug.cgi?id=1312019
%ghost %{_bindir}/jjs
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
%{_jvmdir}/%{sdkdir -- %{?1}}/%{repack_file}
}

%define files_devel() %{expand:
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/bin
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jar
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jarsigner
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javac
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javadoc
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/javap
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jconsole
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdb
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdeps
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jdeprscan
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jfr
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jimage
# Some architectures don't have the serviceability agent
%ifarch %{sa_arches}
%ifnarch %{zero_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jhsdb
%endif
%endif
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jinfo
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jlink
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jmap
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jmod
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jps
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jrunscript
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jshell
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstack
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstat
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jstatd
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/rmic
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/serialver
%ifarch %{aot_arches}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jaotc
%endif
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
%{_mandir}/man1/jrunscript-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jstack-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jstat-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/jstatd-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/rmic-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/serialver-%{uniquesuffix -- %{?1}}.1*
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
%ghost %{_bindir}/jaotc
%ghost %{_bindir}/jlink
%ghost %{_bindir}/jmod
%ghost %{_bindir}/jhsdb
%ghost %{_bindir}/jar
%ghost %{_bindir}/jarsigner
%ghost %{_bindir}/javadoc
%ghost %{_bindir}/javap
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
%ghost %{_bindir}/rmic
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
}

%define files_src() %{expand:
%license %{_jvmdir}/%{sdkdir -- %{?1}}/legal
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/src.zip
%{_jvmdir}/%{sdkdir -- %{?1}}/full_sources
%{_jvmdir}/%{sdkdir -- %{?1}}/%{generated_sources_name}
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
# 2022g required as of JDK-8297804
Requires: tzdata-java >= 2022g
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
Suggests: lksctp-tools%{?_isa}, pcsc-lite-devel%{?_isa}
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

%global portable_name %{name}-portable
# the version must match, but sometmes we need to more precise, so including release
%global portable_version %{version}-1

Name:    java-%{javaver}-%{origin}
Version: %{newjavaver}.%{buildver}
Release: %{?eaprefix}%{rpmrelease}%{?extraver}%{?dist}.1
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
# Automatically converted from old format: ASL 1.1 and ASL 2.0 and BSD and BSD with advertising and GPL+ and GPLv2 and GPLv2 with exceptions and IJG and LGPLv2+ and MIT and MPLv2.0 and Public Domain and W3C and zlib and ISC and FTL and RSA - review is highly recommended.
License:  Apache-1.1 AND Apache-2.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising AND GPL-1.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-GPLv2-with-exceptions AND IJG AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND MPL-2.0 AND LicenseRef-Callaway-Public-Domain AND W3C AND Zlib AND ISC AND FTL AND LicenseRef-RSA
URL:      http://openjdk.java.net/

# Use 'icedtea_sync.sh' to update the following
# They are based on code contained in the IcedTea project (6.x).
# Systemtap tapsets. Zipped up to keep it small.
Source8: tapsets-icedtea-%{icedteaver}.tar.xz

# Desktop files. Adapted from IcedTea
Source9: jconsole.desktop.in

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Ensure ECDSA is working
Source14: TestECDSA.java

# Verify system crypto (policy) can be disabled via a property
Source15: TestSecurityProperties.java

# Ensure vendor settings are correct
Source16: CheckVendor.java

# Ensure translations are available for new timezones
Source18: TestTranslations.java

BuildRequires: %{portable_name}-sources >= %{portable_version}
BuildRequires: %{portable_name}-misc >= %{portable_version}
BuildRequires: %{portable_name}-docs >= %{portable_version}

%if %{include_normal_build}
BuildRequires: %{portable_name}-unstripped >= %{portable_version}
%if %{include_staticlibs}
BuildRequires: %{portable_name}-static-libs >= %{portable_version}
%endif
%endif
%if %{include_fastdebug_build}
BuildRequires: %{portable_name}-devel-fastdebug >= %{portable_version}
%if %{include_staticlibs}
BuildRequires: %{portable_name}-static-libs-fastdebug >= %{portable_version}
%endif
%endif
%if %{include_debug_build}
BuildRequires: %{portable_name}-devel-slowdebug >= %{portable_version}
%if %{include_staticlibs}
BuildRequires: %{portable_name}-static-libs-slowdebug >= %{portable_version}
%endif
%endif

BuildRequires: desktop-file-utils
# elfutils only are OK for build without AOT
BuildRequires: elfutils-devel
BuildRequires: gdb
# Requirement for setting up nss.cfg and nss.fips.cfg
BuildRequires: nss-devel
# Requirement for system security property test
BuildRequires: crypto-policies
BuildRequires: pkgconfig
BuildRequires: zip
BuildRequires: unzip
BuildRequires: javapackages-filesystem
# ?
BuildRequires: tzdata-java >= 2022g

%if %{with_systemtap}
BuildRequires: systemtap-sdt-devel
%endif

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
The %{origin_nice} %{featurever} development tools.
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
Obsoletes: javadoc-zip-slowdebug < 1:11.0.3.7-4

%{java_javadoc_rpo -- %{nil} -zip}
%{java_javadoc_rpo -- %{nil} %{nil}}

%description javadoc-zip
The %{origin_nice} %{featurever} API documentation compressed in a single archive.
%endif

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

%setup -q -c -n %{uniquesuffix ""} -T
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 8 ] ; then
 echo "priority must be 8 digits in total, violated"
 exit 14
fi

tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable.sources.noarch.tar.xz
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable*.misc.%{_arch}.tar.xz
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable*.docs.%{_arch}.tar.xz

%if %{include_normal_build}
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable.unstripped.jdk.%{_arch}.tar.xz
%if %{include_staticlibs}
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable.static-libs.%{_arch}.tar.xz
%endif
%endif
%if %{include_fastdebug_build}
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable.fastdebug.jdk.%{_arch}.tar.xz
%if %{include_staticlibs}
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable.fastdebug.static-libs.%{_arch}.tar.xz
%endif
%endif
%if %{include_debug_build}
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable.slowdebug.jdk.%{_arch}.tar.xz
%if %{include_staticlibs}
tar -xf %{portablejvmdir}/%{compatiblename}*%{version}*portable.slowdebug.static-libs.%{_arch}.tar.xz
%endif
%endif

# print out info abot binaries used for repack. The version-less fallbacks are for development only, where can be cheated environment
echo "Those RPMs are just repacking portable tarballs extracted from portable RPMs" > %{repack_file}
echo "Usually this exact portable RPM can not be obtained via dnf install, but you can download it." >> %{repack_file}
echo "The exact info is at bottom." >> %{repack_file}
echo "All java- names and versions:" >> %{repack_file}
ls -l %{_jvmdir} >> %{repack_file}
rpm -qa | grep "java-" >> %{repack_file}
echo "Used %{compatiblename}.*portable:" >> %{repack_file}
ls -l %{_jvmdir} | grep "%{compatiblename}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used %{name}.*portable:" >> %{repack_file}
rpm -qa | grep "%{name}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used %{version}.*portable:" >> %{repack_file}
ls -l %{_jvmdir} | grep "%{version}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used portable.*%{version}:" >> %{repack_file}
rpm -qa | grep "portable.*%{version}" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Where this is %{fullversion}" >> %{repack_file}
portableNvr=`rpm -qa | grep %{name}-portable-misc-%{version} | sed "s/-misc-/-/" | sed "s/.%{_arch}.*//"`
if [ "x${portableNvr}" == x ] ; then
  portableNvr=`rpm -qa | grep %{name}-portable-misc- | sed "s/-misc-/-/" | sed "s/.%{_arch}.*//"`" #incorrect!"
fi
echo "Which repacked ${portableNvr}" >> %{repack_file}
echo "You can download the repacked portables from:" >> %{repack_file}
echo "https://koji.fedoraproject.org/koji/search?match=glob&type=build&terms=${portableNvr}" >> %{repack_file}
echo "`date`" >> %{repack_file}

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

%build
# we need to symlink sources to expected location, so debuginfo strip can locate debugsources
src_image=`ls -d %{compatiblename}*%{version}*portable.sources.noarch`
misc_image=`ls -d %{compatiblename}*%{version}*portable.misc.%{_arch}`
cp -rf $misc_image/%{generated_sources_name}/%{vcstag}/ $src_image # it would be nice to remove them once debugsources are generated:(
ln -s $src_image/%{vcstag} %{vcstag}
mkdir build
pushd build
  cp -r ../$misc_image/%{generated_sources_name}/jdk%{featurever}.build* .
popd
doc_image=`ls -d %{compatiblename}*%{version}*portable.docs.%{_arch}`
# in addition the builddir must match the builddir of the portables, including release
# be aware, even os may be different, especially with buildonce, repack everywhere
# so deducting it from installed deps
portablenvr=`echo ${misc_image} | sed "s/portable.*.misc.//"`
portablebuilddir=/builddir/build/BUILD
  # Fix build paths in ELF files so it looks like we built them
  for file in $(find `pwd` -type f | grep -v -e "$src_image" -e "$doc_image") ; do
      if file ${file} | grep -q 'ELF'; then
          %{debugedit} -b "${portablebuilddir}/${portablenvr}" -d "$(pwd)" -n "${file}"
      fi
  done

%install
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
      	#is already there from portables
        # Install nss.fips.cfg: NSS configuration for global FIPS mode (crypto-policies)
      	#is already there from portables

        # Turn on system security properties
        sed -i -e "s:^security.useSystemPropertiesFile=.*:security.useSystemPropertiesFile=true:" \
            ${imagepath}/conf/security/java.security

        # Use system-wide tzdata
        mv ${imagepath}/lib/tzdb.dat{,.upstream}
        ln -sv %{javazidir}/tzdb.dat ${imagepath}/lib/tzdb.dat

        # Rename OpenJDK cacerts database
        mv ${imagepath}/lib/security/cacerts{,.upstream}
        # Install cacerts symlink needed by some apps which hard-code the path
        ln -sv /etc/pki/java/cacerts ${imagepath}/lib/security

        # add alt-java man page
	#  alt-java man and bianry are here from portables. Or not?
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

for suffix in %{build_loop} ; do
  if [ "x$suffix" = "x" ] ; then
      debugbuild=""
  else
      # change -something to .something
      debugbuild=`echo $suffix  | sed "s/-/./g"`
  fi
  # Final setup on the untarred images
  # TODO revisit. jre may be complety useless to unpack and process,
  # as all the files are taken from JDK tarball ans put to packages manually.
  # jre tarball may be usefull for  checking integrity of jre and jre headless subpackages
  #for jdkjre in jdk jre ; do
  for jdkjre in jdk ; do
    buildoutputdir=`ls -d %{compatiblename}*portable${debugbuild}.${jdkjre}*`
    top_dir_abs_main_build_path=$(pwd)/${buildoutputdir}
    installjdk ${top_dir_abs_main_build_path}
    # Check debug symbols were built into the dynamic libraries
    if [ $jdkjre == jdk ] ; then
      #jdk only?
      debugcheckjdk ${top_dir_abs_main_build_path}
    fi
    # Print release information
    cat ${top_dir_abs_main_build_path}/release
  done
# build cycles
done # end of release / debug cycle loop

STRIP_KEEP_SYMTAB=libjvm*

for suffix in %{build_loop} ; do
  if [ "x$suffix" = "x" ] ; then
      debugbuild=""
  else
      # change -something to .something
      debugbuild=`echo $suffix  | sed "s/-/./g"`
  fi
  buildoutputdir=`ls -d %{compatiblename}*portable${debugbuild}.jdk*`
  top_dir_abs_main_build_path=$(pwd)/${buildoutputdir}
%if %{include_staticlibs}
  top_dir_abs_staticlibs_build_path=`ls -d $top_dir_abs_main_build_path/lib/static/*/glibc/`
%endif
  jdk_image=${top_dir_abs_main_build_path}
  src_image=`echo ${top_dir_abs_main_build_path} | sed "s/portable.*.%{_arch}/portable.sources.noarch/"`
  misc_image=`echo ${top_dir_abs_main_build_path} | sed "s/portable.*.%{_arch}/portable.misc.%{_arch}/"`
  docs_image=`echo ${top_dir_abs_main_build_path} | sed "s/portable.*.%{_arch}/portable.docs.%{_arch}/"`

# Install the jdk
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}

# Install icons
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
     ${src_image}/%{vcstag}/src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
     $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-%{origin}.png
done


cp -a ${jdk_image} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}
cp -a ${src_image} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/full_sources
# JDK11 specific, bianry file in sources
cp -a ${misc_image}/%{generated_sources_name} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}
cp %{repack_file} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/

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
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename $manpage .1)-%{uniquesuffix -- $suffix}.1
  done
  # Remove man pages from jdk image
  rm -rf $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/man

popd

# Install static libs artefacts
%if %{include_staticlibs}
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/%{static_libs_install_dir}
cp -a ${top_dir_abs_staticlibs_build_path}/*.a $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/%{static_libs_install_dir}
%endif

if ! echo $suffix | grep -q "debug" ; then
  # Install Javadoc documentation
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}
  built_doc_archive=$(basename $(ls ${docs_image}/jdk*docs.zip))
  cp -a ${docs_image}/${built_doc_archive} \
     $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}.zip
  pushd $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir -- $suffix}
    unzip ${docs_image}/${built_doc_archive} 
  popd
fi

# Install release notes
commondocdir=${RPM_BUILD_ROOT}%{_defaultdocdir}/%{uniquejavadocdir -- $suffix}
install -d -m 755 ${commondocdir}
cp -a ${top_dir_abs_main_build_path}/NEWS ${commondocdir}

# Install desktop files
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix -- $suffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

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

#TODO this is done also i portables and in install jdk. But hard to say where the operation will hapen at the end
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
$JAVA_HOME/bin/java -XX:+UseShenandoahGC -version
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
# set_speculation function exists in both cases, so check for prctl call
%ifarch %{ssbd_arches}
nm $JAVA_HOME/bin/%{alt_java_name} | grep prctl
%else
if ! nm $JAVA_HOME/bin/%{alt_java_name} | grep prctl ; then true ; else false; fi
%endif

# Check correct vendor values have been set
$JAVA_HOME/bin/javac -d . %{SOURCE16}
#TODO skipped vendor check. It now points to PORTABLE version of jdk.
#$JAVA_HOME/bin/java $(echo $(basename %{SOURCE16})|sed "s|\.java||") "%{oj_vendor}" "%{oj_vendor_url}" "%{oj_vendor_bug_url}" "%{oj_vendor_version}"

# Check translations are available for new timezones
$JAVA_HOME/bin/javac -d . %{SOURCE18}
#TODO doublecheck tzdata handling
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE18})|sed "s|\.java||") JRE || echo "TZDATA no longer can be synced with system, because we repack"
$JAVA_HOME/bin/java -Djava.locale.providers=CLDR $(echo $(basename %{SOURCE18})|sed "s|\.java||") CLDR || echo "TZDATA no longer can be synced with system, because we repack"

%if %{include_staticlibs}
# Check debug symbols in static libraries (smoke test)
export STATIC_LIBS_HOME=${JAVA_HOME}/%{static_libs_install_dir}
readelf --debug-dump $STATIC_LIBS_HOME/libnet.a | grep Inet4AddressImpl.c
readelf --debug-dump $STATIC_LIBS_HOME/libnet.a | grep Inet6AddressImpl.c
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
-- the returns from copy_jdk_configs.lua should not affect this 'main', so it shodl run under all circumstances, except fatal error
-- https://bugzilla.redhat.com/show_bug.cgi?id=1820172
-- https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
-- Define the path to directory being replaced below.
-- DO NOT add a trailing slash at the end.
path1 = "%{_jvmdir}/%{sdkdir -- %{nil}}/conf"
path2 = "%{_jvmdir}/%{sdkdir -- %{nil}}/lib/security"
array = {path1, path2}
for index, path in pairs(array) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end

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
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1:11.0.24.0.8-2.1
- convert license to SPDX

* Sat Jul 20 2024 Jiri Vanek <jvanek@redhat.com> - 1:11.0.24.0.8-1
- July CPU

* Wed May 01 2024 Jiri Vanek <jvanek@redhat.com> - 1:11.0.23.0.9-1
- added logic to print repacked info to repack.info
- April CPU

* Wed Feb 21 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 1:11.0.22.0.7-2
- Add riscv64 support

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1:11.0.22.0.7-1.1
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Jiri Vanek <jvanek@redhat.com> - 1:11.0.22.0.7-1
- updated to OpenJDK 11.0.22 (2024-01-16)
- removed removal of /test/jdk/sun/management/jmxremote/bootstrap/solaris-sparcv9/launcher
-- no longer here

* Sat Dec 16 2023 Jiri Vanek <jvanek@redhat.com> - 1:11.0.21.0.9-3
* using generated sources from portables for final debuginfo

* Sat Dec 09 2023 Jiri Vanek <jvanek@redhat.com> - 1:11.0.21.0.9-2
- proeprly filing debugsources pkg
  by addedd symlinks restructuring the structure for original build sources
- according to logs, some are still missing
  probably generated during the build, and thus not existing in prep,
  when the sources subpkg is created after patching

* Wed Nov 22 2023 Jiri Vanek <jvanek@redhat.com> -  1:11.0.21.0.9-1
- updated to OpenJDK 11.0.9 (2023-10-17)

* Fri Sep 29 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1:11.0.20.0.8-2
- Fix flatpak build by handling different installation prefixes of package dependencies

* Sun Aug 06 2023 Jiri Vanek <jvanek@redhat.com> - 1:11.0.20.0.8-1
- updated to july security update 11.0.20.0.2 

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.19.0.7-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 29 2023 Jiri Vanek <jvanek@redhat.com> - 1:11.0.19.0.7-1
- updated to 17.0.7.0.7 underlying portables
- requirign 17.0.7.0.7-2 due to news, and much more tuning
- now untarring enforced version
- repacked bits are now requested in exact version
- repacked portables
- using icons from source package
- providing full sources via src package
- requiring exact version.reelase of portables
- todo, lost alt java manpage.. probably already in portables
- TODO conslut this clean up - javdoc
- todo, debuginfo

* Thu Jan 26 2023 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.18.0.10-1
- Update to jdk-11.0.18+10 (GA)
- Update release notes to 11.0.18+10
- Switch to GA mode for release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.18.0.9-0.1.ea.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.18.0.9-0.1.ea
- Update to jdk-11.0.18+9
- Update release notes to 11.0.18+9
- Drop local copy of JDK-8293834 now this is upstream
- Require tzdata 2022g due to inclusion of JDK-8296108, JDK-8296715 & JDK-8297804
- Update TestTranslations.java to test the new America/Ciudad_Juarez zone

* Thu Dec 15 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.18.0.1-0.1.ea
- Update to jdk-11.0.18+1
- Update release notes to 11.0.18+1
- Switch to EA mode for 11.0.18 pre-release builds.
- Drop local copies of JDK-8294357 & JDK-8295173 now upstream contains tzdata 2022e

* Wed Oct 19 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.17.0.8-1
- Update to jdk-11.0.17+8 (GA)
- Update release notes to 11.0.17+8
- Switch to GA mode for release
- The stdc++lib, zlib & freetype options should always be set from the global, so they are not altered for staticlibs builds
- Remove freetype sources along with zlib sources

* Sat Oct 15 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.17.0.7-0.2.ea
- Update in-tree tzdata to 2022e with JDK-8294357 & JDK-8295173
- Update CLDR data with Europe/Kyiv (JDK-8293834)
- Drop JDK-8292223 patch which we found to be unnecessary
- Update TestTranslations.java to use public API based on TimeZoneNamesTest upstream

* Wed Oct 05 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.17.0.7-0.1.ea
- Update to jdk-11.0.17+7
- Update release notes to 11.0.17+7

* Tue Sep 06 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.17.0.1-0.1.ea
- Update to jdk-11.0.17+1
- Update release notes to 11.0.17+1
- Switch to EA mode for 11.0.17 pre-release builds.
- Bump HarfBuzz bundled version to 4.4.1 following JDK-8289853
- Bump FreeType bundled version to 2.12.1 following JDK-8290334

* Tue Aug 30 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.16.1.1-2
- Switch to static builds, reducing system dependencies and making build more portable

* Wed Aug 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.16.1.1-1
- Update to jdk-11.0.16.1+1
- Update release notes to 11.0.16.1+1
- Add patch to provide translations for Europe/Kyiv added in tzdata2022b
- Add test to ensure timezones can be translated

* Fri Jul 22 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.16.0.8-1
- Update to jdk-11.0.16+8
- Update release notes to 11.0.16+8
- Switch to GA mode for release
- Exclude x86 where java_arches is undefined, in order to unbreak build

* Fri Jul 22 2022 Jiri Vanek <gnu.andrew@redhat.com> - 1:11.0.16.0.7-0.4.ea
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
- https://bugzilla.redhat.com/show_bug.cgi?id=2104126

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.16.0.7-0.3.ea.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.16.0.7-0.3.ea
- Try to build on x86 again by creating a husk of a JDK which does not depend on itself

* Sun Jul 17 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.16.0.7-0.2.ea
- Exclude x86 from builds as the bootstrap JDK is now completely broken and unusable

* Thu Jul 14 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.16.0.7-0.1.ea
- Update to jdk-11.0.16+7
- Update release notes to 11.0.16+7
- Switch to EA mode for 11.0.16 pre-release builds.
- Use same tarball naming style as java-17-openjdk and java-latest-openjdk
- Drop JDK-8282004 patch which is now upstreamed under JDK-8282231
- Drop JDK-8257794 patch now upstreamed
- Print release file during build, which should now include a correct SOURCE value from .src-rev
- Update tarball script with IcedTea GitHub URL and .src-rev generation
- Use "git apply" with patches in the tarball script to allow binary diffs
- Include script to generate bug list for release notes
- Update tzdata requirement to 2022a to match JDK-8283350

* Thu Jul 14 2022 Jiri Vanek <jvanek@redhat.com> - 1:11.0.16.0.7-0.1.ea
- Add additional patch during tarball generation to align tests with ECC changes

* Thu Jul 14 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.15.0.10-7
- Explicitly require crypto-policies during build and runtime for system security properties

* Thu Jul 14 2022 Jiri Vanek <jvanek@redhat.com> - 1:11.0.15.0.10-6
- Replaced binaries and .so files with bash-stubs on i686 in preparation of the removal on that architecture:
- https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs

* Thu Jul 14 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1:11.0.15.0.10-5
- Add javaver- and origin-specific javadoc and javadoczip alternatives.

* Thu Jul 14 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.15.0.10-4
- Make use of the vendor version string to store our version & release rather than an upstream release date

* Thu Jul 07 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.15.0.10-3
- Rebase FIPS patches from fips branch and simplify by using a single patch from that repository
- * RH2036462: sun.security.pkcs11.wrapper.PKCS11.getInstance breakage
- * RH2090378: Revert to disabling system security properties and FIPS mode support together
- Rebase RH1648249 nss.cfg patch so it applies after the FIPS patch
- Enable system security properties in the RPM (now disabled by default in the FIPS repo)
- Improve security properties test to check both enabled and disabled behaviour
- Run security properties test with property debugging on

* Thu Jun 30 2022 Francisco Ferrari Bihurriet <fferrari@redhat.com> - 1:11.0.15.0.10-2
- RH2007331: SecretKey generate/import operations don't add the CKA_SIGN attribute in FIPS mode

* Sun Apr 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.15.0.10-1
- Update to jdk-11.0.15.0+10
- Update release notes to 11.0.15.0+10
- Switch to GA mode for release

* Tue Apr 12 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.15.0.8-0.1.ea
- Update to jdk-11.0.15.0+8
- Update release notes to 11.0.15.0+8
- Rebase RH1996182 FIPS patch after JDK-8254410

* Tue Apr 12 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.15.0.1-0.1.ea
- Update to jdk-11.0.15.0+1
- Update release notes to 11.0.15.0+1
- Switch to EA mode for 11.0.15 pre-release builds.

* Tue Apr 12 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.1.1-7
- Detect NSS at runtime for FIPS detection
- Turn off build-time NSS linking and go back to an explicit Requires on NSS

* Fri Apr 08 2022 Stephan Bergmann <sbergman@redhat.com> - 1:11.0.14.1.1-6
- Fix flatpak builds by exempting them from bootstrap

* Thu Feb 17 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.1.1-5
- Sync cleanups from release branch.

* Wed Feb 16 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.1.1-4
- Reinstate JIT builds on x86_32.
- Add JDK-8282004 to fix missing CALL effects on x86_32.

* Wed Feb 16 2022 Jiri Vanek <jvanekredhat.com> - 1:11.0.14.1.1-3
- Bump release for no apparent reason.

* Mon Feb 14 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.1.1-2
- Require tzdata 2021e as of JDK-8275766.

* Fri Feb 11 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.1.1-1
- Update to jdk-11.0.14.1+1
- Update release notes to 11.0.14.1+1

* Wed Feb 09 2022 Jiri Vanek <jvanek@redhat.com> - 1:11.0.14.0.9-9
- Storing and restoring alterntives during update manually
- Fixing Bug 2001567 - update of JDK/JRE is removing its manually selected alterantives and select (as auto) system JDK/JRE
-- The move of alternatives creation to posttrans to fix:
-- Bug 1200302 - dnf reinstall breaks alternatives
-- Had caused the alternatives to be removed, and then created again,
-- instead of being added, and then removing the old, and thus persisting
-- the selection in family
-- Thus this fix, is storing the family of manually selected master, and if
-- stored, then it is restoring the family of the master

* Wed Feb 09 2022 Jiri Vanek <jvanek@redhat.com> - 1:11.0.14.0.9-8
- Family extracted to globals

* Wed Feb 09 2022 Jiri Vanek <jvanek@redhat.com> - 1:11.0.14.0.9-7
- javadoc-zip got its own provides next to plain javadoc ones

* Mon Feb 07 2022 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.14.0.9-6
- Re-enable gdb backtrace check.

* Thu Feb 03 2022 Jiri Vanek <jvanek@redhat.com> - 1:11.0.14.0.9-5
- moved to stop being system jdk

* Wed Feb 02 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.9-3
- Temporarily move x86 to use Zero in order to get a working build
- Replace -mstackrealign with -mincoming-stack-boundary=2 -mpreferred-stack-boundary=4 on x86_32 for stack alignment
- Refactor build functions so we can build just HotSpot without any attempt at installation.
- Explicitly list JIT architectures rather than relying on those with slowdebug builds
- Disable the serviceability agent on Zero architectures even when the architecture itself is supported
- Add backport of JDK-8257794 to fix bogus assert on slowdebug x86-32 Zero builds

* Mon Jan 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.9-2
- Separate crypto policy initialisation from FIPS initialisation, now they are no longer interdependent

* Mon Jan 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.9-1
- Update to jdk-11.0.14.0+9
- Update release notes to 11.0.14.0+9
- Switch to GA mode for final release.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.14.0.8-0.3.ea.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.8-0.3.ea
- Improve architecture restrictions for the gdb test.
- Disable only on x86, x86_64, ppc64le & s390x while these are broken in rawhide.

* Tue Jan 18 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.8-0.2.ea
- Fix FIPS issues in native code and with initialisation of java.security.Security

* Mon Jan 17 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.8-0.1.ea
- Sync gdb test with java-1.8.0-openjdk and disable for now until gdb is fixed.

* Fri Jan 14 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.8-0.1.ea
- Update to jdk-11.0.14.0+8
- Update release notes to 11.0.14.0+8

* Mon Dec 13 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.14.0.1-0.1.ea
- Update to jdk-11.0.14.0+1
- Update release notes to 11.0.14.0+1
- Switch to EA mode for 11.0.14 pre-release builds.
- Rename blacklisted.certs to blocked.certs following JDK-8253866
- Rebase RH1996182 login patch and drop redundant security policy extension after JDK-8269034

* Mon Nov 08 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.13.0.8-4
- Turn off bootstrapping for slow debug builds, which are particularly slow on ppc64le.

* Wed Nov 03 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.13.0.8-3
- Use 'sql:' prefix in nss.fips.cfg as F35+ no longer ship the legacy
  secmod.db file as part of nss

* Wed Oct 13 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.13.0.8-2
- Reduce disk footprint by removing build artifacts by default.

* Wed Oct 13 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.13.0.8-1
- Update to jdk-11.0.12.0+8
- Update release notes to 11.0.12.0+8
- Switch to GA mode for final release.

* Tue Oct 12 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.13.0.7-0.1.ea
- Update to jdk-11.0.13.0+7
- Update release notes to 11.0.13.0+7

* Mon Oct 11 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.13.0.1-0.1.ea
- Update to jdk-11.0.13.0+1
- Update release notes to 11.0.13.0+1
- Update tarball generation script to use git following OpenJDK 11u's move to github
- Switch to EA mode for 11.0.13 pre-release builds.
- Remove "-clean" suffix as no 11.0.13 builds are unclean.
- Drop JDK-8269668 patch which is now applied upstream.

* Tue Oct 05 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.7-9
- Allow plain key import to be disabled with -Dcom.redhat.fips.plainKeySupport=false

* Tue Oct 05 2021 Martin Balao <mbalao@redhat.com> - 1:11.0.12.0.7-9
- Add patch to allow plain key import.

* Sun Oct 03 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.7-8
- Restructure the build so a minimal initial build is then used for the final build (with docs)
- This reduces pressure on the system JDK and ensures the JDK being built can do a full build

* Sun Sep 05 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.7-7
- Add patch to login to the NSS software token when in FIPS mode.
- Extend the default security policy to accomodate PKCS11 accessing jdk.internal.misc.

* Thu Sep 02 2021 Jiri Vanek <jvanek@redhat.com> - 1:11.0.12.0.7-6
- added posttrans hook which persist sanity of dir->symlink change in case of udpate from ancient versions

* Thu Sep 02 2021 Jiri Vanek <jvanek@redhat.com> - 1:11.0.12.0.7-5
- minor cosmetic improvements to make spec more comparable between variants

* Tue Aug 31 2021 Jiri Vanek <jvanek@redhat.com> - 1:11.0.12.0.7-3
- alternatives creation moved to posttrans
- Thus fixing the old reisntall issue:
- https://bugzilla.redhat.com/show_bug.cgi?id=1200302
- https://bugzilla.redhat.com/show_bug.cgi?id=1976053

* Mon Aug 09 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.7-2
- Remove non-Free test from source tarball.

* Wed Jul 28 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.12.0.7-1
- Add patch in order to fix java.library.path issue on aarch64 (JDK-8269668)
- Resolves: rhbz#1977671

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.12.0.7-0.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.7-0
- Update to jdk-11.0.12.0+7
- Update release notes to 11.0.12.0+7
- Switch to GA mode for final release.

* Thu Jul 08 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.6-0.0.ea
- Update to jdk-11.0.12.0+6
- Update release notes to 11.0.12.0+6
- Skip 11.0.12.0+5 as 11.0.12.0+6 only adds a test change

* Thu Jul 08 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.4-0.0.ea
- Update to jdk-11.0.12.0+4
- Update release notes to 11.0.12.0+4
- Correct bug ID JDK-8264846 to intended ID of JDK-8264848

* Mon Jul 05 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.3-0.0.ea
- Update to jdk-11.0.12.0+3
- Update release notes to 11.0.12.0+3

* Fri Jul 02 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.2-0.1.ea
- Use the "reverse" build loop (debug first) as the main and only build loop to get more diagnostics.
- Remove restriction on disabling product build, as debug packages no longer have javadoc packages.

* Fri Jul 02 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.2-0.0.ea
- Update to jdk-11.0.12.0+2
- Update release notes to 11.0.12.0+2

* Mon Jun 28 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.12.0.1-0.0.ea
- Update to jdk-11.0.12.0+1
- Update release notes to 11.0.12.0+1
- Switch to EA mode for 11.0.12 pre-release builds.
- Update ECC patch following JDK-8226374 (bug ID yet to be confirmed)

* Tue Jun 08 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.9-5
- Minor code cleanups on FIPS detection patch and check for SECMOD_GetSystemFIPSEnabled in configure.
- Remove unneeded Requires on NSS as it will now be dynamically linked and detected by RPM.

* Tue Jun 08 2021 Martin Balao <mbalao@redhat.com> - 1:11.0.11.0.9-5
- Detect FIPS using SECMOD_GetSystemFIPSEnabled in the new libsystemconf JDK library.

* Wed Jun 02 2021 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.9-4
- Update RH1655466 FIPS patch with changes in OpenJDK 8 version.
- SunPKCS11 runtime provider name is a concatenation of "SunPKCS11-" and the name in the config file.
- Change nss.fips.cfg config name to "NSS-FIPS" to avoid confusion with nss.cfg.
- No need to substitute path to nss.fips.cfg as java.security file supports a java.home variable.
- Disable FIPS mode support unless com.redhat.fips is set to "true".
- Enable alignment with FIPS crypto policy by default (-Dcom.redhat.fips=false to disable).
- Add explicit runtime dependency on NSS for the PKCS11 provider in FIPS mode
- Move setup of JavaSecuritySystemConfiguratorAccess to Security class so it always occurs (RH1915071)
- Resolves: rhbz#1830090

* Wed Jun 02 2021 Martin Balao <mbalao@redhat.com> - 1:11.0.11.0.9-4
- Support the FIPS mode crypto policy (RH1655466)
- Use appropriate keystore types when in FIPS mode (RH1818909)
- Disable TLSv1.3 when the FIPS crypto policy and the NSS-FIPS provider are in use (RH1860986)
- Resolves: rhbz#1830090

* Fri May 07 2021 Jiri Vanek <jvanek@redhat.com> - 1:11.0.11.0.9-3
- removed cjc backward comaptiblity, to fix when both rpm 4.16 and 4.17 are in transaction

* Fri Apr 30 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.11.0.9-2
- Remove -fcommon work-around as the OpenJDK 11
  code has been fixed.

* Fri Apr 30 2021 Jiri Vanek <jvanek@redhat.com> - 1:11.0.11.0.9-1
- adapted to newst cjc to fix issue with rpm 4.17

* Wed Apr 21 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.9-0
- Update to jdk-11.0.11.0+9
- Update release notes to 11.0.11.0+9
- Switch to GA mode for final release.
- Require tzdata 2021a to match upstream change JDK-8260356

* Tue Apr 20 2021 Stephan Bergmann <sbergman@redhat.com> - 1:11.0.11.0.7-1.0.ea
- Disable copy-jdk-configs for Flatpak builds

* Sun Apr 11 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.7-0.0.ea
- Update to jdk-11.0.11.0+7
- Update release notes to 11.0.11.0+7

* Fri Apr 09 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.6-0.0.ea
- Update to jdk-11.0.11.0+6
- Update release notes to 11.0.11.0+6

* Tue Apr 06 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.5-0.0.ea
- Update to jdk-11.0.11.0+5
- Update release notes to 11.0.11.0+5

* Mon Mar 29 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.4-0.1.ea
- Update tapsets from IcedTea 6.x repository with fix for JDK-8015774 changes (_heap->_heaps)
- Update icedtea_sync.sh with a VCS mode that retrieves sources from a Mercurial repository

* Mon Mar 29 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.4-0.0.ea
- Update to jdk-11.0.11.0+4
- Update release notes to 11.0.11.0+4

* Sun Mar 28 2021 Jayashree Huttanagoudar <jhuttana@redhat.com> - 1:11.0.11.0.3-0.1.ea
- Fix issue where CheckVendor.java test erroneously passes when it should fail.
- Add proper quoting so '&' is not treated as a special character by the shell.

* Mon Mar 08 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.3-0.0.ea
- Update to jdk-11.0.11.0+3
- Update release notes to 11.0.11.0+3
- Remove upstreamed patch JDK-8259949

* Tue Mar 02 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.2-0.0.ea
- Update to jdk-11.0.11.0+2
- Update release notes to 11.0.11.0+2

* Sun Feb 21 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.11.0.1-0.0.ea
- Update to jdk-11.0.11.0+1
- Update release notes to 11.0.11.0+1
- Switch to EA mode for 11.0.11 pre-release builds.
- Require tzdata 2020f to match upstream change JDK-8259048

* Fri Feb 19 2021 Stephan Bergmann <sbergman@redhat.com> - 1:11.0.10.0.9-2
- Hardcode /usr/sbin/alternatives for Flatpak builds

* Fri Feb 12 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.9-1
- Perform static library build on a separate source tree with bundled image libraries
- Make static library build optional
- Based on initial work by Severin Gehwolf

* Mon Feb  1 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.9-0
- Update to jdk-11.0.10.0+9
- Update release notes to 11.0.10.0+9
- Switch to GA mode for final release.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.10.0.8-0.5.ea.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.5.ea
- Fix location and comment differences from RHEL.

* Mon Jan 25 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.5.ea
- Following JDK-8005165, class data sharing can be enabled on all JIT architectures

* Sun Jan 24 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.4.ea
- Include a test in the RPM to check the build has the correct vendor information.

* Sun Jan 24 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.4.ea
- Update build documentation to reflect this is java-11-openjdk, not java-1.8.0-openjdk
- Remove redundant closure and immediate reopening of include_normal_build block.

* Sun Jan 24 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.3.ea
- Use RSA as default for keytool, as DSA is disabled in all crypto policies except LEGACY
- Adjust RH1842572 patch due to context change from JDK-8213400

* Sat Jan 23 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.2.ea
- Need to support noarch for creating source RPMs for non-scratch builds.

* Mon Jan 18 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.2.ea
- Introduce stapinstall variable to set SystemTap arch directory correctly (e.g. arm64 on aarch64)

* Mon Jan 18 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.1.ea
- Use -march=i686 for x86 builds if -fcf-protection is detected (needs CMOV)

* Thu Jan 14 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.8-0.0.ea
- Update to jdk-11.0.10.0+8
- Update release notes to 11.0.10.0+8.
- Update tarball generation script to use PR3818 which handles JDK-8171279 changes
- Drop JDK-8250861 as applied upstream.

* Tue Dec 22 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.10.0.1-0.0.ea
- Update to jdk-11.0.10.0+1
- Update release notes to 11.0.10.0+1
- Use JEP-322 Time-Based Versioning so we can handle a future 11.0.9.1-like release correctly.
- Still use 11.0.x rather than 11.0.x.0 for file naming, as the trailing zero is omitted from tags.
- Revert configure and built_doc_archive hacks to build 11.0.9.1 from 11.0.9.0 sources, and synced with RHEL version.
- Cleanup debug package descriptions and version number placement.
- Switch to EA mode for 11.0.10 pre-release builds.
- Drop JDK-8222286 & JDK-8254177 as applied upstream
- Use system harfbuzz now this is supported.

* Tue Dec 22 2020 Jiri Vanek <jvanek@redhat.com> - 1:11.0.9.11-9
- fixed missing condition for fastdebug packages being counted as debug ones

* Sat Dec 19 2020 Jiri Vanek <jvanek@redhat.com> - 1:11.0.9.11-8
- removed lib-style provides for fastdebug_suffix_unquoted

* Thu Dec 17 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.11-6
- introduced nm based check to verify alt-java on x86_64 is patched, and no other alt-java or java is patched
- patch600 rh1750419-redhat_alt_java.patch amended to die, if it is used wrongly
- introduced ssbd_arches with currently only valid arch of x86_64 to separate real alt-java architectures

* Tue Dec 01 2020 Jiri Vanek <jvanek@redhat.com> - 1:11.0.9.11-5
- removed patch6, rh1566890-CVE_2018_3639-speculative_store_bypass.patch, surpassed by new patch
- added patch600, rh1750419-redhat_alt_java.patch, suprassing removed patch
- no longer copying of java->alt-java as it is created by  patch600

* Mon Nov 23 2020 Jiri Vanek <jvanek@redhat.com> - 1:11.0.9.11-4
- Create a copy of java as alt-java with alternatives and man pages
- java-11-openjdk doesn't have a JRE tree, so don't try and copy alt-java there...

* Fri Nov 06 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.11-3
- Update release notes for 11.0.9.1 release.

* Wed Nov 04 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.9.11-2
- Update to jdk-11.0.9.1+1
- RPM version stays at 11.0.9.11-2 so as to not break upgrade path.
- Adds a single patch for JDK-8250861.

* Thu Oct 29 2020 Jiri Vanek <jvanek@redhat.com> - 1:11.0.9.11-1
- Move all license files to NVR-specific JVM directory.
- This bad placement was killing parallel installability and thus having a bad impact on leapp, if used.

* Mon Oct 19 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.9.11-0
- Fix directory ownership of static-libs package

* Thu Oct 15 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.11-0
- Update to jdk-11.0.9+11
- Update release notes for 11.0.9 release.
- Add backport of JDK-8254177 to update to tzdata 2020b
- Require tzdata 2020b due to resource changes in JDK-8254177

* Mon Oct 05 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.10-0.0.ea
- Update to jdk-11.0.9+10 (EA)

* Mon Oct 05 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.9-0.0.ea
- Update to jdk-11.0.9+9 (EA)

* Thu Oct 01 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.8-0.0.ea
- Update to jdk-11.0.9+8 (EA)

* Mon Sep 28 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.7-0.0.ea
- Update to jdk-11.0.9+7 (EA)

* Tue Sep 15 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.9.6-0.1.ea
- Update static-libs packaging to new layout

* Tue Sep 15 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.6-0.0.ea
- Update to jdk-11.0.9+6 (EA)
- Update tarball generation script to use PR3802, handling JDK-8233228 & JDK-8177334
- Resolves: rhbz#1869017

* Tue Sep 08 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.5-0.0.ea
- Update to jdk-11.0.9+5 (EA)

* Thu Sep 03 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.4-0.0.ea
- Update to jdk-11.0.9+4 (EA)

* Wed Aug 19 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.3-0.0.ea
- Update to jdk-11.0.9+3 (EA)

* Tue Aug 11 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.2-0.0.ea
- Update to jdk-11.0.9+2 (EA)
- With Shenandoah now upstream in OpenJDK 11, we can use jdk-updates/jdk11 directly

* Tue Aug 11 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.1-0.2.ea
- Cleanup architecture and JVM feature handling in preparation for using upstreamed Shenandoah.

* Sun Aug 09 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.9.1-0.1.ea
- Update to shenandoah-jdk-11.0.9+1 (EA)
- Switch to EA mode for 11.0.9 pre-release builds.
- Drop JDK-8247874 backport now applied upstream.
- JDK-8245832 increases the set of static libraries, so try and include them all with a wildcard.

* Tue Jul 28 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.8.10-1
- Disable LTO as this breaks the build. See RHBZ#1861401.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.8.10-0.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.10-0
- Update to shenandoah-jdk-11.0.8+10 (GA)
- Switch to GA mode for final release.
- Update release notes with last minute fix (JDK-8248505).

* Fri Jul 10 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.9-0.0.ea
- Update to shenandoah-jdk-11.0.8+9 (EA)
- Update release notes for 11.0.8 release.

* Thu Jul 09 2020 Jiri Vanek <jvanek@redhat.com> - 1:11.0.8.8-0.2.ea
- bumped to become system jdk, is_system_jdk moved from 0 to 1

* Thu Jul 09 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.8-0.1.ea
- Re-introduce java-openjdk-src & java-openjdk-demo for system_jdk builds.
- Fix accidental renaming of java-openjdk-devel to java-devel-openjdk.

* Tue Jun 30 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.8-0.0.ea
- Update to shenandoah-jdk-11.0.8+8 (EA)

* Tue Jun 23 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.7-0.0.ea
- Update to shenandoah-jdk-11.0.8+7 (EA)

* Tue Jun 23 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.6-0.0.ea
- Update to shenandoah-jdk-11.0.8+6 (EA)

* Tue Jun 23 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.5-0.3.ea
- Add release notes.
- Amend release notes, removing issue actually fixed in 11.0.6.

* Tue Jun 23 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.5-0.2.ea
- Sync JDK-8247874 patch with upstream status in 11.0.9.
- Add missing ChangeLog entry from last series of commits.

* Mon Jun 22 2020 Jayashree Huttanagoudar <jhuttana@redhat.com> - 1:1.0.8.5-0.2.ea
- Added a patch jdk8247874-fix_ampersand_in_vm_bug_url.patch

* Thu Jun 18 2020 Jayashree Huttanagoudar <jhuttana@redhat.com> - 1:1.0.8.5-0.2.ea
- Moved vendor_version_string to better place

* Thu Jun 18 2020 Jiri Vanek <jvanek@redhat.com> - 1:11.0.8.5-0.2.ea
- set vendor property and vendor urls
- made urls to be preconfigured by os

* Tue Jun 09 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.8.5-0.1.ea
- Disable stripping of debug symbols for static libraries part of
  the -static-libs sub-package.

* Sun Jun 07 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.5-0.0.ea
- Update to shenandoah-jdk-11.0.8+5 (EA)

* Mon May 25 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.4-0.0.ea
- Update to shenandoah-jdk-11.0.8+4 (EA)
- Require tzdata 2020a due to resource changes in JDK-8243541

* Fri May 22 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.8.3-0.1.ea
- Build static-libs-image and add resulting files via -static-libs
  sub-package.

* Tue May 19 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.3-0.0.ea
- Update to shenandoah-jdk-11.0.8+3 (EA)
- Drop JDK-8233880 backport now applied upstream.

* Mon May 18 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.2-0.0.ea
- Update to shenandoah-jdk-11.0.8+2 (EA)

* Mon May 18 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.8.1-0.0.ea
- Update to shenandoah-jdk-11.0.8+1 (EA)
- Switch to EA mode for 11.0.8 pre-release builds.
- Drop JDK-8237396 & JDK-8228407 backports now applied upstream.

* Sun May 17 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.10-2
- Backport JDK-8233880 to fix version detection of GCC 10.
- Remove explicit compiler flags which should be handled by the upstream build
  (-std=gnu++98, -fno-delete-null-pointer-checks, -fno-lifetime-dse)

* Fri Apr 24 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.10-1
- Make use of --with-extra-asflags introduced in jdk-11.0.6+1.

* Wed Apr 22 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.10-0
- Update to shenandoah-jdk-11.0.7+10 (GA)
- Switch to GA mode for final release.
- Remove JDK-8237879 backport as this was integrated upstream in jdk-11.0.7+10.

* Tue Apr 21 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.9-0.0.ea
- Update to shenandoah-jdk-11.0.7+9 (EA)
- Remove JDK-8241296 backport as this was integrated upstream in jdk-11.0.7+9.

* Tue Apr 21 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.8-0.0.ea
- Update to shenandoah-jdk-11.0.7+8 (EA)

* Mon Apr 20 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.7-0.0.ea
- Update to shenandoah-jdk-11.0.7+7 (EA)

* Mon Apr 20 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.6-0.0.ea
- Update to shenandoah-jdk-11.0.7+6 (EA)

* Sun Apr 19 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.5-0.0.ea
- Update to shenandoah-jdk-11.0.7+5 (EA)

* Sun Apr 19 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.4-0.0.ea
- Update to shenandoah-jdk-11.0.7+4 (EA)

* Thu Apr 16 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.3-0.0.ea
- Add JDK-8228407 backport to resolve crashes during verification.

* Thu Apr 16 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.3-0.0.ea
- Update to shenandoah-jdk-11.0.7+3 (EA)

* Mon Apr 06 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.2-0.5.ea
- Sync SystemTap & desktop files with upstream IcedTea release 3.15.0 using new script

* Sat Mar 28 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.2-0.4.ea
- Add JDK-8237396 backport to resolve Shenandoah TCK breakage in traversal mode.

* Tue Mar 24 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.7.2-0.3.ea
- Revert GCC 10 workaround for s390x.
- Resolves RHBZ#1799087.

* Fri Mar 20 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.2-0.2.ea
- Backport JDK-8241296 to fix segfaults when active_handles is NULL (RH1813550)

* Fri Mar 13 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.7.2-0.1.ea
- Add patch for make 4.3 (JDK-8237879)

* Wed Mar 04 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.7.2-0.0.ea
- Update to shenandoah-jdk-11.0.7+2 (EA)
- Drop JDK-8224851 backport now included upstream.

* Thu Feb 27 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.7.1-0.0.ea
- Update to shenandoah-jdk-11.0.7+1 (EA)
- Switch to EA mode for 11.0.7 pre-release builds.
- Drop JDK-8236039 backport now applied upstream.

* Thu Feb 27 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.6.10-0
- Add workaround for building with GCC 10 on s390x. See RHBZ#1799087

* Wed Jan 29 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.6.10-0
- Account for building with GCC 10: JDK-8224851, -fcommon switch.

* Wed Jan 29 2020 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.6.10-0
- Update to shenandoah-jdk-11.0.6+10 (GA)
- Add JDK-8236039 backport to resolve OpenShift blocker.
- Add JDK-8224851 backport to resolve AArch64 compiler issues.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.6.9-0.1.ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.6.9-0.0.ea
- Update to shenandoah-jdk-11.0.6+9 (EA)

* Mon Dec 30 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.6.2-0.0.ea
- Update to shenandoah-jdk-11.0.6+2 (EA)

* Thu Dec 19 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.6.1-0.0.ea
- Update to shenandoah-jdk-11.0.6+1 (EA)
- Switch to EA mode for 11.0.6 pre-release builds.
- Add support for jfr binary.

* Wed Oct 09 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.5.10-0
- Update to shenandoah-jdk-11.0.5+10 (GA)
- Switch to GA mode for final release.

* Mon Oct 07 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.5.9-0.0.ea
- Update to shenandoah-jdk-11.0.5+9 (EA)

* Tue Aug 27 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.5.2-0.2.ea
- Update generate_source_tarball.sh script to use the PR3751 patch and retain the secp256k1 curve.
- Regenerate source tarball using the updated script and add the -'4curve' suffix.
- PR3751 includes the changes in the PR1834/RH1022017 patch which is removed.

* Sat Aug 24 2019 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.5.2-0.1.ea
- Update to shenandoah-jdk-11.0.5+2 (EA)

* Mon Aug 12 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.5.1-0.1.ea
- Update to shenandoah-jdk-11.0.5+1 (EA)
- Switch to EA mode for 11.0.5 pre-release builds.

* Thu Aug 08 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.4.11-4
- Switch to in-tree SunEC code, dropping NSS runtime dependencies and patches to link against it.

* Fri Jul 26 2019 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.4.11-3
- Drop unnecessary build requirement on gtk3-devel, as OpenJDK searches for Gtk+ at runtime.
- Add missing build requirement for libXrender-devel, previously masked by Gtk3+ dependency
- Add missing build requirement for libXrandr-devel, previously masked by Gtk3+ dependency
- fontconfig build requirement should be fontconfig-devel, previously masked by Gtk3+ dependency

* Fri Jul 26 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.4.11-2
- Rebuild with itself as boot JDK.

* Fri Jul 26 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.4.11-1
- Remove -fno-tree-ch workaround for i686 as the root cause has been
  fixed with 11.0.4+9.
- Resolves RHBZ#1683095

* Tue Jul 09 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.4.11-0
- Update to shenandoah-jdk-11.0.4+11 (GA)
- Switch to GA mode for final release.

* Mon Jul 08 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.4.10-0.2.ea
- Obsolete javadoc-slowdebug and javadoc-slowdebug-zip packages via javadoc and javadoc-zip respectively.

* Mon Jul 08 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.4.10-0.1.ea
- Update to shenandoah-jdk-11.0.4+10 (EA)

* Sun Jun 30 2019 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.4.2-0.1.ea
- Update to shenandoah-jdk-11.0.4+2 (EA)

* Fri Jun 21 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.4.2-0.1.ea
- Package jspawnhelper (see JDK-8220360).

* Fri Jun 21 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.3.7-6
- Include 'ea' designator in Release when appropriate.

* Wed May 22 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.3.7-6
- Handle milestone as variables so we can alter it easily and set the docs zip filename appropriately.

* Tue May 14 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.3.7-5
- Bump release for rebuild.

* Fri May 10 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.3.7-4
- Add -fno-tree-ch in order to work around GCC 9 issue on
  i686.
- Resolves: RHBZ#1683095

* Thu Apr 25 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.3.7-3
- Don't produce javadoc/javadoc-zip sub packages for the
  debug variant build.
- Don't perform a bootcycle build for the debug variant build.

* Wed Apr 24 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.3.7-2
- Don't generate lib-style requires for -slowdebug subpackages.
- Resolves: RHBZ#1702379

* Tue Apr 23 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.3.7-1
- Fix requires/provides for the non-system JDK case. JDK 11
  isn't a system JDK at this point.
- Resolves: RHBZ#1702324

* Sun Apr 07 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.3.7-0
- Update to shenandoah-jdk-11.0.3+7 (April 2019 GA)

* Sat Apr 06 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.3.6-0
- Update to shenandoah-jdk-11.0.3+6 (April 2019 EA)
- Drop JDK-8210416/RH1632174 applied upstream.
- Drop JDK-8210425/RH1632174 applied upstream.
- Drop JDK-8210647/RH1632174 applied upstream.
- Drop JDK-8210761/RH1632174 applied upstream.
- Drop JDK-8210703/RH1632174 applied upstream.
- Add cast to resolve s390 ambiguity in call to log2_intptr

* Thu Mar 21 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.2.7-9
- Add patch for RH1566890

* Wed Mar 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1:11.0.2.7-8
- Drop chkconfig dep, 1.7 shipped in f24

* Mon Mar 11 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.2.7-7
- Add -Wa,--generate-missing-build-notes=yes C flags. So as to
  fix annocheck warnings for assembler source files.

* Tue Feb 26 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.2.7-6
- Don't package lib/client and lib/client/classes.jsa
  which don't exist.
- Resolves: RHBZ#1643469

* Tue Feb 19 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.2.7-5
- Add explicit requirement for libXcomposite which is used when performing
  screenshots from Java.
- Add explicit BR unzip required for building OpenJDK.

* Thu Feb 14 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.2.7-4
- Add a test verifying system crypto policies can be disabled

* Tue Feb 12 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.2.7-3
- Don't build the test images needlessly.

* Thu Feb 07 2019 Andrew John Hughes <gnu.andrew@redhat.com> - 1:11.0.2.7-2
- Add PR3695 to allow the system crypto policy to be turned off.
- Correct original system crypto policy patch to refer to OpenJDK 11 bug (PR3694)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.0.2.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.2.7-0
- Update to shenandoah-jdk-11.0.2+7 (January 2019 CPU)
- Drop JDK-8211105/RH1628612/RH1630996 applied upstream.
- Drop JDK-8209639/RH1640127 applied upstream.
- Re-generate JDK-8210416/RH1632174 following JDK-8209786

* Fri Jan 11 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:11.0.1.13-11
- Update to shenandoah-jdk-11.0.1+13-20190101
- Update tarball generation script in preparation for PR3681/RH1656677 SunEC changes.
- Use remove-intree-libraries.sh to remove the remaining SunEC code for now.
- Fix PR1983 SunEC patch so that ecc_impl.h is patched rather than added
- Add missing RH1022017 patch to reduce curves reported by SSL to those we support.
- Remove RH1648995; fixed upstream.

* Wed Dec 5 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.1.13-9
- for non debug supackages, ghosted all masters and slaves (rhbz1649776)
- for tech-preview packages, if-outed versionless provides. Aligned versions to be %%{epoch}:%%{version}-%%{release} instead of chaotic
- Removed all slowdebug provides (rhbz1655938); for tech-preview packages also removed all internal provides

* Wed Nov 28 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.1.13-8
- Added %%global _find_debuginfo_opts -g
- Resolves: RHBZ#1520879 (Detailed NMT issue)

* Mon Nov 12 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.1.13-6
- fixed tck failures of arraycopy and process exec with shenandoah on
- added patch585 rh1648995-shenandoah_array_copy_broken_by_not_always_copy_forward_for_disjoint_arrays.patch

* Wed Nov 07 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.1.13-5
- headless' suggests of cups, replaced by Requires of cups-libs

* Thu Nov 01 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.1.13-3
- added Patch584 jdk8209639-rh1640127-02-coalesce_attempted_spill_non_spillable.patch

* Mon Oct 29 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.1.13-3
- Use upstream's version of Aarch64 intrinsics disable patch:
  - Removed:
    RHBZ-1628612-JDK-8210461-workaround-disable-aarch64-intrinsic.patch
    RHBZ-1630996-JDK-8210858-workaround-disable-aarch64-intrinsic-log.patch
  - Superceded by:
    jdk8211105-aarch64-disable_cos_sin_and_log_intrinsics.patch

* Thu Oct 18 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.1.13-2
- Use LTS designator in version output for RHEL.

* Thu Oct 18 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.1.13-1
- Update to October 2018 CPU release, 11.0.1+13.

* Wed Oct 17 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.0.28-2
- Use --with-vendor-version-string=18.9 so as to show original
  GA date for the JDK.

* Fri Sep 28 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.0.28-1
- Identify as GA version and no longer as early access (EA).
- JDK 11 has been released for GA on 2018-09-25.

* Fri Sep 28 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.28-9
- Rework changes from 1:11.0.ea.22-6. RHBZ#1632174 supercedes
  RHBZ-1624122.
- Add patch, jdk8210416-rh1632174-compile_fdlibm_with_o2_ffp_contract_off_on_gcc_clang_arches.patch, so as to
  optimize compilation of fdlibm library.
- Add patch, jdk8210425-rh1632174-sharedRuntimeTrig_sharedRuntimeTrans_compiled_without_optimization.patch, so
  as to optimize compilation of sharedRuntime{Trig,Trans}.cpp
- Add patch, jdk8210647-rh1632174-libsaproc_is_being_compiled_without_optimization.patch, so as to
  optimize compilation of libsaproc (extra c flags won't override
  optimization).
- Add patch, jdk8210761-rh1632174-libjsig_is_being_compiled_without_optimization.patch, so as to
  optimize compilation of libjsig.
- Add patch, jdk8210703-rh1632174-vmStructs_cpp_no_longer_compiled_with_o0, so as to
  optimize compilation of vmStructs.cpp (part of libjvm.so).
- Reinstate filtering of opt flags coming from redhat-rpm-config.

* Thu Sep 27 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.28-8
- removed version less provides
- javadocdir moved to arched dir as it is no longer noarch

* Thu Sep 20 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.28-6
- Add patch, RHBZ-1630996-JDK-8210858-workaround-disable-aarch64-intrinsic-log.patch,
  so as to disable log math intrinsic on aarch64. Work-around for
  JDK-8210858

* Thu Sep 13 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.28-5
- Add patch, RHBZ-1628612-JDK-8210461-workaround-disable-aarch64-intrinsic.patch,
  so as to disable dsin/dcos math intrinsics on aarch64. Work-around for
  JDK-8210461.

* Wed Sep 12 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.22-6
- Add patch, JDK-8210416-RHBZ-1624122-fdlibm-opt-fix.patch, so as to
  optimize compilation of fdlibm library.
- Add patch, JDK-8210425-RHBZ-1624122-sharedRuntimeTrig-opt-fix.patch, so
  as to optimize compilation of sharedRuntime{Trig,Trans}.cpp
- Add patch, JDK-8210647-RHBZ-1624122-libsaproc-opt-fix.patch, so as to
  optimize compilation of libsaproc (extra c flags won't override
  optimization).
- Add patch, JDK-8210703-RHBZ-1624122-vmStructs-opt-fix.patch, so as to
  optimize compilation of vmStructs.cpp (part of libjvm.so).
- No longer filter -O flags from C flags coming from
  redhat-rpm-config.

* Mon Sep 10 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.28-4
- link to jhsdb followed its file to ifarch jit_arches ifnarch s390x

* Fri Sep 7 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.28-3
- Enable ZGC on x86_64.

* Tue Sep 4 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.28-2
- jfr/*jfc files listed for all arches
- lib/classlist do not exists s390, ifarch-ed via jit_arches out

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.28-1
- Update to latest upstream build jdk11+28, the first release
  candidate.

* Wed Aug 29 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.22-8
- Adjust system NSS patch, pr1983-rh1565658-support_using_the_system_installation_of_nss_with_the_sunec_provider_jdk11.patch, so
  as to filter -Wl,--as-needed from linker flags. Fixes FTBFS issue.

* Thu Aug 23 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.22-6
- dissabled accessibility, fixed provides for main package's debug variant

* Mon Jul 30 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.22-5
- now buildrequires javapackages-filesystem as the  issue with macros should be fixed

* Wed Jul 18 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.22-2
- changed to build by itself instead of by jdk10

* Tue Jul 17 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.22-1
- added Recommends gtk3 for main package
- changed BuildRequires from gtk2-devel to gtk3-devel (it can be more likely dropped)
- added Suggests lksctp-tools, pcsc-lite-devel, cups for headless package
- see RHBZ1598152
- added trick to catch hs_err files (sgehwolf)
- updated to shenandaoh-jdk-11+22

* Sat Jul 07 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.20-1
- removed patch6 JDK-8205616-systemLcmsAndJpgFixFor-rev_f0aeede1b855.patch
- improved a bit generate_source_tarball.sh to serve also for systemtap
- thus deleted generate_tapsets.sh
- simplified and cleared update_package.sh
- moved to single source jdk - from shenandoah/jdk11
- bumped to latest jdk11+20
- adapted PR2126 to jdk11+20
- adapted handling of systemtap sources to new style
- (no (misleading) version inside (full version is in name), thus different sed on tapsets and different directory)
- shortened summaries and descriptions to around 80 chars
- Hunspell spell checked
- license fixed to correct jdk11 (sgehwolf)
- more correct handling of internal libraries (sgehwolf)
- added lib/security/public_suffix_list.dat as +20 have added it (JDK-8201815)
- added test for shenandaoh GC presence where expected
- Removed workaround for broken aarch64 slowdebug build
- Removed all defattrs
- Removed no longer necessary cleanup of diz and  debuginfo files

* Fri Jun 22 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.ea.19-1
- updated sources to jdk-11+19
- added patch6 systemLcmsAndJpgFixFor-f0aeede1b855.patch to fix regression of system libraries after f0aeede1b855 commit
- adapted pr1983-rh1565658-support_using_the_system_installation_of_nss_with_the_sunec_provider_jdk11.patch to accommodate changes after f0aeede1b855 commit

* Thu Jun 14 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.16-5
- Revert rename: java-11-openjdk => java-openjdk.

* Wed Jun 13 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.16-4
- Add aarch64 to aot_arches.

* Wed Jun 13 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.16-3
- Rename to package java-11-openjdk.

* Wed Jun 13 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.16-2
- Disable Aarch64 slowdebug build (see JDK-8204331).
- s390x doesn't have the SA even though it's a JIT arch.

* Wed Jun 13 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.ea.16-1
- Initial version of JDK 11 ea based on tag jdk-11+16.
- Removed patches no longer needed or upstream:
  sorted-diff.patch (see JDK-8198844)
  JDK-8201788-bootcycle-images-jobs.patch
  JDK-8201509-s390-atomic_store.patch
  JDK-8202262-libjsig.so-extra-link-flags.patch (never was an issue on 11)
  JDK-8193802-npe-jar-getVersionMap.patch
- Updated and renamed patches:
  java-openjdk-s390-size_t.patch => JDK-8203030-s390-size_t.patch
- Updated patches for JDK 11:
  pr1983-rh1565658-support_using_the_system_installation_of_nss_with_the_sunec_provider_jdk11.patch

* Tue Jun 12 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.1.10-9
- Use proper private_libs expression for filtering requires/provides.

* Fri Jun 08 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.1.10-8
- Bump release and rebuild for fixed gdb. See RHBZ#1589118.

* Mon Jun 04 2018 Jiri Vanek <jvanek@redhat.com> - 1:10.0.1.10-7
- quoted sed expressions, changed possibly confusing # by @
- added vendor(origin) into icons
- removed last trace of relative symlinks
- added BuildRequires of javapackages-tools to fix build failure after Requires change to javapackages-filesystem

* Thu May 17 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.1.10-5
- Move to javapackages-filesystem for directory ownership.
  Resolves RHBZ#1500288

* Mon Apr 30 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.1.10-4
- Add JDK-8193802-npe-jar-getVersionMap.patch so as to fix
  RHBZ#1557375.

* Mon Apr 23 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.1.10-3
- Inject build flags properly. See RHBZ#1571359
- Added patch JDK-8202262-libjsig.so-extra-link-flags.patch
  since libjsig.so doesn't get linker flags injected properly.

* Fri Apr 20 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.1.10-2
- Removed unneeded patches:
  PStack-808293.patch
  multiple-pkcs11-library-init.patch
  ppc_stack_overflow_fix.patch 
- Added patches for s390 Zero builds:
  JDK-8201495-s390-java-opts.patch
  JDK-8201509-s390-atomic_store.patch
- Renamed patches for clarity:
  aarch64BuildFailure.patch => JDK-8200556-aarch64-slowdebug-crash.patch
  systemCryptoPolicyPR3183.patch => pr3183-rh1340845-support_fedora_rhel_system_crypto_policy.patch
  bootcycle_jobs.patch => JDK-8201788-bootcycle-images-jobs.patch
  system-nss-ec-rh1565658.patch => pr1983-rh1565658-support_using_the_system_installation_of_nss_with_the_sunec_provider_jdk11.patch

* Fri Apr 20 2018 Jiri Vanek <jvanek@redhat.com> - 1:10.0.1.10-1
- updated to security update 1
- jexec unlinked from path
- used java-openjdk as boot jdk
- aligned provides/requires
- renamed zip javadoc

* Tue Apr 10 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.0.46-12
- Enable basic EC ciphers test in %%check.

* Tue Apr 10 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:10.0.0.46-11
- Port Martin Balao's JDK 9 patch for system NSS support to JDK 10.
- Resolves RHBZ#1565658

* Mon Apr 09 2018 Jiri Vanek <jvanek@redhat.com> - 1:10.0.0.46-10
- jexec linked to path

* Fri Apr 06 2018 Jiri Vanek <jvanek@redhat.com> - 1:10.0.0.46-9
- subpackage(s) replaced by sub-package(s) and other cosmetic changes

* Tue Apr 03 2018 Jiri Vanek <jvanek@redhat.com> - 1:10.0.0.46-8
- removed accessibility sub-packages
- kept applied patch and properties files
- debug sub-packages renamed to slowdebug

* Fri Feb 23 2018 Jiri Vanek <jvanek@redhat.com> - 1:10.0.0.46-1
- initial load
