%global date 20231031
%global commit 8fa12dd2d81c4b5d2a713e169cac70898512322e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           widevine-installer
Version:        0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Widevine CDM installer for aarch64 systems

License:        MIT
URL:            https://github.com/AsahiLinux/widevine-installer
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
# Use /var/lib instead of /opt
Patch:          %{url}/pull/2.patch
# Use environment.d instead of the bash profile
Patch:          %{url}/pull/5.patch

BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  systemd-rpm-macros
BuildRequires:  sed

Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       glibc >= 2.36
Requires:       python3
Requires:       setup
Requires:       squashfs-tools
Requires:       systemd

Enhances:       chromium
Enhances:       firefox
Enhances:       qt5-webengine
Enhances:       qt6-webengine

ExclusiveArch:  aarch64

%description
This tool will download and install Widevine systemwide for aarch64 systems. It
performs the necessary configuration changes to make Widevine available for
both Firefox and Chromium-based browsers.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Configs are already installed by the package
sed -i 's/COPY_CONFIGS=1/COPY_CONFIGS=0/' widevine-installer

%build
# Nothing to build

%install
DESTDIR="%{buildroot}" ./widevine-installer --distinstall

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%dir %{_libdir}/chromium-browser
%{_libdir}/chromium-browser/WidevineCdm
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/defaults
%dir %{_libdir}/firefox/defaults/pref
%{_libdir}/firefox/defaults/pref/gmpwidevine.js
%{_environmentdir}/50-gmpwidevine.conf
%dir %{_sharedstatedir}/widevine
%dir %ghost %{_sharedstatedir}/widevine/gmp-widevinecdm
%dir %ghost %{_sharedstatedir}/widevine/gmp-widevinecdm/system-installed
%ghost %{_sharedstatedir}/widevine/gmp-widevinecdm/system-installed/libwidevinecdm.so
%ghost %{_sharedstatedir}/widevine/gmp-widevinecdm/system-installed/manifest.json
%ghost %{_sharedstatedir}/widevine/libwidevinecdm.so
%ghost %{_sharedstatedir}/widevine/LICENSE
%ghost %{_sharedstatedir}/widevine/manifest.json
%{_sharedstatedir}/widevine/README
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm
%ghost %{_sharedstatedir}/widevine/WidevineCdm/manifest.json
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_arm64
%ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_arm64/libwidevinecdm.so
%dir %ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_x64
%ghost %{_sharedstatedir}/widevine/WidevineCdm/_platform_specific/linux_x64/libwidevinecdm.so

%changelog
%autochangelog
