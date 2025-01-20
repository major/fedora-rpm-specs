# Force out of source build
%undefine __cmake_in_source_build

Name:           rclone-browser
Version:        1.8.0
Release:        13%{?dist}
Summary:        Simple cross platform GUI for rclone

License:        Unlicense
URL:            https://github.com/kapitainsky/RcloneBrowser
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       rclone

%description
Simple cross platfrom GUI for rclone command line tool.

Features:
 - Allows to browse and modify any rclone remote, including encrypted ones
 - Uses same configuration file as rclone, no extra configuration required
 - Supports custom location and encryption for .rclone.conf configuration file
 - Simultaneously navigate multiple repositories in separate tabs
 - Lists files hierarchically with file name, size and modify date
 - All rclone commands are executed asynchronously, no freezing GUI
 - File hierarchy is lazily cached in memory, for faster traversal of folders
 - Allows to upload, download, create new folders, rename or delete files and
   folders
 - Allows to calculate size of folder, export list of files and copy rclone
   command to clipboard
 - Can process multiple upload or download jobs in background
 - Drag & drop support for dragging files from local file explorer for
   uploading
 - Streaming media files for playback in player like mpv or similar
 - Mount and unmount folders on macOS and GNU/Linux
 - Optionally minimizes to tray, with notifications when upload/download
   finishes
 - Supports portable mode (create .ini file next to executable with same 
   name), rclone and .rclone.conf path now can be relative to executable


%prep
%autosetup -n RcloneBrowser-%{version}
# Do not report warnings as errors
sed -i "s|-Werror ||" src/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
install -Dpm 0644 assets/rclone-browser.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 23:35:18 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 15:15:07 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.0-2
- Fix URL

* Fri Dec 06 15:59:51 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.0-1
- Release 1.7.0 based on official kapitainsky fork

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2-1
- Initial package
