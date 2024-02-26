%bcond_without debug

# tests fail with multiple Error: symbol ... is already defined
%bcond_with check

%if %{without debug}
%global debug_package %{nil}
%endif

%global forgeurl https://github.com/facebook/mcrouter
%global tag 2024.02.19.00
%global date %(echo %{tag} | sed -e 's|.00$||' | sed -e 's|\\.||g')

# lib/fbi/cpp/LowerBoundPrefixMap.cpp includes folly/container/tape.h
# which uses std::ranges which is part of C++20
%global optflags %optflags -std=c++20

Name:           mcrouter
Version:        0.41.0.%{date}
Release:        %autorelease
Summary:        Memcached protocol router for scaling memcached deployments

License:        MIT
URL:            %{forgeurl}
Source:         %{url}/archive/v%{tag}/%{name}-%{tag}.tar.gz
# distutils deprecated in Python 3.10
Patch:          %{name}-0.41.0-no_distutils.patch

ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  gcc-c++
BuildRequires:  folly-devel
BuildRequires:  fizz-devel
BuildRequires:  wangle-devel
BuildRequires:  fbthrift-devel
BuildRequires:  fbthrift
BuildRequires:  libatomic
# for free
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  ragel
# Test dependencies
BuildRequires:  gtest-devel

%description
Mcrouter (pronounced mc router) is a memcached protocol router for scaling
memcached deployments.

Because the routing and feature logic are abstracted from the client in
mcrouter deployments, the client may simply communicate with destination
hosts through mcrouter over a TCP connection using standard memcached
protocol. Typically, little or no client modification is needed to use
mcrouter, which was designed to be a drop-in proxy between the client and
memcached hosts.


%prep
%autosetup -p1 -n %{name}-%{tag}
pushd %{name}
# Fix detecting ppc64le: bug 1943729
sed -i m4/ax_boost_base.m4 -e 's@ppc64|@ppc64|ppc64le|@'
echo "%{version}" > VERSION
autoreconf --install


%build
pushd %{name}
export FBTHRIFT_BIN="%{_bindir}"
export INSTALL_DIR="%{_prefix}"
export PYTHON_VERSION="%{python3_version}"
%configure --enable-shared --disable-static
# do not eat all memory
%make_build %{limit_build -m 4096}


%install
pushd %{name}
%make_install


%if %{with check}
%check
pushd %{name}
%make_build check
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/*


%changelog
%autochangelog
