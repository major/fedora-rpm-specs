# Review at https://bugzilla.redhat.com/show_bug.cgi?id=452395

%global		use_release	0
%global		use_gitbare	1

%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20250329
%global		gittartime		1503
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250328
%global		git_rev		4266f49fcc519346f9f509e4eed991383eb110ad
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif


%global		main_version	0.2.8

Name:           lxlauncher
Version:        0.2.8
Release:        2%{?dist}
Summary:        Open source replacement for Launcher on the EeePC

# src/exo-wrap-table.c	LGPL-2.0-or-later
# Otherwise	GPL-2.0-or-later
# SPDX confirmed
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		https://github.com/lxde/%{name}/archive/%{main_version}/%{name}-%{version}.tar.gz
%endif
Source1:		create-%{name}-git-bare-tarball.sh

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(x11)
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  intltool

%description
LXLauncher is designed as an open source replacement for the Asus Launcher
included in their EeePC. It is desktop-independent and follows 
freedesktop.org specs, so newly added applications will automatically show 
up in the launcher, and vice versa for the removed ones.
LXLauncher is part of LXDE, the Lightweight X11 Desktop Environment.

%prep
%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{git_builddir}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

git checkout -b %{main_version}-fedora %{git_rev}

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

cp -a [A-Z]* ..
%endif

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

sh autogen.sh


%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%configure --disable-silent-rules
# workaround for FTBFS #539147 and #661008
#touch -r po/Makefile po/stamp-it
%make_build


%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
mkdir -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/backgrounds
mkdir -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/icons

%if 0%{?use_gitbare}
cd ..
%endif
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS
%doc README
%license COPYING

%dir %{_sysconfdir}/xdg/lxlauncher/
%config(noreplace) %{_sysconfdir}/xdg/lxlauncher/gtkrc
%config(noreplace) %{_sysconfdir}/xdg/lxlauncher/gtk.css
%config(noreplace) %{_sysconfdir}/xdg/lxlauncher/settings.conf
%config(noreplace) %{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/desktop-directories/lxde-*.directory
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Mar 29 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.8-1
- 0.2.8

* Tue Mar 11 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.7-1
- 0.2.7

* Sun Feb 16 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.6-1
- 0.2.6

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5-17
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.5-1
- 0.2.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.4-1
- 0.2.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Christoph Wickert <wickert@kolabsys.com> - 0.2.2-4
- Rebuild for new menu-cache 0.5.x

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2
- Drop upstreamed patches
- Add patch to fix empty lxlauncher

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.1-10
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-8
- Use workaround for build loop again (#661008)
- Fix segfault if a window manager returns no data for current desktop

* Thu Jun 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-7
- Proper fix for build loop (#539147)

* Sat Feb 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-6
- Rebuild for menu-cache 0.3.2 soname bump

* Sun Feb 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-5
- Fix for the new behavior of menu-cache 0.3.0

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-4
- Add patch to fix DSO linking (#565072)

* Mon Nov 23 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-3
- Workaround for infinite loop that causes FTBFS (#539147)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1
- Switch from libgnome-menu to menu-cache

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 21 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.2-1
- Update to 0.2
- Remove empty ChangeLog

* Mon May 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-1
- Initial Fedora RPM
