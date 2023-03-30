# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%undefine __cmake_in_source_build
%global uuid    org.%{name}.%{name}

Name:           corectrl
Version:        1.3.4
Release:        %autorelease
Summary:        Friendly hardware control

# The entire source code is GPLv3+ except bundled libs:
# * Boost:          tests/3rdparty/catch
#                   tests/3rdparty/trompeloeil
# * MIT:            3rdparty/units
# * Public Domain:  FindBotan.cmake
License:        GPLv3+ and Boost and MIT and Public Domain
URL:            https://gitlab.com/corectrl/corectrl
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        README.fedora.md

BuildRequires:  cmake >= 3.3
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++ >= 8
BuildRequires:  libappstream-glib
BuildRequires:  libdrm-devel
BuildRequires:  ninja-build

BuildRequires:  cmake(fmt)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(pugixml)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.9
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(easyloggingpp)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(quazip1-qt5)
BuildRequires:  pkgconfig(x11)

Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}
Requires:       qca-qt5-ossl%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}

# Used to gather more information
#   * For glxinfo
Recommends:     mesa-demos%{?_isa}
#   * For lscpu
Recommends:     util-linux%{?_isa}
#   * For vulkaninfo
Recommends:     vulkan-tools%{?_isa}

# https://gitlab.com/corectrl/corectrl/issues/13
Provides:       bundled(units)

%description
CoreCtrl is a Free and Open Source GNU/Linux application that allows you to
control with ease your computer hardware using application profiles. It aims
to be flexible, comfortable and accessible to regular users.

- For setup instructions run:

  $ xdg-open %{_docdir}/%{name}/README.fedora.md

- or go to the project wiki:

  https://gitlab.com/corectrl/corectrl/wikis


%prep
%autosetup -n %{name}-947719d97a37f67315cf38d5dc986c06aa85aa99
# Unbundle 3rdparty
pushd 3rdparty
rm -rf \
    easyloggingpp \
    fmt \
    pugixml \
    %{nil}
popd
# lib soversion fix
echo "set_property(TARGET corectrl_lib PROPERTY SOVERSION 0)" >> src/CMakeLists.txt


%build
%cmake \
    -G Ninja \
    -DBUILD_TESTING=ON \
    %{nil}
%ninja_build -C %{_vpath_builddir}


%install
%ninja_install -C %{_vpath_builddir}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.fedora.md
find README.md -type f -perm /111 -exec chmod 644 {} \;
find %{buildroot}/%{_datadir}/. -type f -executable -exec chmod -x "{}" \;

# Useless symlink without headers
rm %{buildroot}/%{_libdir}/libcorectrl.so


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING LICENSE
%doc README.md README.fedora.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/polkit-1/actions/*.policy
%{_libdir}/libcorectrl.so.0*
%{_libexecdir}/%{name}/%{name}_helper
%{_libexecdir}/%{name}/%{name}_helperkiller
%{_metainfodir}/*.xml


%changelog
%autochangelog
