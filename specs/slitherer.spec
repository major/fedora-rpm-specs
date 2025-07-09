%global qt_minver 6.8

%global commit 1e00f77b60a3af67b0b459e5b619c4373ae48af2
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20250617


Name:           slitherer
Version:        0~git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        Simple QtWebView based runner for Anaconda installer Web UI

License:        MPL-2.0 and BSD-3-Clause
URL:            https://gitlab.com/VelocityLimitless/Projects/slitherer
Source:         %{url}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Make slitherer operate in fullscreen mode
## TODO: Get done upstream in a configurable fashion
Patch:          slitherer-fullscreen-window.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  cmake(Qt6Core) >= %{qt_minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt_minver}
BuildRequires:  cmake(Qt6Qml) >= %{qt_minver}
BuildRequires:  cmake(Qt6Quick) >= %{qt_minver}
BuildRequires:  cmake(Qt6WebView) >= %{qt_minver}

Requires:       anaconda-webui
# Only Fedora Workstation doesn't want this by default
Supplements:    (anaconda-webui unless fedora-release-workstation)

%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit} -S git_am


%conf
%cmake_qt6


%build
%cmake_build


%install
%cmake_install


# Anaconda launcher executable
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-anaconda



%files
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}*


%changelog
* Tue Jun 17 2025 Neal Gompa <ngompa@fedoraproject.org> - 0~git20250617.1e00f77b-1
- Initial package

