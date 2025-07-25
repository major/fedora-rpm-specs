# It is not possible to unbundle libelectronic-id, read
# https://github.com/web-eid/libelectronic-id/issues/120 
# https://bugzilla.redhat.com/show_bug.cgi?id=2325424


%global build_number 654-2004

Name:    web-eid
Version: 2.6.0
Release: 4%{?dist}
Summary: Web eID browser extension helper application
License: MIT
URL:     https://github.com/web-eid/web-eid-app
Source0: %{url}/releases/download/v%{version}/%{name}_%{version}.%{build_number}.tar.xz
# https://github.com/web-eid/web-eid-app/issues/359#issuecomment-2796312287
Patch0: 126.patch
BuildRequires: bash
BuildRequires: desktop-file-utils
BuildRequires: git
BuildRequires: qt6-qtbase-devel >= 6.7.1
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qttools-devel
BuildRequires: pcsc-lite
BuildRequires: pcsc-lite-devel
BuildRequires: clang
BuildRequires: git-clang-format
BuildRequires: valgrind
BuildRequires: gtest
BuildRequires: gtest-devel
BuildRequires: openssl-devel

Requires: hicolor-icon-theme
Requires: mozilla-filesystem
Requires: qt6-qtbase
Requires: qt6-qtsvg

%if %{defined fedora} && 0%{?fedora} <= 40
Obsoletes: webextension-token-signing <= 1.1.5
Provides: webextension-token-signing = %{version}-%{release}
# Provides for firefox-pkcs11-loader is not necessary, see:
# 
# If a package supersedes/replaces an existing package without being a
# sufficiently compatible replacement as defined above, use only the Obsoletes:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/
Obsoletes: firefox-pkcs11-loader <= 3.13.6
%endif
Provides: bundled(libelectronic-id)

%description
The Web eID application performs cryptographic digital signing and
authentication operations with electronic ID smart cards for the Web eID
browser extension (it is the native messaging host for the extension). Also
works standalone without the extension in command-line mode.

%prep
%autosetup -n %{name} -p1


%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

install -m 644 -Dt %{buildroot}/%{_sysconfdir}/chromium/native-messaging-hosts %{buildroot}/%{_datadir}/web-eid/eu.webeid.json
install -m 644 -Dt %{buildroot}/%{_sysconfdir}/opt/chrome/native-messaging-hosts %{buildroot}/%{_datadir}/web-eid/eu.webeid.json

rm -f %{buildroot}/%{_datadir}/web-eid/eu.webeid.json

%check
export QT_QPA_PLATFORM='offscreen' # needed for running headless tests
%ctest

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license LICENSE
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_sysconfdir}/chromium/native-messaging-hosts/
%{_sysconfdir}/opt/chrome/native-messaging-hosts/
%{_libdir}/mozilla/native-messaging-hosts/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/chromium/extensions/ncibgoaomkmdpilpocfeponihegamlic.json
%{_datadir}/google-chrome/extensions/
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun May 11 2025 Germano Massullo <germano.massullo@gmail.com> - 2.6.0-3
- Removed unnecessary %%global _hardened_build 1

* Fri Apr 11 2025 Germano Massullo <germano.massullo@gmail.com> - 2.6.0-2
- Adds 126.patch

* Wed Apr 09 2025 Germano Massullo <germano.massullo@gmail.com> - 2.6.0-1
- 2.6.0 release
- Removed %%define debug_package %%{nil}
- Added -DCMAKE_INSTALL_SYSCONFDIR=%%{_sysconfdir}
- Modified %%files section

* Wed Apr 09 2025 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-7
- Adds Provides: bundled(libelectronic-id)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-5
- add Obsoletes: firefox-pkcs11-loader

* Tue Sep 24 2024 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-4
- add %%{?dist}

* Fri Sep 20 2024 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-3
- remove Requires: libstdc++, openssl-libs, pcsc-lite-libs
- add LICENSE

* Sun Jul 21 2024 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-2
- add Obsoletes and Provides

* Mon Jul 01 2024 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.5.0-1
- update release to 2.5.0

* Thu Sep 21 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.4.0-2
- remove mozilla/extensions from files (arun.neelicattu@gmail.com)

* Thu Sep 21 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.4.0-1
- update to v2.4.0 release (arun.neelicattu@gmail.com)
- Fix another typo (me@treier.xyz)
- readme: add firefox instruction for extension (arun.neelicattu@gmail.com)
- Fix typo in install command (me@treier.xyz)

* Sat Jun 24 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-8
- fix epel builds (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-7
- add desktop-file-utils to build requires (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-6
- fix desktop file validation path (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-5
- move desktop file validation to check (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-4
- fix post install script to use correct desktop file
  (arun.neelicattu@gmail.com)
- use upstream libpcsc-mock patch (arun.neelicattu@gmail.com)
- fix spec file formatting (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-3
- workaround patch file issue for tito (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-2
- fix readme typo (arun.neelicattu@gmail.com)

* Fri Jun 23 2023 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.3.1-1
- new package built with tito

