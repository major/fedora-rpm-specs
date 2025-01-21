# Hi Googlers! If you're looking in here for patches, nifty.
# You (and everyone else) are welcome to use any of my Chromium spec files and
# patches under the terms of the GPLv2 or later.
# You (and everyone else) are welcome to use any of my V8-specific spec files
# and patches under the terms of the BSD license.
# You (and everyone else) may NOT use my spec files or patches under any other
# terms.
# I hate to be a party-pooper here, but I really don't want to help Google
# make a proprietary browser. There are enough of those already.
# All copyrightable work in these spec files and patches is Copyright 2011
# Tom Callaway <spot@fedoraproject.org>

# This package is like a horrible time capsule. If you're reading this, it
# is never too late to turn back.

# For the 1.2 branch, we use 0s here
# For 1.3+, we use the three digit versions
# Hey, now there are four digits. What do they mean? Popsicle.
%global somajor 3
%global sominor 14
%global sobuild 5
%global sotiny 10
%global sover %{somajor}.%{sominor}.%{sobuild}
%global truename v8
# You don't really want to turn this on, because the "v8" package has this, and we'd
# conflict for no good reason.
%global with_python 0

Name:		%{truename}-314
Version:	%{somajor}.%{sominor}.%{sobuild}.%{sotiny}
Release:	39%{?dist}
Summary:	JavaScript Engine
License:	BSD-3-Clause
URL:		https://developers.google.com/v8/
# Once found at http://commondatastorage.googleapis.com/chromium-browser-official/
# Now, we're the canonical source for the tarball. :/
Source0:	v8-%{version}.tar.bz2
ExclusiveArch:	%{ix86} x86_64 %{arm} mips mipsel ppc ppc64
BuildRequires:	scons, readline-devel, libicu-devel
BuildRequires:	valgrind-devel
BuildRequires:	gcc, gcc-c++

#backport fix for CVE-2013-2634 (RHBZ#924495)
Patch1:		v8-3.14.5.8-CVE-2013-2634.patch

#backport fix for CVE-2013-2882 (RHBZ#991116)
Patch2:		v8-3.14.5.10-CVE-2013-2882.patch

#backport fix for CVE-2013-6640 (RHBZ#1039889)
Patch3:		v8-3.14.5.10-CVE-2013-6640.patch

#backport fix for enumeration for objects with lots of properties
#   https://codereview.chromium.org/11362182
Patch4:		v8-3.14.5.10-enumeration.patch

#backport fix for CVE-2013-6640 (RHBZ#1059070)
Patch5:		v8-3.14.5.10-CVE-2013-6650.patch

#backport only applicable fix for CVE-2014-1704 (RHBZ#1077136)
#the other two patches don't affect this version of v8
Patch6:		v8-3.14.5.10-CVE-2014-1704-1.patch

# use clock_gettime() instead of gettimeofday(), which increases performance
# dramatically on virtual machines
# https://github.com/joyent/node/commit/f9ced08de30c37838756e8227bd091f80ad9cafa
# see above link or head of patch for complete rationale
Patch7:		v8-3.14.5.10-use-clock_gettime.patch

# fix corner case in x64 compare stubs
# fixes bug resulting in an incorrect result when comparing certain integers
# (e.g. 2147483647 > -2147483648 is false instead of true)
# https://code.google.com/p/v8/issues/detail?id=2416
# https://github.com/joyent/node/issues/7528
Patch8:		v8-3.14.5.10-x64-compare-stubs.patch

# backport security fix for memory corruption/stack overflow (RHBZ#1125464)
# https://groups.google.com/d/msg/nodejs/-siJEObdp10/2xcqqmTHiEMJ
# https://github.com/joyent/node/commit/530af9cb8e700e7596b3ec812bad123c9fa06356
Patch9:		v8-3.14.5.10-mem-corruption-stack-overflow.patch

# backport bugfix for x64 MathMinMax:
#   Fix x64 MathMinMax for negative untagged int32 arguments.
#   An untagged int32 has zeros in the upper half even if it is negative.
#   Using cmpq to compare such numbers will incorrectly ignore the sign.
# https://github.com/joyent/node/commit/3530fa9cd09f8db8101c4649cab03bcdf760c434
Patch10:	v8-3.14.5.10-x64-MathMinMax.patch

# backport bugfix that eliminates unused-local-typedefs warning
# https://github.com/joyent/node/commit/53b4accb6e5747b156be91a2b90f42607e33a7cc
Patch11:	v8-3.14.5.10-unused-local-typedefs.patch

# backport security fix: Fix Hydrogen bounds check elimination
# resolves CVE-2013-6668 (RHBZ#1086120)
# https://github.com/joyent/node/commit/fd80a31e0697d6317ce8c2d289575399f4e06d21
Patch12:	v8-3.14.5.10-CVE-2013-6668.patch

# backport fix to segfault caused by the above patch
# https://github.com/joyent/node/commit/3122e0eae64c5ab494b29d0a9cadef902d93f1f9
Patch13:	v8-3.14.5.10-CVE-2013-6668-segfault.patch

# Use system valgrind header
# https://bugzilla.redhat.com/show_bug.cgi?id=1141483
Patch14:	v8-3.14.5.10-system-valgrind.patch

# Fix issues with abort on uncaught exception
# https://github.com/joyent/node/pull/8666
# https://github.com/joyent/node/issues/8631
# https://github.com/joyent/node/issues/8630
Patch15:	v8-3.14.5.10-abort-uncaught-exception.patch

# Fix unhandled ReferenceError in debug-debugger.js
# https://github.com/joyent/node/commit/0ff51c6e063e3eea9e4d9ea68edc82d935626fc7
# https://codereview.chromium.org/741683002
Patch16:	v8-3.14.5.10-unhandled-ReferenceError.patch

# Don't busy loop in CPU profiler thread
# https://github.com/joyent/node/pull/8789
Patch17:	v8-3.14.5.10-busy-loop.patch

# Log V8 version in profiler log file
# (needed for compatibility with profiler tools)
# https://github.com/joyent/node/pull/9043
# https://codereview.chromium.org/806143002
Patch18:	v8-3.14.5.10-profiler-log.patch

# Fix CVE in ARM code
# https://bugzilla.redhat.com/show_bug.cgi?id=1101057
# https://codereview.chromium.org/219473002
Patch19:	v8-3.4.14-CVE-2014-3152.patch

# Add REPLACE_INVALID_UTF8 handling that nodejs needs
Patch20:	v8-3.14.5.10-REPLACE_INVALID_UTF8.patch

# mips support (from debian)
Patch21:	0002_mips.patch
Patch22:	0002_mips_r15102_backport.patch
Patch23:	0002_mips_r19121_backport.patch

# Forced whole instruction cache flushing on Loongson (from debian)
Patch24:	0012_loongson_force_cache_flush.patch

# ppc/ppc64 support (from Ubuntu, who got it from IBM)
# Rediffed from 0099_powerpc_support.patch
Patch25:	v8-powerpc-support.patch

# Fix for CVE-2016-1669 (thanks to bhoordhuis)
Patch26:	v8-3.14.5.10-CVE-2016-1669.patch

# Report builtins by name
# https://github.com/nodejs/node/commit/5a60e0d904c38c2bdb04785203b1b784967c870d
Patch27:	v8-3.14.5.10-report-builtins-by-name.patch

# Fix compile with gcc7
# (thanks to Ben Noordhuis)
Patch28:	v8-3.14.5.10-gcc7.patch

# MOAR PPC
Patch29:	v8-powerpc-support-SConstruct.patch

# GCC8 HAPPY FUN TIME
Patch30:	v8-3.14.5.10-gcc8.patch

# Python3
Patch31:	v8-314-python3.patch

# gcc-11 diagnostics
Patch32:	v8-314-gcc11.patch

# Disable -Werror
Patch33:	v8-3.14.5.10-no-Werror.patch

%description
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used 
in Google Chrome, the open source browser from Google. V8 implements ECMAScript 
as specified in ECMA-262, 3rd edition. This is version 3.14, which is no longer
maintained by Google, but was adopted by a lot of other software.

%package devel
Summary:	Development headers and libraries for v8
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for v8 3.14.

%if 0%{?with_python}
%package python
Summary:	Python libraries from v8
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description python
Python libraries from v8.
%endif

%prep
%setup -q -n %{truename}-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1 -b .system-valgrind
%patch -P15 -p1 -b .abort-uncaught-exception
%patch -P16 -p1 -b .unhandled-ReferenceError
%patch -P17 -p1 -b .busy-loop
%patch -P18 -p1 -b .profiler-log
%patch -P19 -p1 -b .cve20143152
%patch -P20 -p1 -b .riu
%patch -P21 -p1 -b .mips
%patch -P22 -p1 -b .r15102
%patch -P23 -p1 -b .r19121
%patch -P24 -p1 -b .loongson
%patch -P25 -p1 -b .ppc
%patch -P26 -p1 -b .CVE-2016-1669
%patch -P27 -p1 -b .builtinname
%patch -P28 -p1 -b .gcc7
%patch -P29 -p1 -b .ppc-harder
%patch -P30 -p1 -b .gcc8
%patch -P31 -p1 -b .python3
%patch -P32 -p1 -b .gcc11
%patch -P33 -p1 -b .no-error

# Do not need this lying about.
rm -rf src/third_party/valgrind

#Patch7 needs -lrt on glibc < 2.17 (RHEL <= 6)
%if (0%{?rhel} > 6 || 0%{?fedora} > 18)
%global lrt %{nil}
%else
%global lrt -lrt
%endif

# -fno-strict-aliasing is needed with gcc 4.4 to get past some ugly code
PARSED_OPT_FLAGS=`echo \'$RPM_OPT_FLAGS %{lrt} -fPIC -fno-strict-aliasing -Wno-unused-parameter -Wno-error=strict-overflow -Wno-unused-but-set-variable -Wno-error=cast-function-type -Wno-error=class-memaccess -Wno-error=stringop-overflow= -Wno-error=array-bounds -Wno-error=dangling-pointer= -Wno-error=use-after-free -fno-delete-null-pointer-checks\'| sed "s/ /',/g" | sed "s/',/', '/g"`
sed -i "s|'-O3',|$PARSED_OPT_FLAGS,|g" SConstruct

# clear spurious executable bits
find . \( -name \*.cc -o -name \*.h -o -name \*.py \) -a -executable \
  |while read FILE ; do
    echo $FILE
    chmod -x $FILE
  done

%build
mkdir -p obj/release/
export GCC_VERSION="44"

# SCons is going away, but for now build with
# I_know_I_should_build_with_GYP=yes
scons library=shared snapshots=on \
%ifarch x86_64
arch=x64 \
%endif
%ifarch ppc64
arch=ppc64 \
%endif
%ifarch ppc
arch=ppc \
%endif
%ifarch armv7hl armv7hnl
armeabi=hard \
%endif
%ifarch armv5tel armv6l armv7l
armeabi=soft \
%endif
visibility=default \
env=CCFLAGS:"-fPIC" \
I_know_I_should_build_with_GYP=yes

%if 0%{?fedora} >= 16
export ICU_LINK_FLAGS=`pkg-config --libs-only-l icu-i18n`
%else
export ICU_LINK_FLAGS=`pkg-config --libs-only-l icu`
%endif

# When will people learn to create versioned shared libraries by default?
# first, lets get rid of the old .so file
rm -rf libv8.so libv8preparser.so
# Now, lets make it right.
g++ $RPM_OPT_FLAGS -fPIC -o libv8preparser.so.%{sover} -shared -Wl,-soname,libv8preparser.so.%{somajor} \
	src/allocation.os \
	src/bignum.os \
	src/bignum-dtoa.os \
	src/cached-powers.os \
	src/diy-fp.os \
	src/dtoa.os \
	src/fast-dtoa.os \
	src/fixed-dtoa.os \
	src/preparse-data.os \
	src/preparser-api.os \
	src/preparser.os \
	src/scanner.os \
	src/strtod.os \
	src/token.os \
	src/unicode.os \
	src/utils.os

# "obj/release/preparser-api.os" should not be included in the libv8.so file.
export RELEASE_BUILD_OBJS=`echo src/*.os | sed 's|src/preparser-api.os||g'`

%ifarch %{arm}
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/arm/*.os $ICU_LINK_FLAGS
%endif
%ifarch %{ix86}
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/ia32/*.os $ICU_LINK_FLAGS
%endif
%ifarch x86_64
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/x64/*.os $ICU_LINK_FLAGS
%endif
%ifarch mips
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/mips/*.os $ICU_LINK_FLAGS
%endif
%ifarch mipsel
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/mipsel/*.os $ICU_LINK_FLAGS
%endif
%ifarch ppc ppc64
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/ppc/*.os $ICU_LINK_FLAGS
%endif


# We need to do this so d8 can link against it.
ln -sf libv8.so.%{sover} libv8.so
ln -sf libv8preparser.so.%{sover} libv8preparser.so

# This will fail to link d8 because it doesn't use the icu libs.
# Don't build d8 shared. Stupid Google. Hate.
# SCons is going away, but for now build with
# I_know_I_should_build_with_GYP=yes
scons d8 \
I_know_I_should_build_with_GYP=yes \
%ifarch x86_64
arch=x64 \
%endif
%ifarch armv7hl armv7hnl
armeabi=hard \
%endif
%ifarch armv5tel armv6l armv7l
armeabi=soft \
%endif
%ifarch ppc64
arch=ppc64 \
%endif
%ifarch ppc
arch=ppc \
%endif
snapshots=on console=readline visibility=default || :
# library=shared snapshots=on console=readline visibility=default || :

# Sigh. I f*****g hate scons.
# But gyp is worse.
# rm -rf d8

# g++ $RPM_OPT_FLAGS -o d8 obj/release/d8.os -lreadline -lpthread -L. -lv8 $ICU_LINK_FLAGS

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_includedir}/v8-3.14/
mkdir -p %{buildroot}%{_libdir}
install -p include/*.h %{buildroot}%{_includedir}/v8-3.14/
install -p libv8.so.%{sover} %{buildroot}%{_libdir}
install -p libv8preparser.so.%{sover} %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 d8 %{buildroot}%{_bindir}/d8-314

pushd %{buildroot}%{_libdir}
ln -sf libv8.so.%{sover} libv8.so
ln -sf libv8.so.%{sover} libv8.so.%{somajor}
ln -sf libv8.so.%{sover} libv8.so.%{somajor}.%{sominor}
ln -sf libv8preparser.so.%{sover} libv8preparser.so
ln -sf libv8preparser.so.%{sover} libv8preparser.so.%{somajor}
ln -sf libv8preparser.so.%{sover} libv8preparser.so.%{somajor}.%{sominor}
popd

chmod -x %{buildroot}%{_includedir}/v8-3.14/v8*.h

mkdir -p %{buildroot}%{_includedir}/v8-3.14/v8/extensions/
install -p src/extensions/*.h %{buildroot}%{_includedir}/v8-3.14/v8/extensions/

chmod -x %{buildroot}%{_includedir}/v8-3.14/v8/extensions/*.h

%if 0%{?with_python}
# install Python JS minifier scripts for nodejs
install -d %{buildroot}%{python_sitelib}
sed -i 's|/usr/bin/python2.4|/usr/bin/env python|g' tools/jsmin.py
sed -i 's|/usr/bin/python2.4|/usr/bin/env python|g' tools/js2c.py
install -p -m0744 tools/jsmin.py %{buildroot}%{python_sitelib}/
install -p -m0744 tools/js2c.py %{buildroot}%{python_sitelib}/
chmod -R -x %{buildroot}%{python_sitelib}/*.py*
%endif

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog
%license LICENSE
%{_bindir}/d8-314
%{_libdir}/*.so.*

%files devel
%{_includedir}/v8-3.14/
%{_libdir}/*.so

%if 0%{?with_python}
%files python
%{python2_sitelib}/j*.py*
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-38
- Rebuild for ICU 76

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 10 2024 Tom Callaway <spot@fedoraproject.org> - 3.14.5.10-36
- disable -Werror. This package is filled with worms, we know it.
- fix license tag

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 3.14.5.10-33
- Rebuilt for ICU 73.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-31
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.14.5.10-30
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Tom Callaway <spot@fedoraproject.org> - 3.14.5.10-28
- "fix" FTBFS

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-25
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-24
- Rebuild for ICU 69

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 18 2020 Jeff Law <law@redhat.com> - 3.14.5.10-22
- Fix diagnostics reported by gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-20
- Rebuild for ICU 67

* Thu Feb  6 2020 Tom Callaway <spot@fedoraproject.org> - 3.14.5.10-19
- it is alive! (what have i done)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.14.5.10-16
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-14
- Rebuild for ICU 63

* Tue Jul 24 2018 Tom Callaway <spot@fedoraproject.org> - 3.14.5.10-13
- add BuildRequires: gcc, gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-11
- Rebuild for ICU 62

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 3.14.5.10-10
- fix build of this dinosaur with gcc8, mostly by telling the compiler to ignore all the nasty code errors

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.14.5.10-8
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Tom Callaway <spot@fedoraproject.org> - 3.14.5.10-5
- fix FTBFS (thanks to Ben Noordhuis)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 25 2016 Tom Callaway <spot@fedoraproject.org> - 3.14.5.10-3
- drop epoch (new package, doesn't need it)

* Wed Jul  6 2016 Tom Callaway <spot@fedoraproject.org> - 1:3.14.5.10-2
- apply fixes from nodejs for CVE-2016-1669 and reporting builtins by name

* Tue Jun  7 2016 Tom Callaway <spot@fedoraproject.org> - 1:3.14.5.10-1
- make into v8-314 package

* Mon Jun 06 2016 Vít Ondruch <vondruch@redhat.com> - 1:3.14.5.10-24
- Use "-fno-delete-null-pointer-checks" to workaround GCC 6.x compatibility
  (rhbz#1331480, rhbz#1331458).

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.14.5.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1:3.14.5.10-22
- rebuild for ICU 56.1

* Mon Sep 21 2015 Tom Callaway <spot@fedoraproject.org> - 1:3.14.5.10-21
- add REPLACE_INVALID_UTF8 code needed for nodejs

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.14.5.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  8 2015 Tom Callaway <spot@fedoraproject.org> - 1:3.14.5.10-19
- split off python subpackage (bz 959145)

* Thu Apr 23 2015 Tom Callaway <spot@fedoraproject.org> - 1:3.14.5.10-18
- backport security fix for ARM - CVE-2014-3152

* Thu Feb 19 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-17
- backports for nodejs 0.10.36

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1:3.14.5.10-16
- rebuild for ICU 54.1

* Tue Dec  2 2014 Tom Callaway <spot@fedoraproject.org> - 1:3.14.5.10-15
- use system valgrind header (bz1141483)

* Wed Sep 17 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-14
- backport bugfix that eliminates unused-local-typedefs warning
- backport security fix: Fix Hydrogen bounds check elimination (CVE-2013-6668; RHBZ#1086120)
- backport fix to segfault caused by the above patch

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1:3.14.5.10-13
- rebuild for ICU 53.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.14.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-11
- backport security fix for memory corruption and stack overflow (RHBZ#1125464)
  https://groups.google.com/d/msg/nodejs/-siJEObdp10/2xcqqmTHiEMJ
- backport bug fix for x64 MathMinMax for negative untagged int32 arguments.
  https://github.com/joyent/node/commit/3530fa9cd09f8db8101c4649cab03bcdf760c434

* Thu Jun 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-10
- fix corner case in integer comparisons (v8 bug#2416; nodejs bug#7528)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.14.5.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-8
- use clock_gettime() instead of gettimeofday(), which increases V8 performance
  dramatically on virtual machines

* Tue Mar 18 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-7
- backport fix for unsigned integer arithmetic (RHBZ#1077136; CVE-2014-1704)

* Mon Feb 24 2014 Tomas Hrcka <thrcka@redhat.com> - 1:3.14.5.10-6
- Backport fix for incorrect handling of popular pages (RHBZ#1059070; CVE-2013-6640)

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-5
- rebuild for icu-52

* Mon Jan 27 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-4
- backport fix for enumeration for objects with lots of properties

* Fri Dec 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-3
- backport fix for out-of-bounds read DoS (RHBZ#1039889; CVE-2013-6640)

* Fri Aug 02 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-2
- backport fix for remote DoS or unspecified other impact via type confusion
  (RHBZ#991116; CVE-2013-2882)

* Wed May 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.10-1
- new upstream release 3.14.5.10

* Mon May 06 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:3.14.5.8-2
- Fix ownership of include directory (#958729)

* Fri Mar 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.14.5.8-1
- new upstream release 3.14.5.8
- backport security fix for remote DoS via crafted javascript (RHBZ#924495; CVE-2013-2632)

* Mon Mar 11 2013 Stephen Gallagher <sgallagh@redhat.com> - 1:3.14.5.7-3
- Update to v8 3.14.5.7 for Node.js 0.10.0

* Sat Jan 26 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:3.13.7.5-2
- rebuild for icu-50
- ignore new GCC 4.8 warning

* Tue Dec  4 2012 Tom Callaway <spot@fedoraproject.org> - 1:3.13.7.5-1
- update to 3.13.7.5 (needed for chromium 23)
- Resolves multiple security issues (CVE-2012-5120, CVE-2012-5128)
- d8 is now using a static libv8, resolves bz 881973)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul  6 2012 Tom Callaway <spot@fedoraproject.org> 1:3.10.8-1
- update to 3.10.8 (chromium 20)

* Tue Jun 12 2012 Tom Callaway <spot@fedoraproject.org> 1:3.9.24-1
- update to 3.9.24 (chromium 19)

* Mon Apr 23 2012 Thomas Spura <tomspur@fedoraproject.org> 1:3.7.12.6
- rebuild for icu-49

* Fri Mar 30 2012 Dennis Gilmore <dennis@ausil.us> 1:3.7.12-5
- make sure the right arm abi is used in the second call of scons

* Thu Mar 29 2012 Dennis Gilmore <dennis@ausil.us> 1:3.7.12-4
- use correct arm macros
- use the correct abis for hard and soft float

* Tue Mar 20 2012 Tom Callaway <spot@fedoraproject.org> 3.7.12-3
- merge changes from Fedora spec file, sync, add epoch

* Fri Feb 17 2012 Tom Callaway <spot@fedoraproject.org> 3.7.12-2
- add -Wno-error=strict-overflow for gcc 4.7 (hack, hack, hack)

* Mon Feb 13 2012 Tom Callaway <spot@fedoraproject.org> 3.7.12-1
- update to 3.7.12

* Thu Nov  3 2011 Tom Callaway <spot@fedoraproject.org> 3.5.10-1
- update to 3.5.10

* Mon Sep 26 2011 Tom Callaway <spot@fedoraproject.org> 3.4.14-2
- final 3.4.14 tag
- include JavaScript minifier scripts in -devel

* Fri Jun 10 2011 Tom Callaway <spot@fedoraproject.org> 3.2.10-1
- tag 3.2.10

* Thu Apr 28 2011 Tom Callaway <spot@fedoraproject.org> 3.1.8-1
- "stable" v8 match for "stable" chromium (tag 3.1.8)

* Tue Feb 22 2011 Tom Callaway <spot@fedoraproject.org> 3.1.5-1.20110222svn6902
- update to 3.1.5
- enable experimental i18n icu stuff for chromium

* Tue Jan 11 2011 Tom Callaway <spot@fedoraproject.org> 3.0.7-1.20110111svn6276
- update to 3.0.7

* Tue Dec 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.0-2.20101209svn5957
- fix sloppy code where NULL is used

* Thu Dec  9 2010 Tom "spot" Callaway <tcallawa@redhat.com> 3.0.0-1.20101209svn5957
- update to 3.0.0

* Fri Oct 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.5.1-1.20101022svn5692
- update to 2.5.1
- fix another fwrite with no return checking case

* Thu Oct 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.5.0-1.20101014svn5625
- update to 2.5.0

* Mon Oct  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.4.8-1.20101004svn5585
- update to 2.4.8

* Tue Sep 14 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.4.3-1.20100914svn5450
- update to 2.4.3

* Tue Aug 31 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.11-1.20100831svn5385
- update to svn5385

* Fri Aug 27 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.11-1.20100827svn5365
- update to 2.3.11, svn5365

* Tue Aug 24 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.10-1.20100824svn5332
- update to 2.3.10, svn5332

* Wed Aug 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.9-1.20100819svn5308
- update to 2.3.9, svn5308

* Wed Aug 11 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.7-1.20100812svn5251
- update to svn5251

* Wed Aug 11 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.7-1.20100811svn5248
- update to 2.3.7, svn5248

* Tue Aug 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.6-1.20100809svn5217
- update to 2.3.6, svn5217

* Fri Aug  6 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.5-1.20100806svn5198
- update to 2.3.5, svn5198

* Mon Jul 26 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.3-1.20100726svn5134
- update to 2.3.3, svn5134

* Fri Jul 16 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.0-1.20100716svn5088
- update to 2.3.0, svn5088

* Tue Jul  6 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.22-1.20100706svn5023
- update to 2.2.22, svn5023

* Fri Jul  2 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.21-1.20100702svn5010
- update to svn5010

* Wed Jun 30 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.21-1.20100630svn4993
- update to 2.2.21, svn4993
- include checkout script

* Thu Jun  3 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.14-1.20100603svn4792
- update to 2.2.14, svn4792

* Tue Jun  1 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.13-1.20100601svn4772
- update to 2.2.13, svn4772

* Thu May 27 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.12-1.20100527svn4747
- update to 2.2.12, svn4747

* Tue May 25 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.11-1.20100525svn4718
- update to 2.2.11, svn4718

* Thu May 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-1.20100520svn4684
- update to svn4684

* Mon May 17 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.10-1.20100517svn4664
- update to 2.2.10, svn4664

* Thu May 13 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.9-1.20100513svn4653
- update to svn4653

* Mon May 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.9-1.20100510svn4636
- update to 2.2.9, svn4636

* Tue May  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.7-1.20100504svn4581
- update to 2.2.7, svn4581

* Mon Apr 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.3-1.20100419svn4440
- update to 2.2.3, svn4440

* Tue Apr 13 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.2-1.20100413svn4397
- update to 2.2.2, svn4397

* Thu Apr  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.1-1.20100408svn4359
- update to 2.2.1, svn4359

* Mon Mar 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.2.0-1.20100329svn4309
- update to 2.2.0, svn4309

* Thu Mar 25 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.8-1.20100325svn4273
- update to 2.1.8, svn4273

* Mon Mar 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.5-1.20100322svn4204
- update to 2.1.5, svn4204

* Mon Mar 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.4-1.20100315svn4129
- update to 2.1.4, svn4129

* Wed Mar 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.0-1.20100310svn4088
- update to 2.1.3, svn4088

* Thu Feb 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.0-1.20100218svn3902
- update to 2.1.0, svn3902

* Fri Jan 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.6-1.20100122svn3681
- update to 2.0.6, svn3681

* Tue Dec 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.5-1.20091229svn3528
- svn3528

* Mon Dec 21 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.5-1.20091221svn3511
- update to 2.0.5, svn3511

* Wed Dec  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.3-1.20091209svn3443
- update to 2.0.3, svn3443

* Tue Nov 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.2-1.20091124svn3353
- update to 2.0.2, svn3353

* Wed Nov 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0.0-1.20091118svn3334
- update to 2.0.0, svn3334

* Tue Oct 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.16-1.20091027svn3152
- update to 1.3.16, svn3152

* Tue Oct 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.15-1.20091013svn3058
- update to svn3058

* Thu Oct  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.15-1.20091008svn3036
- update to 1.3.15, svn3036

* Tue Sep 29 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.13-1.20090929svn2985
- update to svn2985
- drop unused parameter patch, figured out how to work around it with optflag mangling
- have I mentioned lately that scons is garbage?

* Mon Sep 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.13-1.20090928svn2980
- update to 1.3.13, svn2980

* Wed Sep 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.11-1.20090916svn2903
- update to 1.3.11, svn2903

* Wed Sep  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.9-1.20090909svn2862
- update to 1.3.9, svn2862

* Thu Aug 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.8-1.20090827svn2777
- update to 1.3.8, svn2777

* Mon Aug 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.6-1.20090824svn2747
- update to 1.3.6, svn2747

* Tue Aug 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.4-1.20090818svn2708
- update to svn2708, build and package d8

* Fri Aug 14 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.4-1.20090814svn2692
- update to 1.3.4, svn2692

* Wed Aug 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.3-1.20090812svn2669
- update to 1.3.3, svn2669

* Mon Aug 10 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.2-1.20090810svn2658
- update to svn2658

* Fri Aug  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.2-1.20090807svn2653
- update to svn2653

* Wed Aug  5 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.2-1.20090805svn2628
- update to 1.3.2, svn2628

* Mon Aug  3 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.1-1.20090803svn2607
- update to svn2607

* Fri Jul 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.1-1.20090731svn2602
- update to svn2602

* Thu Jul 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.1-1.20090730svn2592
- update to 1.3.1, svn 2592

* Mon Jul 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.0-1.20090727svn2543
- update to 1.3.0, svn 2543

* Fri Jul 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090724svn2534
- update to svn2534

* Mon Jul 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090720svn2510
- update to svn2510

* Thu Jul 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090716svn2488
- update to svn2488

* Wed Jul 15 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.14-1.20090715svn2477
- update to 1.2.14, svn2477

* Mon Jul 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.13-1.20090713svn2434
- update to svn2434

* Sat Jul 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.13-1.20090711svn2430
- update to 1.2.13, svn2430

* Wed Jul  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.12-1.20090708svn2391
- update to 1.2.12, svn2391

* Sat Jul  4 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.11-1.20090704svn2356
- update to 1.2.11, svn2356

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.9-1.20090626svn2284
- update to svn2284

* Wed Jun 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.9-1.20090624svn2262
- update to 1.2.9, svn2262

* Thu Jun 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-2.20090618svn2219
- fix unused-parameter patch

* Thu Jun 18 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-1.20090618svn2219
- update to 1.2.8, svn2219

* Mon Jun 8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-2.20090608svn2123
- fix gcc44 compile for Fedora 11

* Mon Jun  8 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.7-1.20090608svn2123
- update to 1.2.7, svn2123

* Thu May 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.2.5-1.20090528svn2072
- update to newer svn checkout

* Sun Feb 22 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.1-1.20090222svn1332
- update to newer svn checkout

* Sun Sep 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2-2.20080914svn300
- make a versioned shared library properly

* Sun Sep 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.2-1.20080914svn300
- Initial package for Fedora

