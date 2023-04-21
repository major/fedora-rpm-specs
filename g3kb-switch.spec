%global uuid g3kb-switch@g3kb-switch.org

Name:           g3kb-switch
Version:        1.1
Release:        %autorelease
Summary:        CLI keyboard layout switcher for GNOME Shell

# g3kb-switch: BSD-2-Clause
# extension/g3kb-switch@g3kb-switch.org: GPL-2.0-only
License:        BSD-2-Clause AND GPL-2.0-only
URL:            https://github.com/lyokha/g3kb-switch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# merged upstream
# https://github.com/lyokha/g3kb-switch/pull/14
# https://github.com/lyokha/g3kb-switch/pull/15
# ability to set installation paths + avoid unnecessary CMakeDetermineCXXCompiler check
Patch0:         g3kb-switch-cmake-fixes.patch
Patch1:         g3kb-switch-gnome-44-support.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)

Requires:       gnome-shell

%description
This is a CLI keyboard layout switcher for Gnome 3 and 4x. It is
not based on the X interface but rather implements direct D-Bus
messaging with the Gnome Shell.


%package        zsh-completion
Summary:        Zsh completion for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description    zsh-completion
Zsh command line completion support for %{name}.


%package        bash-completion
Summary:        Bash completion for %{name}
BuildArch:      noarch
BuildRequires:  bash-completion
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description    bash-completion
Bash command line completion support for %{name}.

%prep
%autosetup -p1
sed -i '1{\@#!/usr/bin/env bash@d}' g3kb-switch-completion.bash

%build
%cmake -DG3KBSWITCH_WITH_GNOME_SHELL_EXTENSION:BOOL=ON \
       -DG3KBSWITCH_VIM_XKBSWITCH_LIB_PATH:PATH=%{_lib}/%{name}
%cmake_build


%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -ap extension/%{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libg3kbswitch.so
%{_datadir}/gnome-shell/extensions/%{uuid}/

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%files bash-completion
%{bash_completions_dir}/%{name}

%changelog
%autochangelog
