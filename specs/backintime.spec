Name:             backintime
Version:          1.5.3
Release:          3%{?dist}
Summary:          Simple backup tool inspired from the Flyback project and TimeVault
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              https://github.com/bit-team/backintime
Source0:          https://github.com/bit-team/backintime/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    cronie
BuildRequires:    desktop-file-utils
BuildRequires:    gettext
BuildRequires:    python-rpm-macros
BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    systemd
Requires:         %{name}-common = %{version}-%{release}
# we place additional icons
Requires:         hicolor-icon-theme

# execution of tests
BuildRequires:    python%{python3_pkgversion}-keyring
BuildRequires:    python%{python3_pkgversion}-pyfakefs
BuildRequires:    python%{python3_pkgversion}-pytest
BuildRequires:    python%{python3_pkgversion}-dbus
BuildRequires:    python%{python3_pkgversion}-pyqt6-base
BuildRequires:    /usr/bin/ssh-agent
BuildRequires:    /usr/bin/ps
BuildRequires:    /usr/bin/rsync
BuildRequires: make

%description
Back In Time is a simple backup system for Linux inspired from 
“flyback project” and “TimeVault”. The backup is done by taking 
snapshots of a specified set of directories.

%package          common
Summary:          Common files for %{name}
Requires:         cronie
Requires:         openssh-clients
Requires:         python%{python3_pkgversion}-keyring
Requires:         python%{python3_pkgversion}-dbus
Requires:         python%{python3_pkgversion}-packaging
Requires:         fuse-sshfs
Requires:         fuse-encfs
Requires:         bindfs
Requires:         /usr/bin/ssh-agent
Requires:         /usr/bin/ps
Requires:         /usr/bin/rsync

%description      common
Back In Time is a simple backup system for Linux inspired from 
“flyback project” and “TimeVault”. The backup is done by taking 
snapshots of a specified set of directories.

This package contains non GUI files for %{name}.

%package          plugins
Summary:          Plugins for %{name}
Requires:         %{name}-common = %{version}-%{release}
Provides:         backintime-notify = %{version}-%{release}
Obsoletes:        backintime-notify < 1.1.12-1

%description      plugins
%summary}.

%package          qt
Summary:          Qt frontend for %{name}
Requires:         %{name}-common = %{version}-%{release}
Requires:         libnotify
Requires:         polkit
Requires:         python%{python3_pkgversion}-pyqt6
Requires:         python%{python3_pkgversion}-SecretStorage
Requires:         python%{python3_pkgversion}-keyring
Requires:         qt6-qttranslations
Requires:         xdpyinfo
Provides:         backintime-gnome = %{version}-%{release}
Obsoletes:        backintime-gnome < 1.1.12-1
Provides:         backintime-kde = %{version}-%{release}
Obsoletes:        backintime-kde < 1.1.12-1
Provides:         %{name}-qt4 = %{version}-%{release}
Obsoletes:        %{name}-qt4 < 1.1.24-8

Recommends:       %{name}-plugins

%description      qt
BackInTime is a simple backup system for Linux inspired from 
“flyback project” and “TimeVault”. The backup is done by taking 
snapshots of a specified set of directories.

This package contains the Qt frontend of BackInTime.


%prep
%setup -q

# Fix documentation directories.
#sed -i -e "s|'%{name}-common'|'%{name}'|g" common/config.py
#sed -i -e "s|%{name}-common|%{name}|g" common/configure qt/configure

%build
pushd common
%configure \
    --python=%{__python3} 
popd
pushd qt
%configure \
    --python=%{__python3} 
popd

%make_build -C common
%make_build -C qt


%install
#Force Python 3 to be used for byte compilation:
%global __python %{__python3}
%make_install -C common
%make_install -C qt

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/qt

%find_lang %{name}

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}-qt.desktop
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications/ \
        --add-category="Settings;" \
        %{buildroot}%{_datadir}/applications/%{name}-qt-root.desktop

ln -s consolehelper \
      %{buildroot}%{_bindir}/%{name}-qt-root

mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps/
cat << EOF > %{buildroot}%{_sysconfdir}/security/console.apps/%{name}-qt-root
USER=root
PROGRAM=%{_bindir}/%{name}-qt-root
SESSION=true
EOF

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat << EOF > %{buildroot}%{_sysconfdir}/pam.d/%{name}-qt-root
#%PAM-1.0
auth            include         config-util
account         include         config-util
session         include         config-util
EOF


%check
rm common/test/test_tools.py
rm common/test/test_sshtools.py
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
rm common/test/test_lint.py qt/test/test_lint.py
# remove test until PyFakeFS is not updated 
rm common/test/test_uniquenessset.py
make -C common test-v

%files common -f %{name}.lang
%doc %{_datadir}/doc/%{name}-common/
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_bindir}/%{name}-askpass
%{_datadir}/%{name}/common/
%{_datadir}/bash-completion/completions/backintime
%{_datadir}/dbus-1/system-services/net.launchpad.backintime.serviceHelper.service
%{_datadir}/polkit-1/actions/net.launchpad.backintime.policy
%{_datadir}/dbus-1/system.d/net.launchpad.backintime.serviceHelper.conf
%{_datadir}/metainfo/io.github.bit_team.back_in_time.gui.metainfo.xml
%{_mandir}/man1/%{name}*

%files plugins
%{_datadir}/%{name}/plugins/

%files qt
%doc %{_docdir}/%{name}-qt/
%{_bindir}/%{name}-qt
%{_bindir}/%{name}-qt-root
%{_bindir}/%{name}-qt_polkit
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/applications/%{name}-qt-root.desktop
%{_datadir}/backintime/qt/
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_datadir}/bash-completion/completions/backintime-qt
%config(noreplace) %{_sysconfdir}/pam.d/%{name}-qt-root
%config %{_sysconfdir}/security/console.apps/%{name}-qt-root


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- fix build for https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 Johannes Lips <hannes@fedoraproject.org> - 1.5.3-1
- update to latest upstream release

* Tue Aug 06 2024 Johannes Lips <hannes@fedoraproject.org> - 1.5.2-1
- update to latest upstream release

* Sat Jul 27 2024 Johannes Lips <hannes@fedoraproject.org> - 1.5.1-1
- update to latest upstream release
- move to PyQt6

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.3-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 01 2024 Johannes Lips <hannes@fedoraproject.org> - 1.4.3-1
- update to latest upstream release

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 02 2023 Johannes Lips <hannes@fedoraproject.org> - 1.4.1-1
- update to latest upstream release

* Sat Sep 16 2023 Johannes Lips <hannes@fedoraproject.org> - 1.4.0-1
- update to latest upstream release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Johannes Lips <hannes@fedoraproject.org> - 1.3.3-1
- update to latest upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 19 2022 Johannes Lips <hannes@fedoraproject.org> - 1.3.2-1
- upstream fix for issue https://github.com/bit-team/backintime/issues/1175

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Johannes Lips <hannes@fedoraproject.org> - 1.3.1-2
- added patch to fix tests with python 3.10

* Mon Jul 05 2021 Johannes Lips <hannes@fedoraproject.org> - 1.3.1-1
- update to latest upstream release

* Sun Jul 04 2021 Johannes Lips <hannes@fedoraproject.org> - 1.3.0-1
- update to latest upstream release

* Sun May 30 2021 Johannes Lips <hannes@fedoraproject.org> - 1.2.1-7
- fix non-updating progress bar

* Sun May 30 2021 Johannes Lips <hannes@fedoraproject.org> - 1.2.1-6
- fix for crash

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 1.2.1-4
- Require xdpyinfo not xorg-x11-utils

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Johannes Lips <hannes@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- clean up of post, postun and posttrans sections

* Tue Aug 20 2019 Johannes Lips <hannes@fedoraproject.org> - 1.2.0-6
- added upstream patch to fix #1709064

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Raphael Groner <projects.rg@smart.ms> - 1.2.0-4
- reenable execution of tests

* Tue Apr 30 2019 Johannes Lips <hannes@fedoraproject.org> - 1.2.0-3
- fixed the obsoletes and provides

* Mon Apr 29 2019 Johannes Lips <hannes@fedoraproject.org> - 1.2.0-2
- fixed bytecompilation 
- readded plugins subpackage

* Sat Apr 27 2019 Johannes Lips <hannes@fedoraproject.org> - 1.2.0-1
- update to version 1.2.0
- switch to Qt5
- renamed the Qt4 subpackage and removed the plugins subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 14 2018 Raphael Groner <projects.rg@smart.ms> - 1.1.24-6
- prope bytecompilation of python and comply with modules policy, rhbz#1634323
- introduce plugins subpackage

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.24-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.24-2
- Remove obsolete scriptlets

* Fri Nov 10 2017 Johannes Lips <hannes@fedoraproject.org> - 1.1.24-1
- update to version 1.1.24
- fixing CVE-2017-16667

* Sun Oct 29 2017 Johannes Lips <hannes@fedoraproject.org> - 1.1.22-1
- update to version 1.1.22

* Sat Aug 05 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.20-3
- Fix FTBFS with new BR python-rpm-macros

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Johannes Lips <hannes@fedoraproject.org> - 1.1.20-1
- update to version 1.1.20

* Fri Mar 31 2017 Johannes Lips <hannes@fedoraproject.org> - 1.1.18-1
- update to version 1.1.18

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Johannes Lips <hannes@fedoraproject.org> - 1.1.12-3
- fixed icon removal with sed

* Wed Jul 13 2016 Raphael Groner <projects.rg@smart.ms> - 1.1.12-2
- use make and python3 macros
- execute tests for common

* Thu Mar 03 2016 Johannes Lips <hannes@fedoraproject.org> - 1.1.12-1
- update to version 1.1.12
- removal of desktop dependent sub-packages

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 12 2014 Christopher Meng <rpm@cicku.me> - 1.0.36-1
- Update to 1.0.36

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 22 2013 Christopher Meng <rpm@cicku.me> - 1.0.34-1
- Update to 1.0.34(BZ#1043054)
- Switch to kdesu(BZ#1038893)

* Sun Nov 24 2013 Christopher Meng <rpm@cicku.me> - 1.0.28-2
- Enable notify plugin, separate plugins into different subpackages.
- Add missing python-SecretStorage dependency(BZ#1031403).
- Remove fuse group check(BZ#1010728).
- python-keyring incompatibility fix(BZ#1026542).

* Mon Oct 21 2013 Christopher Meng <rpm@cicku.me> - 1.0.28-1
- Update to 1.0.28(BZ#1021192) with fixes(BZ#1014293),(BZ#1014976).

* Thu Sep 12 2013 Christopher Meng <rpm@cicku.me> - 1.0.26-2
- Add missing python-keyring dependency(BZ#1007315).

* Wed Sep 11 2013 Christopher Meng <rpm@cicku.me> - 1.0.26-1
- Update to 1.0.26(BZ#1003304),(BZ#951248).
- Fix Bugs(BZ#999935),(BZ#922534).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 09 2011 Tim Jackson <rpm@timj.co.uk> - 1.0.8-2
- Add missing dependency on gnome-python2-gnome (rhbz#720577)

* Sun Oct 09 2011 Tim Jackson <rpm@timj.co.uk> - 1.0.8-1
- Update to version 1.0.8

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Tim Jackson <rpm@timj.co.uk> - 1.0.6-3
- Fix bad ownership of language files (RHBZ #569407)

* Wed Feb 02 2011 Tim Jackson <rpm@timj.co.uk> - 1.0.6-2
- Fix error if notify-python is not installed (RHBZ #630969)

* Wed Feb 02 2011 Tim Jackson <rpm@timj.co.uk> - 1.0.6-1
- Update to version 1.0.6

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.26-4
- recompiling .py files against Python 2.7 (rhbz#623275)

* Wed Sep 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.26-3
- Add patch0 to secure backups

-* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.26-1
- New upstream release
- Drop 'removecheck'-patch

* Sun May 17 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.24-3
- Fix sammries, RHBZ #501085

* Tue May 12 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.24-2
- fix doc issues, LP #375113

* Thu May 07 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.24-1
- New upstream release

* Sat Apr 25 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.22-2
- Remove Patch for desktop-files and do the changes in spec-file
- Change description of gnome package to "Gnome frontend for NAME" 
- Change description of kde package to "KDE frontend for NAME"
- Add TRANSLATIONS to DOC of common package
- Mark _DATADIR/gnome/help/NAME as DOC
- Mark _DATADIR/doc/kde4/HTML/en/NAME as DOC
- Use cp -p when copying from bindir to sbindir

* Wed Apr 22 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.22-1
- New upstream release
- Add Patch to remove the Desktopchecks in configure

* Mon Apr 06 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.20-1
- New upstream release
- Add consolehelperstuff for root-access

* Tue Mar 17 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.16.1-1
- New upstream release

* Tue Mar 10 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.9.14-1
- Initial Package build
