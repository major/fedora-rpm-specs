%if ! 0%{?rhel} || 0%{?rhel} > 8
%bcond scons_quirk 0
%else
%bcond scons_quirk 1
%endif

%if %{without scons_quirk}
%global scons scons
%else
%global scons scons-3
%endif

Summary:        Free firewire audio driver library
Name:           libffado
Version:        2.4.8
Release:        %autorelease
License:        GPLv2 or GPLv3
URL:            http://www.ffado.org/
Source0:        http://www.ffado.org/files/%{name}-%{version}.tgz
# The trunk is tarballed as follows:
# bash libffado-snapshot.sh 2088
# The fetch script
Source9:        libffado-snapshot.sh
Patch0:         libffado-2.4.4-no-test-apps.patch
Patch1:         libffado-2.4.4-icon-name.patch
Patch2:         libffado-2.4.4-scons-quirk.patch
# Patch for Python 3.12 imp module removal
Patch3:         libffado-2.4.7-python312-imp-removal.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  dbus-c++-devel
BuildRequires:  dbus-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  graphviz
BuildRequires:  libappstream-glib
BuildRequires:  libconfig-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libxml++-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-devel
%if %{without scons_quirk}
BuildRequires:  python3-scons >= 3.0.2
%else
BuildRequires:  python3-scons
%endif
BuildRequires:  python3dist(setuptools)
BuildRequires:  rpm_macro(py3_shebang_fix)
ExcludeArch:    s390 s390x


%description
The FFADO project aims to provide a generic, open-source solution for the
support of FireWire based audio devices for the Linux platform. It is the
successor of the FreeBoB project.

%package devel
Summary:        Free firewire audio driver library development headers
License:        GPLv2 or GPLv3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files needed to build applications against libffado.

%package -n ffado
Summary:        Free firewire audio driver library applications and utilities
# support/tools/* is GPLv3
# Some files in support/mixer-qt4/ffado are GPLv3+
# The rest is GPLv2 or GPLv3
License:        GPLv3 and GPLv3+ and (GPLv2 or GPLv3)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dbus
Requires:       python3-dbus
Requires:       python3-qt5

%description -n ffado
Applications and utilities for use with libffado.


%prep
%autosetup -N -n %{name}-%{version}/libffado
%patch -P0 -p1 -b .no-test-apps
%patch -P1 -p1 -b .icon-name
%if %{with scons_quirk}
%patch -P2 -p1 -b .scons-quirk
%endif
%patch -P3 -p1 -b .py312-imp-removal

# Fix Python shebangs
%py3_shebang_fix \
    admin/*.py doc/SConscript tests/python/*.py tests/*.py \
    support/mixer-qt4/ffado-mixer* support/mixer-qt4/SConscript \
    support/tools/*.py support/tools/SConscript

%build
export CFLAGS="%{optflags} -ffast-math"
export CXXFLAGS="%{optflags} -ffast-math --std=gnu++11"
export LDFLAGS="%{build_ldflags}"
%{scons} %{?_smp_mflags} \
      DETECT_USERSPACE_ENV=False \
      ENABLE_SETBUFFERSIZE_API_VER=True \
      ENABLE_OPTIMIZATIONS=True \
      CUSTOM_ENV=True \
      BUILD_DOC=user \
      PREFIX=%{_prefix} \
      LIBDIR=%{_libdir} \
      MANDIR=%{_mandir} \
      UDEVDIR=%{_prefix}/lib/udev/rules.d/ \
      PYPKGDIR=%{python3_sitelib}/ffado/ \
      PYTHON_INTERPRETER=/usr/bin/python3 \
      BUILD_TESTS=1

%install
# Exporting flags so that the install does not trigger another build
export CFLAGS="%{optflags} -ffast-math"
export CXXFLAGS="%{optflags} -ffast-math --std=gnu++11"
export LDFLAGS="%{build_ldflags}"
%{scons} DESTDIR=%{buildroot} PREFIX=%{_prefix}\
      install

# We need to install the xdg stuff manually
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     --add-category="Settings" \
                     --set-icon=ffado \
                     support/xdg/ffado.org-ffadomixer.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
ln -s ../../../../libffado/icons/hi64-apps-ffado.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/ffado.png

# Install ffado-test RHBZ#805940
install -m 755 tests/ffado-test %{buildroot}%{_bindir}

%ldconfig_scriptlets

%check
desktop-file-validate \
      %{buildroot}%{_datadir}/applications/ffado.org-ffadomixer.desktop
appstream-util validate-relax --nonet \
      %{buildroot}%{_datadir}/metainfo/ffado-mixer.appdata.xml

%files
%license LICENSE.*
%doc AUTHORS ChangeLog README
%{_libdir}/libffado.so.*
%dir %{_datadir}/libffado/
%{_datadir}/libffado/configuration
%{_prefix}/lib/udev/rules.d/*
%{_libdir}/libffado/static_info.txt

%files devel
%doc doc/reference/html/
%{_includedir}/libffado/
%{_libdir}/pkgconfig/libffado.pc
%{_libdir}/libffado.so

%files -n ffado
%{_mandir}/man1/ffado-*.1*
%{_bindir}/*
%{_datadir}/libffado/*.xml
%{_datadir}/libffado/icons/
%{_datadir}/dbus-1/services/org.ffado.Control.service
%{_datadir}/applications/ffado.org-ffadomixer.desktop
%{_datadir}/icons/hicolor/64x64/apps/ffado.png
%{_datadir}/metainfo/ffado-mixer.appdata.xml
%{python3_sitelib}/ffado/


%changelog
%autochangelog
