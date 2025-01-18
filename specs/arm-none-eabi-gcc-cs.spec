%global processor_arch arm
%global target         %{processor_arch}-none-eabi
%global gcc_ver        %{version}
%global gcc_short_ver  13.1

# we need newlib to compile complete gcc, but we need gcc to compile newlib,
# so compile minimal gcc first
%global bootstrap      0

Name:           %{target}-gcc-cs
Epoch:          1
Version:        14.1.0
Release:        3%{?dist}
Summary:        GNU GCC for cross-compilation for %{target} target
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            https://gcc.gnu.org/
Source0:        http://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

Source1:        README.fedora
Source2:        bootstrapexplain

Patch1:  	gcc12-hack.patch

#BuildRequires:	autoconf = 2.69
BuildRequires:  gcc-c++
BuildRequires:  %{target}-binutils >= 2.21, zlib-devel gmp-devel mpfr-devel libmpc-devel flex autogen
%if ! %{bootstrap}
BuildRequires:  %{target}-newlib
BuildRequires: make
%endif
Requires:       %{target}-binutils >= 2.21
Provides:       %{target}-gcc = %{gcc_ver}

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# ppl-devel is no longer available for 32bit, so we have to skip it too
ExcludeArch:    %{ix86}
%endif

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %{target} platform, instead of for the
native %{_arch} platform.

%package c++
Summary:        Cross Compiling GNU GCC targeted at %{target}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       %{target}-gcc-c++ = %{gcc_ver}

%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %{target} platform, instead of for the native 
%{_arch} platform.

%prep
%setup -q -c
pushd gcc-%{gcc_ver}
%patch -P1 -p0 -b .hack
popd
pushd gcc-%{gcc_ver}/libiberty
#autoconf -f
popd
pushd gcc-%{gcc_ver}

contrib/gcc_update --touch
popd
cp -a %{SOURCE1} .

# Extract %%__os_install_post into os_install_post~
cat << \EOF > os_install_post~
%__os_install_post
EOF

# Generate customized brp-*scripts
cat os_install_post~ | while read a x y; do
case $a in
# Prevent brp-strip* from trying to handle foreign binaries
*/brp-strip*)
  b=$(basename $a)
  sed -e 's,find "*$RPM_BUILD_ROOT"*,find "$RPM_BUILD_ROOT%_bindir" "$RPM_BUILD_ROOT%_libexecdir",' $a > $b
  chmod a+x $b
  ;;
esac
done

sed -e 's,^[ ]*/usr/lib/rpm.*/brp-strip,./brp-strip,' \
< os_install_post~ > os_install_post 


%build
# This package's testsuite fails on s390 when LTO is enabled.  Disable
# LTO for now on s390x until the root cause is identified
%ifarch s390x
%define _lto_cflags %{nil}
%endif
mkdir -p gcc-%{target} gcc-nano-%{target}

#### normal version

pushd gcc-%{target}
FILTERED_RPM_OPT_FLAGS=$(echo "${RPM_OPT_FLAGS}" | sed 's/Werror=format-security/Wno-format-security/g')
export CFLAGS=$FILTERED_RPM_OPT_FLAGS
export CXXFLAGS=$FILTERED_RPM_OPT_FLAGS
CC="%{__cc} ${FILTERED_RPM_OPT_FLAGS} -fno-stack-protector" \
../gcc-%{gcc_ver}/configure --prefix=%{_prefix} --mandir=%{_mandir} \
  --with-pkgversion="Fedora %{version}-%{release}" \
  --with-bugurl="https://bugzilla.redhat.com/" \
  --infodir=%{_infodir} --target=%{target} \
  --enable-interwork --enable-multilib \
  --with-python-dir=share/%{target}/gcc-%{version}/python \
  --with-multilib-list=rmprofile \
  --enable-plugins \
  --disable-decimal-float \
  --disable-libffi \
  --disable-libgomp \
  --disable-libmudflap \
  --disable-libquadmath \
  --disable-libssp \
  --disable-libstdcxx-pch \
  --disable-nls \
  --disable-shared \
  --disable-threads \
  --disable-tls \
%if %{bootstrap}
   --enable-languages=c --with-newlib --disable-nls --disable-shared --disable-threads --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --without-headers --with-system-zlib
%else
   --enable-languages=c,c++ --with-newlib --disable-nls --disable-shared --disable-threads --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --with-headers=yes --with-system-zlib --with-sysroot=/usr/%{target}
%endif

%if %{bootstrap}
make all-gcc  INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
%else
make %{_smp_mflags} INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
%endif
popd

######### nano version build part (only relevant if not bootstrap)
%if %{bootstrap}
%else

mkdir -p gcc-nano-%{target}
pushd gcc-nano-%{target}

export CFLAGS_FOR_TARGET="$CFLAGS_FOR_TARGET -fno-exceptions -Os "
export CXXFLAGS_FOR_TARGET="$CXXFLAGS_FOR_TARGET -fno-exceptions -Os "

CC="%{__cc} ${RPM_OPT_FLAGS}  -fno-stack-protector " \
../gcc-%{gcc_ver}/configure --prefix=%{_prefix} --mandir=%{_mandir} \
  --with-pkgversion="Fedora %{version}-%{release}" \
  --with-bugurl="https://bugzilla.redhat.com/" \
  --infodir=%{_infodir} --target=%{target} \
  --enable-interwork --enable-multilib \
  --with-python-dir=share/%{target}/gcc-%{version}/python \
  --with-multilib-list=rmprofile \
  --enable-plugins \
  --disable-decimal-float \
  --disable-libffi \
  --disable-libgomp \
  --disable-libmudflap \
  --disable-libquadmath \
  --disable-libssp \
  --disable-libstdcxx-pch \
  --disable-nls \
  --disable-shared \
  --disable-threads \
  --disable-tls \
  --with-sysroot=/usr/%{target} \
 --enable-languages=c,c++ --with-newlib --disable-nls --disable-shared --disable-threads --with-gnu-as --with-gnu-ld --with-gmp --with-mpfr --with-mpc --with-headers=yes --with-system-zlib
make %{_smp_mflags} INHIBIT_LIBC_CFLAGS='-DUSE_TM_CLONE_REGISTRY=0'
popd
%endif


%install
pushd gcc-%{target}
%if %{bootstrap}
make install-gcc DESTDIR=$RPM_BUILD_ROOT
install -p -m 0755 -D %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}/%{target}-g++
install -p -m 0755 -D %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}/%{target}-c++
%else
make install DESTDIR=$RPM_BUILD_ROOT
%endif
popd

##### nano version (only relevant non-bootstrap)

%if %{bootstrap}
%else
# everybody needs to end up built with the One True DESTDIR
# to arrange for that, move the non-nano DESTDIR out of the way
# temporarily, and make an empty one for the nano build to
# populate.  Later we'll pick just the bits from the nano one
# into the non-nano one, and switch the non-nano one to be
# the One True DESTDIR again.
#
# Without this sleight-of-hand we get rpmbuild errors noticing that
# the DESTDIR the nano bits were built with is not the One True
# DESTDIR.

rm -rf $RPM_BUILD_ROOT-non-nano
mv $RPM_BUILD_ROOT $RPM_BUILD_ROOT-non-nano
pushd gcc-nano-%{target}

make install DESTDIR=$RPM_BUILD_ROOT
popd
pushd $RPM_BUILD_ROOT
for i in libstdc++.a libsupc++.a ; do
	find . -name "$i" | while read line ; do
		R=`echo $line | sed "s/\.a/_nano\.a/g"`
		echo "$RPM_BUILD_ROOT/$line -> $RPM_BUILD_ROOT-non-nano/$R"
		cp $line $RPM_BUILD_ROOT-non-nano/$R
	done 
done
popd

# junk the nano DESTDIR now we picked out the bits we needed into
# the non-nano destdir
rm -rf $RPM_BUILD_ROOT

# put the "non-nano + picked nano bits" destdir back at the
# One True DESTDIR location.  Even though it has bits from two different
# builds, all the bits feel they were installed to DESTDIR
mv $RPM_BUILD_ROOT-non-nano $RPM_BUILD_ROOT

%endif
### end of nano version install magic


# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/libiberty.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libcc1* ||:
# these directories are often empty
rmdir $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver} ||:
rmdir $RPM_BUILD_ROOT/usr/%{target}/share ||:
# and these aren't usefull for embedded targets
rm -r $RPM_BUILD_ROOT%{_prefix}/lib*/gcc/%{target}/%{gcc_ver}/install-tools ||:
rm -r $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{gcc_ver}/install-tools ||:
rm -f $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{gcc_ver}/*.la


mkdir -p $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver}/
mv $RPM_BUILD_ROOT/%{_datadir}/gcc-%{gcc_ver}/* $RPM_BUILD_ROOT/usr/%{target}/share/gcc-%{gcc_ver}/ ||:
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gcc-%{gcc_ver} ||:

%global __os_install_post . ./os_install_post


%check
exit 0 # broken test, temporarily disable
%if %{bootstrap}
exit 0
%endif

%ifarch ppc64
# test does not work, upstream ignores it, https://gcc.gnu.org/bugzilla/show_bug.cgi?id=57591
exit 0
%endif

pushd gcc-%{target}
#BuildRequires: autoge may be needed
make check
popd

%files
%license gcc-%{gcc_ver}/COPYING*
%doc gcc-%{gcc_ver}/README README.fedora
%{_bindir}/%{target}-*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{target}
%{_prefix}/lib/gcc/%{target}/%{gcc_ver}
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{target}
%{_libexecdir}/gcc/%{target}/%{gcc_ver}
%{_mandir}/man1/%{target}-*.1.gz
%if ! %{bootstrap}
/usr/%{target}/lib/
%dir /usr/share/%{target}/gcc-%{gcc_ver}/python/
%exclude %{_bindir}/%{target}-?++
%exclude %{_libexecdir}/gcc/%{target}/%{gcc_ver}/cc1plus
%exclude %{_mandir}/man1/%{target}-g++.1.gz
%endif

%files c++
%{_bindir}/%{target}-?++
%if ! %{bootstrap}
%{_libexecdir}/gcc/%{target}/%{gcc_ver}/cc1plus
/usr/%{target}/include/c++/
/usr/share/%{target}/gcc-%{gcc_ver}/python/libstdcxx/
%{_mandir}/man1/%{target}-g++.1.gz
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:14.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:14.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:14.1.0-1
- full build of gcc 14.1

* Wed May 22 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:14.1.0-0
- updated to 14.1.0, bootstrap build, do not use

* Tue Mar 19 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:13.2.0-5
- drop i686 build as not all i686 requirements are available anymore

* Tue Mar 19 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:13.2.0-4
- rebuild with updated newlib

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:13.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:13.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:13.2.0-1
- updated to 13.2.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:13.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:13.1.0-1
- updated to 13.1.0

* Wed May 24 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:12.3.0-1
- updated to 12.3.0

* Wed May 10 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:12.2.0-5
- update license tag format (SPDX migration) for https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_1

* Wed Apr 12 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:12.2.0-4
- rebuild for updated newlib package

* Thu Jan 19 2023 Florian Weimer <fweimer@redhat.com> - 1:12.2.0-3
- Backport upstream patches for improved C99 compatibility

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:12.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:12.2.0-1
- updated to 12.2.0

* Tue Aug 02 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:12.1.0-2
- fix FTBFS (#2113112)

* Wed Jul 27 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:12.1.0-1
- updated to 12.1.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:11.3.0-1
- updated to 11.3.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:11.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:11.1.0-1
- regular build for 11.1.0

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:11.1.0-0
- bootstrap build for 11.1.0

* Sun Apr 11 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:10.2.0-5
- add explicit requirement for autoconf 2.69

* Wed Feb 24 2021 Jeff Law <law@redhat.com> - 1:10.2.0-4
- Packport fix for libbacktrace's handling of dwarf-5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:10.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Michal Hlavinka <mhlavink@redhat.com> - 1:10.2.0-2
- regular build for 10.2.0

* Wed Nov 04 2020 Michal Hlavinka <mhlavink@redhat.com> - 1:10.2.0-1
- bootstrap build for gcc 10.2.0

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 1:9.2.0-8
- Disable LTO on s390x for now

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.2.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jeff Law <law@redhat.com> - 1:9.2.0-5
- Fix broken configured tests compromised by LTO
- Add autoconf to BuildRequires

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:9.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1:9.2.0-3
- Backport change to libbacktrace testsuite so it works with gcc-10

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 1:9.2.0-2
- Rebuild for mpfr 4

* Wed Aug 21 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:9.2.0-1
- updated to 9.2.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Michal Hlavinka <mhlavink@redhat.com> - 1:7.4.0-1
- updated to 7.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Michal Hlavinka <mhlavink@redhat.com> - 1:7.3.0-1
- updated to 7.3.0
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Michal Hlavinka <mhlavink@redhat.com> - 1:7.1.0-3
- propper build for 7.1.0, prev one was still bootstrap

* Fri Jun 23 2017 Michal Hlavinka <mhlavink@redhat.com> - 1:7.1.0-2
- propper build for 7.1.0

* Thu Jun 22 2017 Michal Hlavinka <mhlavink@redhat.com> - 1:7.1.0-1
- bootstrap build for 7.1.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2.0-2
- propper build for 6.2.0

* Sun Nov 13 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:6.2.0-1
- bootstrap build for 6.2.0

* Fri Jul 08 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:6.1.0-2
- proper build of new version

* Tue Jun 28 2016 Michal Hlavinka <mhlavink@redhat.com> - 1:6.1.0-1
- bootstrap build for gcc 6.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:5.2.0-3
- build nano libstdc++ (credits: Andy Green)

* Thu Sep 03 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:5.2.0-2
- regular build of 5.2.0

* Wed Sep 02 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:5.2.0-1
- bootstrap build of 5.2.0 update

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:5.1.0-3
- updated to gcc 5.1.0

* Wed Apr 15 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:4.9.2-3
- regular build

* Wed Apr 15 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:4.9.2-2
- add epoch number

* Tue Apr 14 2015 Michal Hlavinka <mhlavink@redhat.com> - 1:4.9.2-1
- update to gcc 4.9.2
- fix library compatiblity 
- BOOTSTRAP version, not for regular use

* Tue Sep 02 2014 Michal Hlavinka <mhlavink@redhat.com> - 2014.05.28-2
- update workaround that prevents stripping of arm libraries

* Thu Aug 21 2014 Michal Hlavinka <mhlavink@redhat.com> - 2014.05.28-1
- updated to 2014.05-28

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Michal Hlavinka <mhlavink@redhat.com> - 2013.11.24-2
- complete build with newlib

* Tue Jan 14 2014 Michal Hlavinka <mhlavink@redhat.com> - 2013.11.24-1
- updated to 2013.11-24

* Fri Oct 11 2013 Michal Hlavinka <mhlavink@redhat.com> - 2013.05.23-2
- replace arm*-g++ with explanation script that this is just unsupported 
  package used for bootstrapping

* Sun Aug 25 2013 Michal Hlavinka <mhlavink@redhat.com> - 2013.05.23-1
- updated to 2013.05-23 release (gcc 4.7.3)

* Wed Aug 14 2013 Michal Hlavinka <mhlavink@redhat.com> - 2012.09.63-3
- fix aarch64 support (#925023)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.09.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Michal Hlavinka <mhlavink@redhat.com> - 2012.09.63-1
- initial package

