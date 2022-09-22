Name:           bear
Version:        3.0.20
Release:        %autorelease
Summary:        Tool that generates a compilation database for clang tooling

License:        GPLv3+
URL:            https://github.com/rizsotto/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(spdlog)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  grpc-plugins
BuildRequires:  make
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(grpc++)
BuildRequires:  python3

# Needed for functional tests
BuildRequires:  python3dist(lit)
BuildRequires:  /usr/bin/more
BuildRequires:  /usr/bin/xargs
BuildRequires:  gcc-fortran
BuildRequires:  valgrind
BuildRequires:  fakeroot

# Work around RHBZ#1959600 (https://github.com/rizsotto/Bear/issues/309), which
# caused a test failure on s390x. It may only be happenstance that no other
# architectures were affected.
%global _lto_cflags %{nil}

%description
Build ear produces compilation database in JSON format. This database describes
how single compilation unit should be processed and can be used by Clang
tooling.

%prep
%autosetup -p 1 -n Bear-%{version}


%build
for f in $(ls test/bin/); do
    sed -i "s|^#\!/usr/bin/env\s\+python\s\?$|#!%{__python3}|" test/bin/$f
done

# Functional tests are broken for some unknown reason, disable for now.
%cmake -DENABLE_FUNC_TESTS=ON -DENABLE_UNIT_TESTS=ON
%cmake_build

%install
%cmake_install

mv %{buildroot}/%{_docdir}/Bear %{buildroot}/%{_docdir}/bear

%check
# Tests run as part of build, because it's the same build target.
# There is no check target.


%files
%{_bindir}/bear
%{_bindir}/citnames
%{_bindir}/intercept
%{_libdir}/bear
%{_mandir}/man1/bear.1*
%{_mandir}/man1/citnames.1*
%{_mandir}/man1/intercept.1*

# rpmbuild on RHEL won't automatically pick up ChangeLog.md & README.md
%if 0%{?rhel}
%{_datadir}/doc/bear
%endif

%license COPYING
%doc %{_docdir}/bear

%changelog
%autochangelog
