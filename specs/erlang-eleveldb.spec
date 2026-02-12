%global realname eleveldb


Name:		erlang-%{realname}
Version:	3.0.12
Epoch:		1
Release:	%autorelease
Summary:	Erlang LevelDB API
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		scm:git:%{url}.git
Source0:	%{url}/archive/riak_kv-%{version}/%{realname}-%{version}.tar.gz
Source1:	https://github.com/basho/leveldb/archive/2.0.38/basho-leveldb-2.0.38.tar.gz
# Fedora/EPEL-specific
Patch1:		erlang-eleveldb-0001-Use-system-wide-snappy.patch
Patch2:		erlang-eleveldb-0002-Don-t-treat-warnings-as-errors.patch
Patch3:		erlang-eleveldb-0003-Disable-eqc-rebar3-plugin-for-now.patch
Patch4:		erlang-eleveldb-0004-FIXME-temporarily-disable-plugins.patch
Patch101:	basho-leveldb-0001-Fix-least-byte-extraction.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-os_mon
#BuildRequires:	leveldb-devel
BuildRequires:	make
# Requires for using ps utility in tests
BuildRequires:	procps-ng
BuildRequires:	snappy-devel
# Remove when https://bugzilla.redhat.com/show_bug.cgi?id=1770256 is resolved
#ExcludeArch: s390x


%description
Erlang LevelDB API.


%prep
%setup -q -n %{realname}-riak_kv-%{version}
rm -f c_src/build_deps.sh
rm -f c_src/snappy-1.0.4.tar.gz
%patch -P1 -p1 -b .use_systemwide
%patch -P2 -p1 -b .no_warns_as_errors
%patch -P3 -p1 -b .disable_eqc
%patch -P4 -p1 -b .disable_plugins
tar xvf %{SOURCE1}
cd leveldb-2.0.38
%patch -P101 -p1 -b .fix_extraction
cd -


%build
# Building Basho's leveldb fork first
#cd leveldb-%{version}
cd leveldb-2.0.38
OPT="%{optflags}" make
cd -

%{erlang3_compile}

g++ c_src/eleveldb.cc $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include  -I leveldb-2.0.38/include -I leveldb-2.0.38 -o c_src/eleveldb.o
g++ c_src/refobjects.cc $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include  -I leveldb-2.0.38/include -I leveldb-2.0.38 -o c_src/refobjects.o
g++ c_src/workitems.cc $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include  -I leveldb-2.0.38/include -I leveldb-2.0.38 -o c_src/workitems.o
g++ c_src/eleveldb.o c_src/refobjects.o c_src/workitems.o $LDFLAGS -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} leveldb-2.0.38/libleveldb.a -lsnappy -shared -o priv/eleveldb.so


%install
%{erlang3_install}

install -p -m 0644 priv/eleveldb.schema %{buildroot}%{erlang_appdir}/priv
install -p -m 0644 priv/eleveldb_multi.schema %{buildroot}%{erlang_appdir}/priv


%check
%{erlang3_test}


%files
%doc README.md
%{erlang_appdir}/


%changelog
%autochangelog
