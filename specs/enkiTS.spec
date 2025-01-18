%global forgeurl  https://github.com/dougbinks/enkiTS
%global version0  1.11
%global commit 686d0ec31829e0d9e5edf9ceb68c40f9b9b20ea9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%forgemeta

Name:           enkiTS
Version:        %{forgeversion}
Release:        2%{?dist}
Summary:        A C and C++ task scheduler for creating parallel programs

License:        Zlib
URL:            %{forgeurl}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
The primary goal of enkiTS is to help developers create programs which handle
both data and task level parallelism to utilize the full performance of
multicore CPUs, whilst being lightweight (only a small amount of code) and easy
to use.

%package devel
Summary:   A C and C++ task scheduler for creating parallel programs
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for enkiTS.

%package examples
Summary:   A C and C++ task scheduler for creating parallel programs
BuildArch:  noarch

%description examples
Examples for how to use enkiTS.

%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%cmake -DENKITS_BUILD_SHARED=ON \
       -DENKITS_BUILD_C_INTERFACE=ON \
       -DENKITS_BUILD_EXAMPLES=ON \
       -DENKITS_INSTALL=ON
%cmake_build


%install
%cmake_install

%check
%{_vpath_builddir}/TestAll


%files
%license License.txt
%doc README.md
%{_libdir}/libenkiTS.so.1
%{_libdir}/libenkiTS.so.1.*

%files devel
%dir %{_includedir}/enkiTS
%{_includedir}/enkiTS/TaskScheduler.h
%{_includedir}/enkiTS/LockLessMultiReadPipe.h
%{_includedir}/enkiTS/TaskScheduler_c.h
%dir %{_libdir}/cmake/enkiTS
%{_libdir}/cmake/enkiTS/*.cmake
%{_libdir}/libenkiTS.so

%files examples
%license License.txt
%doc example/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11^git686d0ec-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

%autochangelog
