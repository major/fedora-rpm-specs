Name:           libxls
Version:        1.6.3
Release:        %autorelease
Summary:        Read binary Excel files from C/C++

License:        BSD-2-Clause
URL:            https://github.com/libxls/libxls
Source0:        https://github.com/libxls/libxls/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
This is libxls, a C library for reading Excel files in the old binary OLE
format, plus a command-line tool for converting XLS to CSV (named,
appropriately enough, libxls2csv).


%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}


%prep
%autosetup -p1


%build
# Add prefix to not conflict executables with catdoc.
%configure --program-prefix=lib
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete


%check
PATH=%{buildroot}%{_bindir}:$PATH LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
    make check || ( cat ./test-suite.log && exit 1 )


%files
%doc README.md AUTHORS
%license LICENSE
%{_bindir}/libxls2csv
%{_libdir}/libxlsreader.so.8
%{_libdir}/libxlsreader.so.8.*
%{_mandir}/man1/libxls2csv.1*

%files devel
%{_includedir}/xls.h
%{_includedir}/libxls
%{_libdir}/libxlsreader.so
%{_libdir}/pkgconfig/libxls.pc


%changelog
%autochangelog
