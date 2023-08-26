%global date 20161009
%global commit 6601b32feacecd18bc12f0a4c23a063c3545a095
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gogextract
Version:        0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Script for unpacking GOG Linux installers

License:        MIT
URL:            https://github.com/Yepoleb/gogextract
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:      noarch

%description
This package provides a script for unpacking GOG Linux installers.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
# Nothing to build

%install
install -Dpm0755 %{name}.py %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
