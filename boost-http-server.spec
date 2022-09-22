%global forgeurl https://github.com/SRombauts/BoostHttpServer
%global commit cd5245f068833f3b0b7907b5cb1fd1ec39f7f29b
%forgemeta

%global _description %{expand:
This is a simple C++ embeddable web server build from the Boost.Asio
multithreaded HTTP 1.0 Server Example.}

Name:           boost-http-server
Version:        0
Release:        %autorelease
Summary:        Improvements on top of the Boost Asio HTTP server example

License:        Boost
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  boost-devel
BuildRequires:  CTML-devel

%description    %{_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{_description}

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       js-jquery

%description    doc
This package contains documentation for %{name}.

%prep
%forgesetup

# Fix CTML include to point to the system one
sed -i 's:"../../CTML/include/ctml.hpp":<CTML/ctml.hpp>:' src/example2_dynamic/main.cpp
# Remove bundled copy of jquery
rm docs/jquery.js

%build
mkdir Debug
%set_build_flags
%make_build LINK_FLAGS="%{build_ldflags}"
doxygen docs
ln -sf %{_datadir}/javascript/jquery/latest/jquery.js html/jquery.js

%install
install -Dpm0755 Debug/example1_static %{buildroot}%{_bindir}/http_server_static
install -Dpm0755 Debug/example2_dynamic %{buildroot}%{_bindir}/http_server_dynamic
install -Dpm0644 -t %{buildroot}%{_includedir}/%{name} src/server/*

%files
%license LICENSE_1_0.txt
%doc README.md
%{_bindir}/*

%files devel
%license LICENSE_1_0.txt
%doc README.md
%{_includedir}/%{name}

%files doc
%license LICENSE_1_0.txt
%doc html

%changelog
%autochangelog
