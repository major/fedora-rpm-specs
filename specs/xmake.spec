%bcond_with luajit

Name:       xmake
Version:    3.0.5

%global __requires_exclude_from ^%{_datadir}/%{name}/scripts/.+\\.ps1$
%global forgeurl https://github.com/xmake-io/xmake

%forgemeta

Release:    %autorelease
Summary:    A cross-platform build utility based on Lua

License:    Apache-2.0
URL:        https://xmake.io
Source:     %forgesource

Patch0:     0001-pkgconfig-fix-check.patch
Patch1:     0001-system-include.patch
Patch2:     0001-add-relwithdebinfo-build-mode.patch

BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(libtbox)
BuildRequires:  pkgconfig(libsv)
%if %{with luajit}
BuildRequires:  pkgconfig(luajit)
%else
BuildRequires:  pkgconfig(lua) >= 5.4
%endif

BuildRequires:  bash
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++

Requires: %{name}-data = %{version}-%{release}

%description
xmake is a lightweight cross-platform build utility based on Lua.

It uses xmake.lua to maintain project builds. Compared with
makefile/CMakeLists.txt, the configuration syntax is more concise and
intuitive. It is very friendly to novices and can quickly get started in
a short time. Let users focus more on actual project development.

It can compile the project directly like Make/Ninja, or generate project
files like CMake/Meson, and it also has a built-in package management
system to help users solve the integrated use of C/C++ dependent
libraries.

%package data
Summary:  Common data-files for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description data
This package contains common data-files for %{name}.

%prep
%forgeautosetup -p1

# Cleanup bundled deps
rm -rf core/src/{lua,luajit,lua-cjson,lz4,pdcurses,sv,tbox,xxhash}/*/

# Fix shebang since the configure script is not strictly POSIX sh
# and relies on bash-specific behavior
sed -i '1 s|#!/bin/sh|#!/bin/bash|' %{_configure}

%build
%configure --external=yes --mode=relwithdebinfo \
%if %{with luajit}
  --runtime=luajit
%else
  --runtime=lua
%endif

%make_build

%install
mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm0755 build/xmake \
        %{buildroot}%{_bindir}/%{name}
install -Dpm0755 scripts/xrepo.sh \
        %{buildroot}%{_bindir}/xrepo
install -Dpm0644 scripts/man/*1 \
        %{buildroot}%{_mandir}/man1/
install -Dpm0644 xmake/scripts/completions/register-completions.bash \
        %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm0644 xmake/scripts/completions/register-completions.fish \
        %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm0644 xmake/scripts/completions/register-completions.zsh \
        %{buildroot}%{zsh_completions_dir}/_%{name}
cp -rp xmake \
        %{buildroot}%{_datadir}/%{name}

%check
%{buildroot}%{_bindir}/%{name} --version
%{buildroot}%{_bindir}/xrepo --version

%files
%doc README.md CHANGELOG.md
%license LICENSE.md NOTICE.md
%{_bindir}/%{name}
%{_bindir}/xrepo
%{bash_completions_dir}/%{name}
%{zsh_completions_dir}/_%{name}
%{fish_completions_dir}/%{name}.fish
%{_mandir}/man1/*.1*

%files data
%{_datadir}/%{name}

%changelog
%autochangelog
