%global         main_ver      1.4.5

%global         reponame      ClipIt
%global         gitdate       20241103
%global         gitcommit     f35db540c9d3c57b13439d66597736e917e8c9a1
%global         shortcommit   %(c=%{gitcommit}; echo ${c:0:7})

%global         tarballdate   20250116
%global         tarballtime   2347

%global         use_release   0
%global         use_gitbare   1
%global         use_gitcommit_as_ver  1

%if 0%{?use_gitbare} < 1
%global         use_release   1
%endif

%if 0%{?use_gitcommit_as_ver} >= 1
%global         rpm_ver       %{main_ver}^%{gitdate}git%{shortcommit}
%global         builddir_ver  %{main_ver}-%{gitdate}git%{shortcommit}
%else
%define         rpmver        %{main_ver}
%global         builddir_ver  %{main_ver}
%endif


Name:           clipit
Version:        %{rpm_ver}
Release:        1%{?dist}
Summary:        A lightweight, fully featured GTK+ clipboard manager

# meson.build says:	 GPL-3.0-or-later
# src/eggaccelerators.{c,h}	LGPL-2.1-or-later
# src/keybinder.{c,h}	LGPL-2.1-or-later
# Other source	GPL-3.0-or-later
# SPDX confirmed
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/CristianHenzel/ClipIt
%if 0%{?use_release} >= 1
Source0:        https://github.com/CristianHenzel/ClipIt/archive/v%{version}.tar.gz
%endif
%if 0%{?use_gitbare} >= 1
Source0:        %{reponame}-%{tarballdate}T%{tarballtime}.tar.gz
%endif
Source1:        %{name}.appdata.xml
Source2:        create-clipit-git-bare-tarball.sh
# clipit doesn't autostart in MATE
# Fixed upstream but not yet merged
Patch0:         0001-Autostart-in-MATE.patch
# Force GDK_BACKEND to x11
Patch1:         clipit-1.4.5-force-gdk_backend-x11.patch
# Fix -Werror=incompatible-pointer-types
Patch3:         https://sources.debian.org/data/main/c/clipit/1.4.5%2Bgit20210313-3/debian/patches/incompatible-pointer-types.patch
# https://github.com/CristianHenzel/ClipIt/pull/211
# Fix compilation with C23 struct function prototype
Patch4:         clipit-pr211-c23-function-prototype.patch

%if 0%{?use_gitbare} >= 1
BuildRequires:  git
%endif
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  /usr/bin/appstream-util
Requires:       xdotool

%description
ClipIt is a lightweight, fully featured GTK+ clipboard manager. It was forked
from Parcellite, adding additional features and bug-fixes to the project.
ClipIts main features are:
* Save a history of your last copied items
* Search through the history
* Global hot-keys for most used functions
* Execute actions with clipboard items
* Exclude specific items from history


%prep
%if 0%{?use_release} >= 1
%setup -q -n %{reponame}-%{builddir_ver}
%endif

%if 0%{?use_gitbare} >= 1
%setup -q -c -n %{reponame}-%{builddir_ver} -T -a 0
git clone ./%{reponame}.git

cd %{reponame}
git checkout -b fedora-%{builddir_ver}-head %{gitcommit}
cp -a [A-Z]* ..

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"
%endif

%patch -P0 -p1 -b .mate
%patch -P1 -p1 -b .nowayland
%patch -P3 -p1 -b .c99_cast
%patch -P4 -p1 -b .c23

sed -i data/clipit.desktop.in -e '\@_Comment.*hr@d'
sed -i data/clipit-startup.desktop.in -e '\@_Comment.*hr@d'

%if 0%{?use_gitbare} >= 1
git commit -m "Apply Fedora specific configuration" -a
%endif

./autogen.sh
%global optflags %optflags -std=gnu23

%build
%if 0%{?use_gitbare} >= 1
cd %{reponame}
%endif

%configure \
	--with-gtk3 \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare} >= 1
cd %{reponame}
%endif

%make_install

%if 0%{?use_gitbare} >= 1
cd ..
%endif

%find_lang %{name}

desktop-file-install --delete-original \
    --remove-category=Application \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --delete-original \
    --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-startup.desktop

mkdir -p %{buildroot}%{_metainfodir}
install -c -p -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc README.md

%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/icons/hicolor/scalable/apps/%{name}-trayicon*.svg
%{_metainfodir}/%{name}.appdata.xml

%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop

%changelog
* Thu Jan 16 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5^20241103gitf35db54-1
- Update to the latest git (20241103gitf35db54)
- Fix compilation with C23 for struct function prototypes

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5^20210513gite5fa64c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5^20210513gite5fa64c-6
- Apply debian patch for -Werror=incompatible-pointer-types

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5^20210513gite5fa64c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5^20210513gite5fa64c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5^20210513gite5fa64c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5^20210513gite5fa64c-2
- Change -Wincompatible-pointer-types from error to warning

* Wed Jan 10 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5^20210513gite5fa64c-1
- Use hat for release, change EVR scheme
- SPDX migration

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4.D20210513gite5fa64c.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4.D20210513gite5fa64c.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Florian Weimer <fweimer@redhat.com> - 1.4.5-4.D20210513gite5fa64c.3
- C99 compatibility fixes

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4.D20210513gite5fa64c.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4.D20210513gite5fa64c.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5-4.D20210513gite5fa64c
- Update to the latest git
  - increase POPUP_DELAY to workaround hotkey popup issue

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 29 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5-2
- Force GDK_BACKEND to x11 (bug 1943480, bug 1943509)

* Fri Mar 19 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5-1
- 1.4.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.4-8
- Backport upstream patch to fix history purge time being too short (bug 1640765)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Michael Simacek <msimacek@redhat.com> - 1.4.4-2
- Fix starting outside terminal

* Fri Jun 29 2018 Michael Simacek <msimacek@redhat.com> - 1.4.4-1
- Update to upstream version 1.4.4

* Mon Feb 19 2018 Michael Simacek <msimacek@redhat.com> - 1.4.2-17
- AppData fixes
- Specfile cleanup
- Add BRs on gcc and make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.2-15
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Nikos Roussos <nikos@autoverse.net> 1.4.2-9
- Fix appdata syntax

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Nikos Roussos <nikos@autoverse.net> 1.4.2-6
- Add EPEL support

* Thu Sep 12 2013 Nikos Roussos <nikos@autoverse.net> 1.4.2-5
- Fix MATE autostart. Add appdata

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Nikos Roussos <nikos@autoverse.net> 1.4.2-1
- Update to 1.4.2

* Wed Feb 29 2012 Nikos Roussos <nikos@autoverse.net> 1.4.1-5
- Fix gtk+ inclusion bug, see patch1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Nikos Roussos <nikos@autoverse.net> 1.4.1-3
- Fixed dependency missing, de translation bug, desktop icon bug

* Fri Jul 01 2011 Nikos Roussos <nikos@autoverse.net> 1.4.1-2
- Fixed config warning and more spec errors

* Wed Jun 01 2011 Nikos Roussos <nikos@autoverse.net> 1.4.1-1
- Initial Fedora RPM
