Name:		scim-hangul
Version:	0.4.0
Release:	10%{?dist}

License:	GPL-3.0-only
URL:		https://github.com/libhangul/scim-hangul
BuildRequires:	make
BuildRequires:	scim-devel >= 1.2.0 libhangul-devel
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
Patch1:     scim-hangul-0.3.2.gcc47.patch
Patch2:     scim-hangul-0.4.0-fixes-gtk2-compile.patch

Summary:	Hangul Input Method Engine for SCIM
Requires:	scim
BuildRequires:  gcc-c++
%ifarch aarch64
BuildRequires:	autoconf
%endif

%description
Scim-hangul is a SCIM IMEngine module for Korean (Hangul) input support.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%ifarch aarch64
autoconf
%endif
%configure --disable-static
make %{?_smp_mflags}


%install
make DESTDIR=${RPM_BUILD_ROOT} install

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/{IMEngine,SetupUI}/hangul*.la

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/scim-1.0/*/IMEngine/hangul.so
%{_libdir}/scim-1.0/*/SetupUI/hangul-imengine-setup.so
%{_datadir}/scim/icons/scim-hangul*.png
%{_datadir}/scim/hangul


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May  9 2023 Peng Wu <pwu@redhat.com> - 0.4.0-6
- Migrate to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Peng Wu <pwu@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-32
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jens Petersen <petersen@redhat.com> - 0.3.2-26
- BR gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.2-19
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep  2 2013 Jens Petersen <petersen@redhat.com> - 0.3.2-16
- BR autoconf for aarch64

* Mon Sep  2 2013 Jens Petersen <petersen@redhat.com> - 0.3.2-15
- run autoconf on aarch64 (#926495)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.3.2-12
- Fix FTBFS for gcc-4.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Jens Petersen <petersen@redhat.com> - 0.3.2-9
- rebuild against latest libhangul

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec  2 2008 Jens Petersen <petersen@redhat.com> - 0.3.2-5
- own datadir/scim/hangul (#473663)

* Mon Mar 03 2008 Hu Zheng <zhu@redhat.com> - 0.3.2-4
- ppc64 build fix.

* Mon Feb 25 2008 Hu Zheng <zhu@redhat.com> - 0.3.2-3
- Gcc4.3 compile fix.

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.2-2
- Autorebuild for GCC 4.3

* Tue Jan 8 2008 Hu Zheng <zhu@redhat.com> - 0.3.2-1
- New upstream release.

* Thu Mar 22 2007 Akira TAGOH <tagoh@redhat.com> - 0.3.1-1
- New upstream release.
  - remove the unnecessary patches:
    - scim-hangul-0.2.2-help.patch
    - scim-hangul-0.2.2-ascii-mode.patch
    - scim-hangul-0.2.2-swap-keybinding.patch
    - scim-hangul-update-caret.patch

* Tue Feb  6 2007 Akira TAGOH <tagoh@redhat.com> - 0.2.2-8
- cleanups for mass package review. (#226393)

* Tue Aug 29 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-7
- scim-hangul-update-caret.patch: backported from CVS to update the caret.
  (#198721)

* Tue Jul 25 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-6
- scim-hangul-0.2.2-swap-keybinding.patch: swap the keybindings to move
  the cursor on the candidate window according to the candidate window's
  orientation.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.2.2-5.1
- rebuild

* Wed Jul  5 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-5
- add a keybindings documentation into the online help. (#186884)
- use dist tag.

* Fri Jun  9 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-4
- gettextized the input layout string on panel. (#194444)

* Wed May 17 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-3
- scim-hangul-0.2.2-ascii-mode.patch: applied to support the ASCII input mode
  in scim-hangul. (#185506)

* Fri Mar 31 2006 Jens Petersen <petersen@redhat.com> - 0.2.2-2.fc6
- rebuild without libstdc++so7

* Thu Mar 30 2006 Akira TAGOH <tagoh@redhat.com> - 0.2.2-1
- New upstream release.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.2.1-3.fc5.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Jens Petersen <petersen@redhat.com> - 0.2.1-3
- build conditionally with libstdc++so7 preview library (#166041)
  - add with_libstdc_preview switch and tweak libtool to link against newer lib
- update filelist since moduledir is now api-versioned

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 14 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.1-2
- added Obsoletes: iiimf-le-hangul <= 12.2 to ensure the upgrade path.

* Mon Oct 31 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.1-1
- New upstream release.
- scim-hangul-0.2.0-ignore-invisible-char.patch: removed.

* Thu Oct  6 2005 Jens Petersen <petersen@redhat.com> - 0.2.0-6
- require scim

* Thu Aug 25 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.0-5
- fixed the description of this package. (Ryo Dairiki)
- scim-hangul-0.2.0-ignore-invisible-char.patch: applied to not commit any
  Hangul characters with the keys unrelated to Yetgeul. (#166138)

* Tue Aug 16 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.0-4
- Rebuild.

* Fri Aug  5 2005 Warren Togami <wtogami@redhat.com> - 0.2.0-3
- minor spec cleanup

* Thu Aug  4 2005 Akira TAGOH <tagoh@redhat.com> - 0.2.0-2
- Import into Core.
- clean up the spec.

* Sun Jun 13 2004 James Su <suzhe@tsinghua.org.cn>
- first release of scim-uim.

