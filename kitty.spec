%if 0%{?fedora} >= 36
# Rawhide builds is broken,
#    see: https://bugzilla.redhat.com/show_bug.cgi?id=2043178,
#         https://bugzilla.redhat.com/show_bug.cgi?id=2048952
%undefine _package_note_file
%endif

%global optflags %{optflags} -Wno-array-bounds

%bcond_without test
%bcond_without doc

Name:           kitty
Version:        0.26.4
Release:        %autorelease
Summary:        Cross-platform, fast, feature full, GPU based terminal emulator

# BSD:          docs/_templates/searchbox.html
# zlib:         glfw/
License:        GPLv3 and zlib and BSD
URL:            https://sw.kovidgoyal.net/kitty
Source0:        https://github.com/kovidgoyal/kitty/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source4:        https://github.com/kovidgoyal/kitty/releases/download/v%{version}/%{name}-%{version}.tar.xz.sig
Source5:        https://calibre-ebook.com/signatures/kovid.gpg

# Add AppData manifest file
# * https://github.com/kovidgoyal/kitty/pull/2088
Source1:        https://raw.githubusercontent.com/kovidgoyal/kitty/46c0951751444e4f4994008f0d2dcb41e49389f4/kitty/data/%{name}.appdata.xml

Source2:        kitty.sh
Source3:        kitty.fish

## upstream patches

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

# For tests:
BuildRequires:  /usr/bin/ssh
BuildRequires:  /usr/bin/getent

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

# non-executable-script
sed -e "s/f.endswith('\.so')/f.endswith('\.so') or f.endswith('\.py')/g" -i setup.py

# script-without-shebang '__init__.py'
find -type f -name "*.py*" -exec chmod -x "{}"  \;


%install
%set_build_flags
%{__python3} setup.py linux-package \
    --libdir-name=%{_lib}           \
    --prefix=%{buildroot}%{_prefix} \
    --update-check-interval=0       \
    --verbose                       \
    --debug                         \
    --shell-integration "disabled"  \
    %{nil}

install -m0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

install -m0644 -Dp %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -m0644 -Dp %{SOURCE3} %{buildroot}%{_sysconfdir}/fish/conf.d/%{name}.fish

sed 's|KITTY_INSTALLATION_DIR=.*|KITTY_INSTALLATION_DIR="%{_libdir}/%{name}"|' \
 -i %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
sed 's|set -l KITTY_INSTALLATION_DIR .*|set -l KITTY_INSTALLATION_DIR "%{_libdir}/%{name}"|' \
 -i %{buildroot}%{_sysconfdir}/fish/conf.d/%{name}.fish

# script-without-shebang '__init__.py'
find %{buildroot} -type f -name "*.py*" ! -name askpass.py -exec chmod -x "{}"  \;

%if %{with doc}
# rpmlint fixes
rm %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo \
   %{buildroot}%{_datadir}/doc/%{name}/html/.nojekyll
%endif


%check
%if %{with test}
# Some tests ignores PATH env...
mkdir -p kitty/launcher
ln -s %{buildroot}%{_bindir}/%{name} kitty/launcher/
export PATH=%{buildroot}%{_bindir}:$PATH
%{__python3} setup.py test          \
    --prefix=%{buildroot}%{_prefix} \
    ||:
%endif

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files
%license LICENSE
%{_bindir}/%{name}
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
