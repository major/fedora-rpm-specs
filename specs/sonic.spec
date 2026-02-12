%global  commit       ba331411f17702e01f6c2d7016eefebaa695871f
%global  shortcommit  %{sub %{commit} 1 7}
%global  commitdate   20210316

Name:           sonic
Version:        0.2.0^%{commitdate}git%{shortcommit}
Release:        %{autorelease}
Summary:        Library to speed up or slow down speech

License:        Apache-2.0
URL:            https://github.com/waywardgeek/sonic
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
Requires: libsonic%{?_isa} = %{version}-%{release}

%description
Sonic is a simple algorithm for speeding up or slowing down speech.  However,
it's optimized for speed ups of over 2X, unlike previous algorithms for changing
speech rate.  The Sonic library is a very simple ANSI C library that is designed
to easily be integrated into streaming voice applications, like TTS back ends.

The primary motivation behind Sonic is to enable the blind and visually impaired
to improve their productivity with open source speech engines, like espeak.
Sonic can also be used by the sighted.  For example, Sonic can improve the
experience of listening to an audio book on an Android phone.

%package -n libsonic
Summary: Library package

%description -n libsonic
Sonic shared library package.

%package -n libsonic-devel
Summary:  Development files for sonic
Requires: libsonic%{?_isa} = %{version}-%{release}

%description -n libsonic-devel
Development files and libraries for sonic.

%prep
%autosetup -n sonic-%{commit}
sed -i 's|LIBDIR=$(PREFIX)/lib|LIBDIR=%{_libdir}|g' Makefile

%build
%make_build

%install
%make_install
install -pDm0644 sonic.1 %{buildroot}%{_mandir}/man1/sonic.1
# Do not package static library
rm %{buildroot}/%{_libdir}/libsonic.a

%check
make check

%files
%{_bindir}/sonic
%{_mandir}/man1/sonic.1*

%files -n libsonic
%license COPYING
%doc README
%{_libdir}/libsonic.so.0.3.0
%{_libdir}/libsonic.so.0

%files -n libsonic-devel
%{_includedir}/sonic.h
%{_libdir}/libsonic.so

%changelog
%autochangelog
