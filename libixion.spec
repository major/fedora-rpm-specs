%global apiversion 0.18

Name: libixion
Version: 0.19.0
Release: %autorelease
Summary: A general purpose formula parser & interpreter library

License: MPL-2.0
URL: https://gitlab.com/ixion/ixion
Source0: https://kohei.us/files/ixion/src/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: automake
BuildRequires: pkgconfig(mdds-2.1)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(spdlog)
BuildRequires: make

%description
Ixion is a general purpose formula parser & interpreter that can calculate
multiple named targets, or "cells".

The goal of this project is to create a library for calculating the results of
formula expressions stored in multiple named targets, or “cells”. The cells can
be referenced from each other, and the library takes care of resolving their
dependencies automatically upon calculation. The caller can run the calculation
routine either in a single-threaded mode, or a multi-threaded mode. The library
also supports re-calculations where the contents of one or more cells have been
modified since the last calculation, and a partial calculation of only the
affected cells need to be calculated.

Supported features:
- Each calculation session is defined in a plain text file, which is parsed and
  interpreted by the Ixion parser.
- Fully threaded calculation.
- Name resolution using A1-style references.
- Support 2D cell references and named expressions.
- Support range references.
- Dependency tracking during both full calculation and partial re-calculation.
- Inline strings.
- Volatile functions. The framework for volatile functions is implemented. We
  just need to implement more functions.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Testing tools for libixion
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Testing tools for %{name}.

%package python3
Summary: Python 3 bindings for libixion
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < 0.9.1-1
Suggests: %{name}-doc = %{version}-%{release}

%description python3
Python 3 bindings for %{name}.

%package doc
Summary: API documentation for %{name}
BuildArch: noarch

%description doc
API documentation for %{name}.

%prep
%autosetup -p1

%build
autoreconf
%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{python3_sitearch}/*.la

# create and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -S '%{name} %{version}' -N -n 'formula tokenizer' -o ixion-formula-tokenizer.1 ./src/ixion-formula-tokenizer
help2man -S '%{name} %{version}' -N -n 'parser' -o ixion-parser.1 ./src/ixion-parser
help2man -S '%{name} %{version}' -N -n 'sorter' -o ixion-sorter.1 ./src/ixion-sorter
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 ixion-*.1 %{buildroot}/%{_mandir}/man1

# generate docs
# make doc

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%ifnarch %{ix86}
make %{?_smp_mflags} check
%endif

%files
%doc AUTHORS
%license LICENSE
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files tools
%{_bindir}/ixion-formula-tokenizer
%{_bindir}/ixion-parser
%{_bindir}/ixion-sorter
%{_mandir}/man1/ixion-formula-tokenizer.1*
%{_mandir}/man1/ixion-parser.1*
%{_mandir}/man1/ixion-sorter.1*

%files python3
%{python3_sitearch}/ixion.so

%files doc
%license LICENSE
%doc doc/python

%changelog
%autochangelog
