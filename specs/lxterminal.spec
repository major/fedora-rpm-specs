%global		use_release	0
%global		use_git		0
%global		use_gitbare	1

%if 0%{?use_git} < 1
%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20250210
%global		gittartime		1638

%global		gitbaredate	20241210
%global		git_rev		116f89f71769b9a9852845f9308f73ba5de26bff
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_git} || 0%{?use_gitbare}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif


%global		main_version	0.4.0

%dnl	%global		use_gcc_strict_sanitize	1

%undefine		_changelog_trimtime

%global		baserelease	1

Name:			lxterminal
Version:		%{main_version}%{git_ver_rpm}
Release:		%{baserelease}%{?dist}%{?use_gcc_strict_sanitize:.san}
Summary:		Desktop-independent VTE-based terminal emulator
Summary(de):	Desktop-unabhängiger VTE-basierter Terminal Emulator

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:		%{name}-%{main_version}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{main_version}.tar.xz
%endif
# Shell script to create tarball from git scm
Source100:		create-lxterminal-git-bare-tarball.sh
# Fix segfault when closing window (bug 2207699)
Patch0:		lxterminal-0.4.0-avoid-segv-on-window-close.patch

BuildRequires:	git

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(vte-2.91)

BuildRequires:	/usr/bin/xsltproc
BuildRequires:	docbook-utils
BuildRequires:	docbook-style-xsl

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gettext

%if 0%{?git_snapshot}
BuildRequires:	automake
BuildRequires:	libtool
%endif

%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif

%description
LXterminal is a VTE-based terminal emulator with support for multiple tabs. 
It is completely desktop-independent and does not have any unnecessary 
dependencies. In order to reduce memory usage and increase the performance 
all instances of the terminal are sharing a single process.

%description -l de
LXTerminal ist ein VTE-basierter Terminalemulator mit Unterstützung für 
mehrere Reiter. Er ist komplett desktop-unabhängig und hat keine unnötigen 
Abhängigkeiten. Um den Speicherverbrauch zu reduzieren und die Leistung zu
erhöhen teilen sich alle Instanzen des Terminals einen einzigen Prozess.

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

%patch -P0 -p1 -b .closewin
git commit -m "Avoid segfault" -a

sh autogen.sh

%build
%global optflags_orig %optflags
%global optflags %optflags_orig -fno-optimize-sibling-calls

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

%if 0%{?use_gitbare}
cd %{name}
%endif

%configure \
	--enable-gtk3 \
	--enable-man \
	--disable-silent-rules \
	%{nil}

%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif


%make_install

desktop-file-install \
	--delete-original \
	--remove-category=Utility \
	--add-category=System \
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
	${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}


%files -f %{name}.lang
%doc	AUTHORS
%license	COPYING
%doc	NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*.1*


%changelog
* Mon Feb 10 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20241210git116f89f7-1
- Update to the latest git

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0^20240821gitda62ee20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20240821gitda62ee20-1
- Update to the latest git

* Sun Aug 11 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20240806gitb6aad51b-1
- Update to the latest git

* Wed Aug 07 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20240806gita942d552-1
- Update to the latest git

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0^20230917git9b4299c2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20230917git9b4299c2-4
- Apply upstream patch for gcc14 -Werror=incompatible-pointer-types

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0^20230917git9b4299c2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20230917git9b4299c2-2
- Change -Wincompatible-pointer-types from error to warning

* Sun Dec 31 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20230917git9b4299c2-1
- Update to the latest git

* Thu Aug 31 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0^20230828gita349c517-1
- Update to the latest git

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9.D20211203git0febe16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun  9 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-8.D20211203git0febe16
- Avoid segfault when closing window (bug 2207699)
- SPDX migration

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7.D20211203git0febe16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-6.D20211203git0febe16
- Update to the latest git

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov  5 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-3
- Disable call instruction optimization to jmp for debugging
  (c.f. bug 2016637)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-1
- 0.4.0

* Fri Feb  5 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-9.D20210202git54cd5fc
- Update to the latest git

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8.D20200316gitcb2992e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7.D20200316gitcb2992e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-6.D20200316gitcb2992e
- Update to the latest git

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5.D20190717gitcb2992e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-4.D20190717gitcb2992e
- Update to the latest git
- F-31+: use vte-2.91 + gtk3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-1
- 0.3.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6.D20180225git3779fce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-5.D20180225git3779fce
- Use latest git, switch to git bare
- PR patch for unixsocket.c optimization issue merged upstream

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-3
- Remove obsolete scriptlets

* Mon Dec 25 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-2
- Add PR patch for unixsocket.c optimization / startup issue

* Mon Nov  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.1-1
- 0.3.1

* Fri Sep  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-6.D20170822git1e9f2d4d
- Update to the latest git

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-3
- Upstream git patch to address CVE-2016-10369 (bug 1449114)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-8.D20161208git9e61321c
- Update to the latest git

* Sun Dec  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-7.D20161202git6da8eae6
- Update to the latest git

* Wed Aug 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-6.D20160809git80291921
- Update to the latest git
  - https://github.com/lxde/lxterminal/pull/21
  - https://github.com/lxde/lxterminal/issues/20

* Thu Aug  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-5.D20160607gitd4014424
- Try the latest git

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.D20151126gitbe658ad3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-3.D20151126gitbe658ad3
- Try the latest git

* Thu Jul 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-2
- Fix scriptlet

* Thu Jun 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-1
- 0.2.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.11-7
- Really drop desktop vendor tag.

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.11-6
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.11-2
- Rebuild for new libpng

* Tue Aug 30 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11
- Remove upstreamed vte patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9
- Add patch for vte >= 0.20.0

* Mon Jul 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8
- Drop all previous patches, they are part of 0.1.8
- Update German translation

* Thu May 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.7-2
- Major code rework from git (fixes #571591 and 596358)

* Wed Mar 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Wed Feb 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-3
- Add patch to fix DSO linking (#564717)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6
- Remove missing-icons.patch, changes got upstreamed

* Tue Jun 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-2
- Rebuilt for libvte SONAME bump

* Wed May 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5
- Fix icon for Info menu entry

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 26 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sat Jun 28 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3
- Add the new manpage

* Fri Jun 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Initial Fedora package
