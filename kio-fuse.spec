%global         min_qt_version 5.12
%global         min_kf_version 5.66

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:           kio-fuse
Version:        5.0.1
Release:        6%{?dist}
Summary:        KIO FUSE

License:        GPLv3+
URL:            https://invent.kde.org/system/kio-fuse
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

## upstream fixes

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules  >= %{min_kf_version}

BuildRequires:  pkgconfig(fuse3)

BuildRequires:  cmake(Qt5Core)       >= %{min_qt_version}
BuildRequires:  cmake(Qt5Test)       >= %{min_qt_version}

BuildRequires:  cmake(KF5KIO)        >= %{min_kf_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{min_kf_version}

%if 0%{?tests}
BuildRequires:  dbus-x11
BuildRequires:  kio-extras
BuildRequires:  make
%endif

Requires:       systemd
Requires:       dbus-common

%description
KioFuse works by acting as a bridge between KDE's KIO filesystem design and
FUSE.


%prep
%autosetup -p1 -n %{name}-v%{version}


%build
%cmake_kf5 -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build


%install
%cmake_install


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
dbus-launch --exit-with-session \
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%files
%license LICENSES/GPL-3.0-or-later.txt
%doc README
%{_libexecdir}/kio-fuse
%{_userunitdir}/kio-fuse.service
%{_kf5_datadir}/dbus-1/services/org.kde.KIOFuse.service
%{_tmpfilesdir}/%{name}-tmpfiles.conf


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.0.1-1
- version 5.0.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-4
- pull in upstream crash fix
- move BR: make inside '%%if %%{tests}' (only explicitly used there)

* Sat Jan  9 16:34:01 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.0.0-3
- ignore exit status of `make test`

* Sat Jan  9 16:15:31 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.0.0-2
- cleaned up build dependicies & tests enabled

* Fri Jan  1 15:55:51 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.0.0-1
- version 5.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.95.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 4.95.0-1
- first spec for version 4.95.0

