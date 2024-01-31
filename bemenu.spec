Name:       bemenu
Version:    0.6.17
Release:    %{autorelease}
Summary:    Dynamic menu library and client program inspired by dmenu

# In case upstream do not bump program version when tagging; this should usually just resolve to %%{version}
%global     soversion   %{version}

# Library and bindings are LGPLv3+, other files are GPLv3+
License:    GPLv3+ and LGPLv3+
URL:        https://github.com/Cloudef/bemenu
Source0:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:    https://cloudef.pw/bemenu-pgp.txt

Patch:      respect-env-build-flags.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  scdoc

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for extending %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%set_build_flags
%make_build   PREFIX='%{_prefix}' libdir='/%{_lib}'

%install
%make_install PREFIX='%{_prefix}' libdir='/%{_lib}'

%files
%doc README.md
%license LICENSE-CLIENT LICENSE-LIB
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_mandir}/man1/%{name}*.1*
# Long live escaping! %%%% resolves to %%; ${v%%.*} strips everything after first dot
%{_libdir}/lib%{name}.so.%(v=%{soversion}; echo ${v%%%%.*})
%{_libdir}/lib%{name}.so.%{soversion}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-renderer-curses.so
%{_libdir}/%{name}/%{name}-renderer-wayland.so
%{_libdir}/%{name}/%{name}-renderer-x11.so

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%{autochangelog}
