# FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for ARM.
# The related discussion can be found here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global _binaries_in_noarch_packages_terminate_build 0

%global target arm-none-eabi
%global pkg_version 4.4.0.20231231

Name:           %{target}-newlib
Version:        4.4.0.20231231
Release:        4%{?dist}
Summary:        C library intended for use on %{target} embedded systems
# For a breakdown of the licensing, see NEWLIB-LICENSING
License:        BSD-2-Clause AND BSD-4-Clause AND LGPL-2.1-or-later AND ISC AND GPL-3.0-or-later AND MIT
URL:            http://sourceware.org/newlib/
Source0:        ftp://sourceware.org/pub/newlib/newlib-%{pkg_version}.tar.gz
Source1:        README.fedora
Source2:        NEWLIB-LICENSING

BuildRequires:  gcc
BuildRequires:  %{target}-binutils %{target}-gcc %{target}-gcc-c++ texinfo texinfo-tex
BuildRequires: make
BuildArch:      noarch

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products.

%prep
%setup -q -n newlib-%{pkg_version}


%build
rm -rf build-{newlib,nano}
mkdir build-{newlib,nano}

pushd build-newlib

export CFLAGS_FOR_TARGET="-g -O2 -ffunction-sections -fdata-sections"
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --htmldir=%{_docdir}/html \
    --pdfdir=%{_docdir}/pdf \
    --target=%{target} \
    --enable-newlib-io-long-long \
    --enable-newlib-register-fini \
    --enable-newlib-retargetable-locking \
    --disable-newlib-supplied-syscalls \
    --disable-nls \
    --enable-multilib \
    --disable-libssp \
    --with-float=soft

make

popd
pushd build-nano
export CFLAGS_FOR_TARGET="-g -Os -ffunction-sections -fdata-sections"
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --target=%{target} \
    --disable-newlib-supplied-syscalls    \
    --enable-newlib-reent-small           \
    --enable-newlib-retargetable-locking  \
    --disable-newlib-fvwrite-in-streamio  \
    --disable-newlib-fseek-optimization   \
    --disable-newlib-wide-orient          \
    --enable-newlib-nano-malloc           \
    --disable-newlib-unbuf-stream-opt     \
    --enable-lite-exit                    \
    --enable-newlib-global-atexit         \
    --enable-newlib-nano-formatted-io     \
    --disable-nls

make -j

popd

%install
pushd build-newlib
make install DESTDIR=%{buildroot}
popd
pushd build-nano
NANO_ROOT=%{buildroot}/nano
make install DESTDIR=$NANO_ROOT

for i in $(find $NANO_ROOT -regex ".*/lib\(c\|g\|rdimon\)\.a"); do
    file=$(basename $i | sed "s|\.a|_nano\.a|")
    target_path=$(dirname $i | sed "s|$NANO_ROOT||")
    cp $i "%{buildroot}$target_path/$file"
done
mkdir -p %{buildroot}/usr/arm-none-eabi/include/newlib-nano/
cp -p $NANO_ROOT/usr/arm-none-eabi/include/newlib.h %{buildroot}/usr/arm-none-eabi/include/newlib-nano/newlib.h
popd

cp %{SOURCE1} .
cp %{SOURCE2} .

# we don't want these as we are a cross version
rm -rf %{buildroot}%{_infodir}

rm -rf $NANO_ROOT
# despite us being noarch redhat-rpm-config insists on stripping our files
%global __os_install_post /usr/lib/rpm/brp-compress


%files
%doc README.fedora
%license NEWLIB-LICENSING COPYING*
%dir %{_prefix}/%{target}
%dir %{_prefix}/%{target}/include/
%{_prefix}/%{target}/include/*
%dir %{_prefix}/%{target}/lib
%{_prefix}/%{target}/lib/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0.20231231-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0.20231231-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Michal Hlavinka <mhlavink@redhat.com> - 4.4.0.20231231-2
- rebuild for new gcc 14.1

* Mon Mar 18 2024 Michal Hlavinka <mhlavink@redhat.com> - 4.4.0.20231231-1
- updated to 4.4.0.20231231

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0.20230120-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0.20230120-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0.20230120-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Michal Hlavinka <mhlavink@redhat.com> - 4.3.0.20230120-3
- rebuild for new gcc

* Wed May 10 2023 Michal Hlavinka <mhlavink@redhat.com> - 4.3.0.20230120-2
- update license tag format (SPDX migration) for https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_1

* Wed Apr 12 2023 Michal Hlavinka <mhlavink@redhat.com> - 4.3.0.20230120-1
- updated to 4.3.0.20230120

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 4.1.0-7
- Simplify the redhat-rpm-config workaround logic

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 07 2022 Michal Hlavinka <mhlavink@redhat.com> - 4.1.0-5
- enable retargetable locking(#2094193)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 4.1.0-2
- rebuild for gcc 11.1.0

* Tue Mar 02 2021 Michal Hlavinka <mhlavink@redhat.com> - 4.1.0-1
- updated to 4.1.0

* Wed Feb 03 2021 Michal Hlavinka <mhlavink@redhat.com> - 3.3.0-3
- bump release for rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 04 2020 Michal Hlavinka <mhlavink@redhat.com> - 3.3.0-1
- updated to 3.3.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Michal Hlavinka <mhlavink@redhat.com> - 3.1.0-3
- rebuild with gcc 9.2.0

* Mon Mar 11 2019 Michal Hlavinka <mhlavink@redhat.com> - 3.1.0-2
- add nano version of newlib.h

* Fri Mar 08 2019 Michal Hlavinka <mhlavink@redhat.com> - 3.1.0-0
- updated to 3.1.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Michal Hlavinka <mhlavink@redhat.com> - 3.0.0-2
- updated to 3.0.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Michal Hlavinka <mhlavink@redhat.com> - 2.5.0-2
- make sure -Os flags are used for nano version (#1443512)

* Fri Jun 23 2017 Michal Hlavinka <mhlavink@redhat.com> - 2.5.0-1
- updated to 2.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.4.0-8
- bump release and rebuild

* Thu Jun 30 2016 Michal Hlavinka <mhlavink@redhat.com> - 2.4.0-7
- updated to 2.4.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0_1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-6
- bump release and rebuild

* Wed Sep 02 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-5
- add --enable-newlib-io-long-long configure option

* Mon Aug 31 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-4
- added nano versions of libraries
- cleaned up spec file
- credits: Johnny Robeson

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0_1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-2
- rebuild for gcc 5.1

* Tue Apr 14 2015 Michal Hlavinka <mhlavink@redhat.com> - 2.2.0_1-1
- newlib updated to 2.2.0_1

* Mon Jun 09 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-5
- fix FTBFS (#1105970)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-3
- enable libnosys (#1060567,#1058722)

* Tue Jan 14 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-2
- rebuild with newer arm-none-eabi-gcc

* Wed Jan 08 2014 Michal Hlavinka <mhlavink@redhat.com> - 2.1.0-1
- initial import
