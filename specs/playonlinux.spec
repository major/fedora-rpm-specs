Summary:       Graphical front-end for Wine
Name:          playonlinux
Version:       4.4
Release:       14%{?dist}
# playonlinux itself is GPL-3.0-only but uses other source codes, breakdown:
# GPL-2.0-or-later: python/{configurewindow/ConfigureWindow,debug,mainwindow,options,wrapper}.py
# GPL-2.0-or-later: python/{install/InstallWindow,setupwindow/{POL_SetupFrame,gui_server}}.py
# GPL-2.0-or-later: python/wine_versions/WineVersionsWindow.py
# MIT: src/check_direct_rendering.c
License:       GPL-3.0-only AND GPL-2.0-or-later AND MIT
URL:           https://www.playonlinux.com/
Source0:       https://github.com/PlayOnLinux/POL-POM-4/archive/%{version}/POL-POM-4-%{version}.tar.gz
# Upstream changes since last release
Patch0:        https://github.com/PlayOnLinux/POL-POM-4/compare/4.4...76a6580.patch#/playonlinux-4.4-git76a6580.patch
BuildRequires: gcc
BuildRequires: make
BuildRequires: gzip
BuildRequires: mesa-libGL-devel
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-natsort
BuildRequires: python3-wxpython4
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
Requires:      python3
Requires:      python3-natsort
Requires:      python3-wxpython4
# Required by python/mainwindow.py
Requires:      nc
Requires:      tar
Requires:      cabextract
Requires:      ImageMagick
Requires:      wget
Requires:      curl
Requires:      gnupg2
Requires:      xterm
%if 0%{?fedora} || 0%{?rhel} > 9
Requires:      gettext-runtime
%else
Requires:      gettext
%endif
Requires:      icoutils
Requires:      wine
Requires:      unzip
Requires:      jq
Requires:      p7zip-plugins
# Wine supported on these arches
ExclusiveArch: %{arm} aarch64 %{ix86} x86_64

%description
New users can often find Wine to be intimidating and difficult to use.

PlayOnLinux is a graphical front-end for Wine which allows to easily
install and use numerous games and applications designed to run with
Microsoft Windows.

PlayOnLinux has the database of Windows applications from which the user
can install desired application with a few clicks. It will automatically
setup the Wine prefix and download any required Windows libraries.

%prep
%autosetup -p1 -n POL-POM-4-%{version}

%build
%make_build \
  CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
  PYTHON="%{__python3} -m py_compile"

%install
%make_install

# Remove shebang from Python library
sed '1{/^#!\//d}' -i %{buildroot}%{_datadir}/%{name}/python/setupwindow/gui_server.py

# Remove misplaced files and directories
rm -rf %{buildroot}%{_datadir}/%{name}/{bin,tests,CHANGELOG.md,LICENCE,README.md,TRANSLATORS}
rm -f %{buildroot}%{_datadir}/%{name}/etc/PlayOnLinux.{appdata.xml,desktop}

# Byte compile importable Python modules outside of standard paths
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/python/

%find_lang pol

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/PlayOnLinux.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/PlayOnLinux.appdata.xml

%files -f pol.lang
%license LICENCE doc/copyright
%doc CHANGELOG.md README.md TRANSLATORS
%{_bindir}/%{name}
%{_bindir}/%{name}-pkg
%{_libexecdir}/%{name}-check_dd
%{_datadir}/%{name}/
%{_datadir}/appdata/PlayOnLinux.appdata.xml
%{_datadir}/applications/PlayOnLinux.desktop
%{_datadir}/pixmaps/%{name}*.png
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-pkg.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Robert Scheck <robert@fedoraproject.org> 4.4-13
- Add patch to replace pipes.quote() from deprecated Python
  pipes (#2318435, thanks to Sean Carlos and Patrick Scheck)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 26 2024 Robert Scheck <robert@fedoraproject.org> 4.4-11
- Add patch to remove unused import of deprecated Python
  asyncore.dispatcher (#2238120, thanks to Patrick Scheck)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 28 2022 Robert Scheck <robert@fedoraproject.org> 4.4-6
- Depend on gettext-runtime for Fedora 37 and later (#2119025)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 03 2021 Robert Scheck <robert@fedoraproject.org> 4.4-2
- Correct license tag to include GPLv2+ and MIT (#1913737 #c9)

* Thu Jan 07 2021 Robert Scheck <robert@fedoraproject.org> 4.4-1
- Upgrade to 4.4 (#1913737, thanks to Patrick Scheck)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Jiri Konecny <jkonecny@redhat.com> - 4.3.4-3
- Add gnupg as new dependency (Artem Polishchuk <ego.cordatus@gmail.com>)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Jiri Konecny <jkonecny@redhat.com> - 4.3.4-1
- Update to 4.3.4
- Update position of gui_server source code for sed

* Mon Dec 17 2018 Jiri Konecny <jkonecny@redhat.com> - 4.3.3-1
- Update to 4.3.3
- Fix python shebangs to python2
- Add new runtime dependency jq

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 4.2.12-1
- Update to 4.2.12 (#1463027)

* Wed May 31 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 4.2.11-1
- Update to 4.2.11 (#1457013)
- Remove patches contained in the new release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 4.2.10-10
- Define ExclusiveArch with arches wine supports

* Mon Oct 10 2016 Jiri Konecny <jkonecny@redhat.com> - 4.2.10-9
- Add patch to fix GUI layout issues on Wayland

* Sat Sep  3 2016 Jiri Konecny <jkonecny@redhat.com> - 4.2.10-8
- Add new patch for the updated appdata.xml file
- Improve old Patch2 for desktop file
- Rebase Patch6 and Patch7 on top of Patch2

* Wed Mar  9 2016 Jiri Konecny <jkonecny@redhat.com> - 4.2.10-7
- Apply patch which fixing bad icon path in a desktop file

* Sat Mar  5 2016 Ville Skyttä <ville.skytta@iki.fi> - 4.2.10-6
- Build with $RPM_OPT_FLAGS

* Fri Jan 22 2016 Jiri Konecny <jkonecny@redhat.com> 4.2.10-5
- Add patch which will fix installation of locales to the system

* Wed Jan 20 2016 Jiri Konecny <jkonecny@redhat.com> 4.2.10-4
- Change sed command to simpler and safer version
- Change appdata patches
- Fix installation of appdata
- Better description

* Wed Jan 13 2016 Jiri Konecny <jkonecny@redhat.com> 4.2.10-3
- Removed shebang and executable bit from scripts in /usr/share
- Change of summary and description
- Add 2 new patches which adding appdata.xml file
- Add new build requires for appstream-util check

* Thu Jan 7 2016 Jiri Konecny <jkonecny@redhat.com> 4.2.10-2
- Reworked patches for Makefile (Patch0, Patch1, Patch3 changed)
- Using make_install and make_build macros

* Mon Jan 4 2016 Jiri Konecny <jkonecny@redhat.com> 4.2.10-1
- New version 4.2.10
- Use more macros
- Add missing dependencies

* Thu Dec 10 2015 Jiri Konecny <jkonecny@redhat.com> 4.2.9-2
- Fixed missing lang files
- Remove exclude

* Wed Nov 11 2015 Jiri Konecny <jkonecny@redhat.com> 4.2.9-1
- Package creation
