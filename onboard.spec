Name:               onboard

Version:            1.4.1
%global             major_version       1.4

Release:            29%{?dist}
Summary:            On-screen keyboard for TabletPC and mobility impaired users (Xorg only)

# The entire source code is GPLv3 apart from translation strings and
# /gnome/Onboard_Indicator@onboard.org/convenience.js which are both BSD-3-clause
License:            GPLv3 and BSD
URL:                https://launchpad.net/onboard/
Source0:            %{url}%{major_version}/%{version}/+download/onboard-%{version}.tar.gz

# Wrong Python interpreter in Onboard/IconPalette.py
# Reported (2017-03-10, fixed in the upstream): https://bugs.launchpad.net/onboard/+bug/1671930
Patch0:             onboard-1.4.1-pythonversion.patch

# remove an unsupported module
# see: https://bugzilla.redhat.com/show_bug.cgi?id=1905661
Patch1:             0001-remove-tweener.patch

BuildRequires:      gcc-c++
BuildRequires:      python3-devel
BuildRequires:      python3-distutils-extra
BuildRequires:      dconf-devel
BuildRequires:      libcanberra-devel
BuildRequires:      libxkbfile-devel
BuildRequires:      libXtst-devel
BuildRequires:      libX11-devel
BuildRequires:      hunspell-devel
BuildRequires:      python3-devel
BuildRequires:      intltool
BuildRequires:      python3-dbus
BuildRequires:      systemd-devel
BuildRequires:      desktop-file-utils

Requires:           iso-codes
Requires:           dbus-x11
Requires:           python3-gobject
Requires:           onboard-data

%description
Onboard is an onscreen keyboard useful for everybody that cannot use a
hardware keyboard; for example TabletPC users, mobility impaired users...

It has been designed with simplicity in mind and can be used right away
without the need of any configuration, as it can read the keyboard layout
from the X server.

%prep
%autosetup -p1

%build
%py3_build

%check
# No tests defined in the upstream

%install
%py3_install

# Remove icons for Ubuntu
rm %{buildroot}%{_datadir}/icons/ubuntu* -rf

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{_builddir}/%{name}-%{version}/build/share/applications/onboard.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{_builddir}/%{name}-%{version}/build/share/applications/onboard-settings.desktop

# Fix permissions for a couple of scripts so the user may execute them (not normal behaviour, but still)
chmod +x %{buildroot}%{python3_sitearch}/Onboard/IconPalette.py %{buildroot}%{python3_sitearch}/Onboard/settings.py \
         %{buildroot}%{python3_sitearch}/Onboard/pypredict/lm_wrapper.py %{buildroot}%{_datadir}/%{name}/layoutstrings.py

%package data
Summary:        Data for Onboard
BuildArch:      noarch
Requires:       onboard

%description data
%{summary}.

%files
%{_bindir}/%{name}*
%{_datadir}/man/man1/onboard*
%{_datadir}/applications/%{name}*.desktop
%{python3_sitearch}/Onboard/
%{python3_sitearch}/onboard*.egg-info
%{_datadir}/glib-2.0/schemas/org.onboard.gschema.xml

%files data
%doc AUTHORS NEWS README HACKING
%license COPYING COPYING.BSD3 COPYING.GPL3
%defattr(-,root,root,-)
%{_datadir}/%{name}/
%{_datadir}/sounds/freedesktop/stereo/onboard-key-feedback.oga
%{_datadir}/icons/HighContrast/scalable/apps/onboard.svg
%{_datadir}/icons/hicolor/*/apps/onboard.*
%{_datadir}/dbus-1/services/org.onboard.Onboard.service
%{_datadir}/gnome-shell/extensions/Onboard_Indicator@onboard.org

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.1-27
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.1-24
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 22:25:55 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.4.1-22
- Remove an unused gnome module(#1905661)

* Wed Nov 25 12:16:04 CST 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 1.4.1-21
- drop %%_python_bytecompile_extra and rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-18
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-15
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.4.1-14
- Remove obsolete requirements for %%post/%%postun scriptlets

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> - 1.4.1-12
- rebuild for hunspell-1.7.0

* Mon Oct 22 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-11
- Add compiler to BR

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-10
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Mar 15 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.4.1-4
- Fixed spec file in regard to #1431322 comment 7 (1431322#c7)

* Wed Mar 15 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.4.1-3
- Fixed spec file in regard to #1431322 comment 5 (1431322#c5)

* Wed Mar 15 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.4.1-2
- Fixed spec file in regard to #1431322

* Fri Mar 10 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.4.1-1
- Adopted package
- Cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Fabian Affolter <fabian@bernewireless.net> - 0.94.0-1
- Fixed #657147
- Updated to new upstream version 0.94.0

* Sun Aug 01 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.93.0-3
- Fix the build and the scriptlets

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.93.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu May 27 2010 Fabian Affolter <fabian@bernewireless.net> - 0.93.0-1
- Updated docs
- Updated to new upstream version 0.93.0

* Fri Dec 18 2009 Fabian Affolter <fabian@bernewireless.net> - 0.92.0-1
- Desktop file and icon removed
- Translations added
- MIME update added
- Updated to new upstream version 0.92.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Fabian Affolter <fabian@bernewireless.net> 0.91.2-3
- Clean-up
- gnome-python2 removed
- Fixed issues from Comment #2 in #472027

* Mon Dec 08 2008 Parag Nemade <panemade@gmail.com> 0.91.2-2
- spec cleanup

* Mon Nov 17 2008 Fabian Affolter <fabian@bernewireless.net> 0.91.2-1
- Initial package for Fedora
