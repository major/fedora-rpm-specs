# Debug build does not embed lua scripts that are needed for
# correct functionality
%global debug_package %{nil}
# Commit taken from updated README and version number, which is
# 1 commits after indicated version commit
%global    commit        93f6621b979f64aed4f31448cb3ce4b21b758f05
%global    date          20241207
%global    shortcommit   %(c=%{commit}; echo ${c:0:7})
%global    versiontag    1187
Name:           GENie
Version:        %{versiontag}^%{date}.%{shortcommit}
Release:        %{autorelease}
Summary:        Project generator tool

# Most files under BSD-3-Clause
# inspect.lua and profiler.lua under MIT
License:        BSD-3-Clause AND MIT
URL:            https://github.com/bkaradzic/GENie
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/bkaradzic/GENie/pull/478
# Enable builds on i686 and aarch64
Patch:          arch.patch

BuildRequires:  compat-lua-devel
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  make
Recommends:     cmake
Recommends:     make
Recommends:     ninja-build

%description
GENie (pronounced as Jenny) is project generator tool. It automagically
generates project from Lua script, making applying the same settings for
multiple projects easy.

%prep
%autosetup -n %{name}-%{commit} -p 1
# Fix version information
# https://github.com/bkaradzic/GENie/pull/576
pushd src
pushd host
sed -i 's/1181/1187/g' version.h
sed -i 's/29e6832fdf3b106c0906d288c8ced6c0761b8985/6d94bd661b120b2b14432527d2d82fb79111cef0/g' version.h
popd
popd

%build
%make_build 


%install
install -D -p -m 755 bin/linux/genie %{buildroot}%{_bindir}/genie


%check
# Smoke check
%{buildroot}%{_bindir}/genie --version 2>&1 | grep 'version %{versiontag}'

%files
%license LICENSE
%doc README.md
%doc docs/scripting-reference.md
%{_bindir}/genie


%changelog
%autochangelog
