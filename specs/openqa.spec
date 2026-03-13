# Fedora spec initially based on upstream spec file from OBS:
# https://build.opensuse.org/package/view_file/devel:openQA/openQA/openQA.spec
# License: GPLv2+

# openQA has a bunch of private modules (most namespaced but a couple
# not), we do not want automatic provides or requires for these
# ref https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Perl
# but per https://fedorahosted.org/fpc/ticket/591 , these have been
# improved, and contrary to the wiki it is safe to set them first and
# then call perl_default_filter, the values will be properly merged.
# I tried to sell upstream on naming these properly and installing
# them to the perl vendor dir, but they wouldn't bite:
# https://github.com/os-autoinst/os-autoinst/issues/387
# Despite the apparently-CPAN-like name, DBIx::Class::Timestamps is
# installed to openQA's private directory and should be excluded.
# perl(Perl::Critic) requirements come from HashKeyQuotes.pm, which is
# used only for tests, so we don't want a runtime requirement.

%global __provides_exclude_from %{_datadir}/openqa/lib
%global __requires_exclude perl\\((OpenQA|DBIx::Class::Timestamps|MojoDebugHandle|db_helpers|db_profiler|Perl::Critic)
%{?perl_default_filter}

%global github_owner    os-autoinst
%global github_name     openQA
%global github_version  5
%global github_commit   19189f0ef4b285279f0492a5c5f4ded6304984b0
# if set, will be a post-release snapshot build, otherwise a 'normal' build
%global github_date     20260126
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

# can't use linebreaks here!
%global openqa_main_service openqa-webui.service
%global openqa_extra_services openqa-gru.service openqa-websockets.service openqa-scheduler.service openqa-enqueue-audit-event-cleanup.service openqa-enqueue-audit-event-cleanup.timer openqa-enqueue-asset-cleanup.service openqa-enqueue-git-auto-update.service openqa-enqueue-asset-cleanup.timer openqa-enqueue-result-cleanup.service openqa-enqueue-result-cleanup.timer openqa-enqueue-bug-cleanup.service openqa-enqueue-bug-cleanup.timer openqa-enqueue-git-auto-update.timer openqa-enqueue-needle-ref-cleanup.service openqa-enqueue-needle-ref-cleanup.timer openqa-enqueue-scheduled-product-cleanup.service openqa-enqueue-scheduled-product-cleanup.timer
%global openqa_services %{openqa_main_service} %{openqa_extra_services}
%global openqa_worker_services openqa-worker.target openqa-slirpvde.service openqa-vde_switch.service openqa-worker-cacheservice.service openqa-worker-cacheservice-minion.service
%global openqa_localdb_services openqa-setup-db.service openqa-dump-db.service openqa-dump-db.timer

%if %{undefined tmpfiles_create}
%global tmpfiles_create() \
%{_bindir}/systemd-tmpfiles --create %{?*} >/dev/null 2>&1 || :
%{nil}
%endif

# diff from SUSE: we have 'openqa-client', they have 'openQA-client'
%define python_scripts_requires python3-requests openqa-client

# The following line is generated from dependencies.yaml (upstream)
%define assetpack_requires perl(CSS::Minifier::XS) >= 0.01 perl(JavaScript::Minifier::XS) >= 0.11 perl(Mojolicious) perl(Mojolicious::Plugin::AssetPack) >= 1.36 perl(YAML::PP) >= 0.026
# Diff from SUSE: we use 'perl-interpreter' where they use 'perl',
# our 'perl' is a metapackage and we don't want all of it
# we use 'chrony' where they use 'ntp-daemon'
# their versioning of mojolicious is different due to
# https://github.com/openSUSE/cpanspec/issues/47
# The following line is generated from dependencies.yaml (upstream)
%define common_requires chrony perl-interpreter >= 5.20.0 perl(Carp::Always) >= 0.14.02 perl(Config::IniFiles) perl(Config::Tiny) perl(Cpanel::JSON::XS) >= 4.09 perl(Cwd) perl(Data::Dump) perl(Data::Dumper) perl(Digest::MD5) perl(Feature::Compat::Try) perl(Filesys::Df) perl(Getopt::Long) perl(Minion) >= 10.25 perl(Mojolicious) >= 9.34 perl(Regexp::Common) perl(Storable) perl(Text::Glob) perl(Time::Moment)
# Diff from SUSE: we package bsdcat and bsdtar separately
# runtime requirements for the main package that are not required by other sub-packages
# The following line is generated from dependencies.yaml (upstream)
%define main_requires %assetpack_requires bsdcat bsdtar git-core hostname openssh-clients perl(BSD::Resource) perl(Carp) perl(CommonMark) perl(Config::Tiny) perl(DBD::Pg) >= 3.7.4 perl(DBI) >= 1.632 perl(DBIx::Class) >= 0.082801 perl(DBIx::Class::DeploymentHandler) perl(DBIx::Class::DynamicDefault) perl(DBIx::Class::OptimisticLocking) perl(DBIx::Class::ResultClass::HashRefInflator) perl(DBIx::Class::Schema::Config) perl(DBIx::Class::Storage::Statistics) perl(Date::Format) perl(DateTime) perl(DateTime::Duration) perl(DateTime::Format::Pg) perl(Exporter) perl(Fcntl) perl(File::Basename) perl(File::Copy) perl(File::Copy::Recursive) perl(File::Path) perl(File::Spec) perl(FindBin) perl(Getopt::Long::Descriptive) perl(IO::Handle) perl(IPC::Run) perl(JSON::Validator) perl(LWP::UserAgent) perl(Module::Load::Conditional) perl(Module::Pluggable) perl(Mojo::Base) perl(Mojo::ByteStream) perl(Mojo::IOLoop) perl(Mojo::JSON) perl(Mojo::Pg) perl(Mojo::RabbitMQ::Client) >= 0.2 perl(Mojo::URL) perl(Mojo::Util) perl(Mojolicious::Commands) perl(Mojolicious::Plugin) perl(Mojolicious::Plugin::OAuth2) perl(Mojolicious::Static) perl(Net::OpenID::Consumer) perl(POSIX) perl(Pod::POM) perl(SQL::Translator) perl(Scalar::Util) perl(Sort::Versions) perl(Text::Diff) perl(Time::HiRes) perl(Time::ParseDate) perl(Time::Piece) perl(Time::Seconds) perl(URI::Escape) perl(YAML::PP) >= 0.026 perl(YAML::XS) perl(aliased) perl(base) perl(constant) perl(diagnostics) perl(strict) perl(warnings)
# The following line is generated from dependencies.yaml (upstream)
%define client_requires curl git-core jq perl(Getopt::Long::Descriptive) perl(IO::Socket::SSL) >= 2.009 perl(IPC::Run) perl(JSON::Validator) perl(LWP::Protocol::https) perl(LWP::UserAgent) perl(Test::More) perl(YAML::PP) >= 0.020 perl(YAML::XS)
# Diff from SUSE 1: case (they have openQA-client, we have openqa-client)
# Diff from SUSE 2: we have 'sqlite' not 'sqlite3'
# Diff from SUSE 3: we package bsdcat and bsdtar separately
# The following line is generated from dependencies.yaml (upstream)
%define worker_requires bsdcat bsdtar openqa-client optipng os-autoinst perl(Capture::Tiny) perl(File::Map) perl(Minion::Backend::SQLite) >= 5.0.7 perl(Mojo::IOLoop::ReadWriteProcess) >= 0.26 perl(Mojo::SQLite) psmisc sqlite >= 3.24.0
# Diff from SUSE: we don't have perl(MCP) packaged currently
# The following line is generated from dependencies.yaml (upstream)
%define mcp_requires %{nil}
# Diff from SUSE: they have npm as they run npm install in the spec,
# we do it in update-cache.sh
# The following line is generated from dependencies.yaml (upstream)
%define build_requires %assetpack_requires rubygem(sass)

# All requirements needed by the tests executed during build-time.
# Do not require on this in individual sub-packages except for the devel
# package.
# Diff from SUSE: Selenium requirements dropped as not available in Fedora,
# critic and (python) yamllint requirements dropped as we don't run those
# checks in our package build, ssh-keygen is in openssh in Fedora
# (openssh-common in SUSE), Syntax::Keyword::Try::Deparse seems to be
# missing upstream
# The following line is generated from dependencies.yaml (upstream)
%define test_requires %common_requires %main_requires %mcp_requires %python_scripts_requires %worker_requires curl jq openssh os-autoinst perl(App::cpanminus) perl(Test::Exception) perl(Test::Fatal) perl(Test::MockModule) perl(Test::MockObject) perl(Test::Mojo) perl(Test::Most) perl(Test::Output) perl(Test::Pod) perl(Test::Strict) perl(Test::Warnings) >= 0.029 perl(Syntax::Keyword::Try::Deparse) postgresql-server
%ifarch x86_64
%define qemu qemu qemu-kvm
%else
%define qemu qemu
%endif
# Diff from SUSE: perl::Critic::Community is omitted as we do not package it,
# SUSE has python3-yamllint but we just have yamllint
# shfmt is omitted as our package for it was orphaned and retired
# The following line is generated from dependencies.yaml (upstream)
%define style_check_requires ShellCheck perl(Code::TidyAll) perl(Perl::Critic) yamllint
# diff from SUSE: perl(Devel::Cover::Report::Codecovbash) dropped because
# it's not in Fedora (this means you can't run 'make coverage-codecov')
# The following line is generated from dependencies.yaml (upstream)
%define cover_requires perl(Devel::Cover)
# diff from SUSE 1: xorg-x11-fonts dropped because that binary package
# doesn't exist in Fedora (it exists as a source package generating
# multiple binary packages) and I can't find any reason for it
# diff from SUSE 2: we don't have perl(Test::CheckGitStatus) packaged
# The following line is generated from dependencies.yaml (upstream)
%define devel_no_selenium_requires %build_requires %cover_requires %qemu %style_check_requires %test_requires curl perl(Perl::Tidy) postgresql-devel rsync sudo tar
# diff from SUSE: chromedriver dropped as we don't package it
# that makes this look fairly silly, but we want to follow the SUSE
# spec as close as we can
# The following line is generated from dependencies.yaml (upstream)
%define devel_requires %devel_no_selenium_requires

%bcond_without tests

Name:           openqa
Version:        %{github_version}%{?github_date:^%{github_date}git%{shortcommit}}
Release:        %{autorelease}
Summary:        OS-level automated testing framework
# openQA is mostly GPLv2+. some scripts and bundled Node modules are
# MIT, ace-builds is BSD-3-Clause
License:        GPL-2.0-or-later AND MIT AND BSD-3-Clause
Url:            http://os-autoinst.github.io/openQA/
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz
# pre-generated cached assets, build with update-cache.sh. We could
# install without these and let openQA generate them at run time, but
# we don't for two reasons: we don't want to let a webapp rewrite
# itself if avoidable (it's a security risk), and the tests don't work
# without the asset cache present. This should be re-generated any
# time Source0 changes.
Source1:        assetcache-%{github_commit}.tar.xz
# Plugin to restart failed update tests (to avoid spurious failures)
# FIXME: this probably doesn't handle jobs with parents/children
# properly
Source2:        FedoraUpdateRestart.pm
# fedora-messaging publishing plugin (upstream doesn't want this as
# it's too fedora-y for them)
Source3:        FedoraMessaging.pm
# tests for the fedora-messaging publishing plugin
Source4:        23-fedora-messaging.t
# sysusers config files. note these are shipped in the upstream tarball
# but we need to change the groups so we have our own versions here
Source5:        geekotest.conf
Source6:        openQA-worker.conf

BuildRequires: make
BuildRequires:  %{python_scripts_requires}
BuildRequires:  perl-generators
# Standard for packages that have systemd services
BuildRequires:  systemd
# Build and tests need LC_ALL=en_US.UTF-8, so we need this...
BuildRequires:  glibc-langpack-en
BuildRequires:  %{build_requires}
%if %{with tests}
BuildRequires:  %{test_requires}
%endif
BuildRequires:  systemd-rpm-macros
Requires:       perl(Minion) >= 10.0
Requires:       %{main_requires}
Requires:       openqa-common = %{version}-%{release}
Requires:       openqa-client = %{version}-%{release}
Requires(post): coreutils

# Standard for packages that have systemd services & sysusers
%{?systemd_requires}
%{?sysusers_requires_compat}

# the plugin is needed if the auth method is set to "oauth2"
Recommends:     perl(Mojolicious::Plugin::OAuth2)
# required to decompress .tar.xz compressed disk images/isos
Recommends:     perl(IO::Uncompress::UnXz)
# server needs to run an rsync server if worker caching is used
Recommends:     rsync
# Optionally enabled with USE_PNGQUANT=1
Recommends:     pngquant

# For the httpd subpackage split in 4.3-7, needed for updates to work right
Obsoletes:      openqa < 4.3-7

# The NPM bundled dependency generator does not work as the modules
# seem to be stripped down to the minimum openQA needs - package.json
# is stripped out. So we have to list these manually
Provides:       bundled(nodejs-ace-builds) = 1.43.1
Provides:       bundled(nodejs-anser) = 2.3.2
Provides:       bundled(nodejs-bootstrap) = 5.3.7
Provides:       bundled(nodejs-chosen-js) = 1.8.7
Provides:       bundled(nodejs-d3) = 7.9.0
Provides:       bundled(nodejs-dagre-d3) = 0.6.4
Provides:       bundled(nodejs-datatables.net) = 2.3.2
Provides:       bundled(nodejs-datatables.net-bs5) = 2.3.2
Provides:       bundled(nodejs-fork-awesome) = 1.2.0
Provides:       bundled(nodejs-jquery) = 3.7.1
Provides:       bundled(nodejs-jquery-ujs) = 1.2.3
Provides:       bundled(nodejs-timeago) = 1.6.7

# Note: Fedora does not have the issue SUSE has with noarch. on Fedora
# if build for *any* arch fails, the build is considered failed for
# *all* arches, so we can never get in a situation where the
# perl-Mojolicious-Plugin-AssetPack version differs across arches as
# SUSE can
BuildArch:      noarch

%description
openQA is a testing framework that allows you to test GUI applications on one
hand and bootloader and kernel on the other. In both cases, it is difficult to
script tests and verify the output. Output can be a popup window or it can be
an error in early boot even before init is executed.

openQA is an automated test tool that makes it possible to test the whole
installation process of an operating system. It uses virtual machines to
reproduce the process, check the output (both serial console and screen) in
every step and send the necessary keystrokes and commands to proceed to the
next. openQA can check whether the system can be installed, whether it works
properly in 'live' mode, whether applications work or whether the system
responds as expected to different installation options and commands.

Even more importantly, openQA can run several combinations of tests for every
revision of the operating system, reporting the errors detected for each
combination of hardware configuration, installation options and variant of the
operating system.

%package devel
Summary:        Development package pulling in all build+test dependencies
Requires:       %{devel_requires}

%description devel
Development package pulling in all build+test dependencies.


%package common
Summary:        Common components for openQA server and workers
Requires:       %{common_requires}
# critical bug fix
Requires:       perl(DBIx::Class) >= 0.082801
# assetpack has to approximately match version srpm was built with
Requires:       perl(Mojolicious::Plugin::AssetPack) >= 2.01

%description common
This package contains shared resources for the openQA server and
openQA workers.


%package worker
Summary:        The openQA worker
%define worker_requires_including_uncovered_in_tests %worker_requires perl(SQL::SplitStatement)
Requires:       %{worker_requires_including_uncovered_in_tests}
Requires:       openqa-common = %{version}-%{release}
Requires(post): coreutils
Requires(post): os-autoinst >= 4.6
Recommends:     qemu
# Needed for caching - not required if caching not used...
Recommends:     rsync

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description worker
The openQA worker manages the os-autoinst test engine. A system with
openqa-worker installed can run an arbitrary number of openQA workers
(as many as its hardware can support), each of which will run a single
openQA test job at a time, as long as appropriate jobs for the worker
are available from the server it is configured to work for.


%package httpd
Summary:        openQA httpd (Apache) integration
Requires:       httpd
Requires:       httpd-filesystem
# prior to 4.3-7, these files were part of the core package; this is
# here so people who had those versions installed don't lose their
# bits on update
Obsoletes:      openqa < 4.3-7
# Note: does not require any part of openQA as you may wish to have
# Apache and openQA running on different boxes

%description httpd
This package contains httpd (Apache) configuration for the openQA
automated testing framework. openQA runs as a self-contained http
server which is expected to be reverse-proxied by a public-facing http
server (rather than being accessed directly). The config snippets in
this package help you configure openQA to be reverse proxied by httpd.

%package plugin-fedora-messaging
Summary:        openQA plugin for publishing to fedora-messaging
Requires:       openqa >= 4.3-20
Requires:       perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA)
Requires:       perl(UUID::URandom)
BuildRequires:  perl(UUID::URandom)
# Old name
Obsoletes:      %{name}-plugin-fedmsg < 4.7
Provides:       %{name}-plugin-fedmsg = %{version}-%{release}

%description plugin-fedora-messaging
This package contains an openQA plugin which sends fedora-messaging
messages for certain openQA internal events. To enable the plugin, put
'plugins = FedoraMessaging' in the global section of
/etc/openqa/openqa.ini. The plugin piggybacks on the upstream AMQP
plugin, and follows its configuration (in the 'amqp' section of
openqa.ini).

%package plugin-fedoraupdaterestart
Summary:        openQA plugin for restarting failed Fedora update tests
Requires:       openqa

%description plugin-fedoraupdaterestart
This package contains an openQA plugin which restarts update tests that
fail. This is a highly Fedora-specific plugin relying on the flavor
names used for update tests in Fedora. The idea is to re-run failed
tests in case the failure was something transient and unrelated to the
update (network issue, quasi-random bug in underlying package, etc.)

%package client
Summary:        Client tools for remote openQA management
Requires:       openqa-common = %{version}
Requires:       %client_requires

%description client
This package contains the openQA client script, along with several
other useful tools and support files. The client script is a convenient
helper for interacting with the openQA REST API.

%package python-scripts
Summary:        Additional scripts in python
Requires:       %python_scripts_requires

%description python-scripts
Additional scripts for the use of openQA in the python programming language.

%package local-db
Summary:        Helper package to ease setup of postgresql DB
Requires:       %{name} = %{version}
Requires:       postgresql-server
BuildRequires:  postgresql-server
Supplements:    packageand(%name:postgresql-server)

%description local-db
You only need this package if you have a local postgresql server
next to the webui.

%package single-instance
Summary:        Convenience package for a single-instance setup using apache proxy
Provides:       %{name}-single-instance-apache
Provides:       %{name}-single-instance-apache2
Requires:       %{name}-local-db
Requires:       %{name} = %{version}
Requires:       %{name}-worker = %{version}
Requires:       httpd

%description single-instance
Use this package to setup a local instance with all services provided together.

%package single-instance-nginx
Summary:        Convenience package for a single-instance setup using nginx proxy
Requires:       %{name}-local-db
Requires:       %{name} = %{version}
Requires:       %{name}-worker = %{version}
Requires:       nginx

%description single-instance-nginx
Use this package to setup a local instance with all services provided together.

%package bootstrap
Summary:        Automated openQA setup
Requires:       curl
Requires:       iputils
Requires:       procps


%description bootstrap
This can automatically setup openQA - either directly on your system
or within a systemd-nspawn container.

%package doc
Summary:        The openQA documentation

%description doc
Documentation material covering installation, configuration, basic test
writing, etc., covering both openQA and the os-autoinst test engine.

%package munin
Summary:        Munin scripts
Requires:       munin
Requires:       munin-node
Requires:       curl
Requires:       perl-interpreter

%description munin
Use this package to install munin scripts that allow to monitor some openQA
statistics.

%prep
%autosetup -p1 -n %{github_name}-%{github_commit} -a 1
sed -e 's,/bin/env python,/bin/python,' -i script/openqa-label-all
# Fedora calls it httpd.service, SUSE calls it apache2.service...
sed -i -e 's,apache2\.service,httpd\.service,g' systemd/*.service
# ...Fedora keeps httpd config here, SUSE keeps it there.
sed -i -e 's,"$(DESTDIR)"/etc/apache2/vhosts.d,"$(DESTDIR)"%{_sysconfdir}/httpd/conf.d,g' Makefile
sed -i -e 's,/etc/apache2/vhosts.d,%{_sysconfdir}/httpd/conf.d,g' etc/apache2/vhosts.d/*
# ...Fedora keeps nginx config here, SUSE keeps it there.
sed -i -e 's,"$(DESTDIR)"/etc/nginx/vhosts.d,"$(DESTDIR)"%{_sysconfdir}/nginx/conf.d,g' Makefile
# These are the Fedora-y standard TLS cert/key locations.
sed -i -e 's,/etc/apache2/ssl.crt,%{_sysconfdir}/pki/tls/certs,g' etc/apache2/vhosts.d/*
sed -i -e 's,/etc/apache2/ssl.key,%{_sysconfdir}/pki/tls/private,g' etc/apache2/vhosts.d/*
# Add our downstream plugins to the sources
cp %{SOURCE2} lib/OpenQA/WebAPI/Plugin/
cp %{SOURCE3} lib/OpenQA/WebAPI/Plugin/
# we don't really need the tidy test
rm -f t/00-tidy.t
# we don't have the deps for the MCP feature yet
rm -f lib/OpenQA/WebAPI/Plugin/MCP.pm
rm -f t/api/17-mcp.t
# add the fedora-messaging publishing plugin test to the sources
cp %{SOURCE4} t/


%build
# this does nothing, but it's harmless, so just in case it turns up...
make %{?_smp_mflags}

%install
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
%make_install

mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/openqa/script/client %{buildroot}%{_bindir}/openqa-client
ln -s %{_datadir}/openqa/script/openqa-cli %{buildroot}%{_bindir}/openqa-cli
ln -s %{_datadir}/openqa/script/openqa-clone-job %{buildroot}%{_bindir}/openqa-clone-job
ln -s %{_datadir}/openqa/script/openqa-dump-templates %{buildroot}%{_bindir}/openqa-dump-templates
ln -s %{_datadir}/openqa/script/openqa-load-templates %{buildroot}%{_bindir}/openqa-load-templates
ln -s %{_datadir}/openqa/script/openqa-clone-custom-git-refspec %{buildroot}%{_bindir}/openqa-clone-custom-git-refspec
ln -s %{_datadir}/openqa/script/openqa-validate-yaml %{buildroot}%{_bindir}/openqa-validate-yaml
ln -s %{_datadir}/openqa/script/setup-db %{buildroot}%{_bindir}/openqa-setup-db
ln -s %{_datadir}/openqa/script/dump-db %{buildroot}%{_bindir}/openqa-dump-db
ln -s %{_datadir}/openqa/script/openqa-label-all %{buildroot}%{_bindir}/openqa-label-all

install -d -m 755 %{buildroot}%{_datadir}/openqa/client
install -m 755 public/openqa-cli.yaml %{buildroot}%{_datadir}/openqa/client/openqa-cli.yaml

# munin
install -d -m 755 %{buildroot}/%{_datadir}/munin/plugins
install -m 755 contrib/munin/plugins/minion %{buildroot}/%{_datadir}/munin/plugins/openqa_minion_
install -d -m 755 %{buildroot}/%{_sysconfdir}/munin/plugin-conf.d
install -m 644 contrib/munin/config/minion.config %{buildroot}/%{_sysconfdir}/munin/plugin-conf.d/openqa-minion
install -m 755 contrib/munin/utils/munin-mail %{buildroot}/%{_datadir}/openqa/script/munin-mail

# on the whole I think it's "less bad" to install our duplicate copies
# of these over top of the ones from the tarball. if they ever go out
# of sync, at least our scriptlets will match the installed config
# files, rather than there being a mismatch.
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/geekotest.conf
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/openQA-worker.conf

cd %{buildroot}
grep -rl %{_bindir}/env . | while read file; do
    sed -e 's,%{_bindir}/env perl,%{_bindir}/perl,' -i $file
done

# We don't do AppArmor
rm -rf %{buildroot}%{_sysconfdir}/apparmor.d
# these scripts are very SUSE-specific
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-auto-update
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-continuous-update
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-rollback
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-check-devel-repo
rm -f %{buildroot}%{_datadir}/openqa/script/openqa-clean-repo-cache


%check
%if %{with tests}
rm -rf %{buildroot}/DB
export LC_ALL=en_US.UTF-8
# seems necessary to make 24-worker-job.t pass - two subtests there
# rely on one of these files getting uploaded, but that only happens
# if they exist. upstream repo does this in .travis.yml.
touch openqa-debug.log autoinst-log.txt
chmod a+w openqa-debug.log autoinst-log.txt
# we can't use 'unshare' in Fedora package build env
sed -i -e 's,unshare -r -n ,,g' t/40-script_openqa-clone-custom-git-refspec.t
# Skip tests not working currently, or flaky
rm \
    t/01-test-utilities.t \
    t/17-labels_carry_over.t \
    t/25-cache-service.t

# "CI" set with longer timeouts as needed for higher performance variations
# within CI systems, e.g. OBS. See t/lib/OpenQA/Test/TimeLimit.pm
export CI=1
export OPENQA_TEST_TIMEOUT_SCALE_CI=15
# Skip container tests that would need additional requirements, e.g.
# docker-compose. Also, these tests are less relevant (or not relevant) for
# packaging
export CONTAINER_TEST=0
export HELM_TEST=0
# We don't want fatal warnings during package building
export PERL_TEST_WARNINGS_ONLY_REPORT_WARNINGS=1
# GIT_CEILING_DIRECTORIES here avoids a case where git error handling
# can differ when you run the build in mock and cause 16-utils-runcmd
# to fail
make test GIT_CEILING_DIRECTORIES="/" CHECKSTYLE=0 PROVE_ARGS='-r t' TEST_PG_PATH=%{buildroot}/DB
rm -rf %{buildroot}/DB
%endif

%pre
%sysusers_create_compat %{SOURCE5}

%pre worker
%sysusers_create_compat %{SOURCE6}

%post
%tmpfiles_create %{_tmpfilesdir}/openqa-webui.conf
%systemd_post %{openqa_services}

%post worker
%tmpfiles_create %{_tmpfilesdir}/openqa.conf
%systemd_post %{openqa_worker_services}

%post httpd
if [ $1 -eq 1 ]; then
    echo "### copy and edit /etc/httpd/conf.d/openqa.conf.template if using apache!"
    echo "### copy and edit /etc/nginx/conf.d/openqa.conf.template if using nginx!"

fi

%preun
%systemd_preun %{openqa_services}
if [ $1 -eq 0 ]; then
   rm -rf %{_datadir}/openqa/public/packed
fi

%preun worker
%systemd_preun %{openqa_worker_services}

%postun
%systemd_postun_with_restart %{openqa_services}

%postun worker
%systemd_postun_with_restart %{openqa_worker_services}

%post local-db
%systemd_post %{openqa_localdb_services}

%preun local-db
%systemd_preun %{openqa_localdb_services}

%postun local-db
%systemd_postun_with_restart %{openqa_localdb_services}

%files
%doc README.asciidoc
%ghost %config(noreplace) %attr(0644,geekotest,root) %{_sysconfdir}/openqa/openqa.ini
%ghost %config(noreplace) %attr(0640,geekotest,root) %{_sysconfdir}/openqa/database.ini
%dir %{_sysconfdir}/openqa
%dir %{_sysconfdir}/openqa/openqa.ini.d
%dir %{_sysconfdir}/openqa/database.ini.d
%{_datadir}/doc/openqa/examples/openqa.ini
%{_datadir}/doc/openqa/examples/database.ini
%dir %{_datadir}/openqa
%config %{_sysconfdir}/logrotate.d
# init
%{_unitdir}/openqa-webui.service
%{_unitdir}/openqa-livehandler.service
%{_unitdir}/openqa-gru.service
%dir %{_unitdir}/openqa-gru.service.requires
%{_unitdir}/openqa-scheduler.service
%dir %{_unitdir}/openqa-scheduler.service.requires
%{_unitdir}/openqa-websockets.service
%dir %{_unitdir}/openqa-websockets.service.requires
%{_unitdir}/openqa-enqueue-audit-event-cleanup.service
%{_unitdir}/openqa-enqueue-audit-event-cleanup.timer
%{_unitdir}/openqa-enqueue-asset-cleanup.service
%{_unitdir}/openqa-enqueue-asset-cleanup.timer
%{_unitdir}/openqa-enqueue-git-auto-update.service
%{_unitdir}/openqa-enqueue-git-auto-update.timer
%{_unitdir}/openqa-enqueue-result-cleanup.service
%{_unitdir}/openqa-enqueue-result-cleanup.timer
%{_unitdir}/openqa-enqueue-bug-cleanup.service
%{_unitdir}/openqa-enqueue-bug-cleanup.timer
%{_unitdir}/openqa-enqueue-needle-ref-cleanup.service
%{_unitdir}/openqa-enqueue-needle-ref-cleanup.timer
%{_unitdir}/openqa-enqueue-scheduled-product-cleanup.service
%{_unitdir}/openqa-enqueue-scheduled-product-cleanup.timer
%{_tmpfilesdir}/openqa-webui.conf
# web libs
%{_datadir}/openqa/lib/DBIx/
%{_datadir}/openqa/lib/OpenQA/LiveHandler.pm
%{_datadir}/openqa/lib/OpenQA/Resource/
%{_datadir}/openqa/lib/OpenQA/Scheduler/
%{_datadir}/openqa/lib/OpenQA/Schema/
%{_datadir}/openqa/lib/OpenQA/WebAPI/
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraMessaging.pm
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraUpdateRestart.pm
%{_datadir}/openqa/lib/OpenQA/WebSockets/
%{_datadir}/openqa/templates
%{_datadir}/openqa/public
%{_datadir}/openqa/assets
%{_datadir}/openqa/dbicdh
%{_datadir}/openqa/node_modules
%dir %{_datadir}/openqa/script
%{_datadir}/openqa/script/configure-web-proxy
%{_datadir}/openqa/script/create_admin
%{_datadir}/openqa/script/fetchneedles
%{_datadir}/openqa/script/initdb
%{_datadir}/openqa/script/openqa
%{_datadir}/openqa/script/openqa-scheduler
%{_datadir}/openqa/script/openqa-scheduler-daemon
%{_datadir}/openqa/script/openqa-websockets
%{_datadir}/openqa/script/openqa-websockets-daemon
%{_datadir}/openqa/script/openqa-livehandler
%{_datadir}/openqa/script/openqa-livehandler-daemon
%{_datadir}/openqa/script/openqa-enqueue-asset-cleanup
%{_datadir}/openqa/script/openqa-enqueue-audit-event-cleanup
%{_datadir}/openqa/script/openqa-enqueue-bug-cleanup
%{_datadir}/openqa/script/openqa-enqueue-git-auto-update
%{_datadir}/openqa/script/openqa-enqueue-needle-ref-cleanup
%{_datadir}/openqa/script/openqa-enqueue-result-cleanup
%{_datadir}/openqa/script/openqa-enqueue-scheduled-product-cleanup
%{_datadir}/openqa/script/openqa-gru
%{_datadir}/openqa/script/openqa-webui-daemon
%{_datadir}/openqa/script/upgradedb
%{_datadir}/openqa/script/modify_needle
%dir %{_localstatedir}/lib/openqa/share
%defattr(-,geekotest,root)
# the database script does creation with 'geekotest' privileges
%dir %{_localstatedir}/lib/openqa/db
# the server may create files in these locations
%dir %{_localstatedir}/lib/openqa/images
%dir %{_localstatedir}/lib/openqa/webui
%dir %{_localstatedir}/lib/openqa/webui/cache
%dir %{_localstatedir}/lib/openqa/share/factory
%dir %{_localstatedir}/lib/openqa/share/tests
%{_localstatedir}/lib/openqa/testresults
# when sqlite is used this file must be server-writable and *not*
# readable by anyone but server or root, hence expected permissions
%ghost %attr(0640,geekotest,root) %{_localstatedir}/lib/openqa/db/db.sqlite
%{_sysusersdir}/geekotest.conf

%files devel

%files common
%license COPYING
%dir %{_datadir}/doc/openqa
%dir %{_datadir}/doc/openqa/examples
%dir %{_datadir}/openqa
%ghost %dir %{_datadir}/openqa/packed
%{_datadir}/openqa/lib
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraMessaging.pm
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraUpdateRestart.pm
%exclude %{_datadir}/openqa/lib/OpenQA/CacheService/
%exclude %{_datadir}/openqa/lib/DBIx/
%exclude %{_datadir}/openqa/lib/OpenQA/Client.pm
%exclude %{_datadir}/openqa/lib/OpenQA/Client
%exclude %{_datadir}/openqa/lib/OpenQA/UserAgent.pm
%exclude %{_datadir}/openqa/lib/OpenQA/LiveHandler.pm
%exclude %{_datadir}/openqa/lib/OpenQA/Resource/
%exclude %{_datadir}/openqa/lib/OpenQA/Scheduler/
%exclude %{_datadir}/openqa/lib/OpenQA/Schema/
%exclude %{_datadir}/openqa/lib/OpenQA/WebAPI/
%exclude %{_datadir}/openqa/lib/OpenQA/WebSockets/
%exclude %{_datadir}/openqa/lib/OpenQA/Worker/
%dir %{_localstatedir}/lib/openqa
# these are compatibility symlinks into the shared data; they go in
# -common because both server and workers need them but they're not in
# the shared location
%{_localstatedir}/lib/openqa/factory
%{_localstatedir}/lib/openqa/tests
# this is a compat symlink to a directory whose contents are split
# between server and worker
%{_localstatedir}/lib/openqa/script
%{_unitdir}/openqa-minion-restart.service
%{_unitdir}/openqa-minion-restart.path

%files worker
%{_datadir}/openqa/lib/OpenQA/CacheService/
%{_datadir}/openqa/lib/OpenQA/Worker/
%ghost %config(noreplace) %attr(0644,root,root) %{_sysconfdir}/openqa/workers.ini
%ghost %config(noreplace) %attr(0400,_openqa-worker,root) %{_sysconfdir}/openqa/client.conf
%dir %{_sysconfdir}/openqa/workers.ini.d
%dir %{_sysconfdir}/openqa/client.conf.d
%{_datadir}/doc/openqa/examples/workers.ini
%{_datadir}/doc/openqa/examples/client.conf
# init
%dir %{_unitdir}
%{_prefix}/lib/systemd/system-generators/systemd-openqa-generator
%{_unitdir}/openqa-worker.target
%{_unitdir}/openqa-worker.slice
%{_unitdir}/openqa-worker@.service
%{_unitdir}/openqa-worker-plain@.service
%{_unitdir}/openqa-worker-cacheservice-minion.service
%{_unitdir}/openqa-worker-cacheservice.service
%{_unitdir}/openqa-worker-no-cleanup@.service
%{_unitdir}/openqa-worker-auto-restart@.service
%{_unitdir}/openqa-reload-worker-auto-restart@.service
%{_unitdir}/openqa-reload-worker-auto-restart@.path
%{_unitdir}/openqa-slirpvde.service
%{_unitdir}/openqa-vde_switch.service
%{_datadir}/openqa/script/openqa-slirpvde
%{_datadir}/openqa/script/openqa-vde_switch
%{_tmpfilesdir}/openqa.conf
%{_sysusersdir}/openQA-worker.conf
%ghost %dir %attr(0755,_openqa-worker,root) %{_rundir}/openqa
# worker libs
%dir %{_datadir}/openqa
%dir %{_datadir}/openqa/script
%{_datadir}/openqa/script/worker
%{_datadir}/openqa/script/openqa-workercache
%{_datadir}/openqa/script/openqa-workercache-daemon
%{_datadir}/openqa/script/openqa-worker-cacheservice-minion
%dir %{_localstatedir}/lib/openqa/pool
%defattr(-,_openqa-worker,root)
%dir %{_localstatedir}/lib/openqa/cache
# own one pool - to create the others is task of the admin
%dir %{_localstatedir}/lib/openqa/pool/1
%{_prefix}/lib/sysctl.d/01-openqa-reload-worker-auto-restart.conf

# Note: remote workers are required to mount /var/lib/openqa/share
# shared with the server.

%files httpd
%license COPYING
# apache vhost
%config %{_sysconfdir}/httpd/conf.d/openqa.conf.template
%config %{_sysconfdir}/httpd/conf.d/openqa-common.inc
%config %{_sysconfdir}/httpd/conf.d/openqa-ssl.conf.template
# nginx vhost
%dir %{_sysconfdir}/nginx
%dir %{_sysconfdir}/nginx/conf.d
%config %{_sysconfdir}/nginx/conf.d/openqa.conf.template
%config(noreplace) %{_sysconfdir}/nginx/conf.d/openqa-assets.inc
%config(noreplace) %{_sysconfdir}/nginx/conf.d/openqa-endpoints.inc
%config(noreplace) %{_sysconfdir}/nginx/conf.d/openqa-locations.inc
%config(noreplace) %{_sysconfdir}/nginx/conf.d/openqa-upstreams.inc

%files client
%dir %{_datadir}/openqa
%dir %{_datadir}/openqa/client
%{_datadir}/openqa/client/openqa-cli.yaml
%dir %{_datadir}/openqa/script
%{_datadir}/openqa/script/client
%{_datadir}/openqa/script/clone_job.pl
%{_datadir}/openqa/script/dump_templates
%{_datadir}/openqa/script/load_templates
%{_datadir}/openqa/script/openqa-dump-templates
%{_datadir}/openqa/script/openqa-load-templates
%{_datadir}/openqa/script/openqa-cli
%{_datadir}/openqa/script/openqa-clone-job
%{_datadir}/openqa/script/openqa-clone-custom-git-refspec
%{_datadir}/openqa/script/openqa-validate-yaml
%dir %{_datadir}/openqa/lib
%{_datadir}/openqa/lib/OpenQA/Client.pm
%{_datadir}/openqa/lib/OpenQA/Client
%{_datadir}/openqa/lib/OpenQA/UserAgent.pm
%{_bindir}/openqa-client
%{_bindir}/openqa-cli
%{_bindir}/openqa-clone-job
%{_bindir}/openqa-dump-templates
%{_bindir}/openqa-load-templates
%{_bindir}/openqa-clone-custom-git-refspec
%{_bindir}/openqa-validate-yaml

%files python-scripts
%{_datadir}/openqa/script/openqa-label-all
%{_bindir}/openqa-label-all

%files doc
%doc docs/*

%files local-db
%{_unitdir}/openqa-setup-db.service
%{_unitdir}/openqa-dump-db.service
%{_unitdir}/openqa-dump-db.timer
%{_unitdir}/openqa-gru.service.requires/postgresql.service
%{_unitdir}/openqa-scheduler.service.requires/postgresql.service
%{_unitdir}/openqa-websockets.service.requires/postgresql.service
%{_datadir}/openqa/script/setup-db
%{_datadir}/openqa/script/dump-db
%{_bindir}/openqa-setup-db
%{_bindir}/openqa-dump-db
%dir %attr(0755,postgres,root) %{_localstatedir}/lib/openqa/backup

%files single-instance

%files single-instance-nginx

%files bootstrap
%{_datadir}/openqa/script/openqa-bootstrap
%{_datadir}/openqa/script/openqa-bootstrap-container

%files munin
%defattr(-,root,root)
%doc contrib/munin/config/minion.config
%dir %{_datadir}/openqa/script
%dir %{_sysconfdir}/munin
%dir %{_sysconfdir}/munin/plugin-conf.d
%{_datadir}/munin/plugins/openqa_minion_
%{_datadir}/openqa/script/munin-mail
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/openqa-minion

%files plugin-fedora-messaging
%{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraMessaging.pm

%files plugin-fedoraupdaterestart
%{_datadir}/openqa/lib/OpenQA/WebAPI/Plugin/FedoraUpdateRestart.pm

%changelog
%{autochangelog}
