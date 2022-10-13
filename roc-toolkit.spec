# git ls-remote https://github.com/roc-streaming/roc-toolkit.git
%global git_commit 863a0227b78464c3a56fc0484bec73c891e4b7a8
%global git_date 20220829

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		roc-toolkit
Version:	0.1.5^%{git_suffix}
Release:	3%{?dist}
Summary:	Real-time audio streaming
License:	MPL-2.0 AND LGPL-2.1-or-later AND CECILL-C
URL:		https://github.com/roc-streaming/roc-toolkit
#Source0:	%%{URL}/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	python3-devel
BuildRequires:	python3-scons
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	pkgconf-pkg-config
BuildRequires:	gengetopt
BuildRequires:	ragel-devel
BuildRequires:	libuv-devel
BuildRequires:	libunwind-devel
BuildRequires:	sox-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	openfec-devel
BuildRequires:	cpputest-devel
BuildRequires:	sphinx
BuildRequires:	python3-sphinx
BuildRequires:	python3-breathe
# https://github.com/roc-streaming/roc-toolkit/issues/481
Patch0:		roc-toolkit-0.1.5-no-explicit-cpp98.patch

%description
Roc is a toolkit for real-time audio streaming over the network.

%package devel
Summary: Development libraries for roc-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The roc-toolkit-devel package contains header files necessary for
developing programs using roc-toolkit.

%package utils
Summary: Utilities for roc-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for roc-toolkit.

%package doc
Summary: Documentation for roc-toolkit

%description doc
Documentation for roc-toolkit.

%prep
%autosetup -p1 -n %{name}-%{git_commit}

%build
scons %{?_smp_mflags} --with-openfec-includes=%{_includedir}/openfec \
  CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}"
scons docs

%install
scons install --with-openfec-includes=%{_includedir}/openfec --prefix=%{buildroot}%{_prefix} \
  --libdir=%{buildroot}%{_libdir}

%check
# https://github.com/roc-streaming/roc-toolkit/issues/480
%ifnarch i686 armv7hl
scons test --with-openfec-includes=%{_includedir}/openfec
%endif

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libroc.so.0*

%files devel
%{_includedir}/roc
%{_libdir}/libroc.so

%files utils
%{_bindir}/roc-conv
%{_bindir}/roc-recv
%{_bindir}/roc-send
%{_mandir}/man1/*.1.gz

%files doc
%doc html

%changelog
* Tue Oct 11 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.5^20220829git863a0227-3
- Disabled tests on 32 bit architectures (code is broken, use on own risk)

* Mon Oct 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.5^20220829git863a0227-2
- Switched license tag to SPDX format

* Sat Aug 20 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.5^20220829git863a0227-1
- Initial version
