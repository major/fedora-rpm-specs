%global         forgeurl https://github.com/minetest/minetestmapper
%global         tag      20250408
Version:        %{tag}

%forgemeta

Name:           minetestmapper
Release:        %autorelease
Summary:        Generates a overview image of a minetest map

License:        BSD-2-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(leveldb)
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libzstd)

# Wants minetest for ownership of /usr/share/minetest.
# But there's no reason it should *require* minetest.
Suggests:       minetest

%description
Generates a overview image of a minetest map. This is a port of
minetestmapper.py to C++, that is both faster and provides more
details than the deprecated Python script.

%prep
%forgesetup

%build
%cmake -DENABLE_LEVELDB=1 -DENABLE_REDIS=1 -DENABLE_POSTGRESQL=1
%cmake_build

%install
%cmake_install

# Install colors.txt into /usr/share/minetest.
mkdir -p %{buildroot}%{_datadir}/minetest
cp -a colors.txt %{buildroot}%{_datadir}/minetest/

# Remove copy of license from docdir.
rm -rf %{buildroot}%{_pkgdocdir}/COPYING

%files
%{_bindir}/minetestmapper
%{_datadir}/luanti/
%{_datadir}/minetest/
%{_mandir}/man6/minetestmapper.6*
%license COPYING
%doc AUTHORS README.rst

%autochangelog
