Name:           pplite
Version:        0.11
Release:        %autorelease
Summary:        Convex polyhedra library for abstract interpretation

License:        GPL-3.0-or-later
URL:            https://www.cs.unipr.it/~zaffanella/PPLite/
Source0:        https://github.com/ezaffanella/PPLite/raw/main/releases/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  make

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
%autosetup

%build
%configure --disable-arch --disable-static
%make_build

%install
%make_install

%check
make tests

%files
%license COPYING
%doc CREDITS
%{_libdir}/libpplite.so.4*

%files devel
%{_includedir}/pplite/
%{_libdir}/libpplite.so

%files tools
%{_bindir}/pplite_lcdd

%changelog
%autochangelog
