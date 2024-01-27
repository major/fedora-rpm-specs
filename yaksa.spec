%bcond tests 1

Name:           yaksa
Version:        0.3
Release:        %autorelease
Summary:        High-performance library for noncontiguous data

%global forgeurl https://github.com/pmodels/yaksa/
%forgemeta

%global soversion 0

License:        BSD-3-Clause
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3
BuildRequires:  uthash-devel

%description
Yaksa is a high-performance noncontiguous datatype engine that can be used to
express and manipulate noncontiguous data. The library sports features related
to packing/unpacking, I/O vectors, and flattening noncontiguous datatypes.

%package devel
Summary:        Development files for libyaksa
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

# Poor man's unbundling: uthash is a header-only library, so we can
# effectively replace the local version with the system copy by symlinking.
ln -fvs /usr/include/uthash.h src/external/yuthash.h
ln -fvs /usr/include/utlist.h src/external/yutlist.h

%build
./autogen.sh
%configure \
    --disable-static
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/libyaksa.la

%if %{with tests}
%check
timeout -v 2h make -j%{_smp_build_ncpus} testing
%endif

%files
%license COPYRIGHT
%doc README.md
%{_libdir}/libyaksa.so.%{soversion}{,.*}

%files devel
%{_includedir}/yaksa.h
%{_libdir}/libyaksa.so
%{_libdir}/pkgconfig/yaksa.pc

%changelog
%autochangelog
