# Force out of source build
%undefine __cmake_in_source_build

Name:           android-file-transfer
Version:        4.2
Release:        14%{?dist}
Summary:        Reliable Android MTP client with minimalist UI

License:        LGPL-2.1-only
URL:            https://github.com/whoozle/android-file-transfer-linux
Source0:        %{url}/archive/v%{version}/%{name}-linux-%{version}.tar.gz

Patch0001:      0001-Fix-build-with-GCC-13-330.patch

Requires:       hicolor-icon-theme
BuildRequires:  cmake
BuildRequires:  cmake(pybind11)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(taglib)

%description
Android File Transfer for Linux — reliable MTP client with minimalist UI
similar to Android File Transfer for Mac.
Features:
- Simple Qt UI with progress dialogs.
- FUSE wrapper (If you'd prefer mounting your device), supporting partial
  read/writes, allowing instant access to your files.
- No file size limits.
- Automatically renames album cover to make it visible from media player.
- USB 'Zerocopy' support found in recent Linux kernel
- No extra dependencies (e.g. libptp/libmtp).
- Command line tool (aft-mtp-cli)

%prep
%autosetup -p1 -n %{name}-linux-%{version}


%build
# QT requires the main program not to perform local symbol binding,
# -fPIC accomplishes that
export CXXFLAGS="-fPIC $RPM_OPT_FLAGS"
%cmake -GNinja
%cmake_build


%install
%cmake_install
find %{buildroot} -name '*.a' -delete
desktop-file-install                                       \
    --remove-category="System"                             \
    --remove-category="Filesystem"                         \
    --delete-original                                      \
    --dir=%{buildroot}%{_datadir}/applications             \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%license LICENSE
%doc README.md FAQ.md
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 3 2023 Marek Blaha <mblaha@redhat.com> - 4.2-9
- Add missing build dependencies (OpenSSL, taglib, libmagic)

* Tue May 2 2023 Marek Blaha <mblaha@redhat.com> - 4.2-8
- Backport fix to build with GCC 13

* Thu Mar 30 2023 Marek Blaha <mblaha@redhat.com> - 4.2-7
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 5 2020 Marek Blaha <mblaha@redhat.com> - 4.2-1
- New upstream release 4.2

* Wed Dec 16 2020 Marek Blaha <mblaha@redhat.com> - 4.1-1
- New upstream release 4.1

* Mon Nov 30 2020 Marek Blaha <mblaha@redhat.com> - 4.0-1
- New upstream release 4.0

* Fri Oct 2 2020 Jeff Law <law@redhat.com> - 3.9-7
- Add -fPIC to compilation flags

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Marek Blaha <mblaha@redhat.com> - 3.9-2
- Rebuilt with Qt5

* Wed Jun 12 2019 Marek Blaha <mblaha@redhat.com> - 3.9-1
- New upstream release 3.9

* Mon May 20 2019 Marek Blaha <mblaha@redhat.com> - 3.8-1
- New upstream release 3.8

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.7-3
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Marek Blaha <mblaha@redhat.com> - 3.7-1
- New upstream release 3.7

* Thu Nov  8 2018 Marek Blaha <mblaha@redhat.com> - 3.6-1
- New upstream release 3.6

* Tue Jul  3 2018 Marek Blaha <mblaha@redhat.com> - 3.4-1
- Initial rpm release
