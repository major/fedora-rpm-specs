Name:		spacefm
Version:	1.0.6
Release:	19%{?dist}
Summary:	Multi-panel tabbed file and desktop manager

# overall		GPL-3.0-or-later
# src/exo/		LGPL-3.0-or-later
# src/libmd5-rfc/md5.c	Zlib
# src/ptk/		LGPL-3.0-or-later
# SPDX confirmed
License:	GPL-3.0-or-later AND LGPL-3.0-or-later AND Zlib
URL:		http://ignorantguru.github.io/spacefm/
Source0:	https://github.com/IgnorantGuru/spacefm/archive/%{version}/%{name}-%{version}.tar.gz
# Force x11 as gdk backend (bug 1438277)
Patch0:	spacefm-1.0.5-force-x11-backend.patch
# Patch for major(), minor() with glibc 2.28
Patch1:	spacefm-1.0.6-major-glibc228.patch
# Patch to compile with gcc10 -fno-common
Patch2:	spacefm-1.0.6-gcc10-fno-common.patch
# Support C99, use pointer type correctly
Patch3:	spacefm-1.0.6-c99-type-cast.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libX11-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libudev) >= 143

%description
SpaceFM is a multi-panel tabbed file manager with built-in VFS, udev-based
device manager, customizable menu system, and bash integration.

%package	Faenza
Summary:	Faenza theme files for spacefm
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	Faenza
This package contains Faenza theme files for spacefm.

%prep
%setup -q
%patch -P0 -p1 -b .x11
%patch -P1 -p1 -b .glibc228
%patch -P2 -p1 -b .gcc10
%patch -P3 -p1 -b .c99
find . -name \*.c -print0 | xargs --null chmod 0644

%build
%configure \
	--with-gtk3 \
	--disable-video-thumbnails \
	%{nil}
%make_build

%install
%make_install

# Create skeleton configuration file and directory (ref: src/settings.c)
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

# Distro does not require this
rm -f %{buildroot}%{_bindir}/spacefm-installer

# save this
rm -rf tmpdocdir
mv %{buildroot}%{_docdir}/%{name} tmpdocdir

%find_lang %{name}

%check
for f in %{buildroot}%{_datadir}/applications/*desktop
do
	desktop-file-validate $f
done


%post	Faenza
touch --no-create %{_datadir}/icons/Faenza &>/dev/null || :

%postun	Faenza
if [ $1 -eq 0 ] ; then
	touch --no-create %{_datadir}/icons/Faenza &>/dev/null
	gtk-update-icon-cache %{_datadir}/icons/Faenza &>/dev/null || :
fi

%posttrans	Faenza
gtk-update-icon-cache %{_datadir}/icons/Faenza &>/dev/null || :


%files	-f %{name}.lang
%doc	AUTHORS
%license	COPYING*
%doc	ChangeLog
%doc	README

%dir	%{_sysconfdir}/%{name}
%config(noreplace)	%{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}-auth
%{_datadir}/applications/%{name}*desktop
# ref: src/settings.c
%doc	tmpdocdir/%{name}-manual-en.html
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/mime/packages/%{name}-mime.xml
%dir	%{_datadir}/%{name}
%{_datadir}/%{name}/ui/

%files	Faenza
%{_datadir}/icons/Faenza/apps/*/%{name}*

%changelog
* Thu Jan 16 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-19
- Support C99, use pointer type correctly

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 15 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-17
- SPDX migration

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 1.0.6-15
- Change -Wincompatible-pointer-types from error to warning

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-6
- Fix for gcc10 -fno-common

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-2
- Patch for major(), minor() with glibc 2.28

* Tue May 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-1
- 1.0.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-5
- Workaround for crash at drag-and-drop on treeview (bug 1439162)

* Wed Apr  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-4
- Force x11 as gdk backend (bug 1438277)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-1
- 1.0.5

* Sun Oct 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-1
- 1.0.4

* Sat Aug 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.2-1
- 1.0.2

* Wed May  6 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Mon Apr 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.4-4
- update mime scriptlets

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 07 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.4-1
- 0.9.4

* Mon Jan 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-1
- 0.9.3

* Tue Dec 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-1
- 0.9.2

* Mon Nov 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.1-1
- 0.9.1

* Thu Oct 31 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.0-1
- 0.9.0

* Thu Sep 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7-5
- Drop faenza-icon-theme dependency on F-20+ for now

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7-3
- Fix BR for F-17

* Tue Apr 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7-2
- Make -Faenza subpackage depend on faenza-icon-theme
- Create skeleton configuration file and directory

* Mon Apr 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7-1
- Written from scratch
