# Git submodules
#   * i3ipcpp
%global commit1         0daa58349ab3373161a4a73c1ccd2822328d2c73
%global shortcommit1    %(c=%{commit1}; echo ${c:0:7})

#   * xpp
%global commit2         a8b9e682ba65ca4a6d805c8be97c5232bae3c0c1
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

%global url1    https://github.com/%{name}

Name:           polybar
Version:        3.7.2
Release:        %autorelease
Summary:        Fast and easy-to-use status bar

# BSD 2-clause "Simplified" License
# ---------------------------------
# lib/concurrentqueue/
#
# Expat License
# -------------
# lib/i3ipcpp/
# lib/xpp/
#
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            https://polybar.github.io/
Source0:        %{url1}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Bundled libs
Source1:        %{url1}/i3ipcpp/archive/%{commit1}/i3ipcpp-%{shortcommit1}.tar.gz
Source2:        %{url1}/xpp/archive/%{commit2}/xpp-%{shortcommit2}.tar.gz

Patch0:         polybar-3.7.2-include-cstdint.patch

BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  i3-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-sphinx
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp) >= 1.7.7
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libuv) >= 1.3
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb)

Provides:       bundled(i3ipcpp) = 0.7.1~git%{shortcommit1}
Provides:       bundled(xpp) = 1.4.0~git%{shortcommit2}

%description
Polybar aims to help users build beautiful and highly customizable status bars
for their desktop environment, without the need of having a black belt in shell
scripting.


%prep
%setup -q
%setup -q -D -T -a1
%setup -q -D -T -a2

mv i3ipcpp-%{commit1}/* lib/i3ipcpp
mv xpp-%{commit2}/*     lib/xpp

%patch 0 -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md SUPPORT.md
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/
%{_docdir}/%{name}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_sysconfdir}/%{name}/config.ini


%changelog
%autochangelog
