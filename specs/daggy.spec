%undefine __cmake_in_source_build
%global _vpath_srcdir src

Name:           daggy
Version:        2.2.0
Release:        %autorelease
Summary:        Data Aggregation Utility and C/C++ developer library

License:        MIT
URL:            https://github.com/synacker/daggy
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  qt6-qtbase-devel
BuildRequires:  gcc-c++
BuildRequires:  mustache-devel
BuildRequires:  libssh2-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  cmake
ExcludeArch: s390x


%description
Daggy - Data Aggregation Utility and C/C++ developer library for data streams
catching

Daggy main goals are server-less, cross-platform, simplicity and ease-of-use.

Daggy can be helpful for developers, QA, DevOps and engineers for debug,
analyze and control any data streams, including requests and responses, in
distributed network systems, for example, based on micro-service architecture.

%package devel
Summary: Development files for %{name}

%description devel
%{summary}

%prep
%autosetup

%build
%cmake -DVERSION=%{version}.0 src
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:${LD_LIBRARY_PATH}
%ctest

%files
%license LICENSE
%doc docs/*.md
%{_bindir}/%{name}
%{_libdir}/libDaggyCore.so

%files devel
%{_includedir}/DaggyCore

%changelog
%autochangelog
