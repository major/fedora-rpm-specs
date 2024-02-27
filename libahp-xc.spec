%global gittag v1.4.1
#%%global commit dad5c01d83ca8cf9c8d5ab14ad7593d51ce290f3
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#%%global date 20230904

Name:           libahp-xc
%if "%{?gittag}"
Version:        1.4.1
%else
Version:        1.3.5^%{date}.%{shortcommit}
%endif
Release:        %autorelease
Summary:        Driver library for the AHP XC Correlators
License:        GPL-3.0-or-later
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
Driver library for the AHP XC Correlators.


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
Documentation of the AHP XC Correlators API.


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
%license LICENSE.md
%doc CITATION.cff README.md
%{_libdir}/libahp_xc.so.1*
%{_udevrulesdir}/99-libahp-xc.rules

%files devel
%dir %{_includedir}/ahp
%{_includedir}/ahp/ahp_xc.h
%{_libdir}/libahp_xc.so
%{_datadir}/cmake/Modules/FindAHPXC.cmake

%files doc
%doc %{_pkgdocdir}/docs


%changelog
%autochangelog
