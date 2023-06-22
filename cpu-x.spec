Name:           cpu-x
Version:        4.5.3
Release:        %autorelease
Summary:        Gathers information on CPU, motherboard and more
ExclusiveArch:  i686 x86_64

License:        GPLv3+
URL:            https://thetumultuousunicornofdarkness.github.io/CPU-X/
Source0:        https://github.com/TheTumultuousUnicornOfDarkness/CPU-X/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  nasm

BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcpuid) >= 0.6.2  %dnl # Upstream recommends 0.6.3
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libproc2)
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(vulkan)

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme

Recommends:     polkit

# https://github.com/X0rg/CPU-X/issues/105
Provides:       bundled(bandwidth) = 1.5.1
Provides:       bundled(dmidecode) = 3.5.484f893

%description
Free software that gathers information on CPU, motherboard and more.

CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.

This software is written in C and built with CMake tool. It can be used in
graphical mode by using GTK or in text-based mode by using NCurses. A dump
mode is present from command line.


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


%prep
%autosetup -n CPU-X-%{version}


%build
%cmake
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
%{_bindir}/%{name}*
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/glib-2.0/schemas/org.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/polkit-1/actions/org.%{name}-daemon.policy
%{_datadir}/zsh/site-functions/_%{name}
%{_libexecdir}/%{name}-daemon
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
