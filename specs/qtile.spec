%global forgeurl https://github.com/qtile/qtile
%global tag v0.34.1

Name: qtile
Version: 0.34.1
Release: %{autorelease}
Summary: A pure-Python tiling window manager
%forgemeta
Source: %{forgesource}

# Everything licensed under MIT except for the following files.
# GPL-3.0-or-later:
#   libqtile/widget/cmus.py
#   libqtile/widget/moc.py
#
# Slated for removal in the next Qtile release. See:
# https://github.com/qtile/qtile/pull/5738
License: MIT AND GPL-3.0-or-later
Url: http://qtile.org

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pulseaudio

# Test dependencies
BuildRequires:  gcc
BuildRequires:  xcb-util-cursor
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  xterm
BuildRequires:  rsvg-pixbuf-loader
BuildRequires:  wlroots >= 0.19.0
BuildRequires:  wlroots < 0.20.0
BuildRequires:  wlroots-devel >= 0.19.0
BuildRequires:  wlroots-devel < 0.20.0

# Some dependencies are loaded with ffi.dlopen, and to declare them properly
# we'll need this suffix.
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

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

# These are not packaged for Fedora yet
sed -i '/check-manifest/d' ./pyproject.toml
sed -i '/mailbox/d' ./pyproject.toml
sed -i '/imaplib2/d' ./pyproject.toml
sed -i '/xdg/d' ./pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x test,wayland,dev,optional_core,widgets


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
PYTHONPATH=${PWD} %{python3} ./libqtile/backend/wayland/cffi/build.py


%install
%pyproject_install
%pyproject_save_files libqtile

mkdir -p %{buildroot}%{python3_sitearch}/libqtile/backend/wayland/
cp -a ./libqtile/backend/wayland/_ffi.*.so %{buildroot}%{python3_sitearch}/libqtile/backend/wayland/

mkdir -p %{buildroot}%{_datadir}/xsessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/xsessions/ \
    resources/qtile.desktop

mkdir -p %{buildroot}%{_datadir}/wayland-sessions/
desktop-file-install \
    --dir %{buildroot}%{_datadir}/wayland-sessions/ \
    resources/qtile-wayland.desktop


%check
# Tests can sometimes randomly fail. Rebuilding the package again usually solves
# the issue. See https://github.com/qtile/qtile/issues/4573

# Avoid `OSError: [Errno 24] Too Many Open Files` error
ulimit -n 10240

%ifnarch s390x ppc64le
# Disabled tests
# - test/widgets/test_generic_poll_text.py      require network
# - test/backend/wayland/test_idle_inhibit.py   https://github.com/qtile/qtile/issues/5723
%pytest \
    -vv \
    --backend x11 \
    --backend wayland \
    --deselect test/widgets/test_generic_poll_text.py::test_gen_poll_url_text \
    --deselect test/widgets/test_generic_poll_text.py::test_gen_poll_url_json_with_data \
    --deselect test/widgets/test_generic_poll_text.py::test_gen_poll_url_custom_headers \
    --deselect test/backend/wayland/test_idle_inhibit.py::test_inhibitor_open[1-x11-InhibitorConfig] \
    --deselect test/backend/wayland/test_idle_inhibit.py::test_inhibitor_visible[1-x11-InhibitorConfig] \
    --deselect test/backend/wayland/test_idle_inhibit.py::test_inhibitor_focus[1-x11-InhibitorConfig] \
    --deselect test/backend/wayland/test_idle_inhibit.py::test_inhibitor_fullscreen[1-x11-InhibitorConfig] \
    --deselect test/backend/wayland/test_idle_inhibit.py::test_inhibitor_global[1-x11-InhibitorConfig]
%endif


%files
%doc README.rst
%{_bindir}/qtile
%{_datadir}/xsessions/qtile.desktop


%files -n python3-libqtile -f %{pyproject_files}


%files wayland
%{_datadir}/wayland-sessions/qtile-wayland.desktop
%{python3_sitearch}/libqtile/backend/wayland/_ffi.*.so


%autochangelog
