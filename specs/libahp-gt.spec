# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global gittag v1.7.2
#%%global commit 5c8e8ee43ccea13d69b232abd741b653c40c331c
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global date 20230904

Name:           libahp-gt
Version:        1.7.2
Release:        %autorelease
Summary:        Driver library for the AHP GT Controllers
License:        MIT
URL:            https://github.com/ahp-electronics/%{name}
%if "%{?gittag}"
Source0:        %{url}/archive/%{gittag}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros

Requires:       systemd-udev

%description
Driver library for the AHP GT Controllers.


%package devel
Summary:        Development files %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
These are the header files needed to develop a
%{name} application


%package doc
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

Provides:       bundled(js-jquery)

%description doc
Documentation of the AHP GT Controllers API.


%prep
%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

# Fix cmake module installation directory
sed -i 's#cmake-${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}/Modules#cmake/Modules#g' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_pkgdocdir}
cp -r %_vpath_builddir/docs %{buildroot}%{_pkgdocdir}


%files
%license LICENSE
%doc CITATION.cff
%{_libdir}/libahp_gt.so.1*
%{_udevrulesdir}/99-libahp-gt.rules

%files devel
%dir %{_includedir}/ahp
%{_includedir}/ahp/ahp_gt.h
%{_libdir}/libahp_gt.so
%{_datadir}/cmake/Modules/FindAHPGT.cmake

%files doc
%doc %{_pkgdocdir}/docs


%changelog
%autochangelog
