Name:           xkb-switch
Version:        1.8.5
Release:        %autorelease
Summary:        Switch your X keyboard layouts from the command line 

License:        GPL-3.0-or-later
URL:            https://github.com/ierton/xkb-switch
Source0:        https://github.com/ierton/xkb-switch/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libxkbfile-devel

%description
xkb-switch is a C++ program that allows to query and change the XKB layout
state.


%prep
%setup -q -n %{name}-%{version}


%build
%cmake -DBUILD_XKBSWITCH_LIB:BOOL=OFF
%cmake_build


%install
%cmake_install

install -p -D -m644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1


%files
%license COPYING
%doc README.md
%{_mandir}/man1/*
%{_bindir}/xkb-switch



%changelog
%autochangelog
