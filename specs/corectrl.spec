# TODO: Package trompeloeil
# https://github.com/rollbear/trompeloeil
%bcond_with tests

%global forgeurl https://gitlab.com/%{name}/%{name}
%global tag v%{version}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%undefine __cmake_in_source_build
%global uuid    org.%{name}.%{name}

Name:           corectrl
Version:        1.5.1
%forgemeta
Release:        %autorelease
Summary:        Friendly hardware control

# The entire source code is GPLv3+ except bundled libs:
# * Boost:          tests/3rdparty/catch
#                   tests/3rdparty/trompeloeil
# * MIT:            3rdparty/units
# * Public Domain:  FindBotan.cmake
# Automatically converted from old format: GPLv3+ and Boost and MIT and Public Domain - review is highly recommended.
License:        GPL-3.0-or-later AND BSL-1.0 AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        README.fedora.md

BuildRequires:  cmake >= 3.22
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++ >= 13.1
BuildRequires:  libappstream-glib
BuildRequires:  libdrm-devel
BuildRequires:  ninja-build
BuildRequires:  cmake(Catch2)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(pugixml) >= 1.11
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.8
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(QuaZip-Qt6)
BuildRequires:  cmake(spdlog) >= 1.4
BuildRequires:  pkgconfig(botan-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(x11)
%if %{with tests}
BuildRequires:  cmake(trompeloeil) >= 40
%endif

Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}

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
%forgeautosetup -p1
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
    %if %{with tests}
    -DBUILD_TESTING=ON \
    %else
    -DBUILD_TESTING=OFF \
    %endif
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
