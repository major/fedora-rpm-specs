%global optflags %{optflags} -Wno-array-bounds

%bcond_without test
%bcond_without doc

Name:           kitty
Version:        0.28.1
Release:        %autorelease
Summary:        Cross-platform, fast, feature full, GPU based terminal emulator

# Zlib: glfw
# LGPL-2.1-or-later: kitty/iqsort.h
# BSD-1-Clause: kitty/uthash.h
# MIT: docs/_static/custom.css
# MIT: shell-integration/ssh/bootstrap-utils.sh
License:        GPL-3.0-only AND LGPL-2.1-or-later AND Zlib AND BSD-1-Clause AND MIT
URL:            https://sw.kovidgoyal.net/kitty
Source0:        https://github.com/kovidgoyal/kitty/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source4:        https://github.com/kovidgoyal/kitty/releases/download/v%{version}/%{name}-%{version}.tar.xz.sig
Source5:        https://calibre-ebook.com/signatures/kovid.gpg

# Add AppData manifest file
# * https://github.com/kovidgoyal/kitty/pull/2088
Source1:        https://raw.githubusercontent.com/kovidgoyal/kitty/46c0951751444e4f4994008f0d2dcb41e49389f4/kitty/data/%{name}.appdata.xml

Source2:        kitty.sh
Source3:        kitty.fish

# Don't build kitten inside setup.py, use gobuild macro in the spec instead to build with fedora flags
Patch0:         kitty-do-not-build-kitten.patch
## upstream patches


# some golang deps aren't available
ExcludeArch:    s390x %{ix86}

BuildRequires:  golang >= 1.20.0
BuildRequires:  go-rpm-macros

BuildRequires:  gnupg2
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  lcms2-devel
BuildRequires:  libappstream-glib
BuildRequires:  librsync-devel
BuildRequires:  ncurses
BuildRequires:  python3-devel >= 3.8
BuildRequires:  wayland-devel

BuildRequires:  python3dist(setuptools)

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(harfbuzz) >= 2.2
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcrypto)

BuildRequires:  golang(github.com/alecthomas/chroma/v2)
BuildRequires:  golang(github.com/alecthomas/chroma/v2/lexers)
BuildRequires:  golang(github.com/alecthomas/chroma/v2/styles)
BuildRequires:  golang(github.com/ALTree/bigfloat)
BuildRequires:  golang(github.com/bmatcuk/doublestar/v4)
BuildRequires:  golang(github.com/disintegration/imaging)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/jamesruan/go-rfc1924/base85)
BuildRequires:  golang(github.com/seancfoley/ipaddress-go/ipaddr)
BuildRequires:  golang(github.com/shirou/gopsutil/v3/process)
BuildRequires:  golang(golang.org/x/exp/constraints)
BuildRequires:  golang(golang.org/x/exp/maps)
BuildRequires:  golang(golang.org/x/exp/rand)
BuildRequires:  golang(golang.org/x/exp/slices)
BuildRequires:  golang(golang.org/x/image/bmp)
BuildRequires:  golang(golang.org/x/image/tiff)
BuildRequires:  golang(golang.org/x/image/webp)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with test}
# For tests:
BuildRequires:  /usr/bin/ssh
BuildRequires:  /usr/bin/getent
BuildRequires:  /usr/bin/zsh
BuildRequires:  /usr/bin/fish
BuildRequires:  /usr/bin/rg
BuildRequires:  python3dist(pillow)
%endif

Requires:       python3%{?_isa}
Requires:       hicolor-icon-theme

Suggests:       %{name}-bash-integration
Suggests:       %{name}-fish-integration

# Terminfo file has been split from the main program and is required for use
# without errors. It has been separated to support SSH into remote machines using
# kitty as per the maintainers suggestion. Install the terminfo file on the remote
# machine.
Requires:       %{name}-terminfo = %{version}-%{release}

# Very weak dependencies, these are required to enable all features of kitty's
# "kittens" functions install separately
Recommends:     python3-pygments

Suggests:       ImageMagick%{?_isa}

%description
- Offloads rendering to the GPU for lower system load and buttery smooth
  scrolling. Uses threaded rendering to minimize input latency.

- Supports all modern terminal features: graphics (images), unicode, true-color,
  OpenType ligatures, mouse protocol, focus tracking, bracketed paste and
  several new terminal protocol extensions.

- Supports tiling multiple terminal windows side by side in different layouts
  without needing to use an extra program like tmux.

- Can be controlled from scripts or the shell prompt, even over SSH.

- Has a framework for Kittens, small terminal programs that can be used to
  extend kitty's functionality. For example, they are used for Unicode input,
  Hints and Side-by-side diff.

- Supports startup sessions which allow you to specify the window/tab layout,
  working directories and programs to run on startup.

- Cross-platform: kitty works on Linux and macOS, but because it uses only
  OpenGL for rendering, it should be trivial to port to other Unix-like
  platforms.

- Allows you to open the scrollback buffer in a separate window using arbitrary
  programs of your choice. This is useful for browsing the history comfortably
  in a pager or editor.

- Has multiple copy/paste buffers, like vim.


# bash integration package
%package        bash-integration
Summary:        Automatic Bash integration for Kitty Terminal
BuildArch:      noarch

%description    bash-integration
Cross-platform, fast, feature full, GPU based terminal emulator.

Bash integration for Kitty Terminal.


# fish integration package
%package        fish-integration
Summary:        Automatic Fish integration for Kitty Terminal
BuildArch:      noarch

%description    fish-integration
Cross-platform, fast, feature full, GPU based terminal emulator.

Fish integration for Kitty Terminal.


# terminfo package
%package        terminfo
Summary:        The terminfo file for Kitty Terminal
BuildArch:      noarch

Requires:       ncurses-base

%description    terminfo
Cross-platform, fast, feature full, GPU based terminal emulator.

The terminfo file for Kitty Terminal.


# doc package
%if %{with doc}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

BuildRequires:  python3dist(sphinx)
%if ! 0%{?epel}
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinx-inline-tabs)
BuildRequires:  python3dist(sphinxext-opengraph)
%endif

%description    doc
This package contains the documentation for %{name}.
%endif


%prep
%{gpgverify} --keyring='%{SOURCE5}' --signature='%{SOURCE4}' --data='%{SOURCE0}'
%autosetup -p1

# Changing sphinx theme to classic
sed "s/html_theme = 'furo'/html_theme = 'classic'/" -i docs/conf.py

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python3|%{__python3}|g'    \
                                    -e 's|/usr/bin/env python|%{__python3}|g'     \
                                    -e 's|/usr/bin/env -S kitty|/usr/bin/kitty|g' \
                                    -i "{}" \;

mkdir -p src/kitty
ln -s ../../tools src/kitty/tools
ln -s ../../kittens src/kitty/kittens


%build
%set_build_flags
%{__python3} setup.py linux-package \
    --libdir-name=%{_lib}           \
    --update-check-interval=0       \
    --verbose                       \
    --shell-integration "disabled"  \
    %{nil}

export GOPATH=$(pwd):%{gopath}
unset LDFLAGS
mkdir -p _build/bin
%gobuild -o _build/bin/kitten ./src/kitty/tools/cmd

%install
# rpmlint fixes
find linux-package -type f ! -executable -name "*.py" -exec sed -i '1{\@^#!%{__python3}@d}' "{}" \;
find linux-package/%{_lib}/%{name}/shell-integration -type f ! -executable -exec sed -r -i '1{\@^#!/bin/(fish|zsh|sh|bash)@d}' "{}" \;

cp -r linux-package %{buildroot}%{_prefix}
install -m0755 -Dp _build/bin/kitten %{buildroot}%{_bindir}/kitten

install -m0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

install -m0644 -Dp %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -m0644 -Dp %{SOURCE3} %{buildroot}%{_sysconfdir}/fish/conf.d/%{name}.fish

sed 's|KITTY_INSTALLATION_DIR=.*|KITTY_INSTALLATION_DIR="%{_libdir}/%{name}"|' \
 -i %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
sed 's|set -l KITTY_INSTALLATION_DIR .*|set -l KITTY_INSTALLATION_DIR "%{_libdir}/%{name}"|' \
 -i %{buildroot}%{_sysconfdir}/fish/conf.d/%{name}.fish

%if %{with doc}
# rpmlint fixes
rm %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo \
   %{buildroot}%{_datadir}/doc/%{name}/html/.nojekyll   \
   %{buildroot}%{_datadir}/doc/%{name}/html/_static/scripts/furo-extensions.js
%endif


%check
%if %{with test}
export %{gomodulesmode}
export GOPATH=$(pwd):%{gopath}
# Some tests ignores PATH env...
mkdir -p kitty/launcher
ln -s %{buildroot}%{_bindir}/%{name} kitty/launcher/
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONPATH=$(pwd)
%{__python3} setup.py test          \
    --prefix=%{buildroot}%{_prefix} \
    ||:
%endif

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/kitten
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.{png,svg}
%{_libdir}/%{name}/
%if %{with doc}
%{_mandir}/man{1,5}/*.{1,5}*
%endif
%{_metainfodir}/*.xml

%files bash-integration
%{_sysconfdir}/profile.d/%{name}.sh

%files fish-integration
%dir %{_sysconfdir}/fish
%dir %{_sysconfdir}/fish/conf.d
%{_sysconfdir}/fish/conf.d/%{name}.fish

%files terminfo
%license LICENSE
%{_datadir}/terminfo/x/xterm-%{name}

%if %{with doc}
%files doc
%license LICENSE
%doc CONTRIBUTING.md CHANGELOG.rst INSTALL.md
%{_docdir}/%{name}/html
%dir %{_docdir}/%{name}
%endif


%changelog
%autochangelog
