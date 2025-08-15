%bcond libjxl 1
Name:           hyprgraphics
Version:        0.1.5
Release:        %autorelease
Summary:        Graphics library for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprgraphics
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(spng)

%if %{with libjxl}
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_cms)
BuildRequires:  pkgconfig(libjxl_threads)
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.


%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ifarch s390x
rm tests/resource/images/hyprland.jpg
%endif
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libhyprgraphics.so.0
%{_libdir}/libhyprgraphics.so.%{version}

%files devel
%{_includedir}/hyprgraphics
%{_libdir}/libhyprgraphics.so
%{_libdir}/pkgconfig/hyprgraphics.pc

%changelog
%autochangelog
