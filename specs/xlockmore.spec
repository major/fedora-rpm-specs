Summary: Screen lock and screen saver
Name: xlockmore
Version: 5.77
Release: 4%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://sillycycle.com/xlockmore.html
Source0: http://sillycycle.com/xlock/xlockmore-%{version}.tar.xz
BuildRequires: make
BuildRequires: gcc gcc-c++
BuildRequires: pam-devel
BuildRequires: mesa-libGL-devel mesa-libGLU-devel
BuildRequires: desktop-file-utils libXdmcp-devel
BuildRequires: motif-devel gtk2-devel
BuildRequires: libXau-devel
%if 0%{?rhel}
Requires: gnome-icon-theme
%else
Requires: gnome-icon-theme-legacy
%endif

%description
Locks the local X display until a password is entered.

%package motif
Summary: Motif based frontend for xlockmore
Requires: %{name} = %{version}-%{release}

%description motif
Motif based frontend for xlockmore.

%package gtk
Summary: GTK based frontend for xlockmore
Requires: %{name} = %{version}-%{release}

%description gtk
GTK based frontend for xlockmore.

%prep
%setup -q

%{__sed} -i -e "s,/lib,/%{_lib},g;s,-Wno-format,,g;" configure

%build
%configure --with-crypt --enable-pam --enable-syslog --disable-setuid --disable-mb
%{__make} %{?_smp_mflags}

%install
%{__install} -D -m0755 xlock/xlock %{buildroot}%{_bindir}/xlock
%{__install} -D -m0755 xmlock/xmlock %{buildroot}%{_bindir}/xmlock
%{__install} -D -m0755 xglock/xglock %{buildroot}%{_bindir}/xglock
%{__install} -p -D -m0644 xlock/xlock.man %{buildroot}%{_mandir}/man1/xlock.1
%{__install} -p -D -m0644 xlock/XLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XLock
%{__install} -p -D -m0644 xmlock/XmLock.ad %{buildroot}%{_libdir}/X11/app-defaults/XmLock
%{__chmod} 644 README
%{__chmod} 644 docs/Revisions


%{__mkdir_p} %{buildroot}%{_sysconfdir}/pam.d
cat > %{buildroot}%{_sysconfdir}/pam.d/xlock << EOF
#%PAM-1.0
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    include      system-auth
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications

cat >> %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Xlock
Comment=Screen Saver
Encoding=UTF-8
Icon=gnome-lockscreen
Exec=xlock
Terminal=false
Type=Application
EOF

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	--add-category X-Fedora \
	--add-category Application \
	--add-category Graphics \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README docs/*
%doc %{_mandir}/man1/xlock.1*
%{_bindir}/xlock
%{_libdir}/X11/app-defaults/XLock
%config(noreplace) %{_sysconfdir}/pam.d/xlock
%{_datadir}/applications/*

%files motif
%{_bindir}/xmlock
%{_libdir}/X11/app-defaults/XmLock

%files gtk
%{_bindir}/xglock

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 5.77-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 02 2024 Adrian Reber <adrian@lisas.de> - 5.77-1
- Updated to 5.77 (#1837169)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 12 2023 Adrian Reber <adrian@lisas.de> - 5.74-1
- Updated to 5.74 (#1837169)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Adrian Reber <adrian@lisas.de> - 5.70-1
- Updated to 5.70 (#1837169)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 30 2021 Adrian Reber <adrian@lisas.de> - 5.67-1
- Updated to 5.67 (#1837169)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Adrian Reber <adrian@lisas.de> - 5.66-1
- Updated to 5.66 (#1837169)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Adrian Reber <adrian@lisas.de> - 5.64-2
- Applied patch from Jan Kratochvil (#1852546)

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 5.64-1
- Updated to 5.64

* Mon May 11 2020 Adrian Reber <adrian@lisas.de> - 5.63-1
- Updated to 5.63 (#1795091)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Adrian Reber <adrian@lisas.de> - 5.61-1
- Updated to 5.61 (#1762984)
- All patches have been upstreamed

* Thu Dec 05 2019 Adrian Reber <adrian@lisas.de> - 5.60-1
- Updated to 5.60 (#1762984)

* Sat Oct 05 2019 Adrian Reber <adrian@lisas.de> - 5.59-1
- Updated to 5.59

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Adrian Reber <adrian@lisas.de> - 5.56-1
- Updated to 5.56

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 5.55-6
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Jul 18 2018 Adrian Reber <adrian@lisas.de> - 5.55-5
- Added BR: gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 5.55-2
- Rebuilt for switch to libxcrypt

* Thu Aug 10 2017 Adrian Reber <adrian@lisas.de> - 5.55-1
- updated to 5.55

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Adrian Reber <adrian@lisas.de> - 5.53-1
- updated to 5.53

* Thu Mar 16 2017 Adrian Reber <adrian@lisas.de> - 5.51-1
- updated to 5.51

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Adrian Reber <adrian@lisas.de> - 5.49-2
- rebuilt

* Sun Dec 11 2016 Adrian Reber <adrian@lisas.de> - 5.49-1
- updated to 5.49

* Mon May 23 2016 Adrian Reber <adrian@lisas.de> - 5.47-1
- updated to 5.47

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.46-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 06 2015 Adrian Reber <adrian@lisas.de> - 5.46-4
- link against openmotif instead of lesstif
- fixed a changelog date

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.46-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Mar 21 2015 Adrian Reber <adrian@lisas.de> - 5.46-1
- updated to 5.46

* Thu Jan 15 2015 Adrian Reber <adrian@lisas.de> - 5.45-1
- updated to 5.45

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 22 2013  Sebastien Lugan <1698DA98@dynmail.crt1.net> - 5.43-4
- Fixed locale support "xlock need to enter password twice" (#991010)

* Thu Dec 05 2013 Adrian Reber <adrian@lisas.de> - 5.43-3
- fixed "xlockmore FTBFS if "-Werror=format-security" flag is used" (#1037397)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Adrian Reber <adrian@lisas.de> - 5.43-1
- updated to 5.43
- fixed "NULL pointer dereference leads to crash and bypass of screen lock" (#985542)

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 5.41-2
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Tue Nov 20 2012 Adrian Reber <adrian@lisas.de> - 5.41-1
- updated to 5.41
- dropped upstreamed patch for CVE-2012-4524
- fixed "xlock exits on segfault, unlocking the screen" (#874484)

* Mon Oct 22 2012 Adrian Reber <adrian@lisas.de> - 5.40-4
- conditionalize icon BR

* Thu Oct 18 2012 Adrian Reber <adrian@lisas.de> - 5.40-3
- fixed "CVE-2012-4524 xlockmore: Screensaver crash (screen lock bypass) when 'dclock' mode used" (#867908)

* Thu Oct 18 2012 Adrian Reber <adrian@lisas.de> - 5.40-2
- removed esound-devel BR

* Sun Oct 14 2012 Adrian Reber <adrian@lisas.de> - 5.40-1
- updated to 5.40

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 25 2012 Adrian Reber <adrian@lisas.de> - 5.38-1
- updated to 5.38
- removed buildroot and clean section

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 5.34-2
- Rebuild for new libpng

* Tue Jun 07 2011 Adrian Reber <adrian@lisas.de> - 5.34-1
- updated to 5.34
- fixed "Desktop file should not include extension..." (#701699)
- fixed "...missing Requires" (#701699); added R: gnome-icon-theme-legacy

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Adrian Reber <adrian@lisas.de> - 5.31-1
- updated to 5.31
- removed xlockmore-fix_petri.patch

* Sat May 08 2010 Adrian Reber <adrian@lisas.de> - 5.28-2
- fixed "FTBFS xlockmore-5.28-1.fc12: ImplicitDSOLinking" (#564929)

* Sun Aug 30 2009 Adrian Reber <adrian@lisas.de> - 5.28-1
- updated to 5.28
- applied patch to fix "xlock -mode petri segfaults with 32 bit displays" (#518379)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 09 2008 Adrian Reber <adrian@lisas.de> - 5.26.1-1
- updated to 5.26.1

* Mon Feb 18 2008 Adrian Reber <adrian@lisas.de> - 5.25-1
- updated to 5.25

* Sat Oct 13 2007 Adrian Reber <adrian@lisas.de> - 5.24-1
- updated to 5.24

* Tue Feb 06 2007 Adrian Reber <adrian@lisas.de> - 5.23-1
- updated to 5.23

* Tue Sep 12 2006 Adrian Reber <adrian@lisas.de> - 5.22-3
- rebuilt
- swtiched to lesstif

* Sun Jul 09 2006 Adrian Reber <adrian@lisas.de> - 5.22-2
- rebuild for new freetype

* Mon May 01 2006 Adrian Reber <adrian@lisas.de> - 5.22-1
- updated to 5.22
- changed pam file to use include instead of pam_stack.so

* Tue Feb 21 2006 Adrian Reber <adrian@lisas.de> - 5.21-1
- updated to 5.21

* Fri Dec 16 2005 Adrian Reber <adrian@lisas.de> - 5.20.1-1
- updated to 5.20.1
- changes for modular X
- removed "GENTOO" hack

* Sun Aug 21 2005 Adrian Reber <adrian@lisas.de> - 5.19-1
- updated to 5.19
- upstream included a fix for (BZ #161740), but "GENTOO" needs
  to be defined during compilation

* Mon Jun 27 2005 Adrian Reber <adrian@lisas.de> - 5.18-3
- included patch to make it work again with PAM (BZ #161740)

* Fri Jun 17 2005 Adrian Reber <adrian@lisas.de> - 5.18-2
- update to 5.18

* Wed Apr 13 2005 Adrian Reber <adrian@lisas.de> - 5.16-1
- update to 5.16

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb 24 2005 Adrian Reber <adrian@lisas.de> - 5.15-1
- update to 5.15
- moved motif and gtk2 frontend to subpackages
- build with pam support
- added .desktop file

* Sun Dec 12 2004 Dries Verachtert <dries@ulyssis.org> 5.14.1-1
- Update to release 5.14.1.

* Thu Oct 28 2004 Dries Verachtert <dries@ulyssis.org> 5.13-1
- update to release 5.13

* Thu May 27 2004 Dries Verachtert <dries@ulyssis.org> 5.12-1
- update to 5.12

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 5.10-2
- cleanup of spec file

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 5.10-1
- first packaging for Fedora Core 1
