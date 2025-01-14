Name:           spdlog
Version:        1.15.0
Release:        %autorelease

License:        MIT
Summary:        Super fast C++ logging library
URL:            https://github.com/gabime/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-fmt_external.patch

# https://github.com/gabime/spdlog/commit/276ee5f5c0eb13626bd367b006ace5eae9526d8a
# https://github.com/gabime/spdlog/commit/7f8060d5b280eac9786f92ac74d263cc8359c5ed
# https://github.com/gabime/spdlog/commit/96a8f6250cbf4e8c76387c614f666710a2fa9bad
Patch100:       %{name}-1.15.0-fmt11.1-build-fixes.patch

BuildRequires:  catch-devel >= 3.0.0
BuildRequires:  fmt-devel >= 10.0.0
BuildRequires:  google-benchmark-devel
BuildRequires:  systemd-devel

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
This is a packaged version of the gabime/spdlog C++ logging
library available at Github.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
Requires:       fmt-devel%{?_isa}

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep
%autosetup -p1
find . -name '.gitignore' -delete
sed -e "s,\r,," -i README.md
rm -f tests/catch.hpp

%build
%cmake -G Ninja \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_BUILD_TYPE=Release \
    -DSPDLOG_BUILD_SHARED=ON \
    -DSPDLOG_BUILD_EXAMPLE=OFF \
    -DSPDLOG_BUILD_BENCH=OFF \
    -DSPDLOG_BUILD_TESTS=ON \
    -DSPDLOG_INSTALL=ON \
    -DSPDLOG_FMT_EXTERNAL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.1.15*

%files devel
%doc example
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
