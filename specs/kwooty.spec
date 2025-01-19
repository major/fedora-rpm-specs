Name:    kwooty
Summary: A friendly nzb usenet binary download application
Version: 1.1.0
Release: 29%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://kwooty.sourceforge.net/
Source0: http://sourceforge.net/projects/kwooty/files/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: kde-workspace-devel
BuildRequires: kdelibs4-devel
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kde-runtime%{?_kde4_version: >= %{_kde4_version}}
Requires: par2cmdline

# multilib upgrade path, when -libs subpkg was introduced
Obsoletes: kwooty < 1.1.0-4

%description
Kwooty is a NZB usenet binary download application for KDE 4.
It's main features are:
- Automatic file verification/repairing
- Automatic archive extraction (Rar, Zip and 7z archive formats supported)
- Multi-server support
- Built-in YEnc and UUEncode file decoders
- Watch Folder
- File queue and priority management
- System shutdown scheduler.
- Save/Restore pending downloads when application is closed/open.
- Built-in SSL connection support
- Pause/Resume downloads
- Suspends downloads if disk is full
- Display of Remaining Time or Estimated Time of Arrival (ETA)
- Display of available free disk space
- Automatic connection to host at start-up
- Automatic file downloading after opening Nzb file

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/kwooty.desktop

%find_lang kwooty --with-kde

## unpackaged files
# remove lib symlink
rm -f %{buildroot}%{_kde4_libdir}/libkwootycore.so


%files -f kwooty.lang
%doc README.txt TODO
%license COPYING
%{_kde4_bindir}/kwooty
%{_kde4_libdir}/kde4/kwooty_*
%{_kde4_datadir}/applications/kde4/kwooty.desktop
%{_kde4_datadir}/config.kcfg/kwooty_*.kcfg
%{_kde4_datadir}/config.kcfg/kwootysettings.kcfg
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_appsdir}/kwooty/
%{_kde4_datadir}/kde4/services/kwooty*
%{_kde4_datadir}/kde4/servicetypes/kwootyplugin.desktop

%ldconfig_scriptlets libs

%files libs
%{_kde4_libdir}/libkwootycore.so.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-16
- use %%make_build %%license

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-11
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Nov 07 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-4
- cleanup, -libs subpkg

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 17 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Tue Feb 26 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.0.0-1
- 1.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 0.9.1-1
- upgrade to 0.9.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 0.8.4-1
- Version bump.

* Thu Mar 29 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 0.8.3-2
- drop devel package, remove unrar dep, fix files section
- update to offical 0.8.3

* Tue Mar 27 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 0.8.3-1
- update to 0.8.3

* Sun Mar 25 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 0.8.2-1
- Initial packaging
