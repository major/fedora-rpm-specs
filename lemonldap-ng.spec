%global lm_prefix %{_prefix}
%global lm_sharedir %{_datadir}/lemonldap-ng
%global lm_examplesdir %{_docdir}/lemonldap-ng/examples
%global lm_vardir %{_localstatedir}/lib/lemonldap-ng
%global lm_cachedir %{_localstatedir}/cache/lemonldap-ng
%global lm_confdir %{_sysconfdir}/lemonldap-ng
%global lm_storagefile %{lm_confdir}/lemonldap-ng.ini
%global lm_bindir %{_libexecdir}/%{name}/bin
%global lm_sbindir %{_libexecdir}/%{name}/sbin

# Apache configuration directory
%global apache_confdir %{_sysconfdir}/httpd/conf.d

# Apache User and Group
%global lm_apacheuser apache
%global lm_apachegroup apache

# Apache version
%global apache_version 2.4

%global lm_dnsdomain example.com

# SELinux
%global with_selinux 1
%global modulename lemonldap-ng
%global selinuxtype targeted

#global pre_release beta1

Name:           lemonldap-ng
Version:        2.17.1
Release:        %{?pre_release:0.}2%{?pre_release:.%{pre_release}}%{?dist}
Summary:        Web Single Sign On (SSO) and Access Management
# Lemonldap-ng itself is GPLv2+
# Qrious bundled javascript library is GPLv3+
# All other bundled javascript libraries are MIT
# Fontawesome bundled font is OFL
License:        GPL-2.0-or-later AND MIT AND GPL-3.0-or-later AND OFL-1.1-RFN
URL:            https://lemonldap-ng.org
Source0:        https://release.ow2.org/lemonldap/%{name}-%{version}%{?pre_release:~%{pre_release}}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gnupg
BuildRequires:  which
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Apache2::Connection)
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::Filter)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::ServerRec)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(Apache::Session::Browseable)
BuildRequires:  perl(Apache::Session::Generate::MD5)
BuildRequires:  perl(APR::Table)
BuildRequires:  perl(AuthCAS)
BuildRequires:  perl(Authen::Captcha)
BuildRequires:  perl(Authen::PAM)
BuildRequires:  perl(Authen::Radius)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Cache::Cache)
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Cache::Memcached)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(constant)
BuildRequires:  perl(Convert::Base32)
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Crypt::OpenSSL::Bignum)
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(Crypt::OpenSSL::X509)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime::Format::RFC3339)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(Email::Sender)
BuildRequires:  perl(Email::Sender::Simple)
BuildRequires:  perl(Email::Sender::Transport::SMTP)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI::Client)
BuildRequires:  perl(FCGI::ProcManager)
BuildRequires:  perl(feature)
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(GD::SecurityImage)
%if 0%{?fedora}%{?el9}
BuildRequires:  perl(GeoIP2)
%endif
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(GSSAPI)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(HTML::Template)
%if 0%{?fedora}%{?el9}
BuildRequires:  perl(HTTP::BrowserDetect)
%endif
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::Timeout)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::XS)
%if 0%{?fedora}
BuildRequires:  perl(Lasso)
BuildRequires:  perl(Glib)
%endif
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(mod_perl2)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Net::CIDR)
BuildRequires:  perl(Net::Facebook::Oauth2)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Extension::SetPassword)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(Net::OpenID::Consumer)
BuildRequires:  perl(Net::OpenID::Server)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::Handler::CGI)
BuildRequires:  perl(Plack::Handler::FCGI)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
%if ! 0%{?el7}
BuildRequires:  perl(Sentry::Raven)
%endif
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(SOAP::Transport::HTTP)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Random)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Time::Fake)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Unicode::String)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
%if ! 0%{?el7}
BuildRequires:  perl(Web::ID)
%endif
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
%if 0%{?fedora}%{?el9}
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif
BuildRequires:  uglify-js

# Doc
%if 0%{?el7}
BuildRequires:  python-sphinx
BuildRequires:  python2-sphinx-bootstrap-theme
%else
BuildRequires:  python3-sphinx-bootstrap-theme
BuildRequires:  python3-sphinx
%endif

Requires: lemonldap-ng-conf = %{version}-%{release}
Requires: lemonldap-ng-doc = %{version}-%{release}
Requires: lemonldap-ng-handler = %{version}-%{release}
Requires: lemonldap-ng-manager = %{version}-%{release}
Requires: lemonldap-ng-portal = %{version}-%{release}
Requires: lemonldap-ng-test = %{version}-%{release}

%if 0%{?with_selinux} && ! 0%{?el7}
# ! Not available in Centos7, you need to install lemonldap-ng-selinux manually
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:        (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif


# Setup requires filtering
%{?perl_default_filter}
%{?el7:%global __requires_exclude perl\\(Lasso|perl\\(Web::ID|perl\\(Sentry::Raven}
%{?el8:%global __requires_exclude perl\\(Lasso}
%{?el9:%global __requires_exclude perl\\(Lasso}


%description
LemonLdap::NG is a modular Web-SSO based on Apache::Session modules. It
simplifies the build of a protected area with a few changes in the
application. It manages both authentication and authorization and provides
headers for accounting.
So you can have a full AAA protection for your web space as described below.

%package conf
Summary:        LemonLDAP-NG configuration
Requires:       perl(Apache::Session)
Requires:       perl(Apache::Session::Browseable)
Requires:       perl(IO::String)
Requires:       perl(Lemonldap::NG::Common) = %{version}-%{release}
Requires:       perl(mod_perl2)
Requires(post): httpd
Requires:       mod_fcgid

%description conf
This package contains the main storage configuration.

%package doc
Summary:        LemonLDAP-NG documentation
Requires:       lemonldap-ng-conf = %{version}-%{release}

%description doc
This package contains HTML documentation.

%package handler
Summary:        LemonLDAP-NG handler
Requires:       crontabs
Requires:       lemonldap-ng-conf = %{version}-%{release}
Requires:       perl(Lemonldap::NG::Handler) = %{version}-%{release}
Requires:       perl(Lemonldap::NG::SSOaaS::Apache::Client) = %{version}-%{release}

%description handler
This package deploys the Apache Handler.

%package manager
Summary:        LemonLDAP-NG administration interface
Requires:       lemonldap-ng-conf = %{version}-%{release}
Requires:       perl(Lemonldap::NG::Manager) = %{version}-%{release}
Provides:       bundled(js-angular) = 1.7.9
Provides:       bundled(js-angular-bootstrap) = 2.5.0
Provides:       bundled(js-angular-ui-tree) = 2.22.6
Provides:       bundled(js-es5-shim)
Provides:       bundled(js-filesaver)

%description manager
This package deploys the administration interface and sessions explorer.

%package portal
Summary:        LemonLDAP-NG authentication portal
Requires:       crontabs
Requires:       lemonldap-ng-conf = %{version}-%{release}
Requires:       perl(Lemonldap::NG::Portal) = %{version}-%{release}
Requires:       perl(Net::Facebook::Oauth2)
Requires:       perl(Net::OAuth)
Requires:       perl(Net::OpenID::Consumer)
Provides:       bundled(fontawesome-fonts) = 4.7.0
Provides:       bundled(js-bootstrap) = 4.5.2
Provides:       bundled(js-fingerprint2) = 2.1.4
Provides:       bundled(js-jquery) = 3.5.1
Provides:       bundled(js-jquery-ui) = 1.13.2
Provides:       bundled(js-qrious)

%description portal
This package deploys the authentication portal.

%package test
Summary:        LemonLDAP-NG test applications
Requires:       lemonldap-ng-conf = %{version}-%{release}

%description test
This package deploys small test applications.

%package fastcgi-server
Summary:        LemonLDAP-NG FastCGI Server
Requires:       lemonldap-ng-conf = %{version}-%{release}
Requires:       mod_fcgid
Requires:       perl(FCGI::ProcManager)

%description fastcgi-server
This package deploys files needed to start a FastCGI server.

%package uwsgi-app
Summary:        LemonLDAP-NG UWSGI Application
Requires:       uwsgi-plugin-psgi

%description uwsgi-app
LemonLDAP::NG uWSGI server provides a replacement to LemonLDAP::NG FastCGI
server, using uWSGI instead of Plack FCGI.

%package nginx
Summary:        LemonLDAP-NG Nginx support
Requires:       nginx

%description nginx
Nginx support for LemonLDAP::NG.

%package -n perl-Lemonldap-NG-Common
Summary:        LemonLDAP-NG Common Modules
Requires:       perl(JSON::XS)
Requires:       perl(String::Random)
Requires:       perl(Cache::Cache)

%description -n perl-Lemonldap-NG-Common
This package installs the configuration libraries used by other LemonLDAP::NG
modules.

%package -n perl-Lemonldap-NG-Handler
Summary:        LemonLDAP-NG Handler Modules

%description -n perl-Lemonldap-NG-Handler
This package installs the Apache module part (handler) used to protect web
areas.

%package -n perl-Lemonldap-NG-Manager
Summary:        LemonLDAP-NG Manager Modules

%description -n perl-Lemonldap-NG-Manager
This package installs the administration interface (manager).

%package -n perl-Lemonldap-NG-Portal
Summary:        LemonLDAP-NG Portal Modules

%description -n perl-Lemonldap-NG-Portal
This package installs the authentication portal.

%if 0%{?with_selinux}
%package selinux
Summary:             LemonLDAP-NG SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}

%description selinux
Custom SELinux policy module
%endif

%package -n perl-Lemonldap-NG-SSOaaS-Apache-Client
Summary:        Lemonldap-NG SSOaaS client for Apache

%description -n perl-Lemonldap-NG-SSOaaS-Apache-Client
This package permits one to enroll an Apache server
into Lemonldap::NG's SSOaaS service.


%prep
%setup -q -n %{name}-%{version}%{?pre_release:~%{pre_release}}


%build
%make_build configure \
    STORAGECONFFILE=%{lm_storagefile} \
    DATADIR=%{lm_vardir} \
    CACHEDIR=%{lm_cachedir} \
    PERLOPTIONS="INSTALLDIRS=vendor"
%make_build

%if 0%{?with_selinux}
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module
mkdir selinux
cp -p rpm/lemonldap-ng.fc selinux/
cp -p rpm/lemonldap-ng.te selinux/

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif


%install
%make_install \
    PREFIX=%{lm_prefix} \
    BINDIR=%{lm_bindir} \
    SBINDIR=%{lm_sbindir} \
    FASTCGISOCKDIR=%{_rundir}/llng-fastcgi-server \
    DOCUMENTROOT=%{lm_sharedir} \
    EXAMPLESDIR=%{lm_examplesdir} \
    HANDLERDIR=%{lm_sharedir}/handler \
    MANAGERDIR=%{lm_sharedir}/manager \
    STORAGECONFFILE=%{lm_storagefile} \
    TOOLSDIR=%{lm_sharedir}/ressources \
    CONFDIR=%{lm_confdir} \
    CRONDIR=%{_sysconfdir}/cron.d \
    DATADIR=%{lm_vardir} \
    CACHEDIR=%{lm_cachedir} \
    INITDIR=%{_sysconfdir}/init.d \
    ETCDEFAULTDIR=%{_sysconfdir}/default \
    DNSDOMAIN=%{lm_dnsdomain} \
    APACHEVERSION=%{apache_version} \
    APACHELOGDIR=%{_localstatedir}/log/httpd \
    UWSGIYAMLDIR=%{_sysconfdir}/uwsgi/apps-available \
    LLNGAPPDIR=%{lm_sharedir}/llng-server \
    PROD=yes

# Remove some unwanted files
find %{buildroot} -name .packlist -exec rm -f {} \;
find %{buildroot} -name perllocal.pod -exec rm -f {} \;
find %{buildroot} -name *.bak -exec rm -f {} \;

# Install files for FastCGI Server
mkdir -p %{buildroot}%{_unitdir}
install -m644 fastcgi-server/systemd/llng-fastcgi-server.service \
    %{buildroot}%{_unitdir}
sed -i \
    -e 's:__FASTCGISOCKDIR__:%{_rundir}/llng-fastcgi-server:' \
    -e 's:__SBINDIR__:%{lm_sbindir}:' \
    %{buildroot}%{_unitdir}/llng-fastcgi-server.service
rm -f %{buildroot}%{_sysconfdir}/init.d/llng-fastcgi-server

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m644 fastcgi-server/systemd/llng-fastcgi-server.tmpfile \
    %{buildroot}%{_tmpfilesdir}/llng-fastcgi-server.conf
sed -i \
    -e 's:__FASTCGISOCKDIR__:%{_rundir}/llng-fastcgi-server:' \
    -e 's:__USER__:%{lm_apacheuser}:' \
    -e 's:__GROUP__:%{lm_apachegroup}:' \
    %{buildroot}%{_tmpfilesdir}/llng-fastcgi-server.conf

# UWSGI Application
mkdir -p %{buildroot}%{_sysconfdir}/uwsgi/apps-available
mkdir -p %{buildroot}%{lm_sharedir}/llng-server

# Set apache user in some files (see Makefile)
# Note: we do not use the APACHEUSER and APACHEGROUP in make install
# because it launches a 'chown', which is not permitted if RPM is not
# built as root
sed -i 's/nobody/%{lm_apacheuser}/g' \
    %{buildroot}%{_sysconfdir}/cron.d/* \
    %{buildroot}%{lm_bindir}/lmConfigEditor \
    %{buildroot}%{lm_bindir}/lemonldap-ng-sessions \
    %{buildroot}%{lm_bindir}/lemonldap-ng-cli \
    %{buildroot}%{lm_bindir}/llngDeleteSession \
    %{buildroot}%{_sysconfdir}/default/llng-fastcgi-server

# Install httpd conf files
# We use "z-lemonldap-ng-*" so that httpd read the files after "perl.conf"
mkdir -p %{buildroot}%{apache_confdir}
for i in handler manager portal api test; do {
    mv %{buildroot}%{lm_confdir}/$i-apache%{apache_version}.conf \
        %{buildroot}%{apache_confdir}/z-lemonldap-ng-$i.conf
}; done

# Install nginx conf files
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d/
mv %{buildroot}%{lm_confdir}/*nginx*.conf \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/
# Move lua and log configuration
mv %{buildroot}%{_sysconfdir}/nginx/conf.d/nginx-lua-headers.conf \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/nginx-lmlog.conf \
    %{buildroot}%{_sysconfdir}/nginx/
# Replace paths in main configuration files
sed -i 's:/etc/lemonldap-ng/nginx-lmlog.conf:/etc/nginx/nginx-lmlog.conf:' \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/handler-nginx.conf
sed -i 's:/etc/lemonldap-ng/nginx-lua-headers.conf:/etc/nginx/nginx-lua-headers.conf:' \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/test-nginx.conf

# Remove for_etc_hosts from %%{_sysconfdir}
mv %{buildroot}%{lm_confdir}/for_etc_hosts .

# Fix shebang and perms
sed -i -e 's,#!/usr/bin/env plackup,#!/usr/bin/plackup,' \
    %{buildroot}%{lm_sharedir}/manager/api/api.psgi \
    %{buildroot}%{lm_sharedir}/manager/htdocs/manager.psgi \
    %{buildroot}%{lm_examplesdir}/manager/manager.psgi
chmod 755 \
    %{buildroot}%{lm_sharedir}/manager/api/api.psgi \
    %{buildroot}%{lm_sharedir}/manager/htdocs/manager.psgi \
    %{buildroot}%{lm_examplesdir}/manager/manager.psgi
sed -i -e '1i#!/usr/bin/plackup' \
    %{buildroot}%{lm_examplesdir}/llngapp.psgi
chmod 644 %{buildroot}%{lm_sharedir}/test/cas.php

# Install SELinux policy
%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 \
    %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%endif

%check
# This test requires network, use "--with network_tests" to execute it
%{?!_with_network_tests:rm lemonldap-ng-portal/t/02-Password-Demo-checkHIBP.t}
sed -i 's:^dirName.*:dirName = %{buildroot}%{lm_vardir}/conf:' \
    %{buildroot}%{lm_storagefile}
make %{?_smp_mflags} test \
    LLNG_DEFAULTCONFFILE=%{buildroot}%{lm_storagefile}
sed -i 's:^dirName.*:dirName = %{lm_vardir}/conf:' \
    %{buildroot}%{lm_storagefile}


%post conf
# Upgrade from previous version
# See http://lemonldap-ng.org/documentation/1.0/upgrade
if [ $1 -gt 1 ] ; then
    if [ -e %{lm_confdir}/storage.conf \
         -o -e %{lm_confdir}/apply.conf \
         -o -e %{lm_confdir}/apps-list.xml ] ; then
        # Run migration script
        %{lm_bindir}/lmMigrateConfFiles2ini 2>&1 > /dev/null || :
        # Fix ownership
        chgrp %{lm_apachegroup} %{lm_storagefile} || :
    fi
fi

%preun conf
# Upgrade from previous version
if [ $1 -eq 1 ] ; then
    # Remove old symlinks in Apache configuration
    find %{apache_confdir} -name 'z-lemonldap-ng*.conf' \
        -type l -delete 2>&1 > /dev/null || :
fi

%post fastcgi-server
%systemd_post llng-fastcgi-server.service

%preun fastcgi-server
%systemd_preun llng-fastcgi-server.service

%postun fastcgi-server
%systemd_postun_with_restart llng-fastcgi-server.service

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}
# if with_selinux
%endif


%files

%files conf
%doc changelog README.md AUTHORS CONTRIBUTING.md
%doc for_etc_hosts
%license COPYING LICENSE
%dir %{lm_confdir}
%config(noreplace) %attr(-,root,%{lm_apachegroup}) %{lm_storagefile}
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-handler.conf
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-manager.conf
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-api.conf
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-portal.conf
%{_mandir}/man1/convertConfig*
%{_mandir}/man1/convertSessions*
%{_mandir}/man1/encryptTotpSecrets*
%{_mandir}/man1/lemonldap-ng-sessions*
%dir %{_libexecdir}/%{name}
%dir %{lm_sbindir}
%dir %{lm_bindir}
%{lm_bindir}/convertConfig
%{lm_bindir}/convertSessions
%{lm_bindir}/encryptTotpSecrets
%{lm_bindir}/lemonldap-ng-sessions
%{lm_bindir}/importMetadata
%{lm_bindir}/lmMigrateConfFiles2ini
%{lm_bindir}/rotateOidcKeys
%dir %{lm_examplesdir}
%dir %{lm_sharedir}
%{lm_sharedir}/ressources/
%dir %{lm_vardir}
%defattr(640,%{lm_apacheuser},%{lm_apachegroup},750)
%dir %{lm_vardir}/conf
%dir %{lm_vardir}/sessions
%dir %{lm_vardir}/sessions/lock
%dir %{lm_vardir}/psessions
%dir %{lm_vardir}/psessions/lock
%dir %{lm_vardir}/notifications
%dir %{lm_cachedir}
%config(noreplace) %{lm_vardir}/conf/lmConf-1.json

%files doc
%doc %{lm_sharedir}/doc
%doc changelog README.md AUTHORS CONTRIBUTING.md
%license COPYING LICENSE

%files handler
%{lm_bindir}/purgeLocalCache
%config(noreplace) %{_sysconfdir}/cron.d/lemonldap-ng-handler
%{lm_sharedir}/handler
%{lm_examplesdir}/handler
%{lm_sharedir}/llng-server/

%files manager
%{lm_sharedir}/manager
%{lm_examplesdir}/manager
%{lm_bindir}/lmConfigEditor
%{lm_bindir}/lemonldap-ng-cli
%{lm_bindir}/llngDeleteSession
%{_mandir}/man1/lemonldap-ng-cli*
%{_mandir}/man1/importMetadata*

%files portal
%{lm_sharedir}/portal
%{lm_bindir}/purgeCentralCache
%config(noreplace) %{_sysconfdir}/cron.d/lemonldap-ng-portal
%{lm_examplesdir}/portal
%defattr(-,%{lm_apacheuser},%{lm_apachegroup},750)
%dir %{lm_vardir}/captcha

%files test
%{lm_sharedir}/test
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-test.conf

%files fastcgi-server
%{lm_sbindir}/llng-fastcgi-server
%config(noreplace) %{_sysconfdir}/default/llng-fastcgi-server
%{_unitdir}/llng-fastcgi-server.service
%{_tmpfilesdir}/llng-fastcgi-server.conf
%defattr(755,%{lm_apacheuser},%{lm_apachegroup},755)
%dir %{_rundir}/llng-fastcgi-server
%{lm_examplesdir}/llngapp.psgi

%files uwsgi-app
%config(noreplace) %{_sysconfdir}/uwsgi/apps-available/llng-server.yaml

%files nginx
%config(noreplace) %{_sysconfdir}/nginx/conf.d/handler-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/manager-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/nginx-lmlog.conf
%config(noreplace) %{_sysconfdir}/nginx/nginx-lua-headers.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/portal-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/api-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/test-nginx.conf

%files -n perl-Lemonldap-NG-Common
%{_mandir}/man3/Lemonldap::NG::Common*.3pm.*
%dir %{perl_vendorlib}/Lemonldap
%dir %{perl_vendorlib}/Lemonldap/NG
%{perl_vendorlib}/Lemonldap/NG/Common.pm
%{perl_vendorlib}/Lemonldap/NG/Common/
%{perl_vendorlib}/auto/Lemonldap/NG/Common/

%files -n perl-Lemonldap-NG-Handler
%{_mandir}/man3/Lemonldap::NG::Handler*.3pm.*
%{_mandir}/man3/Plack::Middleware::Auth::LemonldapNG.3pm.*
%{perl_vendorlib}/Lemonldap/NG/Handler.pm
%{perl_vendorlib}/Lemonldap/NG/Handler/
%{perl_vendorlib}/auto/Lemonldap/NG/Handler/
%{perl_vendorlib}/Plack/Middleware/Auth/LemonldapNG.pm

%files -n perl-Lemonldap-NG-Manager
%{_mandir}/man3/Lemonldap::NG::Manager*.3pm.*
%{perl_vendorlib}/Lemonldap/NG/Manager.pm
%{perl_vendorlib}/Lemonldap/NG/Manager/

%files -n perl-Lemonldap-NG-Portal
%{_mandir}/man3/Lemonldap::NG::Portal*.3pm.*
%{perl_vendorlib}/Lemonldap/NG/Portal.pm
%{perl_vendorlib}/Lemonldap/NG/Portal/

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%files -n perl-Lemonldap-NG-SSOaaS-Apache-Client
%{_mandir}/man3/Lemonldap::NG::SSOaaS::Apache*.3pm.*
%{perl_vendorlib}/Lemonldap/NG/SSOaaS/Apache/


%changelog
* Mon Oct 02 2023 Xavier Bachelot <xavier@bachelot.org> - 2.17.1-2
- Add a dep on SSOaaS version
- Simplify fix shebang and perms
- Drop INSTALL from %doc

* Mon Sep 25 2023 Clement Oudot <clem.oudot@gmail.com> - 2.17.1-1
- Update to 2.17.1

* Wed Aug 30 2023 Clement Oudot <clem.oudot@gmail.com> - 2.17.0-1
- Update to 2.17.0

* Mon May 15 2023 Xavier Bachelot <xavier@bachelot.org> - 2.16.2-2
- Improve Summary:
- Drop updates-alternatives from %%post
- Split long line
- Drop useless comments
- Add provides for bundled javascript libraries and adapt License tag accordingly
- Add provides for bundled font and adapt License tag accordingly
- Make use of %%lm_sharedir instead of plain path
- Add BR: for uglify-js
- Move examples to %%_docdir
- Fix perms on %%lm_vardir/captcha and %%_rundir/llng-fastcgi-server
- Drop redundant dirs creation and perms change
- Conditionalize test that needs network access

* Fri May 12 2023 Clement Oudot <clem.oudot@gmail.com> - 2.16.2-1
- Update to 2.16.2

* Tue Mar 28 2023 Clement Oudot <clem.oudot@gmail.com> - 2.16.1-1
- Update to 2.16.1

* Wed Feb 01 2023 Clement Oudot <clem.oudot@gmail.com> - 2.0.16-1
- Update to 2.0.16

* Thu Sep 15 2022 Clement Oudot <clem.oudot@gmail.com> - 2.0.15.1-1
- Update to 2.0.15.1

* Fri Sep 09 2022 Clement Oudot <clem.oudot@gmail.com> - 2.0.15-1
- Update to 2.0.15

* Thu Feb 24 2022 Xavier Bachelot <xavier@bachelot.org> - 2.0.14-2
- Prepare for EL9 support

* Sat Feb 19 2022 Clement Oudot <clem.oudot@gmail.com> - 2.0.14-1
- Update to 2.0.14

* Fri Aug 20 2021 Clement Oudot <clem.oudot@gmail.com> - 2.0.13-1
- Update to 2.0.13

* Thu Jul 22 2021 Clement Oudot <clem.oudot@gmail.com> - 2.0.12-1
- Update to 2.0.12

* Wed Mar 17 2021 Xavier Bachelot <xavier@bachelot.org> - 2.0.11-2
- Add BR: make

* Sat Jan 30 2021 Clement Oudot <clem.oudot@gmail.com> - 2.0.11-1
- Update to 2.0.11

* Sun Jan 17 2021 Clement Oudot <clem.oudot@gmail.com> - 2.0.10-1
- Update to 2.0.10

* Sun Sep 06 2020 Clement Oudot <clem.oudot@gmail.com> - 2.0.9-1
- Update to 2.0.9

* Tue May 05 2020 Clement Oudot <clem.oudot@gmail.com> - 2.0.8-1
- Update to 2.0.8

* Sat Dec 21 2019 Clement Oudot <clem.oudot@gmail.com> - 2.0.7-1
- Update to 2.0.7

* Fri Dec 06 2019 Xavier Bachelot <xavier@bachelot.org> - 2.0.6-2
- Tweak for EL8.
- Enhance BuildRequires and Requires.
- Spec clean up.

* Tue Sep 24 2019 Clement Oudot <clem.oudot@gmail.com> - 2.0.6-1
- Update to 2.0.6

* Sat Jun 29 2019 Clement Oudot <clem.oudot@gmail.com> - 2.0.5-1
- Update to 2.0.5

* Fri Jun 07 2019 Xavier Bachelot <xavier@bachelot.org> - 2.0.4-2
- BR: gnupg to fix test 29-AuthGPG.t failure in manager.

* Sun May 12 2019 Clement Oudot <clem.oudot@gmail.com> - 2.0.4-1
- Update to 2.0.4

* Thu Apr 11 2019 Clement Oudot <clem.oudot@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Tue Feb 12 2019 Clement Oudot <clem.oudot@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Fri Dec 21 2018 Clement Oudot <clem.oudot@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Sat Dec 01 2018 Clement Oudot <clem.oudot@gmail.com> - 2.0.0-3
- Fix warnings in Manager

* Fri Nov 30 2018 Xavier Bachelot <xavier@bachelot.org> - 2.0.0-2
- Huge spec file cleanup.

* Fri Nov 30 2018 Clement Oudot <clem.oudot@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Fri Jul 20 2018 Clement Oudot <clem.oudot@gmail.com> - 2.0.0~beta1-1
- First beta version for 2.0.0

* Fri Jan 26 2018 Clement Oudot <clem.oudot@gmail.com> - 2.0.0~alpha3-1
- Third alpha version for 2.0.0

* Thu Sep 14 2017 Clement Oudot <clem.oudot@gmail.com> - 2.0.0~alpha2-1
- Second alpha version for 2.0.0

* Mon Jul 10 2017 Clement Oudot <clem.oudot@gmail.com> - 2.0.0~alpha1-1
- First alpha version for 2.0.0

* Fri May 19 2017 Clement Oudot <clem.oudot@gmail.com> - 1.9.10-1
- Update to 1.9.10

* Thu Mar 16 2017 Clement Oudot <clem.oudot@gmail.com> - 1.9.9-1
- Update to 1.9.9

* Thu Mar 02 2017 Clement Oudot <clem.oudot@gmail.com> - 1.9.8-1
- Update to 1.9.8

* Mon Dec 12 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.7-1
- Update to 1.9.7

* Fri Oct 14 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.6-1
- Update to 1.9.6

* Wed Jul 13 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.5-1
- Update to 1.9.5

* Tue Jun 14 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.4-1
- Update to 1.9.4

* Tue Jun 07 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.3-1
- Update to 1.9.3

* Sun May 01 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Thu Mar 31 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.1-1
- Update to 1.9.1

* Wed Mar 02 2016 Clement Oudot <clem.oudot@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Mon Sep 28 2015 Clement Oudot <clem.oudot@gmail.com> - 1.4.6-1
- Update to 1.4.6

* Mon May 11 2015 Clement Oudot <clem.oudot@gmail.com> - 1.4.5-1
- Update to 1.4.5

* Wed Apr 15 2015 Clement Oudot <clem.oudot@gmail.com> - 1.4.4-1
- Update to 1.4.4

* Thu Dec 18 2014 Clement Oudot <clem.oudot@gmail.com> - 1.4.3-1
- Update to 1.4.3
- Support for CentOS 7

* Fri Oct 31 2014 Clement Oudot <clem.oudot@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jul 25 2014 Clement Oudot <clem.oudot@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Fri Apr 18 2014 Clement Oudot <clem.oudot@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Fri Mar 07 2014 Clement Oudot <clem.oudot@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Thu Jan 23 2014 Clement Oudot <clem.oudot@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Mon Nov 11 2013 Clement Oudot <clem.oudot@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Sat Nov 2 2013 Clement Oudot <clem.oudot@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Mon Aug 26 2013 Clement Oudot <clem.oudot@gmail.com> - 1.2.5-1
- Update to 1.2.5

* Tue Apr 23 2013 Clement Oudot <clem.oudot@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Fri Feb 08 2013 Clement Oudot <clem.oudot@gmail.com> - 1.2.3-1
- Update to 1.2.3

* Mon Sep 17 2012 Clement Oudot <clem.oudot@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Thu Jul 05 2012 Clement Oudot <clem.oudot@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Sun Jun 17 2012 Clement Oudot <clem.oudot@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Fri Oct 07 2011 Clement Oudot <clem.oudot@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Fri Jul 29 2011 Clement Oudot <clem.oudot@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Fri Jul 08 2011 Clement Oudot <clem.oudot@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Thu Jun 30 2011 Clement Oudot <clem.oudot@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Fri Apr 15 2011 Clement Oudot <clem.oudot@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Tue Mar 22 2011 Clement Oudot <clem.oudot@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Mon Mar 07 2011 Clement Oudot <clem.oudot@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Mon Feb 28 2011 Clement Oudot <clem.oudot@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Thu Dec 16 2010 Clement Oudot <clem.oudot@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Fri Nov 26 2010 Clement Oudot <clem.oudot@gmail.com> - 1.0-1
- Update to 1.0

* Wed Jul 21 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.9.4.1-3
- Fix compatibility with perl-LDAP 0.40
- Add BR perl(Auth::CAS)

* Mon Jul 12 2010 Nicolas Chauvet <nchauvet@linagora.com> - 0.9.4.1-2
- Protect lemonldap directories against word readability

* Mon Oct 12 2009 Nicolas Chauvet <nchauvet@linagora.com> - 0.9.4.1-1
- Update to 0.9.4.1

* Thu Sep 24 2009 Nicolas Chauvet <nchauvet@linagora.com> - 0.9.4-2
- Add Missing BuildRequires
- Remove filter for dependencies available in EPEL.
- use %%defattr to define ownership.

* Mon Jul 6 2009 Clement Oudot <coudot@linagora.com> - 0.9.4-1
- Upgrade to release 0.9.4
- Remove cronjob patch (included in 0.9.4)
- Split scriplets into subpackages
- Use conditions to build for other RPM distributions like OpenSuSE (thanks to clauded1)

* Mon Jan 12 2009 Clement Oudot <coudot@linagora.com> - 0.9.3.2-2
- Include cronjob patch
- Delete unwanted files (perllocal.pod, .packlist)
- Follow rpmfusion guidelines

* Fri Jan 9 2009 Clement Oudot <coudot@linagora.com> - 0.9.3.2-1
- Updated to release 0.9.3.2.
- Use internal version number for perl modules (compatibility with RPMforge packages)
- Merge with existing .spec file from RPMforge.
- Use the same directories as the Debian package.
- Create a symlink in Apache confguration.
- Create specific portal/manager/handler/conf packages independent from CPAN packages

* Thu Nov 20 2008 Jean-Christophe Toussaint <jean-christophe.toussaint@ac-nancy-metz.fr> - 0.9.2-1DSI
- Updated to release 0.9.2.
- Using official tar.gz from forge.

* Tue Oct 7 2008 David Hannequin <david.hannequin@linagora.com> 
- New spec file

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 0.85-1
- Updated to release 0.85.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.84-1
- Updated to release 0.84.

* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 0.81-1
- Updated to release 0.81.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.75-1
- Initial package.
