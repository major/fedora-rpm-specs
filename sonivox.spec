Name:           sonivox
Version:        3.6.12
Release:        %{autorelease}
Summary:        Fork of the AOSP 'platform_external_sonivox' to use out of Android

# migrated to SPDX
License:        Apache-2.0
URL:            https://github.com/pedrolcl/sonivox
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel

%description
This is a Wave Table synthesizer, not using external soundfont files but
embedded samples instead. It is also a real time GM synthesizer.

It consumes very little resources, so it may be indicated in projects for small
embedded devices. There is neither MIDI input nor Audio output facilities
included in the library. You need to provide your own input/output.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup


%build
%cmake -DBUILD_SONIVOX_STATIC=OFF
%cmake_build


%install
%cmake_install


%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.3*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%changelog
%autochangelog
