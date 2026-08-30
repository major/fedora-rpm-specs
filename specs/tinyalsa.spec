Name:		tinyalsa
Version:	2.0.0
Release:	%autorelease
Summary:	A small library to interface with ALSA in the Linux kernel

License:	BSD-3-Clause
URL:		https://github.com/tinyalsa/tinyalsa
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExcludeArch:	%{ix86}

BuildRequires:	meson
BuildRequires:	gcc

%description
TinyALSA is a small library to interface with ALSA in the Linux kernel.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/tinycap
%{_bindir}/tinymix
%{_bindir}/tinypcminfo
%{_bindir}/tinyplay
%{_libdir}/libtinyalsa.so.2{,.*}
%{_mandir}/man1/tinycap.1*
%{_mandir}/man1/tinymix.1*
%{_mandir}/man1/tinypcminfo.1*
%{_mandir}/man1/tinyplay.1*

%files devel
%{_includedir}/tinyalsa
%{_libdir}/libtinyalsa.so
%{_libdir}/pkgconfig/tinyalsa.pc

%changelog
%autochangelog
