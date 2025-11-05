# header-only library
%global debug_package %{nil}

Name:           inja
Version:        3.5.0
Release:        1%{?dist}
Summary:        Jinja-inspired template engine for modern C++

License:        MIT
URL:            https://pantor.github.io/inja/
Source:         https://github.com/pantor/inja/archive/v%{version}/%{name}-%{version}.tar.gz

# From: https://github.com/pantor/inja/pull/317
Patch0001:      0001-cmake-Use-GNUInstallDirs-for-install-paths-and-insta.patch

BuildRequires:  cmake
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  gcc-c++

%description
Inja is a template engine for modern C++, loosely inspired by jinja for Python.
It has an easy and yet powerful template syntax with all variables, loops, conditions,
includes, callbacks, and comments you need, nested and combined as you like.


%package        devel
Summary:        Development files for %{name}

%description    devel
Inja is a template engine for modern C++, loosely inspired by jinja for Python.
It has an easy and yet powerful template syntax with all variables, loops, conditions,
includes, callbacks, and comments you need, nested and combined as you like.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%conf
%cmake -DINJA_USE_EMBEDDED_JSON=OFF


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc


%changelog
* Mon Nov 03 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.5.0-1
- Initial package
