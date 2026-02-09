# libbase is a utility library from the same upstream that is only used by this
# project and is statically linked into the build
%global libbase_commit aa0da7a355b04b1dd8572a94261a0b0c497e1a85
%global libbase_url https://github.com/phkaeser/libbase

%bcond docs 1

# wlmclock fails to link against libbase when using gcc
%global toolchain clang

Name:           wlmaker
Version:        0.7
Release:        %autorelease
Summary:        Wayland compositor inspired by Window Maker

License:        Apache-2.0
URL:            https://github.com/phkaeser/wlmaker
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{libbase_url}/archive/%{libbase_commit}/libbase-%{libbase_commit}.tar.gz

# Corrects path to configs https://github.com/phkaeser/wlmaker/pull/429
Patch0:         0001-fix-config-path.patch
# Drops google-chrome from default dock placement, and application menu, adds Firefox
Patch1:         0002-remove-google-chrome.patch

# i686: https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  bison
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  hicolor-icon-theme
BuildRequires:  sed
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  plantuml
%endif

# For libbase
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(cairo) >= 1.16.0

# For wlmaker
BuildRequires:  pkgconfig(wayland-client) >= 1.22.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.31
BuildRequires:  pkgconfig(wayland-server) >= 1.22.0
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xcb) >= 1.15
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(xkbcommon) >= 1.5.0
BuildRequires:  pkgconfig(xwayland) >= 22.1.9

Requires:       hicolor-icon-theme

# These are hardcoded in the stock config
Recommends:     firefox
Recommends:     foot
Recommends:     wdisplays

%if %{with docs}
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description
Wayland Maker is a Wayland compositor inspired by Window Maker.

Key features:
- Compositor for windows in stacking mode.
- Supports multiple workspaces.
- Appearance inspired by Window Maker, following the look and feel of NeXTSTEP.
- Easy to use, lightweight, low gimmicks and fast.
- Dock and clip, to be extended for dockable apps.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
This package provides additional developer documentation for %{name}.

%prep
%autosetup -p1 -b 1

# Drop bundled dependencies
rm -r dependencies

# Ensure libbase can be found; we move instead of symlinking because the build
# uses relative paths for the includes and that confuses things
rm -r submodules/libbase
mv ../libbase-%{libbase_commit}/ submodules/libbase

# Do not abort on warnings
sed -i 's/-Werror//' CMakeLists.txt submodules/libbase/CMakeLists.txt

%conf
%cmake -Dconfig_OPTIM=ON

%build
%cmake_build
%if %{with docs}
%cmake_build --target doc
%endif

%install
%cmake_install

%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/{%{name},%{name}.wlmclock,%{name}.wlmeyes}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/wlmclock
%{_bindir}/wlmeyes
%{_sysconfdir}/xdg/%{name}/
%{_datadir}/applications/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/wayland-sessions/
%{_datadir}/%{name}/icons/

%if %{with docs}
%files doc
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md doc/ROADMAP.md %{_vpath_builddir}/doc/html/
%endif

%changelog
%autochangelog
