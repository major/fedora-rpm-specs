Name:           fastfetch
Version:        1.9.1
Release:        1%{?dist}
Summary:        Like neofetch, but much faster because written in c

License:        MIT
URL:            https://github.com/LinusDierheimer/fastfetch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pciutils-devel
BuildRequires:  wayland-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrandr-devel
BuildRequires:  dconf-devel
BuildRequires:  dbus-devel
BuildRequires:  sqlite-devel
BuildRequires:  ImageMagick-devel
BuildRequires:  zlib-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  xfconf-devel
BuildRequires:  glib2-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  rpm-devel
# vulkan-loader not available in el8 on some arches
%if 0%{?rhel} == 8
  %if "%{_arch}" != "s390x" && "%{_arch}" != "ppc64le"
BuildRequires:  vulkan-loader-devel
  %endif
%else
BuildRequires:  vulkan-loader-devel
%endif
%if 0%{?fedora} >= 36
BuildRequires:  chafa-devel
%endif

Recommends:     pciutils
Recommends:     libxcb
Recommends:     libXrandr
Recommends:     dconf
Recommends:     sqlite
Recommends:     zlib
Recommends:     libglvnd-glx
Recommends:     ImageMagick
Recommends:     glib2
Recommends:     ocl-icd
%if 0%{?fedora} > 36
Recommends:     chafa
%endif

%description
fastfetch is a neofetch-like tool for fetching system information and
displaying them in a pretty way. It is written in c to achieve much better
performance, in return only Linux and Android are supported. It also uses
mechanisms like multithreading and caching to finish as fast as possible.


%package bash-completion
Summary: Bash completion files for %{name}
Requires: bash-completion
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description bash-completion
%{summary}


%prep
%autosetup -p1


%build
%cmake -D BUILD_TESTS=ON
%cmake_build


%check
%ctest


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/flashfetch
%{_datadir}/%{name}/

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
* Wed Jan 25 2023 Jonathan Wright <jonathan@almalinux.org> - 1.9.1-1
- Update to 1.9.1 rhbz#2163335

* Mon Jan 23 2023 Jonathan Wright <jonathan@almalinux.org> - 1.9.0-1
- Update to 1.9.0 rhbz#2163335

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.8.2-1
- Update to 1.8.2 rhbz#2156978

* Tue Oct 11 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7.5-1
- Update to 1.7.5 rhbz#2133467

* Fri Sep 16 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7.2-1
- Update to 1.7.2 rhbz#2127329

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7.0-1
- Update to 1.7.0
- rhbz#2124866

* Tue Aug 23 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.5-1
- Update to 1.6.5
- rhbz#2120472
- Fix typo in first changelog citing "khbz" instead of "rhbz"

* Mon Aug 22 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.4-3
- Compile with rpm support for listing package counts

* Mon Aug 22 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.4-2
- Fix spec for EPEL8 builds

* Tue Aug 16 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.4-1
- Initial package build
- rhbz#2118887
