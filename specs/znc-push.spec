%global forgeurl https://github.com/jreese/znc-push
%global commit  e4250e688b4b45a886928c7e2cdb59747304747d
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}
%forgemeta

%global modname push
%global znc_version %((znc -v 2>/dev/null || echo 'a 0') | head -1 | awk '{print $2}')

Name:           znc-%{modname}
Version:        2.0.0
Release:        %autorelease
Summary:        Push notification service module for ZNC

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  libcurl-devel
BuildRequires:  znc-devel
BuildRequires:  zlib-devel

Requires:       znc%{?_isa} = %znc_version

%description
ZNC Push is a module for ZNC that will send notifications to multiple push
notification services, or SMS for any private message or channel highlight
that matches a configurable set of conditions.

%prep
%forgesetup
# fix README permissions
chmod -x README.md

%build
CXXFLAGS="%{optflags} -DUSE_CURL $(pkg-config --libs libcurl) -DPUSHVERSION=\\\"%{shortcommit}\\\"" \
LDFLAGS="%{__global_ldflags}" \
  znc-buildmod %{modname}.cpp

%install
install -Dpm0755 %{modname}.so %{buildroot}%{_libdir}/znc/%{modname}.so

%files
%license LICENSE
%doc README.md logo.png doc
%{_libdir}/znc/%{modname}.so

%changelog
%autochangelog
