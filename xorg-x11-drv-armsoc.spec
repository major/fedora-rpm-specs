%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir       %{moduledir}/drivers
%define gitdate 20210211
%define gitrev .%{gitdate}

%undefine _hardened_build

Summary:   Xorg X11 armsocdrm driver
Name:      xorg-x11-drv-armsoc
Version:   1.4.1
Release:   4%{?gitrev}%{?dist}
URL:       http://cgit.freedesktop.org/xorg/driver/xf86-video-armsoc
License:   MIT

Source0:    xf86-video-armsoc-%{gitdate}.tar.bz2
Source2:    make-git-snapshot.sh
Patch0:     stat-inc.patch

ExclusiveArch: %{arm} aarch64

BuildRequires: make
BuildRequires: kernel-headers
BuildRequires: libdrm-devel
BuildRequires: libudev-devel
BuildRequires: libXext-devel 
BuildRequires: libXrandr-devel 
BuildRequires: libXv-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pixman-devel
BuildRequires: xorg-x11-server-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: perl-Carp

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 armsocdrm driver for ARM MALI GPUs such as the Samsung 
Exynos 4/5 series ARM devices.

%if 0%{?gitdate}
%define dirsuffix %{gitdate}
%else
%define dirsuffix %{version}
%endif

%prep
%setup -q -n xf86-video-armsoc-%{?gitdate:%{gitdate}}%{!?gitdate:%{dirsuffix}} 
touch AUTHORS
%patch0 -p1

%build
%{?gitdate:autoreconf -v --install}

%configure --disable-static  --libdir=%{_libdir} --mandir=%{_mandir}
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%doc README COPYING
%{driverdir}/armsoc_drv.so
%{_mandir}/man4/armsoc.4*

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4.20210211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3.20210211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2.20210211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 11 2021 Dennis Gilmore <dennis@ausil.us> - 1.4.1-1.20210211
- update to a 1.41 git snapshot

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-15.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 09:46:13 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1.4.0-14.20160929
- Add BuildRequires for make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 1.4.0-8.20160929
- Rebuild for xserver 1.20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4.20160929
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 1.4.0-3.20160929
- Git snapshot du-jour
- Add patches from upstream master for building with 1.19 which the endless
  fork we use misses
- Rebuild against xserver-1.19

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2.20151221
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Dennis Gilmore <dennis@ausil.us> - 1.4.0-1.20151221
- update to latest git
- version bumped to 1.4.0

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> - 1.3.0-4.20150531
- 1.15 ABI rebuild

* Tue Jun 23 2015 Adam Jackson <ajax@redhat.com> - 1.3.0-3.20150531
- Undefine _hardened_build

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2.20150531
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Dennis Gilmore <dennis@ausil.us> - 1.3.0-1.20150531
- update to latest git
- add patch to fix ftbfs for missing includes
- pull source from  https://github.com/endlessm/xf86-video-armsoc

* Mon May 11 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.1.0-2.20150212
- Handle pointer as a pointer to make gcc happy.

* Thu Feb 12 2015 Hans de Goede <hdegoede@redhat.com> - 1.1.0-1.20150212
- Update to git snapshot of the day to fix FTBFS
- This also bumps the version we're based on from 0.7.0 + git patches to
  1.1.0 + git patches.

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 0.7.0-7.20140504
- xserver 1.17 ABI rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6.20140504
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 0.7.0-5.20140504
- xserver 1.15.99.903 ABI rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4.20140504
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.0-3.20140504
- Build on aarch64 too

* Sun May 04 2014 Dennis Gilmore <dennis@ausil.us> - 0.7.0-2.20140504
- update git snapshot for ftbfs

* Thu May 01 2014 Dennis Gilmore <dennis@ausil.us> - 0.7.0-1.20140501
- update git snapshot
- add script to make tarball from git
- xserver 1.15.99-20140428 git snapshot ABI rebuild
- sync package to match other x drivers

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 0.6.0-0.7.3be1f62
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 0.6.0-0.6.3be1f62
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 0.6.0-0.5.3be1f62
- 1.15RC2 ABI rebuild

* Tue Nov 19 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.0-0.4.3be1f62
- update to latest git snapshot

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 0.6.0-0.3.f245da3
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 0.6.0-0.2.f245da3
- ABI rebuild

* Wed Sep 11 2013 Dennis Gilmore <dennis@ausil.us> - 0.6.0-0.1.f245da3
- update to post 0.6.0 snapshot

* Mon Aug 12 2013 Dennis Gilmore <dennis@ausil.us> - 0.5.2-0.4.b4299f8
- update git snapshot

* Sun Jun 02 2013 Dennis Gilmore <dennis@ausil.us> 0.5.2-0.3.40c8ee2
- bump release

* Sun Jun 02 2013 Dennis Gilmore <dennis@ausil.us> 0.5.2-0.2.40c8ee2
- updated git snapshot, set the hwcursor for the one that works on exynos

* Sun Apr 21 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.2-0.1-02465b1
- Move to a git snapshot for the time being

* Thu Apr 04 2013 Dennis Gilmore <dennis@ausil.us> - 0.5.1-9
- patch to fix ftbfs bz#948089

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.5.1-8
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.5.1-7
- ABI rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.5.1-5
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 0.5.1-4
- ABI rebuild

* Sun Nov 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-3
- Review updates

* Sun Nov 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-2
- Update git url

* Sun Nov 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-1
- Initial package
