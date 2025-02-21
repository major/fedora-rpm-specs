#%%define __cmake_in_source_build 1

#%%global commit 35a0b465cebb577389644ca5149c4569b3c2990d
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})

Name:           herbstluftwm
Version:        0.9.5
Release:        %autorelease
Summary:        A manual tiling window manager
License:        BSD
URL:            http://herbstluftwm.org
#Source0:        https://github.com/%%{name}/%%{name}/archive/%%{commit}/%%{name}-%%{shortcommit}.tar.gz
Source0:        http://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz
Patch0:         0.9.5-cstdint-gcc15.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  asciidoc

Requires:       xsetroot

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.
Its main features can be described with:

- The layout is based on splitting frames into subframes which can be split
again or can be filled with windows;
- Tags (or workspaces or virtual desktops or …) can be added/removed at
runtime. Each tag contains an own layout exactly one tag is viewed on each
monitor. The tags are monitor independent;
- It is configured at runtime via ipc calls from herbstclient. So the
configuration file is just a script which is run on startup.

%package        zsh
Summary:        Herbstluftwm zsh completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh

%description    zsh
This package provides zsh completion script of %{name}.

%package        fish
Summary:        Herbstluftwm fish completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       fish

%description    fish
This package provides fish completion script of %{name}.

%prep
#%%autosetup -p1 -n %%{name}-%%{commit}
%autosetup -p1

%build
# Set the proper build flags
%cmake
%cmake_build

%install
%cmake_install

# Change the shebangs of the upstream files to be proper
for f in "%{buildroot}%{_pkgdocdir}/examples/*.sh"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

for f in "%{buildroot}%{_sysconfdir}/xdg/%{name}/*"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

# Remove unnecessary and/or redundant files
rm %{buildroot}%{_pkgdocdir}/LICENSE
rm -r %{buildroot}%{_pkgdocdir}/html

%files
%license LICENSE
%doc AUTHORS MIGRATION NEWS
%doc doc/*.{html,txt}
%{_sysconfdir}/xdg/%{name}
%{_bindir}/*
%{_datadir}/bash-completion/completions/herbstclient
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_pkgdocdir}/examples/
%{_pkgdocdir}/hlwm-doc.json

%files zsh
%{_datadir}/zsh/site-functions/_herbstclient

%files fish
%{_datadir}/fish/vendor_completions.d/herbstclient.fish

%changelog
%autochangelog
