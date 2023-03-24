%undefine __cmake_in_source_build

Name:           wpebackend-fdo
Version:        1.14.2
Release:        %autorelease
Summary:        A WPE backend designed for Linux desktop systems

License:        BSD
URL:            https://github.com/Igalia/%{name}
Source0:        https://github.com/Igalia/%{name}/archive/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/Igalia/%{name}/archive/%{version}/%{name}-%{version}.tar.xz.asc
# Created from https://keys.openpgp.org/vks/v1/by-fingerprint/5AA3BC334FD7E3369E7C77B291C559DBE4C9123B
# $ gpg --import 5AA3BC334FD7E3369E7C77B291C559DBE4C9123B.asc
# $ gpg2 --export --export-options export-minimal 5AA3BC334FD7E3369E7C77B291C559DBE4C9123B > gpgkey-5AA3BC334FD7E3369E7C77B291C559DBE4C9123B.gpg
Source2:        gpgkey-5AA3BC334FD7E3369E7C77B291C559DBE4C9123B.gpg

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wpe-1.0)

%description
A WPE backend designed for Linux desktop systems.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_libdir}/libWPEBackend-fdo-1.0.so.1
%{_libdir}/libWPEBackend-fdo-1.0.so.1.*

%files devel
%{_includedir}/wpe-fdo-1.0
%{_libdir}/libWPEBackend-fdo-1.0.so
%{_libdir}/pkgconfig/wpebackend-fdo-1.0.pc

%changelog
%autochangelog
