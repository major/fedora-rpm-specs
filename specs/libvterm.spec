%global libname vterm

Name:           lib%{libname}
Version:        0.3.3
Release:        %autorelease
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator

License:        MIT
URL:            https://www.leonerd.org.uk/code/libvterm
Source0:        %{url}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool

%description
An abstract C99 library which implements a VT220 or xterm-like
terminal emulator. It does not use any particular graphics toolkit or
output system. Instead, it invokes callback function pointers that
its embedding program should provide it to draw on its behalf.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
%{summary}.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
%set_build_flags
%make_build test

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_includedir}/%{libname}_*.h
%{_libdir}/pkgconfig/%{libname}.pc

%files tools
%{_bindir}/unterm
%{_bindir}/%{libname}-ctrl
%{_bindir}/%{libname}-dump

%changelog
%autochangelog
