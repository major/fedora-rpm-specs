Name:           libmodplug
Version:        0.8.9.2
Release:        %autorelease
Epoch:          1
Summary:        Modplug mod music file format library
License:        LicenseRef-Fedora-Public-Domain
URL:            https://modplug-xmms.sourceforge.net/
Source0:        https://github.com/Konstanty/libmodplug/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
Suggests:      %{_sysconfdir}/timidity.cfg

%description
%{summary}.

%package        devel
Summary:        Development files for the Modplug mod music file format library
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gcc-c++

%description    devel
%{summary}.

%prep
%autosetup -p1
sed -i -e 's/\r//g' ChangeLog

%build
%cmake
%cmake_build

%install
%cmake_install

%check
# There is not any test
#ctest

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/libmodplug.so.1.0.0
%{_libdir}/libmodplug.so.1

%files devel
%{_includedir}/libmodplug/
%{_libdir}/libmodplug.so
%{_libdir}/pkgconfig/libmodplug.pc

%changelog
%autochangelog
