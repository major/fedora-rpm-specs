%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")
# Bug1799474 workaround
%define _legacy_common_support 1

Name:		groonga
Version:	10.0.8
Release:	6%{?dist}
Summary:	An Embeddable Fulltext Search Engine

License:	LGPLv2
URL:		https://groonga.org/
Source0:	https://packages.groonga.org/source/groonga/groonga-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	gcc
BuildRequires:	mecab-devel
BuildRequires:	zlib-devel
BuildRequires:	lz4-devel
BuildRequires:	msgpack-devel
BuildRequires:	zeromq-devel
BuildRequires:	libevent-devel
BuildRequires:	libedit-devel
BuildRequires:	pcre-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:	libstemmer-devel
BuildRequires:	openssl-devel
BuildRequires:	re2c
BuildRequires:	libzstd-devel
BuildRequires:	rapidjson-devel
BuildRequires: make
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-plugin-suggest = %{version}-%{release}
Obsoletes:	%{name}-python < 6.0.9-1
Obsoletes:	%{name}-php < 6.0.9-1

%description
Groonga is an embeddable full-text search engine library.  It can
integrate with DBMS and scripting languages to enhance their search
functionality.  It also provides a standalone data store server based
on relational data model.

%package libs
Summary:	Runtime libraries for Groonga
License:	LGPLv2 and (MIT or GPLv2)

%description libs
This package contains the libraries for Groonga

%package server-common
Summary:	Common packages for the Groonga server and the Groonga HTTP server
License:	LGPLv2
Requires:	%{name} = %{version}-%{release}
Requires(pre):	shadow-utils

%description server-common
This package provides common settings for server use

%package server-gqtp
Summary:	Groonga GQTP server
License:	LGPLv2
Requires:	%{name}-server-common = %{version}-%{release}
Requires(pre):	shadow-utils
Requires(post):	systemd
Requires(preun):	systemd
Obsoletes:	%{name}-server < 2.0.7-0

%description server-gqtp
This package contains the Groonga GQTP server

%package httpd
Summary:	Groonga HTTP server
License:	LGPLv2 and BSD
Requires:	%{name}-server-common = %{version}-%{release}
Provides:	%{name}-server-http = %{version}-%{release}
Obsoletes:	%{name}-server-http <= 4.0.7-2

%description httpd
This package contains the Groonga HTTP server. It has many features
because it is based on nginx HTTP server.

%package doc
Summary:	Documentation for Groonga
License:	LGPLv2 and BSD

%description doc
Documentation for Groonga

%package devel
Summary:	Libraries and header files for Groonga
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Libraries and header files for Groonga

%package tokenizer-mecab
Summary:	MeCab tokenizer for Groonga
Requires:	%{name}-libs = %{version}-%{release}

%description tokenizer-mecab
MeCab tokenizer for Groonga

%package plugin-suggest
Summary:	Suggest plugin for Groonga
Requires:	%{name}-libs = %{version}-%{release}

%description plugin-suggest
Suggest plugin for Groonga

%package plugin-token-filters
Summary:	Token filters plugin for Groonga
Requires:	%{name}-libs = %{version}-%{release}

%description plugin-token-filters
Token filters plugins for Groonga which provides
stop word and stemming features.

%package munin-plugins
Summary:	Munin plugins for Groonga
Requires:	%{name}-libs = %{version}-%{release}
Requires:	munin-node
Requires(post):	munin-node

%description munin-plugins
Munin plugins for Groonga

%prep
#% define optflags -O0
%setup -q
%build
%configure \
  --disable-static \
  --enable-mruby \
  --with-package-platform=fedora \
  --with-zlib --with-lz4 \
  --with-munin-plugins

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|' libtool
make %{?_smp_mflags} unitdir="%{_unitdir}"
# Exit %%build section explicitly not to execute unexpected configure script again
exit 0

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find %{buildroot} -type f -name "*.la" -delete
rm $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/groonga-server-http

mv $RPM_BUILD_ROOT%{_datadir}/doc/groonga groonga-doc

# Since F17, %%{_unitdir} is moved from /lib/systemd/system to
# /usr/lib/systemd/system.  So we need to manually install the service
# file into the new place.  The following should work with < F17,
# though Groonga package started using systemd native service since
# F17 and won't be submitted to earlier releases.
mkdir -p $RPM_BUILD_ROOT%{_unitdir}

# Remove obsolete files
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/groonga-server-http
rm -f $RPM_BUILD_ROOT%{_unitdir}/groonga-server-http.service

mkdir -p $RPM_BUILD_ROOT/run/groonga
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/groonga/db
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/groonga
mkdir -p $RPM_BUILD_ROOT%{_libdir}/groonga/plugins/normalizers

mv $RPM_BUILD_ROOT%{_datadir}/groonga/munin/ $RPM_BUILD_ROOT%{_datadir}/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/munin/plugin-conf.d/
cat <<EOC > $RPM_BUILD_ROOT%{_sysconfdir}/munin/plugin-conf.d/groonga
[groonga_*]
  user groonga
  group groonga
  env.PATH %{_bindir}
  env.database_path %{_localstatedir}/lib/groonga/db/db
  env.host 127.0.0.1

  env.http_host 127.0.0.1
  env.http_port 10041
  env.http_database_path %{_localstatedir}/lib/groonga/db/db
  env.http_pid_path /run/groonga/groonga-http.pid
  env.http_query_log_path %{_localstatedir}/log/groonga/query-http.log

  env.httpd_host 127.0.0.1
  env.httpd_port 10041
  env.httpd_database_path %{_localstatedir}/lib/groonga/db/db
  env.httpd_pid_path /run/groonga/groonga-httpd.pid
  env.httpd_query_log_path %{_localstatedir}/log/groonga/httpd/groonga-query.log

  env.gqtp_host 127.0.0.1
  env.gqtp_port 10043
  env.gqtp_database_path %{_localstatedir}/lib/groonga/db/db
  env.gqtp_pid_path /run/groonga/groonga-gqtp.pid
  env.gqtp_query_log_path %{_localstatedir}/log/groonga/query-gqtp.log
EOC

%ldconfig_scriptlets libs

%post munin-plugins
%{_sbindir}/munin-node-configure --shell --remove-also | grep -e 'groonga_' | sh
[ -f %{_localstatedir}/lock/subsys/munin-node ] && \
	systemctl restart munin-node > /dev/null 2>&1
:

%pre server-common
getent group groonga >/dev/null || groupadd -r groonga
getent passwd groonga >/dev/null || \
       useradd -r -g groonga -d %{_localstatedir}/lib/groonga -s /sbin/nologin \
	-c 'groonga' groonga
if [ $1 = 1 ] ; then
	mkdir -p %{_localstatedir}/lib/groonga/db
	groonga -n %{_localstatedir}/lib/groonga/db/db shutdown > /dev/null
	chown -R groonga:groonga %{_localstatedir}/lib/groonga
	mkdir -p /run/groonga
	chown -R groonga:groonga /run/groonga
fi
exit 0

%post server-gqtp
%systemd_post groonga-server-gqtp.service

%preun server-gqtp
%systemd_preun groonga-server-gqtp.service

%postun server-gqtp
%systemd_postun groonga-server-gqtp.service

%post httpd
%systemd_post groonga-httpd.service

%preun httpd
%systemd_preun groonga-httpd.service

%postun httpd
%systemd_postun groonga-httpd.service

%postun munin-plugins
if [ $1 -eq 0 ]; then
	[ -f %{_localstatedir}/lock/subsys/munin-node ] && \
		systemctl restart munin-node >/dev/null 2>&1
	:
fi


%files
%{_bindir}/groonga
%{_bindir}/groonga-benchmark
%{_bindir}/grndb

%files libs
%license COPYING
%doc README.md
%{_libdir}/*.so.*
%dir %{_libdir}/groonga
%dir %{_libdir}/groonga/plugins
%dir %{_libdir}/groonga/plugins/functions
%dir %{_libdir}/groonga/plugins/query_expanders
%dir %{_libdir}/groonga/plugins/normalizers
%dir %{_libdir}/groonga/plugins/tokenizers
%dir %{_libdir}/groonga/plugins/ruby
%dir %{_libdir}/groonga/plugins/sharding
%dir %{_libdir}/groonga/scripts/ruby
%dir %{_libdir}/groonga/scripts/ruby/command_line
%dir %{_libdir}/groonga/scripts/ruby/context
%dir %{_libdir}/groonga/scripts/ruby/expression_rewriters
%dir %{_libdir}/groonga/scripts/ruby/expression_tree
%dir %{_libdir}/groonga/scripts/ruby/groonga-log
%dir %{_libdir}/groonga/scripts/ruby/initialize
%dir %{_libdir}/groonga/scripts/ruby/logger
%dir %{_libdir}/groonga/scripts/ruby/query_logger
%{_libdir}/groonga/plugins/functions/*.so
%{_libdir}/groonga/plugins/query_expanders/tsv.so
%{_libdir}/groonga/plugins/ruby/*.rb
%{_libdir}/groonga/plugins/*.rb
%{_libdir}/groonga/plugins/sharding/*.rb
%{_libdir}/groonga/scripts/ruby/*.rb
%{_libdir}/groonga/scripts/ruby/command_line/*.rb
%{_libdir}/groonga/scripts/ruby/context/*.rb
%{_libdir}/groonga/scripts/ruby/groonga-log/*.rb
%{_libdir}/groonga/scripts/ruby/expression_rewriters/*.rb
%{_libdir}/groonga/scripts/ruby/expression_tree/*.rb
%{_libdir}/groonga/scripts/ruby/initialize/*.rb
%{_libdir}/groonga/scripts/ruby/logger/*.rb
%{_libdir}/groonga/scripts/ruby/query_logger/*.rb
%{_datadir}/groonga/
%config(noreplace) %{_sysconfdir}/groonga/synonyms.tsv

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

%files httpd
%config(noreplace) %{_sysconfdir}/groonga/httpd/*
%config(noreplace) %{_sysconfdir}/sysconfig/groonga-httpd
%config(noreplace) %{_sysconfdir}/logrotate.d/groonga-httpd
%{_unitdir}/groonga-httpd.service
%{_sbindir}/groonga-httpd
%{_sbindir}/groonga-httpd-restart
%ghost %dir /run/%{name}
%attr(0755,groonga,groonga) %dir %{_localstatedir}/lib/%{name}
%attr(0755,groonga,groonga) %dir %{_localstatedir}/lib/%{name}/db

%files doc
%doc README.md COPYING
%doc groonga-doc/*

%files devel
%{_includedir}/groonga/
%{_libdir}/*.so
%{_libdir}/pkgconfig/groonga*.pc

%files tokenizer-mecab
%{_libdir}/groonga/plugins/tokenizers/mecab.so

%files plugin-token-filters
%{_libdir}/groonga/plugins/token_filters/stop_word.so
%{_libdir}/groonga/plugins/token_filters/stem.so

%files plugin-suggest
%{_bindir}/groonga-suggest-*
%{_libdir}/groonga/plugins/suggest/suggest.so

%files munin-plugins
%{_datadir}/munin/plugins/*
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 10.0.8-4
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 5 2020 Kentaro Hayashi <kenhys@gmail.com>
- New upstream release

* Tue Sep 29 20:31:33 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
- Rebuilt for libevent 2.1.12

* Mon Aug 31 2020 Kentaro Hayashi <kenhys@gmail.com> - 10.0.6-1
- new upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 6 2020 Kentaro Hayashi <kenhys@gmail.com> - 10.0.4-1
- new upstream release

* Sun May 10 2020 Kentaro Hayashi <kenhys@gmail.com> - 10.0.2-1
- new upstream release

* Fri Apr 24 2020 Kentaro Hayashi <hayashi@clear-code.com> - 10.0.1-1
- new upstream release

* Sun Feb 16 2020 Kentaro Hayashi <hayashi@clear-code.com> - 9.1.2-2
- enable legacy common support to fix FTBFS (Bug#1799474).

* Sat Feb 8 2020 Kentaro Hayashi <hayashi@clear-code.com> - 9.1.2-1
- new upstream release
- use https: for upstream URL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Kentaro Hayashi <hayashi@clear-code.com> - 9.0.9-1
- new upstream release

* Thu Oct 3 2019 Kentaro Hayashi <hayashi@clear-code.com> - 9.0.8-1
- new upstream release

* Sun Sep 22 2019 Kentaro Hayashi <hayashi@clear-code.com> - 9.0.7-1
- new upstream release

* Mon Aug 12 2019 Kentaro Hayashi <hayashi@clear-code.com> - 9.0.6-1
- new upstream release

* Sun Jul 28 2019 Kentaro Hayashi <hayashi@clear-code.com> - 9.0.4-1
- new upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Kentaro Hayashi <hayashi@clear-code.com> 9.0.1-1
- new upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Kentaro Hayashi <hayashi@clear-code.com> 8.1.1-1
- new upstream release

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 8.0.9-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Nov 30 2018 Kentaro Hayashi <hayashi@clear-code.com> 8.0.9-1
- new upstream release
- fix E: specfile-error warning: Macro expanded in comment

* Wed Oct 31 2018 Kentaro Hayashi <hayashi@clear-code.com> 8.0.8-1
- new upstream release

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 8.0.7-2
- Drop obsolete deps, use %%license, minor spec cleanups

* Sat Sep 29 2018 Kentaro Hayashi <hayashi@clear-code.com> - 8.0.7-1
- new upstream release

* Wed Aug 29 2018 Kentaro Hayashi <hayashi@clear-code.com>
- new upstream release

* Fri Aug 3 2018 Kentaro Hayashi <hayashi@clear-code.com>
- new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Kentaro Hayashi <hayashi@clear-code.com> - 8.0.3-1
- new upstream release
- drop dependency to initscripts. (Bug#1592357) Reported by David Kaspar.

* Sat May 12 2018 Kentaro Hayashi <hayashi@clear-code.com> - 8.0.2-1
- new upstream release

* Tue Apr 24 2018 Kentaro Hayashi <hayashi@clear-code.com> - 8.0.1-1
- new upstream release

* Thu Feb 22 2018 Kentaro Hayashi <hayashi@clear-code.com> - 8.0.0-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Kentaro Hayashi <hayashi@clear-code.com> - 7.1.0-1
- new upstream release
- add patch disable-glibc-wordaround.patch to fix FTBFS

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 7.0.9-2
- Rebuilt for switch to libxcrypt

* Mon Dec 4 2017 Kentaro Hayashi <hayashi@clear-code.com> - 7.0.9-1
- new upstream release

* Fri Nov 3 2017 Kentaro Hayashi <hayashi@clear-code.com> - 7.0.8-1
- new upstream release

* Sat Sep 9 2017 Kentaro Hayashi <hayashi@clear-code.com> - 7.0.6-1
- new upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Kentaro Hayashi <hayashi@clear-code.com> - 7.0.5-1
- new upstream release
- add /etc/tmpfiles.d/groonga.conf

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Kentaro Hayashi <hayashi@clear-code.com> - 7.0.4-1
- new upstream release

* Fri May 5 2017 Kentaro Hayashi <hayashi@clear-code.com> - 7.0.2-1
- new upstream release

* Thu Mar 30 2017 Kentaro Hayashi <hayashi@clear-code.com> - 7.0.1-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 kenhys@gmail.com - 6.1.5-1
- new upstream release

* Fri Dec 23 2016 kenhys@gmail.com - 6.1.1-1
- new upstream release
- add zstd dependency to compress column.

* Sat Nov 5 2016 Kentaro Hayashi <hayashi@clear-code.com> - 6.1.0-1
- new upstream release.

* Fri Oct 14 2016 Kentaro Hayashi <hayashi@clear-code.com> - 6.0.9-1
- new upstream release.
- drop php binding package.
- drop python binding package.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 8 2016 Kentaro Hayashi <hayashi@clear-code.com> - 6.0.5-1
- new upstream release.

* Fri Jun 17 2016 Kentaro Hayashi <hayashi@clear-code.com> - 6.0.4-1
- new upstream release.

* Wed Apr 13 2016 HAYASHI Kentaro <hayashi@clear-code.com> - 6.0.1-2
- rebuilt for msgpack soname bump

* Mon Apr 4 2016 HAYASHI Kentaro <hayashi@clear-code.com> - 6.0.1-1
- new upstream release.

* Fri Mar 11 2016 HAYASHI Kentaro <hayashi@clear-code.com> - 6.0.0-1
- new upstream release.
- enable TLS for groonga-httpd
- drop groonga-server-http package

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 1 2016 HAYASHI Kentaro <hayashi@clear-code.com> - 5.1.2-1
- new upstream release.
- remove needless Require: libstemmer entry.

* Tue Dec 29 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.1.1-1
- new upstream release.

* Sun Dec 13 2015 Kalev Lember <klember@redhat.com> - 5.1.0-2
- Rebuilt for libmsgpack soname bump

* Wed Dec 9 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.1.0-1
- new upstream release.

* Thu Oct 29 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.9-1
- new upstream release.

* Fri Oct 9 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.8-1
- new upstream release.

* Tue Sep 1 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.7-1
- new upstream release.

* Sat Aug 1 2015 Masafumi Yokoyama <yokoyama@clear-code.com> - 5.0.6-1
- new upstream release.

* Mon Jun 29 2015 Masafumi Yokoyama <yokoyama@clear-code.com> - 5.0.5-1
- new upstream release.

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 5.0.4-3
- rebuilt for new zeromq 4.1.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 2 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.4-1
- new upstream release.

* Thu Apr 30 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.3-1
- new upstream release.
- add vector plugin.

* Sun Apr 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 5.0.2-2
- Drop ExclusiveArch, atomic primitives now supported on all arches

* Wed Apr 1 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.2-1
- new upstream release.
- drop fix-crash-by-missing-libedit-initialization.patch
  This patch is already imported into upstream.

* Mon Mar 30 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.1-1
- new upstream release.
- add a patch to fix crash in standalone mode.
  fix-crash-by-missing-libedit-initialization.patch

* Wed Feb 25 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 5.0.0-1
- new upstream release.
- enable mruby by default.

* Wed Jan 14 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 4.1.0-1
- new upstream release.

* Tue Jan 6 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.9.1-1
- new upstream release.
- remove needless 'g' option to remove rpath.
- use /run/groonga to fix dir-or-file-in-var-run error.

* Mon Dec 1 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.8-1
- new upstream release.
- make groonga-httpd as default HTTP server package
- drop groonga-server-http, it is just changed to transitional package

* Tue Nov 4 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.7-1
- new upstream release.
- drop lzo support.
- add lz4 support.
- add groonga-plugin-token-filters sub package.

* Mon Oct 6 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.6-1
- new upstream release.
- drop a needless patch to fix groonga-httpd service startup failure.

* Mon Sep 8 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.5-1
- new upstream release.
- add a patch to fix groonga-httpd service startup failure.
  add-missing-mkdir-for-groonga-httpd-service.patch

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.4-1
- new upstream release.

* Tue Jul 1 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.3-1
- new upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.2-1
- new upstream release.

* Mon Mar 31 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.1-1
- new upstream release.

* Mon Feb 10 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 4.0.0-1
- new upstream release.

* Mon Feb 3 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 3.1.2-1
- new upstream release.

* Tue Dec 31 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.1.1-1
- new upstream release.

* Fri Nov 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.1.0-1
- new upstream release.

* Tue Oct 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.9-1
- new upstream release.

* Sun Sep 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.8-1
- new upstream release.

* Thu Aug 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.7-1
- new upstream release.

* Wed Jul 31 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.6-2
- unify own directories of plugins.

* Mon Jul 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.6-1
- new upstream release.

* Sat Jun 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.5-1
- new upstream release.

* Wed May 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.4-1
- new upstream release.

* Mon Apr 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.3-1
- new upstream release.
- enable the PIE compiler flags. 

* Fri Mar 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 3.0.2-1
- new upstream release.
- fix wrong directory ownership.
- filter not to export private modules.
- add missing groonga-server-gqtp related systemd macros.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Daiki Ueno <dueno@redhat.com> - 2.0.9-1
- built in Fedora

* Thu Nov 29 2012 HAYASHI Kentaro <hayashi@clear-code.com> - 2.0.9-0
- new upstream release.

* Mon Oct 29 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.8-0
- new upstream release.
- Remove needless "Requires". They will be added by rpmbuild automatically.
  Reported by by Daiki Ueno. Thanks!!!
- Fix license of server-gqtp.
- Fix license of server-http.
- Add more description to server-http and httpd.

* Sat Sep 29 2012 HAYASHI Kentaro <hayashi@clear-code.com> - 2.0.7-0
- new upstream release.
- Split groonga-server package into groonga-server-gqtp and
  groonga-server-http package.

* Wed Aug 29 2012 HAYASHI Kentaro <hayashi@clear-code.com> - 2.0.6-0
- new upstream release.
- Split common tasks for server use into groonga-server-common package.
- groonga-server and groonga-httpd require groonga-server-common package.

* Wed Aug 22 2012 Daiki Ueno <dueno@redhat.com> - 2.0.5-2
- use systemd-rpm macros (#850137)

* Tue Jul 31 2012 Daiki Ueno <dueno@redhat.com> - 2.0.5-1
- built in Fedora

* Sun Jul 29 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.5-0
- new upstream release.

* Mon Jul  2 2012 Daiki Ueno <dueno@redhat.com> - 2.0.4-1
- built in Fedora
- add msgpack-devel to BR

* Fri Jun 29 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.4-0
- new upstream release.
- groonga package does not require groonga-tokenizer-mecab package.

* Mon Jun  4 2012 Daiki Ueno <dueno@redhat.com> - 2.0.3-1
- built in Fedora

* Tue May 29 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.3-0
- new upstream release.

* Tue May  1 2012 Daiki Ueno <dueno@redhat.com> - 2.0.2-1
- built in Fedora

* Sun Apr 29 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.2-0
- new upstream release.
- use libedit.

* Fri Mar 30 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.1-2
- Use shutdown command for stop.

* Fri Mar 30 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.1-1
- Fix bind address argument parameter.
  Patch by Masaharu IWAI. Thanks!!!

* Thu Mar 29 2012 Daiki Ueno <dueno@redhat.com> - 2.0.1-1
- built in Fedora

* Thu Mar 29 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.1-0
- new upstream release.
- ensure removing build directory before installing.
- grntest -> groonga-benchmark.
- remove groonga-tools package.

* Thu Mar  1 2012 Daiki Ueno <dueno@redhat.com> - 2.0.0-1
- built in Fedora

* Wed Feb 29 2012 Kouhei Sutou <kou@clear-code.com> - 2.0.0-0
- new upstream release.
- remove other permission from DB directory.
- use HTTP as the default protocol.
- support effective user and group in systemd.
  Patch by Daiki Ueno. Thanks!!!

* Thu Feb  2 2012 Daiki Ueno <dueno@redhat.com> - 1.3.0-2
- fix systemd service file

* Mon Jan 30 2012 Daiki Ueno <dueno@redhat.com> - 1.3.0-1
- built in Fedora
- migrate groonga-server initscript to systemd service (#781503)
- add groonga-php5.4.patch to compile PHP extension with PHP 5.4

* Sun Jan 29 2012 Kouhei Sutou <kou@clear-code.com> - 1.3.0-0
- new upstream release.
- groonga-server package does not require groonga-munin-plugins package.
  suggested by Masaharu IWAI. Thanks!!!
- groonga package does not require groonga-doc package.
  suggested by Masaharu IWAI. Thanks!!!

* Mon Jan 9 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.2.9-2
- rebuild against new mecab

* Wed Jan  4 2012 Daiki Ueno <dueno@redhat.com> - 1.2.9-1
- build in fedora

* Thu Dec 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.9-0
- new upstream release.

* Tue Nov 29 2011 Daiki Ueno <dueno@redhat.com> - 1.2.8-1
- build in fedora

* Tue Nov 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.8-0
- new upstream release.
- enable zlib support.
- enable lzo support.
- add --with-package-platform=redhat configure option to install init script.
- add --with-munin-plugins cofnigure option to install Munin plugins.

* Tue Nov  1 2011 Daiki ueno <dueno@redhat.com> - 1.2.7-1
- build in fedora

* Sat Oct 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.7-0
- new upstream release.

* Fri Sep 30 2011 Daiki Ueno <dueno@redhat.com> - 1.2.6-1
- build in fedora

* Thu Sep 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.6-0
- new upstream release.

* Mon Sep  5 2011 Daiki Ueno <dueno@redhat.com> - 1.2.5-1
- build in fedora

* Mon Aug 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.5-0
- new upstream release.

* Fri Jul 29 2011 Daiki Ueno <dueno@redhat.com> - 1.2.4-1
- build in fedora

* Fri Jul 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.4-0
- new upstream release.

* Mon Jul  4 2011 Daiki Ueno <dueno@redhat.com> - 1.2.3-1
- build in fedora
- add ruby to BR

* Wed Jun 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.3-0
- new upstream release.
- add a new groong-tools package.

* Tue May 31 2011 Daiki Ueno <dueno@redhat.com> - 1.2.2-1
- build in fedora

* Sun May 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.2-0
- new upstream release.
- split server files into groonga-server package.

* Mon May  2 2011 Daiki Ueno <dueno@redhat.com> - 1.2.1-1
- build in fedora.

* Fri Apr 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.1-0
- new upstream release.

* Wed Mar 30 2011 Daiki Ueno <dueno@redhat.com> - 1.2.0-1
- build in fedora.

* Tue Mar 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.2.0-0
- new upstream release.

* Thu Feb 17 2011 Daiki Ueno <dueno@redhat.com> - 1.1.0-1
- build in fedora.
- don't require zeromq explicitly.

* Wed Feb 09 2011 Kouhei Sutou <kou@clear-code.com> - 1.1.0-0
- new upstream release.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Dan Horák <dan[at]danny.cz> - 1.0.8-2
- add ExclusiveArch (atomic primitives implemented only for x86)

* Thu Feb  3 2011 Daiki Ueno <dueno@redhat.com> - 1.0.8-1
- build in fedora.
- don't depend on libevent explicitly.

* Wed Feb 02 2011 Kouhei Sutou <kou@clear-code.com> - 1.0.8-0
- new upstream release.

* Sat Jan 29 2011 Kouhei Sutou <kou@clear-code.com> - 1.0.7-0
- new upstream release.

* Fri Dec 31 2010 Kouhei Sutou <kou@clear-code.com> - 1.0.6-0
- new upstream release

* Wed Dec 29 2010 Kouhei Sutou <kou@clear-code.com> - 1.0.5-0
- new upstream release.

* Mon Nov 29 2010 Kouhei Sutou <kou@clear-code.com> - 1.0.4-1
- new upstream release

* Wed Nov 24 2010 Daiki Ueno <dueno@redhat.com> - 1.0.3-2
- %%ghost /var/run/*.

* Sat Oct 09 2010 Kouhei Sutou <kou@clear-code.com> - 1.0.3-1
- new upstream release.

* Thu Oct  7 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-7
- own %%_localstatedir/lib/%%name/db.
- use %%_sbindir RPM macro.

* Wed Oct  6 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-6
- use %%python_sitearch and %%php_extdir macros.
- correct directory ownership for -munin-plugins subpackage.
- supply %%optflags when building PHP binding.
- don't set CGROUP_DAEMON in initscript.

* Tue Oct  5 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-5
- correct directory ownership for -munin-plugins subpackage.
- make -doc subpackage require -libs.
- correct directory ownership for directories under %%_localstatedir.
- make initscript disabled by default
- move "build process" of Python and PHP bindings to %%build from %%install
- build against Python 2.7
- fix naming of Python and PHP bindings (python-%%{name} to %%{name}-python)

* Mon Oct  4 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-4
- package Python and PHP bindings.

* Mon Oct  4 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-3
- fix License.
- pass "-p" to the install command to preserve timestamps.
- use RPM macros %%_initddir, %%_localstatedir, %%_prefix, etc.
- use the standard snippet to creating user/group for groonga; don't
  call userdel/groupdel.
- add missing "Require(foo): bar" for /sbin/service, /sbin/chkconfig,
  /sbin/ldconfig, and /usr/sbin/munin-node-configure.
- fix attributes in %%files.
- correct directory ownership.

* Fri Oct  1 2010 Daiki Ueno <dueno@redhat.com> - 1.0.2-2
- don't require autotools when building
- pass --disable-static to %%configure

* Thu Sep 09 2010 Kouhei Sutou <kou@clear-code.com> - 1.0.2-1
- new upstream release.

* Mon Sep 06 2010 Kouhei Sutou <kou@clear-code.com> - 1.0.1-1
- new upstream release.

* Thu Sep 02 2010 Kouhei Sutou <kou@clear-code.com> - 1.0.0-1
- split packages.

* Tue Aug 24 2010 Daiki Ueno <dueno@redhat.com> - 0.7.6-1
- initial packaging for Fedora
