%global catch_version 2.13.10
%global libosmium_version 2.17.0
%global protozero_version 1.6.3
%global json_version 3.0

Name:           osmium-tool
Version:        1.17.0
Release:        %autorelease
Summary:        Command line tool for working with OpenStreetMap data

License:        GPL-3.0-only
URL:            http://osmcode.org/osmium-tool/
Source0:        https://github.com/osmcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable tests which break on big endian architectures
# https://github.com/osmcode/osmium-tool/issues/176
Patch:          osmium-tool-bigendian.patch
# Patch test results for zlib-ng
# https://github.com/osmcode/osmium-tool/issues/274
Patch:          osmium-tool-zlibng.patch

BuildRequires:  cmake make gcc-c++ pandoc man-db git-core

BuildRequires:  catch2-devel >= %{catch_version}
BuildRequires:  libosmium-devel >= %{libosmium_version}
BuildRequires:  libosmium-static >= %{libosmium_version}
BuildRequires:  protozero-devel >= %{protozero_version}
BuildRequires:  protozero-static >= %{protozero_version}
BuildRequires:  json-devel >= %{json_version}
BuildRequires:  json-static >= %{json_version}

%description
Command line tool for working with OpenStreetMap data
based on the Osmium library


%prep
%autosetup -S git
sed -i -e "s/-O3 -g//" CMakeLists.txt
rm -rf include/rapidjson test/include/catch.hpp
ln -sf /usr/include/catch2/catch.hpp test/include


%build
%cmake
%cmake_build


%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
install -p -m644 zsh_completion/* %{buildroot}%{_datadir}/zsh/site-functions


%check
%ctest


%files
%doc README.md CHANGELOG.md
%license LICENSE.txt
%{_bindir}/osmium
%{_mandir}/man1/osmium*.1.gz
%{_mandir}/man5/osmium*.5.gz
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_osmium


%changelog
%autochangelog
