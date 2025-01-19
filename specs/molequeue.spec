%global __cmake_in_source_build 1

# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

Name:    molequeue
Summary: Desktop integration of high performance computing resources
Version: 0.9.0
Release: 24%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/OpenChemistry/molequeue
Source0: https://github.com/OpenChemistry/molequeue/archive/%{version}/%{name}-%{version}.tar.gz

## Main building
BuildRequires: make
BuildRequires: cmake3
BuildRequires: qt5-qtbase-devel, qt5-rpm-macros
BuildRequires: qt5-qtwebkit-devel
%if 0%{?fedora}
BuildRequires: qjson-qt5-devel
%endif
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtxmlpatterns-devel
BuildRequires: desktop-file-utils
BuildRequires: %{?dts}gcc, %{?dts}gcc-c++, doxygen
BuildRequires: python%{python3_pkgversion}-devel
%if 0%{?rhel}
BuildRequires: epel-rpm-macros
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
MoleQueue is an open-source, cross-platform, system-tray resident desktop
application for abstracting, managing, and coordinating the execution of tasks
both locally and on remote computational resources. Users can set up local and
remote queues that describe where the task will be executed. Each queue can
have programs, with templates to facilitate the execution of the program. Input
files can be staged, and output files collected using a standard interface.
Some highlights:

* Open source distributed under the liberal 3-clause BSD license
* Cross platform with nightly builds on Linux, Mac OS X and Windows
* Intuitive interface designed to be useful to whole community
* Support for local executation and remote schedulers (SGE, PBS, SLURM)
* System tray resident application managing queue of queues and job lifetime
* Simple, lightweight JSON-RPC 2.0 based communication over local sockets
* Qt 5 client library for simple integration in Qt applications

%package libs
Summary: Shared and private libraries of %{name}

%description libs
Shared and private libraries of %{name}.

%package  devel
Summary:  Development files of %{name}
Requires: qt5-qtbase-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: HTML documentation of %{name}
BuildArch: noarch
%description doc
HTML documentation of %{name}.

%prep
%autosetup -n %{name}-%{version}

%if 0%{?fedora}
rm -rf thirdparty/qt5json
%endif

%build
mkdir build && cd build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
%cmake3 -Wno-dev \
 -DENABLE_RPATH:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DENABLE_TESTING:BOOL=OFF \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DCMAKE_BUILD_TYPE:STRING=Release ..
%make_build

pushd docs
doxygen
popd

%install
%make_install -C build

rm -rf %{buildroot}%{_datadir}/doc

cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=MoleQueue
Comment=Manage HPC jobs from the system tray
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
EOF

install -Dpm0644 molequeue/app/icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
desktop-file-install %{name}.desktop --dir %{buildroot}%{_datadir}/applications

%ldconfig_scriptlets libs

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files libs
%doc README.md
%license LICENSE
%{_libdir}/*.so
%{_libdir}/%{name}/

%files devel
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/

%files doc
%doc README.md build/docs/html
%license LICENSE

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.0-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.9.0-11
- New rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Antonio Trande <sagitter@fedoraproject.org> - 0.9.0-9
- Fix CMake request

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.0-6
- Switch to python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.0-4
- Use %%ldconfig_scriptlets

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.0-2
- Set scriplets for rhel <= 7

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.0-1
- Update to version 0.9.0
- Run icon-cache scriptlets on rhel only
- Remove patch for GCC-7
- Rebuild for GCC-8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6.20161222giteb397e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5.20161222giteb397e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.8.0-4.20161222giteb397e
- Unbundle qjson-qt5 on fedora only

* Thu Jun 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.8.0-3.20161222giteb397e
- Modified for epel builds

* Fri Mar 17 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.8.0-2.20161222giteb397e
- Add a .desktop file

* Sat Mar 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 0.8.0-1.20161222giteb397e
- First package
