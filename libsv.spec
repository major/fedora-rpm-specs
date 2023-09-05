Name:           libsv
Version:        1.1

%global forgeurl https://github.com/uael/sv
%forgemeta

Release:        %autorelease
Summary:        Semantic versioning for the C language

License:        Unlicense
URL:            %{forgeurl}
Source:         %{forgesource}

# https://github.com/uael/sv/pulls/57
# not released yet
Patch0:         0001-provide-shared-and-pkgconf.patch

BuildRequires:  gcc
BuildRequires:  gcc-g++
BuildRequires:  cmake

%description
Public domain cross-platform semantic versioning in c99

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and development files for %{name}.

%prep
%autosetup -n sv-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license UNLICENSE
%doc     README.md
%{_libdir}/libsv.so.1.0.0
%{_libdir}/libsv.so.1

%files devel
%{_includedir}/sv/
%{_libdir}/libsv.so
%{_libdir}/pkgconfig/libsv.pc

%changelog
%autochangelog
