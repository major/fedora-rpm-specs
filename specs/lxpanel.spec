# Review: https://bugzilla.redhat.com/show_bug.cgi?id=219930

%global	use_release	0
%global	use_gitbare	1

%if 0%{?use_gitbare} < 1
# force
%global	use_release	1
%endif

%global	git_version	%{nil}
%global	git_ver_rpm	%{nil}
%global	git_builddir	%{nil}

%if 0%{?use_gitbare}
%global	gittardate		20241225
%global	gittartime		1813

%global	gitbaredate	20241223
%global	git_rev		d45c45ae6515f70a7f4fc79d5f374183d7b8e4b7
%global	git_short		%(echo %{git_rev} | cut -c-8)
%global	git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitbare}
%global	git_ver_rpm	^%{git_version}
%global	git_builddir	-%{git_version}
%endif

%dnl %global		use_gcc_strict_sanitize	1

%global		main_version	0.10.1
%global		baserelease	1

Name:			lxpanel
Version:		%{main_version}%{git_ver_rpm}
Release:		%{baserelease}%{?dist}%{?use_gcc_strict_sanitize:.san}
Summary:		A lightweight X11 desktop panel

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{main_version}.tar.xz
%endif
# Shell script to create tarball from git scm
Source100:		create-tarball-from-git.sh
Source101:		create-lxpanel-git-bare-tarball.sh

# Fedora bug: https://bugzilla.redhat.com/show_bug.cgi?id=746063
Patch0:		lxpanel-0.8.1-Fix-pager-scroll.patch

# Patches reported upstream
Patch52:		0002-SF-894-task-button-correctly-find-the-window-current.patch

## distro specific patches
# default configuration
Patch100:		lxpanel-0.5.9-default.patch
# use nm-connection-editor to edit network connections
# Applied in 0.8.2
#Patch101:		lxpanel-0.8.1-nm-connection-editor.patch
# use zenity instead of xmessage to display low battery warning
Patch102:		lxpanel-0.8.2-battery-plugin-use-zenity.patch
# volumealsa: poll alsa mixer several times at startup (for pipewire)
# https://bugzilla.redhat.com/show_bug.cgi?id=1960829
Patch103:		lxpanel-0.10.1-0003-volumealsa-poll-alsa-mixer-several-times-at-startup.patch
# batt: make the status green on batt when the state is "not charging"
Patch104:		lxpanel-0.10.1-batt-chaging-pending.patch


#BuildRequires:	docbook-utils
BuildRequires:	make
BuildRequires:	gettext
BuildRequires:	intltool

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(libfm-gtk)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(keybinder)
BuildRequires:	pkgconfig(indicator-0.4)
BuildRequires:	pkgconfig(libmenu-cache) >= 0.3.0
BuildRequires:	pkgconfig(alsa)
BuildRequires:	/usr/bin/curl-config

%if 0%{?use_gitbare}
BuildRequires:	automake
BuildRequires:	libtool
%endif

%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif

BuildRequires:	git
BuildRequires:	gcc

# required for the battery plugin with Patch102
Recommends:	zenity


%description
lxpanel is a lightweight X11 desktop panel. It works with any ICCCM / NETWM 
compliant window manager (eg sawfish, metacity, xfwm4, kwin) and features a 
tasklist, pager, launchbar, clock, menu and sytray.

%package        devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


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

cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
	commit=$(echo "$line" | sed -e 's|[ \t].*||')
	git cherry-pick $commit
done

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

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-maintainer@fedoraproject.org"

%if 0%{?use_release}
git add .
git rm --cached \
	config.guess config.sub configure \
	ltmain.sh \
	%{nil}
git commit -m "base" -q
%endif

cat %PATCH52 | git am
cat %PATCH103 | git am

%patch -P0 -p1 -b .revert

%patch -P100 -p1 -b .default
#%%patch101 -p1 -b .system-config-network
%patch -P102 -p1 -b .zenity
%patch -P104 -p1 -b .batt_pending

git commit -m "Apply Fedora specific configulation" -a

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%if 0%{?use_gitbare}
bash autogen.sh
%endif

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

%configure \
	--enable-indicator-support \
	--disable-silent-rules \
	--with-plugins='netstatus,volume,cpu,deskno,batt,kbled,xkb,thermal,cpufreq,monitors,indicator,weather' \
	%{nil}
%make_build


%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/lxpanel/*.la

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}


%files -f %{name}.lang
%license	COPYING
%doc	AUTHORS
%doc	README
%config(noreplace)	%{_sysconfdir}/xdg/lxpanel/

%{_bindir}/lxpanel*
%{_datadir}/lxpanel/
%{_libdir}/lxpanel/
%{_mandir}/man1/lxpanel*

%files devel
%{_includedir}/lxpanel/
%{_libdir}/pkgconfig/lxpanel.pc

%changelog
* Wed Dec 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20241223gitd45c45ae-1
- Update to the latest git

* Fri Dec 20 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20241213git5eb39f11-1
- Update to the latest git

* Fri Sep 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20240825gitffd815fc-1
- Update to the latest git

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20240823git95815af3-1
- Update to the latest git

* Thu Aug 08 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20240807git65d86bec-1
- Update to the latest git

* Fri Jul 26 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20230918git633a2d46-5
- Apply upstream PR to fix gcc14 -Werror=incompatible-pointer-types

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1^20230918git633a2d46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1^20230918git633a2d46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20230918git633a2d46-2
- Change -Wincompatible-pointer-types from error to warning

* Tue Sep 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20230918git633a2d46-1
- Update to the latest git

* Sun Aug 20 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20230817gitdd010115-1
- Update to the latest git

* Mon Aug 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1^20230806git41a08b51-1
- Update to the latest git

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb  7 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1-4
- batt: make the status green on batt when the state is "not charging"

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10.1-3
- Disable Wireless Extensions support (Fedora 36+)
  https://fedoraproject.org/wiki/Changes/RemoveWirelessExtensions

* Sun Aug  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1-2
- volumealsa: poll alsa mixer several times at startup (for pipewire) (bug 1960829)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.1-1
- 0.10.1 release

* Mon Feb  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-4.D20210130git60edebfe
- Update to the latest git

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2.D20190301gitb9ad6f2a.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2.D20190301gitb9ad6f2a.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2.D20190301gitb9ad6f2a.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2.D20190301gitb9ad6f2a.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-2.D20190301gitb9ad6f2a
- Rebase to the latest git

* Thu Feb 28 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-1
- 0.10.0 release

* Fri Feb 22 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-9.D20190222gitd0d3cb41
- Rebase to the latest git
  - Rework weather plugin to use OpenWeatherMap

* Mon Feb 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-8.D20190106git370382d3
- Rebase to the latest git
  - Upstream fix for correcting "free memory" usage display

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7.D20180305gitb85c71a6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7.D20180305gitb85c71a6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-7.D20180305gitb85c71a6
- Patch53, 54 upstreamed (and Patch54 revised by the upstream, thanks!)

* Sun Mar  4 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-6.D20180109git2ddf8dfc
- Fix segv on another right button click on taskbutton after once destroying window
  using taskbutton with clicking right button on it (SF900)

* Sat Mar  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-5.D20180109git2ddf8dfc
- Remove libtool file

* Wed Feb 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-4.D20180109git2ddf8dfc
- Fix crash when color is removed from monitor settings (bug 1544406)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3.D20180109git2ddf8dfc.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-3.D20180109git2ddf8dfc
- Two fixes for taskbutton plugin related to multiple monitor configuration

* Tue Jan  9 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-2.D20180109git2ddf8dfc
- thermal patch merged upstream
- Update to the latest git

* Mon Jan  8 2018 Mamoru TASAKA <mtasaka@fedoraproject.org>
- dclock, weather - merged upstream
- thermal - rewrite per upstream request
- Backport pager mouse scroll fix

* Wed Jan  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Use git bare source
- Make some plugins reflect panel configuration change immediately (bug 1261464)
  - For dclock weather thermal

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-1
- 0.9.3

* Mon Dec 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-1
- 0.9.2

* Fri Nov 25 2016 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Today's snapshot

* Tue Nov 22 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.1-1
- 0.9.1

* Mon Nov 21 2016 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Today's snapshot

* Sun Nov 20 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.0-1
- 0.9.0

* Sat Nov 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org>
- Today's snapshot

* Wed Nov 16 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.99-0.1.D20161115gitd7022af2
- Update to the latest trunk

* Mon Jun 27 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-2
- Backport some upstream fix
  - batt: select battery number to monitor (bug 1349563)

* Tue Mar  1 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.1-2
- Apply upstream fix for panel size

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.1-1
- 0.8.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.6.1-5
- Fix FTBFS with -Werror=format-security (#1037185, #1106143)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 29 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-3
- Rebuild against menu-cache 0.5.x (#1035902)

* Tue Nov 26 2013  Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-2
- Fix conditional to actually apply the fix for the quicklauncher (#1035004)

* Mon Nov 11 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1
- Fix some changelog dates

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Aug 03 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.12-3
- Use zenity instead of xmessage to display low battery warnings

* Sun May 12 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.12-2
- Another patch for to fix the "flash_window_timeout" crash (#587430)
- Make sure launchers in default config work on Fedora >= 19

* Tue Feb 12 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.12-1
- Update to 0.5.12, should finally fix #587430 (fingers crossed)

* Sun Nov 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.10-3
- Fix annoying crash of the taskbar (#587430)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.10-1
- Update to 0.5.10

* Sun Jun 10 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.9-1
- Update to 0.5.9 (#827779)
- Fix the netstat plugin (#750400)
- Correctly show 'Application launch bar' settings window (#830198)
- Reverse scrolling direction in workspace switcher (#746063)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.8-1
- Update to 0.5.8
- Drop upstreamed fix-build-issue... patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6 (fixes at least #600763 and #607129, possibly more) 
- Remove all patches from GIT

* Sat Mar 20 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-3
- Fix two race conditions (#554174 and #575053)
- Hide empty menus
- Lots of fixes
- Update translations from Transifex

* Sat Feb 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-2
- Rebuild for menu-cache 0.3.2 soname bump
- Add some more menu code changes from git
- New 'lxpanelctl config' command

* Sun Feb 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5 and rebuild against menu-cache 0.3.1
- Drop upstreamed patches
- Add patch to fix DSO linking (#564746)

* Sun Jan 31 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4.1-2
- Fix windows Raise/Focus problem
- Make autohidden panels blink when there is a popup from a systray icon
- Remove debugging output

* Wed Dec 16 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4.1-1
- Update to 0.5.4.1
- Remove upstreamed patches

* Fri Dec 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4
- Restore toggle functionality of the show deskop plugin

* Thu Aug 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.3-1
- Update to 0.5.3, fixes vertical panel size (#515748)

* Thu Aug 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Sun Aug 02 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1
- Remove cpu-history.patch and manpages.patch, fixed upstream

- Thu Jul 27 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Sat Jul 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-2
- Patch to fix CPU usage monitor history
- Make netstatus plugin prefer nm-connetction-editor over system-config-network
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Fri Apr 24 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0 final (fixes #496833)

* Sun Mar 22 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.999-1
- Update to 0.4.0 Beta 2
- Build alsa mixer plugin
- BR wireless-tools-devel

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 01 2008 Christoph Wickert <cwickert@fedoraproject.org> 0.3.8.1-3
- Add battery callback patch
- Add gnome-run icon and update default patch

* Thu Aug 28 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.3.8.1-2
- re-create patches for rpmbuild's fuzz=0

* Tue Jul 08 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.3.8.1-1
- new upstream version: 0.3.8.1

* Fri Jul 04 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.3.8-1
- new upstream version: 0.3.8
- new BR in this version: intltool

* Sun Jun 15 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.3.7-1
- new upstream version: 0.3.7

* Mon May 05 2008 Sebastian Vahl <fedora@deadbabylon.de> 0.3.5.4-1
- new upstream version: 0.3.5.4
- update lxpanel-default.patch

* Mon Mar 31 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.9.0-1
- new upstream version: 0.2.9.0

* Wed Mar 26 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.8-2
- BR: docbook-utils

* Thu Mar 20 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.8-1
- new upstream version: 0.2.8
- add lxpanel-0.2.8-manpage.patch

* Thu Mar 13 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.7.2-1
- new upstream version: 0.2.7.2
- update lxpanel-default.patch

* Mon Feb 25 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.6-1
- new upstream version: 0.2.6
- update lxpanel-default.patch

* Sat Feb 09 2008 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.4-6
- rebuild for new gcc-4.3

* Thu Aug 16 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.4-5
- Change License to GPLv2+

* Mon Jan 08 2007 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.4-4
- Fixed some minor issues from the review process (#219930)

* Sun Dec 17 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.4-3
- BR: startup-notification-devel
- Added Patch1 from Chung-Yen to fix wrong starters in default config
- Removed pcmanfm.desktop from the default config for the moment

* Fri Dec 01 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.4-2
- BR: gettext

* Wed Nov 29 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.4-1
- New upstream version: 0.2.4

* Sun Nov 05 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.2-1
- New upstream version: 0.2.1

* Fri Nov 03 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.2.0-1
- New upstream version: 0.2.0

* Wed Oct 25 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-2
- Rebuild for FC6

* Thu Oct 14 2006 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-1
- Initial Release
