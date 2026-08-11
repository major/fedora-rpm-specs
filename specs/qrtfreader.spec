Name:           qrtfreader
Version:        1.0.0
Release:        1%{?dist}
Summary:        QRtfReader is a library for reading Rtf documents

License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/%{name}
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%conf
%cmake_kf6

%build
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libQRtfReader.so.1
%{_kf6_libdir}/libQRtfReader.so.%{version}
%{_kf6_datadir}/qlogging-categories6/qrtfreader.categories

%files devel
%{_includedir}/QRtfReader/
%{_kf6_libdir}/cmake/QRtfReader/
%{_kf6_libdir}/libQRtfReader.so

%changelog
* Sun Aug 09 2026 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial Release
