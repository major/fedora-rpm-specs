%global debug_package %{nil}

Name:           polylabel
Version:        2.0.1
Release:        3%{?dist}
Summary:        A fast algorithm for finding the pole of inaccessibility of a polygon

License:        ISC
URL:            https://github.com/mapbox/polylabel/
Source0:        https://github.com/mapbox/polylabel/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable mason dependency handling
Patch:          polylabel-mason.patch

BuildRequires:  make gcc-c++
BuildRequires:  geometry-hpp-devel geometry-hpp-static
BuildRequires:  rapidjson-devel rapidjson-static

Requires:       geometry-hpp-devel

%description
A fast algorithm for finding polygon pole of inaccessibility, the most
distant internal point from the polygon outline.

Useful for optimal placement of a text label on a polygon.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
A fast algorithm for finding polygon pole of inaccessibility, the most
distant internal point from the polygon outline.

Useful for optimal placement of a text label on a polygon.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}


%check
%make_build test


%files devel
%license LICENSE
%doc README.md
%{_includedir}/mapbox


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

%autochangelog
