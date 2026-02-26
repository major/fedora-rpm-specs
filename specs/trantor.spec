Name:           trantor
Version:        1.5.26
Release:        %autorelease
Summary:        A non-blocking I/O tcp network lib based on c++14/17

License:        BSD-3-Clause
URL:            https://github.com/an-tao/trantor
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Remove spurious executable permissions from non-script sources
Patch0:          %{url}/pull/395.patch
# https://docs.fedoraproject.org/en-US/packaging-guidelines/CryptoPolicies
Patch1:         trantor-use-the-system-ciphers.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(c-ares)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  cmake(spdlog)
BuildRequires:  cmake(GTest)

# Many source files indicate in comments that they are derived from muduo
# http://code.google.com/p/muduo/, https://github.com/chenshuo/muduo. It is not
# easy to tell what version of muduo was used as the basis for these files. Some
# of the code from muduo has been significantly adapted for trantor, it is
# difficult for unbundling.
Provides:       bundled(muduo)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -C
rm -r third_party/

%build
%cmake -DBUILD_C-ARES=ON -DTRANTOR_USE_TLS=openssl -DUSE_SPDLOG=ON -DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license License
%doc README.md
%{_libdir}/libtrantor.so.1*

%files devel
%{_includedir}/trantor/
%{_libdir}/libtrantor.so
%{_libdir}/cmake/Trantor/

%changelog
%autochangelog
