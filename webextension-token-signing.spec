# original upstream name: chrome-token-signing
# it is a native messaging solution for firefox/chrome signing support
# chrome and firefox dropped legacy npapi support form browsers
# https://developer.chrome.com/apps/nativeMessaging
# and Estonia ID card software now use native messaging to talk with smartcards
# over javascript to create digital signatures.
# Information source user zomps from #esteid Freenode IRC channel
%global upstream_name chrome-token-signing

Name:           webextension-token-signing
Version:        1.1.5
Release:        3%{?dist}
Summary:        Chrome and Firefox extension for signing with your eID on the web
License:        LGPLv2+
URL:            https://github.com/open-eid/chrome-token-signing
Source0:        %{url}/archive/v%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcsclite)
Requires:       opensc%{?_isa}
Requires:       pcsc-lite%{?_isa}
Requires:       pcsc-lite-ccid%{?_isa}
# mozilla-filesystem is required to install files into
# %%_prefix/lib/mozilla and
# %%{_datadir}/mozilla/extensions/
Requires:       mozilla-filesystem

%description
Chrome and Firefox extension for signing with your eID on the web.

%prep
%setup -q -n %{upstream_name}-%{version}

sed -i "s|qmake|%{_qt5_bindir}/qmake \
  QMAKE_CFLAGS_DEBUG=\"%optflags\" \
  QMAKE_CFLAGS_RELEASE=\"%optflags\" \
  LIBPATH=\"%{_libdir}\" \
  QMAKE_CXXFLAGS_DEBUG=\"%optflags\" \
  QMAKE_CXXFLAGS_RELEASE=\"%optflags\" \
  QMAKE_LFLAGS_DEBUG=\"%{?__global_ldflags}\" \
  QMAKE_LFLAGS_RELEASE=\"%{?__global_ldflags}\" \
  QMAKE_STRIP=|" host-linux/GNUmakefile

%build
make %{?_smp_mflags} LIBPATH=%{_libdir}

%install
# make -C host-linux install DESTDIR=%%{buildroot}
make -C host-linux install INSTALL_ROOT=%{buildroot}

# Firefox is the browser installed by default on Fedora
# Chromium is available in the repository
# Chrome extension is supported as an exception
# because it's identicall to Chromium's
mkdir -p $RPM_BUILD_ROOT/usr/share/chromium/extensions
cp $RPM_BUILD_ROOT/opt/google/chrome/extensions/ckjefchnfjhjfedoccjbhjpbncimppeg.json $RPM_BUILD_ROOT/usr/share/chromium/extensions/ckjefchnfjhjfedoccjbhjpbncimppeg.json
mkdir -p $RPM_BUILD_ROOT/usr/share/google-chrome/extensions
mv $RPM_BUILD_ROOT/opt/google/chrome/extensions/ckjefchnfjhjfedoccjbhjpbncimppeg.json $RPM_BUILD_ROOT/usr/share/google-chrome/extensions/ckjefchnfjhjfedoccjbhjpbncimppeg.json
mkdir -p $RPM_BUILD_ROOT/etc/chromium/native-messaging-hosts
cp $RPM_BUILD_ROOT/etc/opt/chrome/native-messaging-hosts/ee.ria.esteid.json $RPM_BUILD_ROOT/etc/chromium/native-messaging-hosts/ee.ria.esteid.json

%files
%{_bindir}/chrome-token-signing
# %%{_datadir} is a macro for /usr/share
%{_datadir}/mozilla/extensions/*
%{_datadir}/chromium/extensions/*
%{_datadir}/google-chrome/extensions/*
# %% dir creates a directory under a specific path
%dir %{_libdir}/mozilla/native-messaging-hosts/
%{_libdir}/mozilla/native-messaging-hosts/ee.ria.esteid.json
%dir %{_sysconfdir}/chromium/native-messaging-hosts/
%{_sysconfdir}/chromium/native-messaging-hosts/ee.ria.esteid.json
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts/
%{_sysconfdir}/opt/chrome/native-messaging-hosts/ee.ria.esteid.json


%doc README.md AUTHORS RELEASE-NOTES.md

%license LICENSE.LGPL

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 27 2021 Dmitri Smirnov <dmitri@smirnov.ee> - 1.1.5-1
- Upstream release 1.1.5

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Mar 8 2021 Dmitri Smirnov <dmitri@smirnov.ee> - 1.1.4-1
- Upstream release 1.1.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Dmitri Smirnov <dmitri@smirnov.ee> - 1.1.2-1
- Upstream release 1.1.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-1
- Upstream release 1.1.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Dmitri Smirnov <dmitri@smirnov.ee> - 1.1.0-1
- Upstream release 1.1.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019  Dmitri Smirnov <dmitri@smirnov.ee> - 1.0.9-1
- 1.0.9 upstream release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 1.0.8-1
- 1.0.8 upstream release

* Tue Dec 04 2018 Pete Walter <pwalter@fedoraproject.org> - 1.0.7-3
- Update summary and description now that Chrome is supported again

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 1.0.7-1
- 1.0.7 upstream release

* Sun Jun 03 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 1.0.6-7
- Added install hint and native messaging host files for Chrome

* Sat May 05 2018 Dmitri Smirnov <dmitri@smirnov.ee> - 1.0.6-6
- Added install hint and native messaging host files for Chromium
- Minor whitespace consistency changes in spec file

* Thu Mar 29 2018 Germano Massullo <germano.massullo@gmail.com> - 1.0.6-5
- removed Requires: esteidcerts

* Wed Mar 21 2018 Germano Massullo <germano.massullo@gmail.com> - 1.0.6-4
- added LIBPATH=\"%%{_libdir}\" in sed command

* Thu Mar 15 2018 Germano Massullo <germano.massullo@gmail.com> - 1.0.6-3
- added libpath patch

* Tue Mar 06 2018 Germano Massullo <germano.massullo@gmail.com> - 1.0.6-2
- improved qmake flags

* Thu Feb 22 2018 Germano Massullo <germano.massullo@gmail.com> - 1.0.6-1
- first release
