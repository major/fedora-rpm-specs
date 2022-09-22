Name:           libwpe
Version:        1.14.0
Release:        %autorelease
Summary:        General-purpose library for the WPE-flavored port of WebKit
License:        BSD
URL:            https://github.com/WebPlatformForEmbedded/%{name}
Source0:        https://github.com/WebPlatformForEmbedded/libwpe/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/WebPlatformForEmbedded/libwpe/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
# Created from https://keys.openpgp.org/vks/v1/by-fingerprint/5AA3BC334FD7E3369E7C77B291C559DBE4C9123B
# $ gpg --import 5AA3BC334FD7E3369E7C77B291C559DBE4C9123B.asc
# $ gpg2 --export --export-options export-minimal 5AA3BC334FD7E3369E7C77B291C559DBE4C9123B > gpgkey-5AA3BC334FD7E3369E7C77B291C559DBE4C9123B.gpg
Source2:        gpgkey-5AA3BC334FD7E3369E7C77B291C559DBE4C9123B.gpg

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(xkbcommon)

%description
General-purpose library developed for the WPE-flavored port of WebKit

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n libwpe-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_libdir}/libwpe-1.0.so.1.*
%{_libdir}/libwpe-1.0.so.1

%files devel
%{_includedir}/wpe-1.0/
%{_libdir}/libwpe-1.0.so
%{_libdir}/pkgconfig/wpe-1.0.pc

%changelog
%autochangelog
