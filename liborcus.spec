%global apiversion 0.18

%if 0%{?rhel}

# build conversion tools
%bcond_with convtools
# build python3 bindings
%bcond_with python

%else
# build conversion tools
%bcond_without convtools
# build python3 bindings
%bcond_without python

%endif

Name: liborcus
Version: 0.19.2
Release: %autorelease
Summary: Standalone file import filter library for spreadsheet documents

License: MPL-2.0
URL: https://gitlab.com/orcus/orcus
Source0: https://kohei.us/files/orcus/src/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: automake
%if %{with convtools}
BuildRequires: help2man
BuildRequires: pkgconfig(libixion-0.18)
%endif
BuildRequires: pkgconfig(mdds-2.1)
%if %{with python}
BuildRequires: pkgconfig(python3)
%if 0%{?rhel}
BuildRequires: python3
%endif
%endif
BuildRequires: pkgconfig(zlib)

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%if %{with convtools}
%package model
Summary: Spreadsheet model for %{name} conversion tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description model
The %{name}-model package contains a spreadsheet model used by the
conversion tools.
%endif

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tools for working with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Helper tools for %{name} and converters of various file formats to HTML
and text.

%if %{with python}
%package python3
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description python3
Python 3 bindings for %{name}.
%endif

%package doc
Summary: API documentation for %{name}
BuildArch: noarch

%description doc
API documentation for %{name}.

%prep
%autosetup -p1

%if %{without convtools}
%global condopts %{?condopts} --disable-spreadsheet-model
%endif
%if %{without python}
%global condopts %{?condopts} --disable-python
%endif

%build
autoreconf
%configure --disable-debug --disable-silent-rules --disable-static \
    --disable-werror --with-pic %{?condopts}
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{python3_sitearch}/*.la

%if %{with convtools}
# create and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -S '%{name} %{version}' -n 'convert a CSV file' -o orcus-csv.1 %{buildroot}%{_bindir}/orcus-csv
help2man -N -S '%{name} %{version}' -n 'convert a Gnumeric file' -o orcus-gnumeric.1 %{buildroot}%{_bindir}/orcus-gnumeric
help2man -N -S '%{name} %{version}' -n 'convert an ODF spreadsheet' -o orcus-ods.1 %{buildroot}%{_bindir}/orcus-ods
help2man -N -S '%{name} %{version}' -n 'transform an XML file' -o orcus-xls-xml.1 %{buildroot}%{_bindir}/orcus-xls-xml
help2man -N -S '%{name} %{version}' -n 'convert a OpenXML spreadsheet' -o orcus-xlsx.1 %{buildroot}%{_bindir}/orcus-xlsx
help2man -N -S '%{name} %{version}' -n 'convert an XML file' -o orcus-xml.1 %{buildroot}%{_bindir}/orcus-xml
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -p -m 0644 orcus-*.1 %{buildroot}/%{_mandir}/man1
%endif

# build documentation
make doc-doxygen

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check %{?_smp_mflags}

%ldconfig_scriptlets

%if %{with convtools}
%ldconfig_scriptlets model
%endif

%files
%doc AUTHORS CHANGELOG
%license LICENSE
%{_libdir}/%{name}-%{apiversion}.so.*
%{_libdir}/%{name}-mso-%{apiversion}.so.*
%{_libdir}/%{name}-parser-%{apiversion}.so.*

%if %{with convtools}
%files model
%{_libdir}/%{name}-spreadsheet-model-%{apiversion}.so.*
%endif

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/%{name}-mso-%{apiversion}.so
%{_libdir}/%{name}-parser-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc
%if %{with convtools}
%{_libdir}/%{name}-spreadsheet-model-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-spreadsheet-model-%{apiversion}.pc
%endif

%files tools
%{_bindir}/orcus-css-dump
%{_bindir}/orcus-detect
%{_bindir}/orcus-json
%{_bindir}/orcus-mso-encryption
%{_bindir}/orcus-zip-dump
%{_bindir}/orcus-yaml
%if %{with convtools}
%{_bindir}/orcus-csv
%{_bindir}/orcus-gnumeric
%{_bindir}/orcus-ods
%{_bindir}/orcus-styles-ods
%{_bindir}/orcus-xls-xml
%{_bindir}/orcus-xlsx
%{_bindir}/orcus-xml
%{_mandir}/man1/orcus-csv.1*
%{_mandir}/man1/orcus-gnumeric.1*
%{_mandir}/man1/orcus-ods.1*
%{_mandir}/man1/orcus-xls-xml.1*
%{_mandir}/man1/orcus-xlsx.1*
%{_mandir}/man1/orcus-xml.1*
%endif

%if %{with python}
%files python3
%{python3_sitearch}/_orcus.so
%{python3_sitearch}/_orcus_json.so
%{python3_sitelib}/orcus
%endif

%files doc
%license LICENSE
%doc doc/_doxygen/html

%changelog
%autochangelog
