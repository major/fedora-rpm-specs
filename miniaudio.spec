%global commit 9a7663496fc06f7a9439c752fd7666ca93328c20
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           miniaudio
Version:        0.11.14
Release:        1%{?dist}
Summary:        Audio playback and capture library

License:        MIT-0
URL:            https://miniaud.io/
Source0:        https://github.com/mackron/miniaudio/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

%package devel
Summary: %summary
Provides:       miniaudio-static = %{version}-%{release}
BuildArch:      noarch

%description
%summary

%description devel
%summary

%prep
%autosetup -n %{name}-%{commit}


%build


%check
# The package does include tests but they are interactive so we cannot use them


%install
mkdir -p %{buildroot}%{_includedir}
install -p %{name}.h %{buildroot}%{_includedir}/


%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.h


%changelog
* Tue Apr 04 2023 Jonathan <jonathan@knownhost.com> - 0.11.14
- Initial package build
