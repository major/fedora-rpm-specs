Name:           stlsplit
Version:        1.2
Release:        %autorelease
Summary:        Split STL file to more files - one shell each
License:        AGPL-3.0-or-later
URL:            https://github.com/admesh/stlsplit/
Source:         https://github.com/admesh/stlsplit/archive/v%{version}.tar.gz
BuildRequires:  admesh-devel >= 0.98
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  premake >= 5

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

%description
stlsplit receives one STL file and splits it to several files -
one shell a file.

%package devel
Summary:        Development files for the %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This tool receives one STL file and splits it to several files -
one shell a file.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%prep
%autosetup -p1

%build
premake5 gmake
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' lib.make
CFLAGS="%{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}" %make_build

%install
install -Dpm 755 build/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 755 build/lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so
install -Dpm 644 %{name}.h %{buildroot}%{_includedir}/%{name}.h

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.1

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
