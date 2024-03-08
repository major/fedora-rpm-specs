# Header-only package, but not noarch per guidelines
%global debug_package %{nil}

Name:           pybind11-json
Version:        0.2.13
Release:        1%{?dist}
Summary:        Using nlohmann::json with pybind11

License:        BSD
URL:            https://github.com/pybind/pybind11_json
Source0:        https://github.com/pybind/pybind11_json/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  pybind11-devel
BuildRequires:  python%{python3_pkgversion}-devel

%description
pybind11_json is an nlohmann::json to pybind11 bridge, it allows you to
automatically convert nlohmann::json to py::object and the other way around.
Simply include the header, and the automatic conversion will be enabled.


%package devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       json-devel
Requires:       pybind11-devel
Provides:       %{name}-static = %{version}-%{release}

%description devel
pybind11_json is an nlohmann::json to pybind11 bridge, it allows you to
automatically convert nlohmann::json to py::object and the other way around.
Simply include the header, and the automatic conversion will be enabled.


%prep
%autosetup -p1 -n pybind11_json-%{version}


%build
%cmake \
  -DBUILD_TESTS=ON
%cmake_build


%install
%cmake_install


%check
%cmake_build -t tests


%files devel
%license LICENSE
%doc README.md
%{_includedir}/pybind11_json/
%{_datadir}/cmake/pybind11_json/


%changelog
* Wed Mar 06 2024 Scott K Logan <logans@cottsay.net> - 0.2.13-1
- Update to 0.2.13

* Thu May 19 2022 Scott K Logan <logans@cottsay.net> - 0.2.12-1
- Initial package
