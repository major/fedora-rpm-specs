%global forgeurl https://github.com/TheTumultuousUnicornOfDarkness/CPU-X
%global tag v%{version}
%global appid io.github.thetumultuousunicornofdarkness.%{name}

Name:           cpu-x
Version:        5.4.0
%forgemeta
Release:        %autorelease
Summary:        Free software that gathers information on CPU, motherboard and more

ExclusiveArch:  i686 x86_64 aarch64

License:        GPL-3.0-or-later
URL:            https://thetumultuousunicornofdarkness.github.io/CPU-X/
Source0:        %{forgesource}
# https://github.com/TheTumultuousUnicornOfDarkness/CPU-X/issues/362
Patch0:         %{name}_policy.patch
# https://github.com/TheTumultuousUnicornOfDarkness/CPU-X/pull/402
Patch1:         0001-use-default-cpu-instead-of-ia64.patch

BuildRequires:  cmake >= 3.12
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  nasm

BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(glfw3) >= 3.3
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-c)
%if 0%{?flatpak}
BuildRequires:  libcpuid-static >= 0.8.0
%else
BuildRequires:  pkgconfig(libcpuid) >= 0.7.1
%endif
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpci)
%if 0%{?fedora} >= 39
BuildRequires:  pkgconfig(libproc2)
%else
BuildRequires:  pkgconfig(libprocps)
%endif
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(vulkan)

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme

Recommends:     polkit

# https://github.com/X0rg/CPU-X/issues/105
Provides:       bundled(bandwidth) = 1.5.1
Provides:       bundled(dmidecode) = 3.6


%global _description %{expand:
CPU-X is a Free software that gathers information on CPU, motherboard and
more. CPU-X is a system profiling and monitoring application (similar to CPU-Z
for Windows), but CPU-X is a Free and Open Source software designed for
GNU/Linux and FreeBSD. This software is written in C++ and built with CMake
tool. It can be used in graphical mode by using GTK or in text-based mode by
using NCurses. A dump mode is present from command line.}

%description %_description


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data %_description

Data files for %{name}.


%prep
%forgeautosetup -p1
%if 0%{?flatpak}
sed -i -e 's#lib/\(aarch64\|x86_64\)-linux-gnu#lib64#' src/daemon/client.cpp
%endif


%build
%cmake %{?flatpak:-DFLATPAK=ON}
%cmake_build


%install
%cmake_install
rm -r %{buildroot}%{_datadir}/icons/hicolor/384x384

# invalid-lc-messages-dir
rm -r %{buildroot}%{_datadir}/locale/zh_Hant/

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/polkit-1/actions/%{appid}-daemon.policy
%{_datadir}/zsh/site-functions/_%{name}
%if 0%{?flatpak}
%{_prefix}/lib/%{name}/%{name}-daemon
%else
%{_libexecdir}/%{name}-daemon
%endif
%{_metainfodir}/*.appdata.xml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions

%files data
%{_datadir}/%{name}/


%changelog
%autochangelog
