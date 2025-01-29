# Build -pythonN subpackage
%bcond_without python

#
Name:           opentrep
Version:        0.07.17
Release:        %autorelease

Summary:        C++ library providing a clean API for parsing travel-focused requests

# The entire source code is LGPLv2+ except opentrep/basic/float_utils_google.hpp,
# which is BSD
License:        LGPL-2.1-or-later
URL:            https://github.com/trep/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(readline)
BuildRequires:  mysql-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  xapian-core-devel
BuildRequires:  mysql-devel
BuildRequires:  sqlite-devel
BuildRequires:  libicu-devel
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-compiler

%description
%{name} aims at providing a clean API, and the corresponding C++
implementation, for parsing travel-focused requests.
It powers the https://transport-search.org Web site.

%{name} uses Xapian (https://www.xapian.org) for the Information Retrieval
part, on freely available travel-related data (e.g., country names and codes,
city names and codes, airline names and codes, etc.), mainly to be found in
the OpenTravelData project (https://github.com/opentraveldata/opentraveldata).

The data files are available from https://transport-search.org/data/optd/por/

%{name} exposes a simple, clean and object-oriented, API. For instance,
the OPENTREP::interpretTravelRequest() method takes, as input, a string
containing the travel request, and yields, as output, the list of the
recognized terms as well as their corresponding types.
As an example, the travel request
'Washington DC Beijing Monday a/r +AA -UA 1 week 2 adults 1 dog' would give
the following list:
 * Origin airport: Washington, DC, USA
 * Destination airport: Beijing, China
 * Date of travel: next Monday
 * Date of return: 1 week after next Monday
 * Preferred airline: American Airlines; non-preferred airline: United Airlines
 * Number of travelers: 2 adults and a dog

The output can then be used by other systems, for instance to book the
corresponding travel or to visualize it on a map and calendar and to
share it with others.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) and
SOCI (https://github.com/SOCI) libraries are used.

Note that %{name} currently only recognizes points of reference (POR),
as to be found in the following file: https://bit.ly/3fQaddv
A good complementary tool is GeoBase
(https://opentraveldata.github.io/geobases), a Python-based software
able to access to any travel-related data source.

%package        devel
Summary:        Header files, libraries and development helper tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, shared libraries and
development helper tools for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%if %{with python}

%package    -n python3-%{name}
Summary:    Python bindings for %{name}
Group:      System Environment/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  boost-python3-devel
%{?python_provide:%python_provide python3-%{name}}


%description -n python3-%{name}
This package contains Python libraries for %{name}

%endif

%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
BuildRequires:  tex(latex), tex(sectsty.sty), tex(tocloft.sty), tex(xtab.sty)
BuildRequires:  texlive-epstopdf
BuildRequires:  doxygen
BuildRequires:  ghostscript

%description    doc
This package contains HTML pages for %{name}. All that documentation
is generated thanks to Doxygen (https://doxygen.org). The content is
the same as what can be browsed online (https://opentrep.sourceforge.net).
Note that the PDF form of the reference manual is mainly available online
(https://opentrep.sourceforge.net/refman.pdf), as the one present in that
package is usually corrupted: it depends on the building conditions,
and it is therefore not reliable.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

# Remove the Doxygen installer
rm -f %{buildroot}%{_docdir}/%{name}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%if %{with python}
# (Pure) Python OpenTREP executable
chmod a-x %{buildroot}%{python3_sitearch}/py%{name}/Travel_pb2.py
%endif


#check
#ctest

%if %{with python}
%post -n python3-%{name}
ln -s -f %{python3_sitearch}/py%{name}/py%{name} %{_bindir}/py%{name}

%postun -n python3-%{name}
rm -f %{_bindir}/py%{name}
%endif

%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%{_bindir}/%{name}-indexer
%{_bindir}/%{name}-searcher
%{_bindir}/%{name}-dbmgr
%{_libdir}/lib%{name}.so.0.*
%{_mandir}/man1/%{name}-indexer.1.*
%{_mandir}/man1/%{name}-searcher.1.*
%{_mandir}/man1/%{name}-dbmgr.1.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%dir %{_datadir}/%{name}/data/por
%{_datadir}/%{name}/data/por/README.md
%{_datadir}/%{name}/data/por/create_trep_user_and_db.sql
%{_datadir}/%{name}/data/por/create_trep_tables_sqlite3.sql
%{_datadir}/%{name}/data/por/create_trep_tables_mysql.sql
%{_datadir}/%{name}/data/por/test_optd_por_public.csv
%{_datadir}/%{name}/data/por/test_optd_por_public_schema.sql
%{_datadir}/%{name}/data/por/test_world_schedule.csv

%files devel
%{_includedir}/%{name}/
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/%{name}/CMake/
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{_docdir}/%{name}/
%license COPYING

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/py%{name}/
%{_mandir}/man1/py%{name}.1.*
%endif

%changelog
%autochangelog

