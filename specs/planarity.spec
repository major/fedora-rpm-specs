Name:		planarity
Summary:	Implementations of several planarity-related graph algorithms
Version:	4.0.0.0
Release:	%autorelease
License:	BSD-3-Clause
URL:		https://github.com/graph-algorithms/edge-addition-planarity-suite
VCS:		git:%{url}.git
Source:		%{url}/archive/Version_%{version}/%{name}-%{version}.tar.gz

%global _docdir_fmt %{name}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	libtool

%description
This code project provides a library for implementing graph algorithms
as well as implementations of several planarity-related graph algorithms.
The origin of this project is the reference implementation for the Edge
Addition Planarity Algorithm, which is now the fastest and simplest
linear-time method for planar graph embedding and planarity obstruction
isolation (i.e. Kuratowski subgraph isolation).

The software in this code project provides a graph algorithm framework and
library, including an updated version of the edge addition combinatorial
planar graph embedder and planar obstruction isolator (i.e., a Kuratowski
subgraph isolator). This code project also includes several extensions
that implement planarity-related algorithms such as a planar graph drawing
algorithm, an outerplanar graph embedder and outerplanar obstruction
isolator, and a number of subgraph homeomorphism search algorithms.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%package	samples
Summary:	Sample files for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	samples
This package contains sample files for planarity.  For example:

planarity -test /usr/share/doc/planarity/samples

%prep
%autosetup -p1 -n edge-addition-%{name}-suite-Version_%{version}

%conf
# Generate the configure script
autoreconf -fi .

%build
%configure --enable-static=false

# Eliminate hardcoded rpaths, and workaround libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool

%make_build

%install
%make_install

# We package the samples below
rm -rf %{buildroot}%{_docdir}

%check
make check

%files
%license LICENSE.TXT
%doc README.md
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.2*

%files		devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libplanarity.pc

%files		samples
%doc c/samples/

%changelog
%autochangelog
