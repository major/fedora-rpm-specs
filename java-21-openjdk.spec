# RPM conditionals so as to be able to dynamically produce
# slowdebug/release builds. See:
# http://rpm.org/user_doc/conditional_builds.html
#
# Examples:
#
# Produce release, fastdebug *and* slowdebug builds on x86_64 (default):
# $ rpmbuild -ba java-21-openjdk.spec
#
# Produce only release builds (no debug builds) on x86_64:
# $ rpmbuild -ba java-21-openjdk.spec --without slowdebug --without fastdebug
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
%global jit_arches      %{arm} %{aarch64} %{ix86} %{power64} s390x sparcv9 sparc64 x86_64 riscv64
# Set of architectures which use the Zero assembler port (!jit_arches)
%global zero_arches ppc s390
# Set of architectures which support SystemTap tapsets
%global systemtap_arches %{jit_arches}
# Set of architectures with a Ahead-Of-Time (AOT) compiler
%global aot_arches      x86_64 %{aarch64}
# Set of architectures which support the serviceability agent
%global sa_arches       %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64} %{arm} riscv64
# As of JDK-8005165 in OpenJDK 10, class sharing is not arch-specific
# However, it does segfault on the Zero assembler port, so currently JIT only
%global share_arches    %{jit_arches}
# Set of architectures for which we build the Shenandoah garbage collector
%global shenandoah_arches x86_64 %{aarch64}
# Set of architectures for which we build the Z garbage collector
%global zgc_arches x86_64 riscv64
# Set of architectures for which alt-java has SSB mitigation
%global ssbd_arches x86_64
# Set of architectures for which java has short vector math library (libsvml.so)
%global svml_arches x86_64
# Set of architectures where we verify backtraces with gdb
# s390x fails on RHEL 7 so we exclude it there
%if (0%{?rhel} > 0 && 0%{?rhel} < 8)
%global gdb_arches %{arm} %{aarch64} %{ix86} %{power64} sparcv9 sparc64 x86_64 %{zero_arches}
%else
%global gdb_arches %{jit_arches} %{zero_arches}
%endif

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
%global stapinstall %{_target_cpu}
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
%global featurever 21
%global interimver 0
%global updatever 4
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
%global buildver        7
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
  --slave %{_bindir}/keytool keytool %{jrebindir -- %{?1}}/keytool \\
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir -- %{?1}}/rmiregistry \\
  --slave %{_mandir}/man1/java.1$ext java.1$ext \\
  %{_mandir}/man1/java-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/%{alt_java_name}.1$ext %{alt_java_name}.1$ext \\
  %{_mandir}/man1/%{alt_java_name}-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jcmd.1$ext jcmd.1$ext \\
  %{_mandir}/man1/jcmd-%{uniquesuffix -- %{?1}}.1$ext \\
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
  --slave %{_bindir}/jwebserver jwebserver %{sdkbindir -- %{?1}}/jwebserver \\
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
  --slave %{_mandir}/man1/jpackage.1$ext jpackage.1$ext \\
  %{_mandir}/man1/jpackage-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \\
  %{_mandir}/man1/jrunscript-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \\
  %{_mandir}/man1/jstack-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \\
  %{_mandir}/man1/jstat-%{uniquesuffix -- %{?1}}.1$ext \\
  --slave %{_mandir}/man1/jwebserver.1$ext jwebserver.1$ext \\
  %{_mandir}/man1/jwebserver-%{uniquesuffix -- %{?1}}.1$ext \\
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
%{_jvmdir}/%{sdkdir -- %{?1}}/NEWS
%dir %{_sysconfdir}/.java/.systemPrefs
%dir %{_sysconfdir}/.java
%dir %{_jvmdir}/%{sdkdir -- %{?1}}
%{_jvmdir}/%{sdkdir -- %{?1}}/release
%{_jvmdir}/%{jrelnk -- %{?1}}
%dir %{_jvmdir}/%{sdkdir -- %{?1}}/bin
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/java
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/%{alt_java_name}
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jcmd
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
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/lible.so
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
%{_mandir}/man1/jcmd-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/keytool-%{uniquesuffix -- %{?1}}.1*
%{_mandir}/man1/rmiregistry-%{uniquesuffix -- %{?1}}.1*
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/
%ifarch %{share_arches}
%attr(444, root, root) %{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/classes.jsa
%ifnarch %{ix86} %{arm32}
%attr(444, root, root) %{_jvmdir}/%{sdkdir -- %{?1}}/lib/%{vm_variant}/classes_nocoops.jsa
%endif
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
%config(noreplace) %{etcjavadir -- %{?1}}/conf/security/nss.fips.cfg
%config(noreplace) %{etcjavadir -- %{?1}}/conf/management/jmxremote.access
# This is a config template, thus not config-noreplace
%config  %{etcjavadir -- %{?1}}/conf/management/jmxremote.password.template
%config  %{etcjavadir -- %{?1}}/conf/sdp/sdp.conf.template
%config(noreplace) %{etcjavadir -- %{?1}}/conf/management/management.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/net.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/sound.properties
%config(noreplace) %{etcjavadir -- %{?1}}/conf/jaxp.properties
%{_jvmdir}/%{sdkdir -- %{?1}}/conf
%{_jvmdir}/%{sdkdir -- %{?1}}/lib/security
%if %is_system_jdk
%if %{is_release_build -- %{?1}}
%ghost %{_bindir}/java
%ghost %{_jvmdir}/jre
%ghost %{_bindir}/%{alt_java_name}
%ghost %{_bindir}/jcmd
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
%{_jvmdir}/%{sdkdir -- %{?1}}/bin/jwebserver
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
%{_mandir}/man1/jwebserver-%{uniquesuffix -- %{?1}}.1*

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

%global portable_name %{name}-portable
# the version must match, but sometmes we need to more precise, so including release
%global portable_version %{version}-1

Name:    java-21-%{origin}
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
# for modyfying build-id in clashing binaries
BuildRequires: /usr/bin/gcc
BuildRequires: /usr/bin/objcopy
BuildRequires: /usr/bin/readelf
# Requirement for setting and nss.fips.cfg
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
Obsoletes: javadoc-zip-slowdebug < 1:13.0.0.33-1.rolling

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
ls -l %{portablejvmdir} >> %{repack_file}
rpm -qa | grep "java-" >> %{repack_file}
echo "Used %{compatiblename}.*portable:" >> %{repack_file}
ls -l %{portablejvmdir} | grep "%{compatiblename}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used %{name}.*portable:" >> %{repack_file}
rpm -qa | grep "%{name}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
echo "Used %{version}.*portable:" >> %{repack_file}
ls -l %{portablejvmdir} | grep "%{version}.*portable" >> %{repack_file} || echo "Not found!" >> %{repack_file}
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
    # it may happen, that some library - in original case libjsvml build identically for two jdks
    # it is becasue of our ld/gcc flags - otherwise rpm build enhances each binarry by full path to it
    # if it is hit then this library needs to have build-id repalced - note, that it do not affect dbugability
    clashinglibs=""
%ifarch %{svml_arches}
    clashinglibs="$clashinglibs lib/libjsvml.so"
%endif
    for lib in $clashinglibs ; do
      libjsvmlgcchackdir=`mktemp -d`
      pushd $libjsvmlgcchackdir
        libjsvml=${top_dir_abs_main_build_path}/$lib
        ls -l $libjsvml
        echo "#include <stdio.h>" > a.c
        echo "int main(void) {  printf(\"$libjsvml\"); }" >> a.c
        gcc a.c -o exe
        readelf -n  exe | grep "Build ID"
        readelf -n  $libjsvml | grep "Build ID"
        objcopy --dump-section .note.gnu.build-id=id exe
        objcopy --update-section  .note.gnu.build-id=id $libjsvml
        readelf -n $libjsvml | grep -i "Build ID"
      popd
      rm -rf $libjsvmlgcchackdir
    done
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
cp -a ${misc_image}/%{generated_sources_name} $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}
cp -a ${misc_image}/alt-java $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir -- $suffix}/bin
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
* Sat Jul 20 2024 Jiri Vanek <jvanek@redhat.com> - 1:21.0.4.0.7-1
- July CPU

* Wed May 01 2024 Jiri Vanek <jvanek@redhat.com> - 1:21.0.3.0.9-1
- added logic to print repacked info to repack.info
- April CPU

* Wed Feb 21 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 1:22.0.0.0.36-3
- Add riscv64 support

* Thu Feb 15 2024 Petra Alice Mikova <pmikova@redhat.com> - 1:21.0.2.0.13-2
- make this package system jdk
- fix release issue introduced by automatic rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:21.0.2.0.13-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Jiri Vanek <jvanek@redhat.com> - 1:21.0.2.0.13-1
* forked from java-latest-openjdk

* Sat Jan 20 2024 Jiri Vanek <jvanek@redhat.com> - 1:21.0.2.0.13-1
- Update to jdk-21.0.2+13 (GA)

* Sat Dec 16 2023 Jiri Vanek <jvanek@redhat.com> - 1:21.0.1.0.12-4.rolling
* using generated sources from portables for final debuginfo

* Sat Dec 09 2023 Jiri Vanek <jvanek@redhat.com> - 1:21.0.1.0.12-3.rolling
- proeprly filing debugsources pkg
  by addedd symlinks restructuring the structure for original build sources
- according to logs, some are still missing
  probably generated during the build, and thus not existing in prep,
  when the sources subpkg is created after patching

* Wed Nov 22 2023 Jiri Vanek <jvanek@redhat.com> - 1:21.0.1.0.12-2.rolling
- added setup and thus enabled debuginfo strip
- note, that debugsources are now empty. Symlink from full sourcess to build/jdk21.build or build/vcstag is needed

* Wed Nov 22 2023 Jiri Vanek <jvanek@redhat.com> - 1:21.0.1.0.12-1.rolling
- updated to OpenJDK 21.0.1 (2023-10-17)

* Fri Sep 29 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1:21.0.0.0.35-3.rolling
- Fix flatpak build by handling different installation prefixes of package dependencies

* Tue Sep 19 2023 Jiri Vanek <jvanek@redhat.com> - 1:21.0.0.0.35-2.rolling
- adapted to new path in sources
- repacked alt-java from misc subpkg
- adapted alt-java to grep correctly prctl
- removed no longer prepared nss.cfg

* Tue Aug 29 2023 Jiri Vanek <jvanek@redhat.com> - 1:21.0.0.0.35-1.rolling
- updated to jdk 21

* Mon Aug 07 2023 Jiri Vanek <jvanek@redhat.com> - 1:20.0.2.0.9-2.rolling
- updated to July security update  20.0.2.9 portables

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.0.1.0.9-8.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Andrew Hughes <gnu.andrew@redhat.com> - 1:20.0.1.0.9-8.rolling
- Following JDK-8005165, class data sharing can be enabled on all JIT architectures

* Wed May 10 2023 Severin Gehwolf <sgehwolf@redhat.com> - 1:20.0.1.0.9-6.rolling
- Fix packaging of CDS archives

* Fri Apr 28 2023 Jiri Vanek <jvanek@redhat.com> - 1:20.0.1.0.9-6.rolling
- faking build-id in libjsvml.so

* Fri Apr 28 2023 Jiri Vanek <jvanek@redhat.com> - 1:20.0.1.0.9-5.rolling
- returned news

* Fri Apr 28 2023 Jiri Vanek <jvanek@redhat.com> - 1:20.0.1.0.9-4.rolling
- now expecting the exact version in portbale filename

* Fri Apr 28 2023 Jiri Vanek <jvanek@redhat.com> - 1:20.0.1.0.9-3.rolling
- updated to 20.0.1.0.9 underlying portables

* Wed Apr 19 2023 Jiri Vanek <jvanek@redhat.com> - 1:20.0.0.0.36-3.rolling
- using icons from source package
- providing full sources via src package
- requiring exact version.reelase of portables
- returned libsystemconf.so

* Mon Apr 03 2023 Jiri Vanek <jvanek@redhat.com> - 1:20.0.0.0.36-1.rolling
- bumed to jdk20
- removed no loger existing libsystemconf.so
- commented out usage if Source15 TestSecurityProperties.java test, as honoring of
-- system crypto policies comes from fips aptch which is not yet adapted

* Mon Jan 30 2023 Jiri Vanek <jvanek@redhat.com> - 1:19.0.2.0.7-5.rolling
- Using icons whcih are now part of the portble tarball

* Mon Jan 30 2023 Jiri Vanek <jvanek@redhat.com> - 1:19.0.2.0.7-4.rolling
- repacked bits are now requested in exact version

* Mon Jan 30 2023 Petra Alice Mikova <pmikova@redhat.com> - 1:19.0.2.0.7-3.rolling
- return libfreetype.so binary to resolve requires problems
- remove BuildRequires: java-21-openjdk

* Thu Jan 26 2023 Jiri Vanek <jvanek@redhat.com> - 1:19.0.2.0.7-2.rolling
- repacked portables
- todo icons
- disabled tzdata tests - todo, resolve
- left some duplicated "final tunings"
- todo, lost alt java manpage.. probably already in portables
- TODO conslut this clean up - javdoc, freetype and NEWS
- todo, debuginfo

* Thu Jan 26 2023 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.2.0.7-1.rolling
- Update to jdk-19.0.2 release
- Update release notes to 19.0.2
- Drop JDK-8293834 (CLDR update for Kyiv) which is now upstream
- Drop JDK-8294357 (tzdata2022d), JDK-8295173 (tzdata2022e) & JDK-8296108 (tzdata2022f) local patches which are now upstream
- Drop JDK-8296715 (CLDR update for 2022f) which is now upstream
- Add local patch JDK-8295447 (javac NPE) which was accepted into 19u upstream but not in the GA tag
- Add local patches for JDK-8296239 & JDK-8299439 (Croatia Euro update) which are present in 8u, 11u & 17u releases

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:19.0.1.0.10-3.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.1.0.10-3.rolling
- Update in-tree tzdata & CLDR to 2022g with JDK-8296108, JDK-8296715 & JDK-8297804
- Update TestTranslations.java to test the new America/Ciudad_Juarez zone

* Wed Dec 07 2022 Stephan Bergmann <sbergman@redhat.com> - 1:19.0.1.0.10-3.rolling
- Fix flatpak builds by disabling TestTranslations test due to missing tzdb.dat

* Wed Oct 26 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.1.0.10-2.rolling
- Update in-tree tzdata to 2022e with JDK-8294357 & JDK-8295173
- Update CLDR data with Europe/Kyiv (JDK-8293834)
- Drop JDK-8292223 patch which we found to be unnecessary
- Update TestTranslations.java to use public API based on TimeZoneNamesTest upstream

* Thu Oct 20 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.1.0.10-1.rolling
- Update to jdk-19.0.1 release
- Update release notes to 19.0.1

* Wed Sep 21 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.0.0.36-3.rolling
- The stdc++lib, zlib & freetype options should always be set from the global, so they are not altered for staticlibs builds
- Remove freetype sources along with zlib sources

* Tue Aug 30 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.0.0.36-2.rolling
- Switch buildjdkver back to being featurever, now java-19-openjdk is available in the buildroot

* Mon Aug 29 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.0.0.36-2.rolling
- Switch to static builds, reducing system dependencies and making build more portable

* Mon Aug 29 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:19.0.0.0.36-1.rolling
- Update to RC version of OpenJDK 19
- Update release notes to 19.0.0
- Rebase FIPS patches from fips-19u branch
- Need to include the '.S' suffix in debuginfo checks after JDK-8284661
- Add patch to provide translations for Europe/Kyiv added in tzdata2022b
- Add test to ensure timezones can be translated
- Remove references to sample directory removed by JDK-8284999

* Fri Jul 22 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.2.0.9-1.rolling
- Update to jdk-18.0.2 release
- Update release notes to 18.0.2
- Drop JDK-8282004 patch which is now upstreamed under JDK-8282231
- Exclude x86 where java_arches is undefined, in order to unbreak build

* Fri Jul 22 2022 Jiri Vanek <gnu.andrew@redhat.com> - 1:18.0.1.1.2-8.rolling
- moved to build only on %%{java_arches}
-- https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
- reverted :
-- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild (always mess up release)
-- Try to build on x86 again by creating a husk of a JDK which does not depend on itself
-- Exclude x86 from builds as the bootstrap JDK is now completely broken and unusable
-- Replaced binaries and .so files with bash-stubs on i686
- added ExclusiveArch:  %%{java_arches}
-- this now excludes i686
-- this is safely backport-able to older fedoras, as the macro was backported properly (with i686 included)
- https://bugzilla.redhat.com/show_bug.cgi?id=2104125

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:18.0.1.1.2-7.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.1.2-7.rolling
- Try to build on x86 again by creating a husk of a JDK which does not depend on itself

* Sun Jul 17 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.1.2-6.rolling
- Exclude x86 from builds as the bootstrap JDK is now completely broken and unusable

* Wed Jul 13 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.1.2-5.rolling
- Explicitly require crypto-policies during build and runtime for system security properties

* Wed Jul 13 2022 Jiri Vanek <jvanek@redhat.com> - 1:18.0.1.1.2-4.rolling.
- Replaced binaries and .so files with bash-stubs on i686 in preparation of the removal on that architecture:
- https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs

* Wed Jul 13 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.1.2-3.rolling
- Make use of the vendor version string to store our version & release rather than an upstream release date

* Tue Jul 12 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1:18.0.1.1.2-2.rolling
- Add javaver- and origin-specific javadoc and javadoczip alternatives.

* Mon Jul 11 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.1.2-1.rolling
- Update to jdk-18.0.1.1 interim release
- Update release notes to actually reflect OpenJDK 18 and subsequent releases 18.0.1 & 18.0.1.1
- Print release file during build, which should now include a correct SOURCE value from .src-rev
- Update tarball script with IcedTea GitHub URL and .src-rev generation
- Include script to generate bug list for release notes
- Update tzdata requirement to 2022a to match JDK-8283350

* Sat Jul 09 2022 Jayashree Huttanagoudar <jhuttana@redhat.com> - 1:18.0.1.0.10-8.rolling
- Fix issue where CheckVendor.java test erroneously passes when it should fail.
- Add proper quoting so '&' is not treated as a special character by the shell.

* Sat Jul 09 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.0.10-8.rolling
- Include a test in the RPM to check the build has the correct vendor information.

* Fri Jul 08 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.0.10-7.rolling
- Fix whitespace in spec file

* Fri Jul 08 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.0.10-7.rolling
- Sequence spec file sections as they are run by rpmbuild (build, install then test)

* Fri Jul 08 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.0.10-7.rolling
- Turn on system security properties as part of the build's install section
- Move cacerts replacement to install section and retain original of this and tzdb.dat
- Run tests on the installed image, rather than the build image
- Introduce variables to refer to the static library installation directories
- Use relative symlinks so they work within the image
- Run debug symbols check during build stage, before the install strips them

* Thu Jul 07 2022 Stephan Bergmann <sbergman@redhat.com> - 1:18.0.1.0.10-6.rolling
- Fix flatpak builds by exempting them from bootstrap

* Thu Jun 30 2022 Francisco Ferrari Bihurriet <fferrari@redhat.com> - 1:18.0.1.0.10-5.rolling
- RH2007331: SecretKey generate/import operations don't add the CKA_SIGN attribute in FIPS mode

* Thu Jun 30 2022 Stephan Bergmann <sbergman@redhat.com> - 1:18.0.1.0.10-4.rolling
- Fix flatpak builds (catering for their uncompressed manual pages)

* Fri Jun 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.0.10-3.rolling
- Update FIPS support to bring in latest changes
- * RH2023467: Enable FIPS keys export
- * RH2094027: SunEC runtime permission for FIPS
- * RH2036462: sun.security.pkcs11.wrapper.PKCS11.getInstance breakage
- * RH2090378: Revert to disabling system security properties and FIPS mode support together
- Rebase RH1648249 nss.cfg patch so it applies after the FIPS patch
- Enable system security properties in the RPM (now disabled by default in the FIPS repo)
- Improve security properties test to check both enabled and disabled behaviour
- Run security properties test with property debugging on
- Minor sync-ups with java-17-openjdk spec file

* Wed May 25 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.1.0.10-2.rolling
- Exclude s390x from the gdb test on RHEL 7 where we see failures with the portable build

* Wed Apr 27 2022 Jiri Vanek <jvanek@redhat.com> - 1:18.0.1.0.10-1.rolling.
- updated to CPU jdk-18.0.1+10 sources

* Wed Apr 06 2022 Jiri Vanek <jvanek@redhat.com> - 1:18.0.0.0.37-4.rolling
- Remove hardcoded /usr/lib/jvm by %%{_jvmdir} to make rpmlint happy

* Wed Mar 23 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.0.0.37-3.rolling
- Automatically turn off building a fresh HotSpot first, if the bootstrap JDK is not the same major version as that being built

* Mon Mar 21 2022 Jiri Vanek <jvanek@redhat.com> - 1:18.0.0.0.37-2.rolling
- replaced tabs by sets of spaces to make rpmlint happy
- set build jdk to 18
- as ga is 1, set vendor_version_string to 22.3

* Wed Mar 16 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:18.0.0.0.37-1.rolling
- Update to RC version of OpenJDK 18
- Support JVM variant zero following JDK-8273494 no longer installing Zero's libjvm.so in the server directory
- Disable HotSpot-only pre-build which is incompatible with the boot JDK being a different major version to that being built
- Rebase FIPS patches from fips-18u branch and simplify by using a single patch from that repository
- Detect NSS at runtime for FIPS detection
- Turn off build-time NSS linking and go back to an explicit Requires on NSS
- Enable AlgorithmParameters and AlgorithmParameterGenerator services in FIPS mode
- Rebase RH1648249 nss.cfg patch so it applies after the FIPS patch

* Wed Mar 16 2022 Petra Alice Mikova <pmikova@redhat.com> - 1:18.0.0.0.37-1.rolling
- update to ea version of jdk18
- add new slave jwebserver and corresponding manpage
- adjust rh1684077-openjdk_should_depend_on_pcsc-lite-libs_instead_of_pcsc-lite-devel.patch

* Wed Feb 16 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-5
- Reinstate JIT builds on x86_32.
- Add JDK-8282004 to fix missing CALL effects on x86_32.

* Mon Feb 07 2022 Severin Gehwolf <sgehwolf@redhat.com> - 1:17.0.2.0.8-4
- Re-enable gdb backtrace check.
- Resolves RHBZ#2041970

* Fri Feb 04 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-3
- Temporarily move x86 to use Zero in order to get a working build
- Replace -mstackrealign with -mincoming-stack-boundary=2 -mpreferred-stack-boundary=4 on x86_32 for stack alignment
- Support a HotSpot-only build so a freshly built libjvm.so can then be used in the bootstrap JDK.
- Explicitly list JIT architectures rather than relying on those with slowdebug builds
- Disable the serviceability agent on Zero architectures even when the architecture itself is supported

* Mon Jan 24 2022 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.2.0.8-2.rolling
- Introduce stapinstall variable to set SystemTap arch directory correctly (e.g. arm64 on aarch64)
- Need to support noarch for creating source RPMs for non-scratch builds.

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

* Fri Nov 05 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-8.rolling
- Patch syslookup.c so it actually has some code to be compiled into libsyslookup
- Related: rhbz#2013846

* Wed Nov 03 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1:17.0.1.0.12-7.rolling
- Use 'sql:' prefix in nss.fips.cfg as F35+ no longer ship the legacy
  secmod.db file as part of nss

* Wed Nov 03 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-6.rolling
- Turn off bootstrapping for slow debug builds, which are particularly slow on ppc64le.

* Thu Oct 28 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-5.rolling
- Sync desktop files with upstream IcedTea release 3.15.0 using new script

* Tue Oct 26 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-4.rolling
- Restructure the build so a minimal initial build is then used for the final build (with docs)
- This reduces pressure on the system JDK and ensures the JDK being built can do a full build

* Tue Oct 26 2021 Jiri Vanek <jvanek@redhat.com> - 1:17.0.1.0.12-3.rolling
- Minor cosmetic improvements to make spec more comparable between variants

* Thu Oct 21 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.1.0.12-2.rolling
- Update tapsets from IcedTea 6.x repository with fix for JDK-8015774 changes (_heap->_heaps) and @JAVA_SPEC_VER@
- Update icedtea_sync.sh with a VCS mode that retrieves sources from a Mercurial repository

* Wed Oct 20 2021 Petra Alice Mikova <pmikova@redhat.com> - 1:17.0.1.0.12-1.rolling
- October CPU update to jdk 17.0.1+12
- dropped commented-out source line

* Sun Oct 10 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.35-5.rolling
- Allow plain key import to be disabled with -Dcom.redhat.fips.plainKeySupport=false

* Sun Oct 10 2021 Martin Balao <mbalao@redhat.com> - 1:17.0.0.0.35-5.rolling
- Add patch to allow plain key import.

* Thu Sep 30 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.35-4.rolling
- Fix unused function compiler warning found in systemconf.c
- Extend the default security policy to accomodate PKCS11 accessing jdk.internal.access.

* Thu Sep 30 2021 Martin Balao <mbalao@redhat.com> - 1:17.0.0.0.35-4.rolling
- Add patch to login to the NSS software token when in FIPS mode.

* Mon Sep 27 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.35-3.rolling
- Update release notes to document the major changes between OpenJDK 11 & 17.

* Thu Sep 16 2021 Martin Balao <mbalao@redhat.com> - 1:17.0.0.0.35-2.rolling
- Add patch to disable non-FIPS crypto in the SUN and SunEC security providers.

* Tue Sep 14 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.35-1.rolling
- Update to jdk-17+35, also known as jdk-17-ga.
- Switch to GA mode.

* Wed Sep 08 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.33-0.3.ea.rolling
- Minor code cleanups on FIPS detection patch and check for SECMOD_GetSystemFIPSEnabled in configure.
- Remove unneeded Requires on NSS as it will now be dynamically linked and detected by RPM.

* Wed Sep 08 2021 Martin Balao <mbalao@redhat.com> - 1:17.0.0.0.33-0.3.ea.rolling
- Detect FIPS using SECMOD_GetSystemFIPSEnabled in the new libsystemconf JDK library.

* Mon Sep 06 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.33-0.2.ea.rolling
- Update RH1655466 FIPS patch with changes in OpenJDK 8 version.
- SunPKCS11 runtime provider name is a concatenation of "SunPKCS11-" and the name in the config file.
- Change nss.fips.cfg config name to "NSS-FIPS" to avoid confusion with nss.cfg.
- No need to substitute path to nss.fips.cfg as java.security file supports a java.home variable.
- Disable FIPS mode support unless com.redhat.fips is set to "true".
- Enable alignment with FIPS crypto policy by default (-Dcom.redhat.fips=false to disable).
- Add explicit runtime dependency on NSS for the PKCS11 provider in FIPS mode
- Move setup of JavaSecuritySystemConfiguratorAccess to Security class so it always occurs (RH1915071)

* Mon Sep 06 2021 Martin Balao <mbalao@redhat.com> - 1:17.0.0.0.33-0.2.ea.rolling
- Support the FIPS mode crypto policy (RH1655466)
- Use appropriate keystore types when in FIPS mode (RH1818909)
- Disable TLSv1.3 when the FIPS crypto policy and the NSS-FIPS provider are in use (RH1860986)

* Mon Aug 30 2021 Jiri Vanek <jvanek@redhat.com> - 1:17.0.0.0.33-0.1.ea.rolling
- alternatives creation moved to posttrans
- Thus fixing the old reisntall issue:
- https://bugzilla.redhat.com/show_bug.cgi?id=1200302
- https://bugzilla.redhat.com/show_bug.cgi?id=1976053

* Fri Jul 30 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.33-0.0.ea.rolling
- Update to jdk-17+33, including JDWP fix and July 2021 CPU
- Resolves: rhbz#1972529

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.0.0.0.26-0.4.ea.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 02 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.26-0.4.ea.rolling
- Use the "reverse" build loop (debug first) as the main and only build loop to get more diagnostics.
- Remove restriction on disabling product build, as debug packages no longer have javadoc packages.

* Mon Jun 28 2021 Petra Alice Mikova <pmikova@redhat.com> - 1:17.0.0.0.26-0.3.ea.rolling
- fix patch rh1648249-add_commented_out_nss_cfg_provider_to_java_security.patch which made the SunPKCS provider show up again
- Resolves: rhbz#1971120

* Thu Jun 24 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1:17.0.0.0.26-0.2.ea.rolling
- Re-enable TestSecurityProperties after inclusion of PR3695

* Thu Jun 24 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:17.0.0.0.26-0.2.ea.rolling
- Add PR3695 to allow the system crypto policy to be turned off

* Thu Jun 24 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1:17.0.0.0.26-0.1.ea.rolling
- Update buildjdkver to 17 so as to build with itself

* Fri Jun 11 2021 Petra Alice Mikova <pmikova@redhat.com> - 1:17.0.0.0.26-0.0.ea.rolling
- update sources to jdk 17.0.0+26
- set is_ga to 0, as this is early access build
- change vendor_version_string
- change path to the version-numbers.conf
- removed rmid binary from files and from slaves
- removed JAVAC_FLAGS=-g from make command, as it breaks the build since JDK-8258407
- add lib/libsyslookup.so to files
- renamed lib/security/blacklisted.certs to lib/security/blocked.certs
- add lib/libsvml.so for intel
- skip debuginfo check for libsyslookup.so on s390x

* Fri May 07 2021 Jiri Vanek <jvanek@redhat.com> -1:16.0.1.0.9-3.rolling
- removed cjc backward comaptiblity, to fix when both rpm 4.16 and 4.17 are in transaction

* Thu Apr 29 2021 Jiri Vanek <jvanek@redhat.com> -  1:16.0.1.0.9-2.rolling
- adapted to newst cjc to fix issue with rpm 4.17
- Disable copy-jdk-configs for Flatpak builds

* Sun Apr 25 2021 Petra Alice Mikova <pmikova@redhat.com> - 1:16.0.1.0.9-1.rolling
- update to 16.0.1+9 april cpu tag
- dropped jdk8259949-allow_cf-protection_on_x86.patch

* Thu Mar 11 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:16.0.0.0.36-2.rolling
- Perform static library build on a separate source tree with bundled image libraries
- Make static library build optional
- Based on initial work by Severin Gehwolf

* Tue Mar 09 2021 Jiri Vanek <jvanek@redhat.com> - 1:16.0.0.0.36-1.rolling
- fixed suggests of wrong pcsc-lite-devel%{?_isa} to correct pcsc-lite-libs%{?_isa}
- bumped buildjdkver to build by itself - 16

* Fri Feb 19 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:16.0.0.0.36-0.rolling
- Update to jdk-16.0.0.0+36
- Update tarball generation script to use git following OpenJDK's move to github
- Update tarball generation script to use PR3823 which handles JDK-8235710 changes
- Use upstream default for version-pre rather than setting it to "ea" or ""
- Drop libsunec.so which is no longer generated, thanks to JDK-8235710
- Drop unnecessary compiler flags, dating back to work on GCC 6 & 10
- Adapt RH1750419 alt-java patch to still apply after some variable re-naming in the makefiles
- Update filever to remove any trailing zeros, as in the OpenJDK build, and use for source filename
- Use system harfbuzz now this is supported.
- Pass SOURCE_DATE_EPOCH to build for reproducible builds

* Fri Feb 19 2021 Stephan Bergmann <sbergman@redhat.com> - 1:15.0.2.0.7-1.rolling
- Hardcode /usr/sbin/alternatives for Flatpak builds

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.0.2.0.7-0.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:15.0.2.0.7-0.rolling
- Update to jdk-15.0.2.0+7
- Add release notes for 15.0.1.0 & 15.0.2.0
- Use JEP-322 Time-Based Versioning so we can handle a future 11.0.9.1-like release correctly.
- Still use 15.0.x rather than 15.0.x.0 for file naming, as the trailing zero is omitted from tags.
- Cleanup debug package descriptions and version number placement.
- Remove unused patch files.

* Tue Jan 19 2021 Andrew Hughes <gnu.andrew@redhat.com> - 1:15.0.1.9-10.rolling
- Use -march=i686 for x86 builds if -fcf-protection is detected (needs CMOV)

* Tue Dec 22 2020 Jiri Vanek <jvanek@redhat.com> - 1:15.0.1.9-9.rolling
- fixed missing condition for fastdebug packages being counted as debug ones

* Sat Dec 19 2020 Jiri Vanek <jvanek@redhat.com> - 1:15.0.1.9-8.rolling
- removed lib-style provides for fastdebug_suffix_unquoted

* Sat Dec 19 2020 Jiri Vanek <jvanek@redhat.com> - 1:15.0.1.9-6.rolling
- many cosmetic changes taken from more maintained jdk11
- introduced debug_arches, bootstrap_arches, systemtap_arches, fastdebug_arches, sa_arches, share_arches, shenandoah_arches, zgc_arches
  instead of various hardcoded ifarches
- updated systemtap
- added requires excludes for debug pkgs
- removed redundant logic around jsa files
- added runtime requires of lksctp-tools and libXcomposite%
- added and used Source15 TestSecurityProperties.java, but is made always positive as jdk15 now does not honor system policies
- s390x excluded form fastdebug build

* Thu Dec 17 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:15.0.1.9-5.rolling
- introduced nm based check to verify alt-java on x86_64 is patched, and no other alt-java or java is patched
- patch600 rh1750419-redhat_alt_java.patch amended to die, if it is used wrongly
- introduced ssbd_arches with currently only valid arch of x86_64 to separate real alt-java architectures

* Wed Dec 9 2020 Jiri Vanek <jvanek@redhat.com> - 1:15.0.1.9-4.rolling
- moved wrongly placed licenses to accompany other ones
- this bad placement was killng parallel-installability and thus having bad impact to leapp if used

* Tue Dec 01 2020 Jiri Vanek <jvanek@redhat.com> - 1:15.0.1.9-3.rolling
- added patch600, rh1750419-redhat_alt_java.patch, suprassing removed patch
- no longer copying of java->alt-java as it is created by  patch600

* Mon Nov 23 2020 Jiri Vanek <jvanek@redhat.com> - 1:15.0.1.9-2.rolling
- Create a copy of java as alt-java with alternatives and man pages
- java-11-openjdk doesn't have a JRE tree, so don't try and copy alt-java there...

* Sun Oct 25 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:15.0.1.9-1.rolling
- updated to October CPU 2020 sources

* Thu Oct 22 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:15.0.0.36-4.rolling
- Fix directory ownership of -static-libs sub-package.

* Fri Oct 09 2020 Jiri Vanek <jvanek@redhat.com> - 1:15.0.0.36-3.rolling
- Build static-libs-image and add resulting files via -static-libs sub-package.
- Disable stripping of debug symbols for static libraries part of the -static-libs sub-package.
- JDK-8245832 increases the set of static libraries, so try and include them all with a wildcard.
- Update static-libs packaging to new layout

* Mon Sep 21 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:15.0.0.36-2.rolling
- Add support for fastdebug builds on 64 bit architectures

* Tue Sep 15 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:15.0.0.36-1.rolling
- Remove EA designation
- Re-generate sources with PR3803 patch

* Mon Aug 31 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:15.0.0.36-0.1.ea.rolling
- Update to jdk 15.0.0.36 tag
- Modify rh1648249-add_commented_out_nss_cfg_provider_to_java_security.patch
- Update vendor version string to 20.9
- jjs removed from packaging after JEP 372: Nashorn removal
- rmic removed from packaging after JDK-8225319

* Mon Jul 27 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:14.0.2.12-2.rolling
- Disable LTO so as to pass debuginfo check

* Wed Jul 22 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:14.0.2.12-1.rolling
- update to jdk 14.0.2.12 CPU version
- remove upstreamed patch jdk8237879-make_4_3_build_fixes.patch
- remove upstreamed patch jdk8235833-posixplatform_cpp_should_not_include_sysctl_h.patch
- remove upstreamed patch jdk8243059-build_fails_when_with_vendor_contains_comma.patch

* Thu Jul 09 2020 Andrew Hughes <gnu.andrew@redhat.com> - 1:14.0.1.7-4.rolling
- Re-introduce java-openjdk-src & java-openjdk-demo for system_jdk builds.
- Fix accidental renaming of java-openjdk-devel to java-devel-openjdk.

* Thu May 14 2020 Petra Alice Mikova <pmikova@redhat.com> -  1:14.0.1.7-3.rolling
- introduce patch jdk8235833-posixplatform_cpp_should_not_include_sysctl_h to fix build issues in rawhide
- rename and reorganize patch sections

* Thu Apr 23 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:14.0.1.7-2.rolling
- Fix vendor version to 20.3 (from 19.9)

* Fri Apr 17 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:14.0.1.7-1.rolling
- April security update
- uploaded new src tarball

* Wed Apr 08 2020 Jiri Vanek <jvanek@redhat.com> - 1:14.0.0.36-4.rolling
- set vendor property and vendor urls
- made urls to be preconfigured by os

* Tue Mar 24 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:14.0.0.36-3.rolling
- Remove s390x workaround flags for GCC 10
- bump buildjdkver to 14
- uploaded new src tarball

* Mon Mar 23 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:14.0.0.36-2.rolling
- removed a whitespace causing fail of postinstall script
- removed backslashes at the end of alternatives command

* Fri Mar 13 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:14.0.0.36-1.rolling
- update to jdk 14+36 ga build
- remove JDK-8224851 patch, as OpenJDK 14 already contains it
- removed pack200 and unpack200 binaries, slaves, manpages and libunpack.so library
- added listings for jpackage binary, manpages and added slave records to alternatives

* Thu Mar 12 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.2.8-4.rolling
- add patch for build issues with make 4.3

* Thu Feb 27 2020 Severin Gehwolf <sgehwolf@redhat.com> - 1:13.0.2.8-3.rolling
- add workaround for issues with build with GCC10 on s390x (see RHBZ#1799531)
- fix issues with build with GCC10: JDK-8224851, -fcommon switch

* Thu Feb 27 2020 Petra Alice Mikova pmikova@redhat.com> - 1:13.0.2.8-3.rolling
- Add JDK-8224851 patch to resolve aarch64 issues

* Tue Feb 04 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.2.8-2.rolling
- fix Release, as it was broken by last rpmdev-bumpspec

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:13.0.2.8-1.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.2.8-1.rolling
- removed patch jdk8231405_guarantee_d_nonequals_null_failed_null_dominator_info.patch
- removed patch jdk8231583_fix_register_clash_in_sbsa_resolve_forwarding_pointer_borrowing.patch
- updated sources to the 13.0.2+8 tag

* Fri Oct 25 2019 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.1.9-2.rolling
- Fixed hardcoded major version in jdk13u to macro
- added jdk8231405_guarantee_d_nonequals_null_failed_null_dominator_info.patch
- added jdk8231583_fix_register_clash_in_sbsa_resolve_forwarding_pointer_borrowing.patch

* Mon Oct 21 2019 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.1.9-1.rolling
- Updated to October 2019 CPU sources

* Wed Oct 16 2019 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.0.33-3.rolling
- synced up generate tarball script with other OpenJDK packages
- dropped pr2126-synchronise_elliptic_curves_in_sun_security_ec_namedcurve_with_those_listed_by_nss.patch from the sources
- regenerated sources with the updated script

* Wed Oct 02 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:13.0.0.33-3.rolling
- Switch to in-tree SunEC code, dropping NSS runtime dependencies and patches to link against it.

* Wed Oct 02 2019 Andrew John Hughes <gnu.andrew@redhat.com> -  1:13.0.0.33-3.rolling
- Drop unnecessary build requirement on gtk3-devel, as OpenJDK searches for Gtk+ at runtime.
- Add missing build requirement for libXrender-devel, previously masked by Gtk3+ dependency
- Add missing build requirement for libXrandr-devel, previously masked by Gtk3+ dependency
- fontconfig build requirement should be fontconfig-devel, previously masked by Gtk3+ dependency

* Wed Oct 02 2019 Andrew Hughes <gnu.andrew@redhat.com> - 1:13.0.0.33-3.rolling
- Obsolete javadoc-slowdebug and javadoc-slowdebug-zip packages via javadoc and javadoc-zip respectively.

* Tue Oct 01 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:13.0.0.33-2.rolling
- Don't produce javadoc/javadoc-zip sub packages for the
  debug variant build.
- Don't perform a bootcycle build for the debug variant build.

* Mon Sep 30 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:13.0.0.33-2.rolling
- Fix vendor version as JDK 13 has been GA'ed September 2019: 19.3 => 19.9

* Wed Aug 14 2019 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.0.33-1.rolling
- updated to 13+33 sources
- added two manpages to file listings (jfr, jaotc)
- set is_ga to 1 to match build from jdk.java.net

* Fri Jul 26 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:13.0.0.28-0.2.ea.rolling
- Fix bootjdkver macro. It attempted to build with jdk 12, which is
  no longer available in rawhide (it's 13 instead).
- Fix Release as rpmdev-bumpspec doesn't do it correctly.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:13.0.0.28-0.1.ea.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Petra Alice Mikova <pmikova@redhat.com> - 1:13.0.0.28-0.1.ea.rolling
- updated to jdk 13
- adapted pr2126-synchronise_elliptic_curves_in_sun_security_ec_namedcurve_with_those_listed_by_nss.patch
- adapted rh1648242-accessible_toolkit_crash_do_not_break_jvm.patch
- fixed file listings
- included https://src.fedoraproject.org/rpms/java-11-openjdk/pull-request/49:
- Include 'ea' designator in Release when appropriate
- Handle milestone as variables so we can alter it easily and set the docs zip filename appropriately

* Tue May 21 2019 Petra Alice Mikova <pmikova@redhat.com> - 1:12.0.1.12-2.rolling
- fixed requires/provides for the non-system JDK case (backport of RHBZ#1702324)

* Thu Apr 18 2019 Petra Mikova <pmikova@redhat.com> - 1:12.0.1.12-1.rolling
- updated sources to current CPU release

* Thu Apr 04 2019 Petra Mikova <pmikova@redhat.com> - 1:12.0.0.33-4.rolling
- added slave for jfr binary in devel package

* Thu Mar 21 2019 Petra Mikova <pmikova@redhat.com> - 1:12.0.0.33-3.rolling
- Replaced pcsc-lite-devel (which is in optional channel) with pcsc-lite-libs.
- added rh1684077-openjdk_should_depend_on_pcsc-lite-libs_instead_of_pcsc-lite-devel.patch to make jdk work with pcsc
- removed LTS string from LTS designator, because epel builds get identified as rhel and JDK 12 is not LTS
- removed duplicated dependency on lksctp-tools

* Wed Mar 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1:12.0.0.33-2.ea.1.rolling
- Drop chkconfig dep, 1.7 shipped in f24

* Thu Mar 07 2019 Petra Mikova <pmikova@redhat.com> - 1:12.0.0.33-1.ea.1.rolling
- bumped sources to jdk12+33

* Mon Feb 11 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1:12.0.0.30-1.ea.1.rolling
- Only build 'bootcycle-images docs' target and 'images docs' targets, respectively.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.0.0.25-0.ea.1.rolling.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Jiri Vanek <jvanek@redhat.com> - 1:12.0.0.25-0.ea.1.rolling
- bumped sources to jdk12. Crypto list synced.
- adapted patches to usptream (removed are upstreamed)
- removed fixed upstreamed patch6, jdk8211105-aarch64-disable_cos_sin_and_log_intrinsics.patch:
- renamed patch5, pr1983-rh1565658-..._sunec_provider_jdk11.patch to pr1983-rh1565658-..._sunec_provider_jdk12.patch
- adapted patch5, pr1983-rh1565658 to jdk12 (libraries.m4 and /Lib-jdk.crypto.ec.gmk)
- removed patch8, jdk8210416-rh1632174-compile_fdlibm_with_o2_ffp_contract_off_on_gcc_clang_arches.patch
- removed patch9, jdk8210425-rh1632174-sharedRuntimeTrig_sharedRuntimeTrans_compiled_without_optimization.patch
- removed patch10, jdk8210647-rh1632174. Is rummored to be in upstream
- removed patch11, jdk8210761-rh1632174-libjsig_is_being_compiled_without_optimization.patch
- removed patch12, jdk8210703-rh1632174-vmStructs_cpp_no_longer_compiled_with_o0
- removed patch584, jdk8209639-rh1640127-02-coalesce_attempted_spill_non_spillable.patch
- removed patch585, jdk8209639-rh1640127-02-coalesce_attempted_spill_non_spillable.patch
- set build jdk to jdk11; buildjdkver set to 11
- todo, revisit _privatelibs and slaves, discuse patch10, more?
- now building with --no-print-directory to workaround JDK8215213
- renamed original of docs zip to jdk-major+build
- check shenandaoh with -XX:+UnlockExperimentalVMOptions
- libjli moved from lib/libjli to lib
- added lib/jspawnhelper and bin/jfr and conf/sdp/sdp.conf.template
- added explanation to the --no-print-directory
- re-added lts_designator_zip macro
- added patch6 for rh1673833-remove_removal_of_wformat_during_test_compilation.patch

* Wed Dec 5 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.1.13-10.rolling
- for non debug supackages, ghosted all masters and slaves (rhbz1649776)
- for tech-preview packages, if-outed versionless provides. Aligned versions to be %%{epoch}:%%{version}-%%{release} instead of chaotic
- Removed all slowdebug provides (rhbz1655938); for tech-preview packages also removed all internal provides

* Tue Dec 04 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:11.0.1.13-9
- Added %%global _find_debuginfo_opts -g
- Resolves: RHBZ#1520879 (Detailed NMT issue)

* Fri Nov 30 2018 Jiri Vanek <jvanek@redhat.com> - 1:11.0.1.13-8
- added rolling suffix to release (before dist) to prevent conflict with java-11-openjdk which now have same major version

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
