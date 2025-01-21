%global snapdate 20161006

Name:           ufw-kde
Version:        0.5.0
Release:        0.27.%{snapdate}git%{?dist}
Summary:        UFW control module for KDE

# Some files GPLv3 only, some files GPLv2+
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://projects.kde.org/projects/playground/sysadmin/ufw-kde
Source0:        ufw-kde-%{version}-%{snapdate}.tar.xz
# releaseme (kdelibs4 branch) scripts used to generate the above source tarball:
Source1:        ufw-kde.rb
Source2:        ufw-kderc
# standalone .desktop file to invoke UFW-KDE outside of systemsettings 4
Source3:        ufw-kde.desktop

# do not use #!/usr/bin/env for the Python helper
Patch0:         ufw-kde-0.5.0-no-env.patch
# rename strings.* to i18nstrings.* to work around strings.h name conflict
# (#1556517, #1606605)
Patch1:         ufw-kde-0.5.0-rename-strings-h.patch

BuildRequires: make
BuildRequires:  cmake
BuildRequires:  kdelibs4-devel
BuildRequires:  gettext
BuildRequires:  python3-devel
# bytecompile with Python 3
%global __python %{__python3}
# for desktop-file-install
BuildRequires:  desktop-file-utils

Requires:       ufw
Requires:       python3
# for kcmshell4, used in the standalone .desktop file
Requires:       kde-runtime

%description
KDE KControl Module to configure and control the Uncomplicated Firewall (UFW).

%prep
%setup -q
%patch -P0 -p1 -b .no-env
%patch -P1 -p1 -b .rename-strings-h

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}

%py_byte_compile %{__python3} %{buildroot}%{_libexecdir}/kde4/
%find_lang %{name} --all-name --with-kde

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_kde4_sysconfdir}/dbus-1/system.d/org.kde.ufw.conf
%{_kde4_libdir}/kde4/kcm_ufw.so
%{_kde4_libexecdir}/kcm_ufw_helper
%{_kde4_libexecdir}/kcm_ufw_helper.py
%{_kde4_libexecdir}/__pycache__/
%{_kde4_datadir}/dbus-1/services/org.kde.ufw.service
%{_kde4_datadir}/dbus-1/system-services/org.kde.ufw.service
%{_kde4_datadir}/kde4/services/ufw.desktop
%{_kde4_datadir}/polkit-1/actions/org.kde.ufw.policy
%{_kde4_appsdir}/kcm_ufw/
%{_datadir}/applications/ufw-kde.desktop

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.27.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-0.26.20161006git
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.25.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.24.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.23.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.22.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.21.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.20.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.19.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.18.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 0.5.0-0.17.git
- Fixed FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.16.20161006git
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.15.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.14.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.13.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.12.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-0.11.20161006git
- rename strings.* to work around strings.h name conflict (#1556517, #1606605)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.10.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-0.9.20161006git
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.8.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.7.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.6.20161006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-0.5.20161006git
- Bump Release for official build

* Sun Feb 05 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-0.4.20161006git
- Do not use #!/usr/bin/env for the Python helper

* Thu Oct 06 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-0.3.20161006git
- New snapshot with (only) some translation updates

* Mon Aug 17 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-0.2.20150817git
- New snapshot with (only) some translation updates
- Add standalone .desktop file to invoke UFW-KDE outside of systemsettings 4
- Change COPYING from %%doc to %%license

* Mon Jan 12 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.5.0-0.1.20150112git
- Initial package
