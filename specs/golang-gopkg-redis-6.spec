# Generated by go2rpm 1
# Tests too slow
%bcond_with check
%global debug_package %{nil}


# https://github.com/go-redis/redis
%global goipath         gopkg.in/redis.v6
%global forgeurl        https://github.com/go-redis/redis
Version:                6.15.9

%gometa

%global goaltipaths     github.com/go-redis/redis

%global common_description %{expand:
Type-safe Redis client for Golang.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Type-safe Redis client for Golang

# Upstream license specification: BSD-2-Clause
# BSD: main library
# ASL 2.0: internal/consistenthash
# Automatically converted from old format: BSD and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# test fixes and do not assume use of system redis-server for testing
Patch0:         redis-testing-fixes.patch

%if %{with check}
# Tests
BuildRequires:  redis
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1
sed -i "s|github.com/go-redis/redis|gopkg.in/redis.v6|" $(find . -iname "*.go" -type f)

%install
%gopkginstall
%global _testdata_redis_src %{_builddir}/redis-%{version}/testdata/redis/src
mkdir -p %{_testdata_redis_src}
ln -s %{_bindir}/redis-server %{_testdata_redis_src}/redis-server

%if %{with check}
%check
# Run a test Redis server rather than assuming the system
# is running one already (see patch0) - non-default port.
redis-cli -p 28126 SHUTDOWN 2>/dev/null || true
redis-server --port 28126 &
sleep 0.2   # time to startup
redis-cli -p 28126 PING || exit 1
%gocheck
redis-cli -p 28126 SHUTDOWN || exit 1
%endif

%gopkgfiles

%changelog
%autochangelog
