%bcond x11 %[!(0%{?rhel} >= 10)]

%global forgeurl https://github.com/qtile/qtile
%global tag v0.36.0

Name: qtile
Version: 0.36.0
Release: %{autorelease}
Summary: A pure-Python tiling window manager
%forgemeta
Source: %{forgesource}
License: MIT
Url: http://qtile.org

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pipewire-pulseaudio

# Test dependencies
BuildRequires:  gcc
BuildRequires:  xcb-util-cursor
%if %{with x11}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-server-Xephyr
%endif
BuildRequires:  xterm
BuildRequires:  rsvg-pixbuf-loader
BuildRequires:  pkgconfig(wlroots-0.19)

# Recommended packages for widgets
Recommends: python3-psutil
Recommends: python3-pyxdg
Recommends: python3-dbus-fast
Recommends: python3-xmltodict
Recommends: python3-dateutil
Recommends: python3-mpd2
Recommends: python3-pulsectl
Recommends: python3-pulsectl-asyncio

Requires: python3-libqtile = %{version}-%{release}
# CFFI loaded runtime deps in libqtile/__init__.py
Requires: glib2%{?_isa}
Requires: pango%{?_isa}
Requires: xcb-util-cursor%{?_isa}
Requires: fontconfig%{?_isa}


%description
A pure-Python tiling window manager.

Features
========

    * Simple, small and extensible. It's easy to write your own layouts,
      widgets and commands.
    * Configured in Python.
    * Command shell that allows all aspects of
      Qtile to be managed and inspected.
    * Complete remote scriptability - write scripts to set up workspaces,
      manipulate windows, update status bar widgets and more.
    * Qtile's remote scriptability makes it one of the most thoroughly
      unit-tested window mangers around.


%package -n python3-libqtile
Summary: Qtile's python library


%description -n python3-libqtile
%{summary}.


%package wayland
Summary: Qtile wayland session
Requires: qtile = %{version}-%{release}
Requires: xorg-x11-server-Xwayland
BuildRequires: xorg-x11-server-Xwayland
BuildRequires: cairo-devel
BuildRequires: gobject-introspection-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel


%description wayland
%{summary}.


%prep
%forgesetup
# No coverage tests in downstream builds
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency pytest-cov:ignore
# These are not packaged for Fedora yet
%pyproject_patch_dependency check-manifest:ignore
%pyproject_patch_dependency mailbox:ignore
%pyproject_patch_dependency imaplib2:ignore


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x dev,optional-core,widgets


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
PYTHONPATH=${PWD} %{python3} ./libqtile/backend/wayland/cffi/build.py


%install
%pyproject_install
%pyproject_save_files libqtile

mkdir -p %{buildroot}%{python3_sitearch}/libqtile/backend/wayland/
cp -a ./libqtile/backend/wayland/_ffi.*.so %{buildroot}%{python3_sitearch}/libqtile/backend/wayland/

%if %{with x11}
mkdir -p %{buildroot}%{_datadir}/xsessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/xsessions/ \
    resources/qtile.desktop
%endif

mkdir -p %{buildroot}%{_datadir}/wayland-sessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/wayland-sessions/ \
    resources/qtile-wayland.desktop


%check
%pyproject_check_import -e '*.iqshell_*' -e '*.khal_calendar' -e '*.wlan'
# Tests can sometimes randomly fail. Rebuilding the package again usually solves
# the issue. See https://github.com/qtile/qtile/issues/4573

# Avoid `OSError: [Errno 24] Too Many Open Files` error
ulimit -n 10240 ||:

%ifnarch s390x ppc64le

%pytest \
    -vv \
%if %{with x11}
    --backend x11 \
%endif
    --backend wayland \
    --deselect \
        test/shell_scripts/test_repl_server.py::test_repl_server_executes_code
%endif


%files
%doc README.rst
%{_bindir}/qtile
%if %{with x11}
%{_datadir}/xsessions/qtile.desktop
%endif


%files -n python3-libqtile -f %{pyproject_files}


%files wayland
%{_datadir}/wayland-sessions/qtile-wayland.desktop
%{python3_sitearch}/libqtile/backend/wayland/_ffi.*.so
%{python3_sitelib}/libqtile/backend/wayland/qw/proto/


%autochangelog
