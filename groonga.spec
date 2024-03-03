Name:           groonga
Version:        13.1.0
Release:        %autorelease
Summary:        An Embeddable Fulltext Search Engine

License:        LGPL-2.1-only
URL:            https://groonga.org/
Source0:        https://github.com/groonga/groonga/releases/download/v%{version}/groonga-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

%ifnarch %{ix86}
BuildRequires:  libarrow-devel
%endif
BuildRequires:  zlib-devel
BuildRequires:  libzstd-devel
BuildRequires:  rapidjson-devel
BuildRequires:  mecab-devel
BuildRequires:  libstemmer-devel
BuildRequires:  zeromq-devel
BuildRequires:  libevent-devel
BuildRequires:  msgpack-devel
BuildRequires:  xxhash-devel
BuildRequires:  lz4-devel
BuildRequires:  croaring-devel
%if 0%{?fedora} >= 40
BuildRequires:  blosc2-devel
# required by blosc2-devel
BuildRequires:  zlib-ng-devel
%endif
BuildRequires:  ruby
BuildRequires:  libedit-devel
BuildRequires:  openssl-devel

BuildRequires:  systemd-rpm-macros

Requires:       %{name}-libs%{?isa} = %{version}-%{release}
Requires:       %{name}-plugin-suggest%{?isa} = %{version}-%{release}

Provides:       bundled(onigmo)

%description
Groonga is an embeddable full-text search engine library.  It can
integrate with DBMS and scripting languages to enhance their search
functionality.  It also provides a standalone data store server based
on relational data model.

%package        libs
Summary:        Runtime libraries for Groonga
License:        LGPL-2.1-only AND (MIT OR GPL-2.0-only)

%description    libs
This package contains the libraries for Groonga.

%package        devel
Summary:        Development files for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for Groonga.

%package        server-common
Summary:        Common files for the Groonga server and the Groonga HTTP server
License:        LGPL-2.1-only
Requires:       %{name}%{?isa} = %{version}-%{release}
Requires(pre):  shadow-utils

%description    server-common
This package provides common settings for server use.

%package        server-gqtp
Summary:        Groonga GQTP server
License:        LGPL-2.1-only
Requires:       %{name}-server-common%{?isa} = %{version}-%{release}
Requires(pre):  shadow-utils
Requires(post): systemd
Requires(preun):systemd

%description    server-gqtp
This package contains the Groonga GQTP server.

%package        server-http
Summary:        Groonga HTTP server
License:        LGPL-2.1-only AND BSD-3-Clause
Requires:       %{name}-server-common%{?isa} = %{version}-%{release}
Requires(pre):  shadow-utils
Requires(post): systemd
Requires(preun):systemd

%description    server-http
This package contains the Groonga HTTP server.

%package        plugin-tokenizer-mecab
Summary:        MeCab tokenizer for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}

%description    plugin-tokenizer-mecab
This package contains MeCab tokenizer for Groonga.

%package        plugin-suggest
Summary:        Suggest plugin for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}

%description    plugin-suggest
This package contains suggest plugin for Groonga.

%package        plugin-token-filters
Summary:        Token filters plugin for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}

%description    plugin-token-filters
Token filters plugins for Groonga, which provides stop word and stemming
features.

%package        munin-plugins
Summary:        Munin plugins for Groonga
Requires:       %{name}-libs%{?isa} = %{version}-%{release}
Requires:       munin-node
Requires(post): munin-node

%description    munin-plugins
This package contains munin plugins for Groonga.

%package        doc
Summary:        Documentation for Groonga
License:        LGPL-2.1-only AND BSD-3-Clause

%description doc
This package contains documentation for Groonga.

%package        examples
Summary:        Examples for Groonga
License:        LGPL-2.1-only
Requires:       %{name}%{?isa} = %{version}-%{release}

%description examples
This package contains the examples for Groonga.

%package        tools
Summary:        Tools for Groonga
License:        LGPL-2.1-only
Requires:       %{name}%{?isa} = %{version}-%{release}

%description tools
This package contains the tools for Groonga.

%prep
%autosetup -p1

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DGRN_FOR_RHEL=ON \
%ifarch riscv64
  -DCMAKE_SKIP_RPATH=TRUE \
%endif
%ifnarch %{ix86}
  -DGRN_WITH_APACHE_ARROW=ON \
%endif
  -DGRN_WITH_ZLIB=ON \
  -DGRN_WITH_ZSTD=ON \
  -DGRN_WITH_RAPIDJSON=ON \
  -DGRN_WITH_MECAB=ON \
  -DGRN_WITH_KYTEA=OFF \
  -DGRN_WITH_LIBSTEMMER=ON \
  -DGRN_WITH_ZEROMQ=ON \
  -DGRN_WITH_LIBEVENT=ON \
  -DGRN_WITH_MESSAGE_PACK=ON \
  -DGRN_WITH_XXHASH=ON \
  -DGRN_WITH_LZ4=ON \
  -DGRN_WITH_ROARING_BITMAPS=ON \
%if 0%{?fedora} >= 40
  -DGRN_WITH_BLOSC=ON \
%else
  -DGRN_WITH_BLOSC=OFF \
%endif
  -DGRN_WITH_MRUBY=ON \
  -DGRN_WITH_MUNIN_PLUGINS=ON \
  -DGRN_WITH_DOC=ON \
  -DGRN_WITH_EXAMPLES=ON \
  -DGRN_WITH_TOOLS=ON \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_localstatedir}/lib/groonga/db
mkdir -p %{buildroot}%{_localstatedir}/log/groonga
mkdir -p %{buildroot}%{_libdir}/groonga/plugins/normalizers

mkdir -p %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/
cat <<EOC > %{buildroot}%{_sysconfdir}/munin/plugin-conf.d/groonga
[groonga_*]
  user groonga
  group groonga
  env.PATH %{_bindir}
  env.database_path %{_localstatedir}/lib/groonga/db/db
  env.host 127.0.0.1

  env.http_host 127.0.0.1
  env.http_port 10041
  env.http_database_path %{_localstatedir}/lib/groonga/db/db
  env.http_pid_path %{_rundir}/groonga/groonga-http.pid
  env.http_query_log_path %{_localstatedir}/log/groonga/query-http.log

  env.gqtp_host 127.0.0.1
  env.gqtp_port 10043
  env.gqtp_database_path %{_localstatedir}/lib/groonga/db/db
  env.gqtp_pid_path %{_rundir}/groonga/groonga-gqtp.pid
  env.gqtp_query_log_path %{_localstatedir}/log/groonga/query-gqtp.log
EOC

%post munin-plugins
%{_sbindir}/munin-node-configure --shell --remove-also | grep -e 'groonga_' | sh
%systemd_postun munin-node

%pre server-common
getent group groonga >/dev/null || groupadd -r groonga
getent passwd groonga >/dev/null || \
       useradd -r -g groonga -d %{_localstatedir}/lib/groonga -s /sbin/nologin \
    -c 'groonga' groonga
if [ $1 = 1 ] ; then
  mkdir -p %{_localstatedir}/log/groonga
  mkdir -p %{_localstatedir}/lib/groonga/db
  groonga -n %{_localstatedir}/lib/groonga/db/db shutdown > /dev/null
  chown -R groonga:groonga %{_localstatedir}/log/groonga
  chown -R groonga:groonga %{_localstatedir}/lib/groonga
  mkdir -p %{_localstatedir}/run/groonga
  chown -R groonga:groonga %{_localstatedir}/run/groonga
fi
exit 0

%post server-gqtp
%systemd_post groonga-server-gqtp.service

%preun server-gqtp
%systemd_preun groonga-server-gqtp.service

%postun server-gqtp
%systemd_postun groonga-server-gqtp.service

%post server-http
%systemd_post groonga-server-http.service

%preun server-http
%systemd_preun groonga-server-http.service

%postun server-http
%systemd_postun groonga-server-http.service

%postun munin-plugins
if [ $1 -eq 0 ]; then
    [ -f %{_localstatedir}/lock/subsys/munin-node ] && \
        systemctl restart munin-node >/dev/null 2>&1
    :
fi


%files
%license COPYING
%doc README.md
%{_bindir}/groonga
%{_bindir}/grndb

%files libs
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/groonga/synonyms.tsv
%{_libdir}/*.so.*
%dir %{_libdir}/groonga
%dir %{_libdir}/groonga/plugins
%dir %{_libdir}/groonga/plugins/functions
%dir %{_libdir}/groonga/plugins/query_expanders
%dir %{_libdir}/groonga/plugins/normalizers
%dir %{_libdir}/groonga/plugins/tokenizers
%dir %{_libdir}/groonga/plugins/ruby
%dir %{_libdir}/groonga/plugins/sharding
%{_libdir}/groonga/plugins/functions/*.so
%{_libdir}/groonga/plugins/query_expanders/tsv.so
%{_libdir}/groonga/plugins/ruby/eval.rb
%{_libdir}/groonga/plugins/sharding/*.rb
%{_libdir}/groonga/plugins/*.rb
%{_libdir}/groonga/scripts/ruby/
%{_datadir}/groonga/

%files devel
%{_includedir}/groonga/
%{_libdir}/*.so
%{_libdir}/cmake/Groonga/
%{_libdir}/pkgconfig/groonga*.pc

%files server-common
%config(noreplace) %{_sysconfdir}/tmpfiles.d/groonga.conf

%files server-gqtp
%config(noreplace) %{_sysconfdir}/groonga/
%config(noreplace) %{_sysconfdir}/sysconfig/groonga-server-gqtp
%config(noreplace) %{_sysconfdir}/logrotate.d/groonga-server-gqtp
%{_unitdir}/groonga-server-gqtp.service
%ghost %dir /run/%{name}
%attr(0755,groonga,groonga) %dir %{_localstatedir}/lib/%{name}
%attr(0755,groonga,groonga) %dir %{_localstatedir}/lib/%{name}/db

%files server-http
%config(noreplace) %{_sysconfdir}/groonga/
%config(noreplace) %{_sysconfdir}/sysconfig/groonga-server-http
%config(noreplace) %{_sysconfdir}/logrotate.d/groonga-server-http
%{_unitdir}/groonga-server-http.service
%ghost %dir /run/%{name}
%attr(0755,groonga,groonga) %dir %{_localstatedir}/lib/%{name}
%attr(0755,groonga,groonga) %dir %{_localstatedir}/lib/%{name}/db

%files plugin-tokenizer-mecab
%{_libdir}/groonga/plugins/tokenizers/mecab.so

%files plugin-token-filters
%{_libdir}/groonga/plugins/token_filters/stop_word.so
%{_libdir}/groonga/plugins/token_filters/stem.so

%files plugin-suggest
%{_bindir}/groonga-suggest-*
%{_libdir}/groonga/plugins/suggest/suggest.so

%files munin-plugins
%{_datadir}/groonga/munin/plugins/*
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/*

%files doc
%doc README.md
%license COPYING
%{_datadir}/doc/groonga/

%files examples
%{_datadir}/groonga/examples/

%files tools
%{_datadir}/groonga/tools/

%changelog
%autochangelog
