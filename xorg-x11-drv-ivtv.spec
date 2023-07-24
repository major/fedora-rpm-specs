%global ivtv_version 1.1.2

%undefine _hardened_build

Name:           xorg-x11-drv-ivtv
Version:        1.2.0
Release:        0.39%{?dist}
Summary:        Xorg X11 ivtv video driver

License:        MIT
URL:            http://ivtvdriver.org
Source0:        http://dl.ivtvdriver.org/xf86-video-ivtv/archive/1.1.x/xf86-video-ivtv-%{ivtv_version}.tar.gz
Source1:        ivtv-compat-api.h
Patch0:         xf86-video-ivtv-1.1.2-svn20120804.patch
Patch1:		ivtv-1.1.2-mibstore.patch

ExcludeArch: s390 s390x

BuildRequires: make
BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: xorg-x11-proto-devel
Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires:  linux-firmware

%description
X.Org X11 ivtv video driver.

%prep
%setup -q -n xf86-video-ivtv-%{ivtv_version}
%patch0 -p1
%patch1 -p1

install -pm 0644 %{SOURCE1} src/compat-api.h


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/ivtv_drv.la


%files
%doc ChangeLog README
%{_libdir}/xorg/modules/drivers/ivtv_drv.so


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 10:08:42 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.0-0.33
- Add BuildRequires for make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 1.2.0-0.27
- Rebuild for xserver 1.20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 1.2.0-0.22
- Rebuild against xserver-1.19

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> - 1.2.0-0.20
- 1.15 ABI rebuild

* Tue Jun 23 2015 Adam Jackson <ajax@redhat.com> - 1.2.0-0.19
- Undefine _hardened_build

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-0.17
- Firmware now part of linux-firmware

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 1.2.0-0.16
- xserver 1.17 ABI rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 1.2.0-0.14
- xserver 1.15.99.903 ABI rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 1.2.0-0.12
- xserver 1.15.99-20140428 git snapshot ABI rebuild

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 1.2.0-0.11
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 1.2.0-0.10
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 1.2.0-0.9
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 1.2.0-0.8
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 1.2.0-0.7
- ABI rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.0-0.5
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.0-0.4
- ABI rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> 1.2.0-0.2
- ABI rebuild

* Sat Aug 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.1
- Update to svn trunk 20120803

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.2-9
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.2-8
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.2-7
- ABI rebuild

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.2-6
- Rebuild for server 1.12

* Wed Nov 09 2011 ajax <ajax@redhat.com> - 1.1.2-5
- ABI rebuild

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 1.1.2-4
- Rebuild for xserver 1.11 ABI

* Mon Feb 28 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-3
- Rebuilt for new Xorg ABI

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Thu Dec 02 2010 Adam Jackson <ajax@redhat.com> 1.1.1-4
- Really rebuild for new Xorg

* Sun Nov 28 2010 Nicolas Chauvet <kwizart@gmail.com> - 1.1.1-3
- Rebuild for new Xorg

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 1.1.1-2
- Add ABI requires magic (#542742)

* Sun Nov 15 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1
- Remove upstreamed patch

* Thu Nov 12 2009 Adam Jackson <ajax@redhat.com> 1.1.0-6
- ExcludeArch: s390 s390x

* Wed Nov 11 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.1.0-5
- Switch to upstream patch.

* Tue Oct 20 2009 kwizart < kwizart at gmail.com > - 1.1.0-3
- Rebuild for F-12
- Add xf86-video-ivtv-1.1.0-Xextproto71.patch to fix new Xorg

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 kwizart < kwizart at gmail.com > - 1.1.0-1
- Update to 1.1.0 (development)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar  6 2008 kwizart < kwizart at gmail.com > - 1.0.1-2
- Add back xf86-video-ivtv-1.0.1-pagesize.patch

* Thu Mar  6 2008 kwizart < kwizart at gmail.com > - 1.0.1-1
- Update to 1.0.1 (final)

* Thu Mar  6 2008 kwizart < kwizart at gmail.com > - 1.0.1-0.2
- Add xf86-video-ivtv-1.0.1-pagesize.patch

* Wed Mar  5 2008 kwizart < kwizart at gmail.com > - 1.0.1-0.1
- Backport the libpciaccess support from pre 1.0.1

* Tue Feb 19 2008 kwizart < kwizart at gmail.com > - 1.0.0-3
- Fix for libpciaccess support

* Mon Feb 18 2008 kwizart < kwizart at gmail.com > - 1.0.0-2
- Bump for Fedora introduction.

* Mon Oct 22 2007 kwizart < kwizart at gmail.com > - 1.0.0-1
- Initial package.
