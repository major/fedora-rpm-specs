Name:           pmix
Version:        6.1.0
Release:        %autorelease
Summary:        Process Management Interface Exascale (PMIx)
License:        BSD-3-Clause
URL:            https://pmix.org/
Source0:        https://github.com/openpmix/openpmix/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  hwloc-devel
BuildRequires:  libevent-devel
BuildRequires:  make
BuildRequires:  munge-devel
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel

ExcludeArch:    %{ix86}

%description
The Process Management Interface (PMI) has been used for quite some time as
a means of exchanging wireup information needed for interprocess
communication. Two versions (PMI-1 and PMI-2) have been released as part of
the MPICH effort. While PMI-2 demonstrates better scaling properties than its
PMI-1 predecessor, attaining rapid launch and wireup of the roughly 1M
processes executing across 100k nodes expected for exascale operations remains
challenging.

PMI Exascale (PMIx) represents an attempt to resolve these questions by
providing an extended version of the PMI standard specifically designed to
support clusters up to and including exascale sizes. The overall objective of
the project is not to branch the existing pseudo-standard definitions - in
fact, PMIx fully supports both of the existing PMI-1 and PMI-2 APIs - but
rather to (a) augment and extend those APIs to eliminate some current
restrictions that impact scalability, and (b) provide a reference
implementation of the PMI-server that demonstrates the desired level of
scalability.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
The %{name}-tools package contains for use with PMIx-based RMs and language-
based starters (e.g., mpirun).

* pinfo - show MCA params, build info, etc.
* pps - get list of active nspaces, retrieve status of jobs/nodes/procs
* pevent - inject an event into the system

%prep
%autosetup -p1

# touch lexer sources to recompile them
find src -name \*.l -print -exec touch --no-create {} \;

%build
export CFLAGS="%{build_cflags} -Wno-unused-function -Wno-attributes"
%configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --disable-static \
    --disable-silent-rules \
    --enable-wrapper-rpath=no \
    --enable-wrapper-runpath=no \
    --enable-ipv6 \
    --enable-shared \
    --with-munge

%make_build

%check
%make_build check

%install
%make_install

# remove libtool archives
find %{buildroot} -name '*.la' | xargs rm -f

%ldconfig_scriptlets
%ldconfig_scriptlets devel

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%{_datadir}/%{name}/*.txt
%{_libdir}/libpmix.so.2*
%{_libdir}/%{name}/*.so
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files devel
%{_datadir}/%{name}/*.supp
%{_includedir}/pmix*.h
%{_includedir}/pmix/
%{_libdir}/libpmix.so
%{_libdir}/pkgconfig/*.pc
%{_docdir}/%{name}/
%{_mandir}/man3/*.3*

%files tools
%{_bindir}/*

%changelog
%autochangelog
