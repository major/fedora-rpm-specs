Name:           mcpanel
Version:        1.0
Release:        %autorelease
Summary:        Library that provides a scope interface for displaying multichannel signal

License:        GPLv3+
URL:            https://opensource.mindmaze.com/
Source0:        https://github.com/nbourdau/mcpanel/archive/%{version}/%{name}-%{version}.tar.gz
#Patch0:         mcpanel-automake.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  automake autoconf libtool
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  rtfilter-devel

%description
mcpanel is a library that provides a scope interface for displaying multichannel
signal. It has been designed to implement easily a realtime display of signal
and can be easily integrated in other projects.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
autoreconf -vfi
%configure --disable-static
%make_build

%install
%make_install

# drop libtool
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
#make check

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.0.0
%{_datadir}/%{name}/

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
