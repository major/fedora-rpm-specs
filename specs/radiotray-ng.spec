Name:           radiotray-ng
Version:        0.2.9
Release:        2%{?dist}
Summary:        Internet radio player

License:        GPL-3.0-or-later
URL:            https://github.com/ebruck/radiotray-ng
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  boost-devel
BuildRequires:  wxGTK-devel
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup
# Correct build flags
sed -i 's|-Wall -Wextra -Werror -Wpedantic|%{optflags}|' CMakeLists.txt
sed -i '/execute_process(COMMAND lsb_release/d' package/CMakeLists.txt
# Fix build with GCC 13
# https://github.com/ebruck/radiotray-ng/pull/193
sed -i "s|#include <string>|#include <string>\n#include <cstdint>|" include/radiotray-ng/i_config.hpp

%build
%cmake3 \
    -DLSB_RELEASE_EXECUTABLE="lsb_release" \
    -DDISTRIBUTOR_ID="fedora"
%cmake_build


%install
%cmake_install
# Remove autostart
rm %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
# Remove themes
rm -rf %{buildroot}%{_datadir}/icons/Yaru
rm -rf %{buildroot}%{_datadir}/icons/breeze
# Remove self-installed license file
rm %{buildroot}%{_datadir}/licences/%{name}/COPYING
#Remove unneeded script
rm %{buildroot}%{_bindir}/rt2rtng

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/rtng-bookmark-editor.desktop


%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_bindir}/rtng-bookmark-editor
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/rtng-bookmark-editor.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Vasiliy Glazov <vascom2@gmail.com> 0.2.9-1
- Update to 0.2.9

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.2.8-11
- Rebuilt for Boost 1.83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.2.8-9
- Rebuilt for Boost 1.81

* Tue Jan 24 2023 Vasiliy Glazov <vascom2@gmail.com> 0.2.8-8
- Fix build with GCC 13

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 0.2.8-6
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.2.8-4
- Rebuilt for Boost 1.78

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 0.2.8-2
- Rebuild (jsoncpp)

* Sun Aug 22 2021 Vasiliy Glazov <vascom2@gmail.com> 0.2.8-1
- Update to 0.2.8.

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.7-11
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.2.7-8
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Björn Esser <besser82@fedoraproject.org> - 0.2.7-6
- Rebuilt again for Boost 1.73

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.2.7-5
- Rebuild (jsoncpp)

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.2.7-4
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.2.7-2
- Rebuild (jsoncpp)

* Mon Oct 21 2019 Vasiliy Glazov <vascom2@gmail.com> 0.2.7-1
- Update to 0.2.7.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Vasiliy Glazov <vascom2@gmail.com> 0.2.6-2
- Use pkgconfig for BR
- Update source url

* Fri Jul 05 2019 Vasiliy Glazov <vascom2@gmail.com> 0.2.6-1
- Initial release
