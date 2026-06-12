# There have been many bugfixes since the 1.3.0 release
%global commit  111c9be5188f7350c2eac9ddaedd8cca3d7bf394
%global date    20210117
%global forgeurl https://github.com/kazuho/picojson

Name:           picojson
Summary:        A header-file-only, JSON parser / serializer in C++
Version:        1.3.0

%forgemeta

Release:        %autorelease
License:        BSD-2-Clause
URL:            %{forgeurl}
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  make

%global desc %{expand:
PicoJSON is a tiny JSON parser / serializer for C++ with following properties:
Header-file only, No external dependencies (only uses standard C++ libraries),
STL-friendly (arrays are represented by using std::vector, objects are std::map)
provides both pull interface and streaming (event-based) interface.}

%description
%desc

%package devel
Summary:        Header files for picojson development
Provides:       %{name}-static = %{version}-%{release}

%description devel
%desc

%prep
%forgeautosetup

%build
# Nothing to build, header-only library

%check
%make_build test

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 0644 picojson.h %{buildroot}%{_includedir}/picojson.h

%files devel
%{_includedir}/picojson.h
%doc README.mkdn examples
%license LICENSE

%changelog
%autochangelog
