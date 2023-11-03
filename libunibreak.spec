%global forgeurl https://github.com/adah1972/libunibreak

Name:           libunibreak
Version:        5.1
Release:        %autorelease -n
Summary:        A Unicode line-breaking library
# Upstream uses tags of the form `libunibreak_X_Y`
%global tag %{name}_%{lua: v = string.gsub(rpm.expand('%{version}'), '%.', '_'); print(v) }
%forgemeta
# SPDX identifier
License:        Zlib
URL:            %forgeurl
Source0:        %forgesource
# test files
Source1:        LineBreakTest.txt
Source2:        WordBreakTest.txt
Source3:        GraphemeBreakTest.txt

# don't download test data
Patch:          offline_files.patch
# update list of broken tests
Patch:          disable_broken_tests.patch
# remove unused var and other build fixes
Patch:          remove_unused_var.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake, autoconf, libtool

%description
Libunibreak is an implementation of the line breaking and word
breaking algorithms as described in Unicode Standard Annex 14 and
Unicode Standard Annex 29. It is designed to be used in a generic text
renderer.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgeautosetup -p1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} src/
sed -r -i 's|^(#!/usr/bin/)env (python)|\1\23|' src/generate_linebreakdata.py
sed -r -i 's|^(#!/usr/bin/)env (python)|\1\23|' src/sort_numeric_hex.py


%build
./autogen.sh
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
%make_build check

%ldconfig_scriptlets


%files
%doc AUTHORS NEWS README.md
%license LICENCE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
