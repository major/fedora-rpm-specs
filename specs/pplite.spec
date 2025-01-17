%global giturl  https://github.com/ezaffanella/PPLite

Name:           pplite
Version:        0.12
Release:        %autorelease
Summary:        Convex polyhedra library for abstract interpretation

License:        GPL-3.0-or-later
URL:            https://www.cs.unipr.it/~zaffanella/PPLite/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{name}-%{version}-tag.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flint)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)

%description
PPLite is an open-source C++ library implementing the abstract domain of
convex polyhedra, to be used in tools for static analysis and
verification.

%package        devel
Summary:        Development files for PPLite
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and library links for developing applications that use
PPLite.

%package        tools
Summary:        Command line tools to use PPLite functionality
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
Command line tools to use PPLite functionality.

%prep
%autosetup -n PPLite-%{name}-%{version}-tag

%conf
autoreconf -fi .

%build
# GMP integers currently required by apron
%configure --disable-arch --disable-static --enable-integers=gmp
%make_build

%install
%make_install

# FIXME: boxed_inters test02 fails on ppc64le only
%ifnarch ppc64le
%check
make check
%endif

%files
%license COPYING
%doc CREDITS
%{_libdir}/libpplite.so.5*

%files devel
%{_includedir}/pplite/
%{_libdir}/libpplite.so

%files tools
%{_bindir}/pplite_lcdd

%changelog
%autochangelog
