%if 0%{?fedora} >= 43
ExcludeArch: %{ix86}
%endif

%bcond_with autoreconf
%bcond_with authorcheck

# Unbundling helper macro
# %1 is the path to dir bundling files (from)
# %2 is the path to dir containing original files (with)
%global unbundle_from_with() \
  bundled_dir="%{buildroot}%1" \
  bundled_files="$(find "${bundled_dir}" -maxdepth 1 -type f -printf '%f\\n')" \
  original_dir="%2" \
  for file in ${bundled_files} \
  do \
    if [ -f "${original_dir}/${file}" ] \
    then \
      rm -f "${bundled_dir}/${file}" \
      ln -s "${original_dir}/${file}" "${bundled_dir}/${file}" \
    fi \
  done

# Bundled Fonts
#
# Fontawesome 6.4 is only available in F39+
%global unbundle_fontawesome       0%{?fc39}
# Not available for EL
%global unbundle_raleway           0

# Bundled javascripts
#
# Not available
%global unbundle_foundation        0
# Not available for EL
%global unbundle_html5shiv         0
# Not available for EL7
%global unbundle_jquery            0%{?fedora}%{?el8}%{?el9}%{?el10}
# Available version is too old
%global unbundle_jquery_migrate    0
# Not available
%global unbundle_jquery_minicolors 0
#
%global unbundle_jquery_ui         0%{?fedora}%{?el8}%{?el9}%{?el10}
# Only available for Fedora
%global unbundle_jqplot            0
#
%global unbundle_respond           0

# Licenses
# Sympa itself is GPLv2+.
# Possibly bundled fonts are :
# - fontawesome-fonts :      OFL
# - fontawesome-fonts-web:   OFL and MIT
# - impallari-raleway-fonts: OFL
# - foundation-icons-fonts:  MIT
# Possibly bundled javascripts are :
# - js-html5shiv:            MIT or GPLv2
# - js-jquery-jqplot:        MIT or GPLv2
# - js-jquery:               MIT
# - js-respond:              MIT
# - js-jquery-ui:            MIT
# - js-foundation:           MIT
# - js-jquery-migrate:       MIT
# - js-jquery-minicolors:    MIT
%global licenses_bundled     %{nil} 
# OFL and MIT
%if ! %{unbundle_fontawesome}
%global licenses_bundled %{licenses_bundled} AND (OFL-1.1-RFN AND MIT)
%endif
# OFL
%if ! %{unbundle_raleway}
%global licenses_bundled %{licenses_bundled} AND OFL-1.1-RFN
%endif
# MIT
%if ! %{unbundle_foundation} || ! %{unbundle_jquery} || ! %{unbundle_jquery_migrate} || ! %{unbundle_jquery_minicolors} || ! %{unbundle_jquery_ui} || ! %{unbundle_respond}
%global licenses_bundled %{licenses_bundled} AND MIT
%endif
# MIT or GPLv2
%if ! %{unbundle_html5shiv} || ! %{unbundle_jqplot}
%global licenses_bundled %{licenses_bundled} and (MIT OR GPL-2.0-only)
%endif

%global static_content %{_datadir}/sympa/static_content

#global pre_rel b.2

Name:        sympa
Version:     6.2.76
Release:     %{?pre_rel:0.}1%{?pre_rel:.%pre_rel}%{?dist}.3
Summary:     Powerful multilingual List Manager
Summary(fr): Gestionnaire de listes électroniques
Summary(ja): 高機能で多言語対応のメーリングリスト管理ソフトウェア
# The License: tag depends on bundled code for a given distro/release
License:     GPL-2.0-or-later%{licenses_bundled}
URL:         http://www.sympa.org
Source0:     https://github.com/sympa-community/sympa/releases/download/%{version}%{?pre_rel}/%{name}-%{version}%{?pre_rel}.tar.gz

Source101:   sympa-httpd24-spawn_fcgi.conf
Source102:   sympa-lighttpd.conf
Source103:   sympa-nginx-spawn_fcgi.conf
Source106:   sympa-rsyslog.conf
Source107:   sympa-logrotate.conf
Source113:   sympa-systemd-README.RPM.md
Source114:   aliases.sympa.sendmail
Source115:   aliases.sympa.postfix
Source129:   sympa.service.d-dependencies.conf
Source130:   sympa-sysconfig

# RPM specific customization of site defaults
Patch13:     sympa-6.2.57b.1-confdef.patch

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: make
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd
%endif
BuildRequires: tzdata

# Only for development
%if %{with autoreconf}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
%endif

BuildRequires: perl-generators
# install & check
BuildRequires: perl(Archive::Zip::SimpleZip)
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(CGI::Cookie)
BuildRequires: perl(CGI::Fast)
BuildRequires: perl(CGI::Util)
BuildRequires: perl(Class::Singleton)
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Password)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Encode)
BuildRequires: perl(Encode::Guess)
BuildRequires: perl(Encode::MIME::Header)
BuildRequires: perl(English)
BuildRequires: perl(FCGI)
BuildRequires: perl(Fcntl)
BuildRequires: perl(feature)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::NFSLock)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::stat)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTML::FormatText)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(HTML::StripScripts::Parser)
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(if)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(IO::Socket::IP)
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(lib)
BuildRequires: perl(Locale::Messages)
BuildRequires: perl(LWP::Protocol::https)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Mail::Address)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(MIME::Charset)
BuildRequires: perl(MIME::EncWords)
BuildRequires: perl(MIME::Entity)
BuildRequires: perl(MIME::Field::ParamVal)
BuildRequires: perl(MIME::Head)
BuildRequires: perl(MIME::Lite::HTML)
BuildRequires: perl(MIME::Parser)
BuildRequires: perl(MIME::Tools)
BuildRequires: perl(Net::CIDR)
BuildRequires: perl(Net::LDAP)
BuildRequires: perl(parent)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(POSIX)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(SOAP::Lite)
BuildRequires: perl(SOAP::Transport::HTTP)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Sys::Syslog)
BuildRequires: perl(Template)
BuildRequires: perl(Term::ProgressBar)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Net::LDAP)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Text::LineFold)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Time::Local)
BuildRequires: perl(Unicode::GCString)
BuildRequires: perl(Unicode::Normalize)
BuildRequires: perl(Unicode::UTF8)
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(warnings)
BuildRequires: perl(XML::LibXML)

# authorcheck
%if %{with authorcheck}
BuildRequires: perl(Test::Fixme)
BuildRequires: perl(Test::Perl::Critic)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Pod::Spelling::CommonMistakes)
%endif

%{?systemd_requires}
Requires:    smtpdaemon
Requires:    mhonarc
Requires:    logrotate
Requires:    perl(DBD::mysql)
Requires:    perl(FCGI)

# Optional CPAN packages
Requires:    perl(Archive::Zip::SimpleZip)
Requires:    perl(AuthCAS)
Requires:    perl(Clone)
Requires:    perl(Crypt::CipherSaber)
Requires:    perl(Crypt::Eksblowfish)
Requires:    perl(Crypt::OpenSSL::X509)
Requires:    perl(Crypt::SMIME)
Requires:    perl(Data::Password)
Requires:    perl(DateTime::TimeZone)
Requires:    perl(DBD::CSV)
Requires:    perl(Encode::Locale)
# Recommended for handling Japanese vendor codepages.
Requires:    perl(Encode::EUCJPASCII)
# Handling several Chinese standards.
Requires:    perl(Encode::HanExtra)
Requires:    perl(IO::Socket::IP)
Requires:    perl(IO::Socket::SSL)
Requires:    perl(List::Util::XS)
Requires:    perl(LWP::Protocol::https)
Requires:    perl(Mail::DKIM::Verifier)
Requires:    perl(Net::DNS)
Requires:    perl(Net::SMTP)
Requires:    perl(Unicode::Normalize)
Requires:    perl(Unicode::UTF8)

# Bundled fonts
%if %{unbundle_fontawesome}
BuildRequires: fontawesome-fonts-web >= 6.4.0
Requires:      fontawesome-fonts-web >= 6.4.0
%else
Provides:      bundled(fontawesome-fonts) = 6.4.0
%endif
%if %{unbundle_raleway}
BuildRequires: impallari-raleway-fonts >= 3.0
Requires:      impallari-raleway-fonts >= 3.0
%else
Provides:      bundled(impallari-raleway-fonts) = 3.0
%endif

# Bundled javascript libs
# foundation
%if %{unbundle_foundation}
BuildRequires: js-foundation6 >= 6.4.2
Requires:      js-foundation6 >= 6.4.2
%else
Provides:      bundled(js-foundation) = 6.4.2
# Bundled in bundled js-foundation
Provides:      bundled(js-what-input) = 4.2.0
%endif
# html5shiv
%if %{unbundle_html5shiv}
BuildRequires: js-html5shiv >= 3.7.2
Requires:      js-html5shiv >= 3.7.2
%else
Provides:      bundled(js-html5shiv) = 3.7.2
%endif
# jquery
%if %{unbundle_jquery}
BuildRequires: js-jquery3 >= 3.5.0
Requires:      js-jquery3 >= 3.5.0
%else
Provides:      bundled(js-jquery) = 3.6.0
%endif
# jquery-migrate
%if %{unbundle_jquery_migrate}
BuildRequires: xstatic-jquery-migrate-common >= 1.4.1
Requires:      xstatic-jquery-migrate-common >= 1.4.1
%else
Provides:      bundled(js-jquery-migrate) = 1.4.1
%endif
# jquery-minicolors
%if %{unbundle_jquery_minicolors}
BuildRequires: js-jquery-minicolors >= 2.3.6
Requires:      js-jquery-minicolors >= 2.3.6
%else
Provides:      bundled(js-jquery-minicolors) = 2.3.6
%endif
# jquery-ui
%if %{unbundle_jquery_ui}
BuildRequires: js-jquery-ui >= 1.13.2
Requires:      js-jquery-ui >= 1.13.2
%else
Provides:      bundled(js-jquery-ui) = 1.13.2
%endif
# jqplot
%if %{unbundle_jqplot}
BuildRequires: js-jquery-jqplot >= 1.0.8
Requires:      js-jquery-jqplot >= 1.0.8
%else
Provides:      bundled(js-jquery-jqplot) = 1.0.8
%endif
# respond
%if %{unbundle_respond}
BuildRequires: js-respond >= 1.4.2
Requires:      js-respond >= 1.4.2
%else
Provides:      bundled(js-respond) = 1.4.2
%endif

%global __requires_exclude perl\\(Conf\\)
%global __provides_exclude perl\\(Conf\\)
%{?perl_default_filter}


%description
Sympa is scalable and highly customizable mailing list manager. It
can cope with big lists (200,000 subscribers) and comes with a
complete (user and admin) Web interface. It is internationalized,
and supports the us, fr, de, es, it, fi, and chinese locales. A
scripting language allows you to extend the behavior of commands.
Sympa can be linked to an LDAP directory or an RDBMS to create
dynamic mailing lists. Sympa provides S/MIME-based authentication
and encryption.

%description -l ja
Sympa はスケーラブルで高いカスタマイズ性を持つメーリングリスト管理
ソフトウェアです。巨大なリスト (登録者数 200,000) にも適用でき、完
全な (一般ユーザ用および管理者用) ウェブインタフェースをそなえてい
ます。国際化されており、多数の言語に対応します。内蔵のスクリプティ
ング言語でコマンドの動作を拡張できます。Sympa はまた、LDAP ディレ
クトリや RDBMS と連携して動的なメーリングリストを作成できます。ま
た、S/MIME に基づく認証や暗号化もできます。


%package httpd
Summary:  Sympa with Apache HTTP Server
Summary(fr): Sympa avec Serveur HTTP Apache
Summary(ja): SympaのApache HTTP Server対応
Requires: %{name} = %{version}-%{release}
Requires: httpd
Requires: multiwatch
Conflicts: %{name}-lighttpd, %{name}-nginx

%description httpd
Apache HTTP Server support for Sympa.

%description httpd -l ja
Sympa の Apache HTTP Server 対応。


%package lighttpd
Summary:  Sympa with lighttpd
Summary(fr): Sympa avec lighttpd
Summary(ja): Sympaのlighttpd対応
Requires: %{name} = %{version}-%{release}
Requires: lighttpd
Requires: lighttpd-fastcgi
Conflicts: %{name}-httpd, %{name}-nginx

%description lighttpd
lighttpd support for Sympa.

%description lighttpd -l ja
Sympa の lighttpd 対応。


%package nginx
Summary:  Sympa with nginx
Summary(fr): Sympa avec nginx
Summary(ja): Sympaのnginx対応
Requires: %{name} = %{version}-%{release}
Requires: nginx
Requires: multiwatch
Conflicts: %{name}-httpd, %{name}-lighttpd

%description nginx
nginx support for Sympa.

%description nginx -l ja
Sympa の nginx 対応。


%package devel-doc
Summary: Sympa devel doc
Requires: %{name} = %{version}-%{release}

%description devel-doc
Sympa documentation for developers.


%prep
%setup -q -n %{name}-%{version}%{?pre_rel}
%patch -P13 -p0 -b .confdef

# Create a sysusers.d config file
cat >sympa.sysusers.conf <<EOF
u sympa - 'System User for Sympa' %{_localstatedir}/lib/sympa -
EOF


%build
# Development
%if %{with autoreconf}
autoreconf --install
%endif

# Give install "-p" preserving mtime to prevent unexpected update of CSS.
%configure \
    --enable-fhs \
    --prefix=%{_prefix} \
    --bindir=%{_libexecdir}/sympa \
    --docdir=%{_docdir}/%{name} \
    --libexecdir=%{_libexecdir}/sympa \
    --localstatedir=%{_localstatedir} \
    --sysconfdir=%{_sysconfdir}/sympa \
    --with-cgidir=%{_libexecdir}/sympa \
    --with-confdir=%{_sysconfdir}/sympa \
    --without-initdir \
    --with-unitsdir=%{_unitdir} \
    --with-piddir=%{_rundir}/sympa \
    --with-smrshdir=%{_sysconfdir}/smrsh \
    --with-aliases_file=%{_localstatedir}/lib/sympa/sympa_aliases \
    --with-perl=%{_bindir}/perl \
    --with-staticdir=%{static_content} \
    --with-cssdir=%{_localstatedir}/lib/sympa/css \
    --with-picturesdir=%{_localstatedir}/lib/sympa/pictures \
    INSTALL_DATA='install -c -p -m 644'
%make_build

# cancel workaround in Makefile getting previous version.
rm -f previous_sympa_version

pushd po/sympa; rm -f stamp-po; make; popd
pushd po/web_help; rm -f stamp-po; make; popd


%install
%make_install

%find_lang %{name}
%find_lang web_help

# Unbundle fonts from static_content/fonts
# font-awesome
%if %{unbundle_fontawesome}
%unbundle_from_with %{static_content}/fonts/font-awesome/webfonts %{_datadir}/fontawesome/webfonts
%unbundle_from_with %{static_content}/fonts/font-awesome/css %{_datadir}/fontawesome/css
%endif

# Raleway
%if %{unbundle_raleway}
rm -f %{buildroot}%{static_content}/fonts/Raleway/OFL.txt
%unbundle_from_with %{static_content}/fonts/Raleway %{_datadir}/fonts/impallari-raleway
%endif

# Unbundle javascript libraries from static_content/js
# FIXME : foundation (Foundation for Sites 6, with float grid support)
%if %{unbundle_foundation}
%unbundle_from_with %{static_content}/js/foundation/js %{_datadir}/javascript/foundation/js
%unbundle_from_with %{static_content}/js/foundation/css %{_datadir}/javascript/foundation/css
# what-input.js
%unbundle_from_with %{static_content}/js/foundation/js/vendor %{_datadir}/javascript
%endif

# html5shiv
%if %{unbundle_html5shiv}
%unbundle_from_with %{static_content}/js/html5shiv %{_datadir}/javascript
%endif

# jquery
%if %{unbundle_jquery}
%unbundle_from_with %{static_content}/js %{_datadir}/javascript/jquery/3
%endif

# FIXME : jquery-migrate
%if %{unbundle_jquery_migrate}
%unbundle_from_with %{static_content}/js %{_datadir}/javascript/jquery_migrate
%endif

# FIXME : jquery-minicolors
%if %{unbundle_jquery_minicolors}
%unbundle_from_with %{static_content}/js/jquery-minicolors %{_datadir}/javascript/jquery-minicolors
%endif

# jquery-ui
%if %{unbundle_jquery_ui}
%unbundle_from_with %{static_content}/js/jquery-ui %{_datadir}/javascript/jquery-ui
# FIXME: Unbundle theme (smoothness ?)
#unbundle_from_with %{static_content}/js/jquery-ui/images %{_datadir}/javascript/jquery-ui/themes/smoothness/images
%endif

# jqplot
%if %{unbundle_jqplot}
%unbundle_from_with %{static_content}/js/jqplot %{_datadir}/javascript/jquery-jqplot
%endif

# respond
%if %{unbundle_respond}
%unbundle_from_with %{static_content}/js/respondjs %{_datadir}/javascript
%endif

# Save version info.
mv %{buildroot}%{_sysconfdir}/sympa/data_structure.version \
    %{buildroot}%{_sysconfdir}/sympa/data_structure.current_version

# Copy *httpd config files.
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE101} %{buildroot}%{_sysconfdir}/httpd/conf.d/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/lighttpd/conf.d
install -m 0644 %{SOURCE102} %{buildroot}%{_sysconfdir}/lighttpd/conf.d/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d
install -m 0644 %{SOURCE103} %{buildroot}%{_sysconfdir}/nginx/conf.d/sympa.conf

# Copy init scripts or unit files for nginx/spawn-fcgi etc.
install -m 0644 service/wwsympa-multiwatch.service \
    %{buildroot}%{_unitdir}/wwsympa.service
install -m 0644 service/wwsympa-multiwatch.socket \
    %{buildroot}%{_unitdir}/wwsympa.socket
install -m 0644 service/sympasoap-multiwatch.service \
    %{buildroot}%{_unitdir}/sympasoap.service
install -m 0644 service/sympasoap-multiwatch.socket \
    %{buildroot}%{_unitdir}/sympasoap.socket
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/wwsympa.socket.d
cat > %{buildroot}%{_sysconfdir}/systemd/system/wwsympa.socket.d/wwsympa-httpd.conf << EOF
[Socket]
SocketUser=apache
EOF
cat > %{buildroot}%{_sysconfdir}/systemd/system/wwsympa.socket.d/wwsympa-nginx.conf << EOF
[Socket]
SocketUser=nginx
EOF
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/sympasoap.socket.d
cat > %{buildroot}%{_sysconfdir}/systemd/system/sympasoap.socket.d/sympasoap-httpd.conf << EOF
[Socket]
SocketUser=apache
EOF
cat > %{buildroot}%{_sysconfdir}/systemd/system/sympasoap.socket.d/sympasoap-nginx.conf << EOF
[Socket]
SocketUser=nginx
EOF
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 service/sympa-tmpfiles.conf \
    %{buildroot}%{_tmpfilesdir}/sympa.conf
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/sympa.service.d
install -m 0644 %{SOURCE129} \
    %{buildroot}%{_sysconfdir}/systemd/system/sympa.service.d/dependencies.conf

# Copy system config file.
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE130} %{buildroot}%{_sysconfdir}/sysconfig/sympa

# Copy docs.
mv %{buildroot}%{_docdir}/%{name} __doc
cp -p AUTHORS.md CONTRIBUTING.md NEWS.md README.md __doc/
cp -p %{SOURCE113} __doc/README.RPM.md
mv %{buildroot}%{_sysconfdir}/sympa/README __doc/
ln -s %{_datadir}/doc/%{name}/README \
    %{buildroot}/%{_sysconfdir}/sympa/README
ln -s %{_datadir}/doc/%{name}/README \
    %{buildroot}/%{_datadir}/sympa/default/README

# Copy robot aliases.
install -m 0644 %{SOURCE114} %{SOURCE115} %{buildroot}%{_sysconfdir}/sympa/
touch %{buildroot}%{_sysconfdir}/sympa/aliases.sympa.sendmail.db
touch %{buildroot}%{_sysconfdir}/sympa/aliases.sympa.postfix.db

# Copy rsyslog config
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d
install -m 0644 %{SOURCE106} %{buildroot}%{_sysconfdir}/rsyslog.d/sympa.conf

# Create logrotate item
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 0644 %{SOURCE107} %{buildroot}%{_sysconfdir}/logrotate.d/sympa

# Create configuration override structure
for conffile in \
    auth.conf charset.conf create_list.conf \
    edit_list.conf nrcpt_by_domain.conf topics.conf \
    mime.types sympa.wsdl ;
    do cp -a %{buildroot}%{_datadir}/%{name}/default/$conffile \
        %{buildroot}%{_sysconfdir}/%{name}/;
done

# Create directory for S/MIME user certificates
mkdir -p %{buildroot}%{_localstatedir}/lib/sympa/X509-user-certs

install -m0644 -D sympa.sysusers.conf %{buildroot}%{_sysusersdir}/sympa.conf


%check
make check
%if %{with authorcheck}
make authorcheck || true
%endif


%pre
# Fix CSS and pictures paths
if [ $1 -gt 1 ]; then
    if [ -d %{_localstatedir}/lib/%{name}/static_content/css ]; then
        mv -fu %{_localstatedir}/lib/%{name}/static_content/css/* \
            %{_localstatedir}/lib/%{name}/css/ \
            && rm -rf %{_localstatedir}/lib/%{name}/static_content/css/
    fi
    if [ -d %{_localstatedir}/lib/%{name}/static_content/pictures ]; then
        mv -fu %{_localstatedir}/lib/%{name}/static_content/pictures/* \
            %{_localstatedir}/lib/%{name}/pictures/ \
            && rm -rf %{_localstatedir}/lib/%{name}/static_content/pictures/
    fi
    if [ ! -d %{_localstatedir}/lib/%{name}/static_content/css \
        -a ! -d %{_localstatedir}/lib/%{name}/static_content/pictures \
        -a -d %{_localstatedir}/lib/%{name}/static_content ]; then
        rm -r %{_localstatedir}/lib/%{name}/static_content/
    fi
fi
exit 0


%post
# register service
%systemd_post sympa.service

# create cookie
function create_cookie {
    cook=`mktemp`
    perl -ne 'chomp $_; print $1 if /^cookie\s+(\S.*)/' \
        %{_sysconfdir}/sympa/sympa.conf > $cook
    if [ '!' -s $cook ]; then
        if [ -e %{_sysconfdir}/sympa/cookies.history ]; then
            cp -p %{_sysconfdir}/sympa/cookies.history $cook
        else
            dd if=/dev/urandom bs=2048 count=1 2>/dev/null | md5sum | \
            cut -d" " -f1 > $cook
        fi
        perl -i -pe '/^#cookie\s/ and $_ = "cookie ".`cat '$cook'`."\n"' \
            %{_sysconfdir}/sympa/sympa.conf
    fi
    rm -f $cook
}

# create config at first time.
function create_config {
    ## create site configurations
    if [ '!' -e %{_sysconfdir}/sympa/data_structure.version ]; then
        cp -p %{_sysconfdir}/sympa/data_structure.current_version \
            %{_sysconfdir}/sympa/data_structure.version
    fi
    ## create sympa_aliases
    if [ '!' -e %{_localstatedir}/lib/sympa/sympa_aliases ]; then
        touch %{_localstatedir}/lib/sympa/sympa_aliases
        chown sympa:sympa %{_localstatedir}/lib/sympa/sympa_aliases
        chmod 644 %{_localstatedir}/lib/sympa/sympa_aliases
        touch %{_localstatedir}/lib/sympa/sympa_aliases.db
        chown sympa:root %{_localstatedir}/lib/sympa/sympa_aliases.db
        chmod 664 %{_localstatedir}/lib/sympa/sympa_aliases.db
    fi
}

function upgrade_data_structure {
    # Stop sympa if it is running
    if systemctl is-active sympa > /dev/null 2>&1; then
        /usr/bin/systemctl stop sympa > /dev/null 2>&1
        ACTIVE="yes"
    fi
    # Upgrade
    rm -f %{_sysconfdir}/sympa/sympa.conf.bin > /dev/null 2>&1
    if %{_sbindir}/sympa.pl --upgrade > /dev/null 2>&1; then
        # Start sympa if it was running previously
        if [ "$ACTIVE" == "yes" ]; then
            /usr/bin/systemctl start sympa > /dev/null 2>&1
        fi
    else
        echo ============================================================
        echo Notice: Failed upgrading data structure.  See logfile.
        echo Sympa is stopped.
        echo ============================================================
    fi
}

# Install
if [ $1 -eq 1 ]; then
    create_cookie
    create_config
    echo ============================================================
    echo Sympa had been installed successfully.  If you installed
    echo Sympa at first time, please read:
    echo %{_docdir}/%{name}-%{version}/README.RPM.md
    echo ============================================================
fi

# Update
if [ $1 -gt 1 ]; then
    upgrade_data_structure
fi


%preun
%systemd_preun sympa.service

%postun
%systemd_postun_with_restart sympa.service

# httpd
%post httpd
# register service
%systemd_post wwsympa.service
%systemd_post sympasoap.service

%preun httpd
%systemd_preun wwsympa.service
%systemd_preun sympasoap.service

%postun httpd
%systemd_postun_with_restart wwsympa.service
%systemd_postun_with_restart sympasoap.service

# nginx
%systemd_preun wwsympa.service
%systemd_preun sympasoap.service

%post nginx
# register service
%systemd_post wwsympa.service
%systemd_post sympasoap.service

%postun nginx
%systemd_postun_with_restart wwsympa.service
%systemd_postun_with_restart sympasoap.service


%files -f %{name}.lang -f web_help.lang
%doc __doc/*
%license COPYING
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/
%{_sysconfdir}/sympa/README
%config(noreplace) %attr(0640,sympa,sympa) %{_sysconfdir}/sympa/sympa.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/auth.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/charset.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/create_list.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/edit_list.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/nrcpt_by_domain.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/topics.conf
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/mime.types
%config(noreplace,missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/sympa.wsdl
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/create_list_templates
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/tasks
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/scenari
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/mail_tt2
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/web_tt2
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/custom_actions
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/custom_conditions
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/data_sources
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/families
%dir %attr(-,sympa,sympa) %{_sysconfdir}/sympa/search_filters
%config(missingok) %attr(-,sympa,sympa) %{_sysconfdir}/sympa/data_structure.current_version
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.sendmail
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.sendmail.db
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.postfix
%config(noreplace) %{_sysconfdir}/sympa/aliases.sympa.postfix.db
%{_sysconfdir}/smrsh/*
%config(noreplace) %{_sysconfdir}/rsyslog.d/*
%config(noreplace) %{_sysconfdir}/logrotate.d/sympa
%{_sbindir}/*
%dir %{_libexecdir}/sympa/
%attr(4755,sympa,sympa) %{_libexecdir}/sympa/bouncequeue
%attr(4755,sympa,sympa) %{_libexecdir}/sympa/familyqueue
%attr(4755,sympa,sympa) %{_libexecdir}/sympa/queue
%attr(4750,root,sympa) %{_libexecdir}/sympa/sympa_newaliases-wrapper
%{_libexecdir}/sympa/sympa_soap_server.fcgi
%attr(6755,sympa,sympa) %{_libexecdir}/sympa/sympa_soap_server-wrapper.fcgi
%{_libexecdir}/sympa/wwsympa.fcgi
%attr(6755,sympa,sympa) %{_libexecdir}/sympa/wwsympa-wrapper.fcgi
%attr(-,sympa,sympa) %{_localstatedir}/lib/sympa/
%attr(-,sympa,sympa) %{_localstatedir}/spool/sympa/
%{_datadir}/sympa/
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_unitdir}/sympa.service
%{_unitdir}/sympa-outgoing.service
%{_unitdir}/sympa-archive.service
%{_unitdir}/sympa-bounce.service
%{_unitdir}/sympa-task.service
%{_tmpfilesdir}/sympa.conf
%ghost %attr(-,sympa,sympa) %{_rundir}/sympa/
%dir %{_sysconfdir}/systemd/system/sympa.service.d/
%config(noreplace) %{_sysconfdir}/systemd/system/sympa.service.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/sympa
%{_sysusersdir}/sympa.conf


%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/sympa.conf
%{_unitdir}/wwsympa.service
%{_unitdir}/wwsympa.socket
%{_unitdir}/sympasoap.service
%{_unitdir}/sympasoap.socket
%dir %{_sysconfdir}/systemd/system/wwsympa.socket.d
%config(noreplace) %{_sysconfdir}/systemd/system/wwsympa.socket.d/wwsympa-httpd.conf
%dir %{_sysconfdir}/systemd/system/sympasoap.socket.d
%config(noreplace) %{_sysconfdir}/systemd/system/sympasoap.socket.d/sympasoap-httpd.conf


%files lighttpd
%config(noreplace) %{_sysconfdir}/lighttpd/conf.d/sympa.conf


%files nginx
%config(noreplace) %{_sysconfdir}/nginx/conf.d/sympa.conf
%{_unitdir}/wwsympa.service
%{_unitdir}/wwsympa.socket
%{_unitdir}/sympasoap.service
%{_unitdir}/sympasoap.socket
%dir %{_sysconfdir}/systemd/system/wwsympa.socket.d
%config(noreplace) %{_sysconfdir}/systemd/system/wwsympa.socket.d/wwsympa-nginx.conf
%dir %{_sysconfdir}/systemd/system/sympasoap.socket.d
%config(noreplace) %{_sysconfdir}/systemd/system/sympasoap.socket.d/sympasoap-nginx.conf


%files devel-doc
%{_mandir}/man3/*


%changelog
* Mon Jul 28 2025 Michal Schorm <mschorm@redhat.com> - 6.2.76-1.3
- Rebuild without i686 architecture - MySQL 8.4 no longer supports it,
  so perl-DBD-MySQL no longer builds it

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.76-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.2.76-1.1
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Tue Feb 04 2025 Xavier Bachelot <xavier@bachelot.org> - 6.2.76-1
- Update to 6.2.76

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.74-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Xavier Bachelot <xavier@bachelot.org> - 6.2.74-1
- Update to 6.2.74, fix for CVE-2024-55919
  - Full changelog: https://github.com/sympa-community/sympa/releases/tag/6.2.74

* Thu Aug 22 2024 Xavier Bachelot <xavier@bachelot.org> 6.2.72-5
- Drop EL7 support
- Fix filter ordering
- Fix httpd config needed after httpd fix for CVE-2024-38477 (RHBZ#2307179)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.72-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 22 2024 Xavier Bachelot <xavier@bachelot.org> 6.2.72-4
- Tidy up BuildRequires/Requires
- BR: tzdata, which is not pulled from dependencies on F39+ (RHBZ#2261742)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.72-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.72-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Xavier Bachelot <xavier@bachelot.org> 6.2.72-3
- Workaround DKIM issues on EL7
- Add missing BuildRequires:

* Thu Jun 01 2023 Xavier Bachelot <xavier@bachelot.org> 6.2.72-2
- Update to 6.2.72 (fixes CVE-2021-4243)
- Convert License: to SPDX

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.70-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 11 2022 Xavier Bachelot <xavier@bachelot.org> 6.2.70-2
- Fix sympasoap socket ownership for httpd (RHBZ#2152381)
- Fix both wwwsympa and sympasoap socket ownership for nginx

* Wed Nov 30 2022 Xavier Bachelot <xavier@bachelot.org> 6.2.70-1
- Update to 6.2.70

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.68-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Xavier Bachelot <xavier@bachelot.org> 6.2.68-1
- Update to 6.2.68
- Dont unbundle jquery-ui on EL9
- Use Archive::Zip::SimpleZip instead of Archive::Zip where available

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.66-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 05 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.66-1
- Update to 6.2.66

* Thu Jul 15 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.64-1
- Update to 6.2.64
- Fix jquery-ui unbundling
- Add 2 upstream patches

* Tue Apr 27 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.62-1
- Update to 6.2.62
  - Fixes CVE-2020-26880 (RHBZ#1886232 - RHBZ#1886233)
- Unbundle jquery-ui
- Unbundle jquery on EL8

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.2.60-2.1
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 17 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.60-2
- Prepare for jquery-ui retirement in F34
- Remove conditionals for F31

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.60-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.60-1
- Update to 6.2.60
  - Fixes CVE-2020-29668 (RHBZ#1906576)

* Sat Nov 07 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.58-2
- Add BR: perl-Test-Net-LDAP
- Remove all of EL6 thus sysvinit support

* Tue Oct 20 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.58-1
- Update to 6.2.58

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.56-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.56-2
- Prepare for some js packages retirement in Fedora

* Sun May 24 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.56-1
- Update to 6.2.56 (Fixes CVE-2020-10936)
- Fix typo in url and also socket location in lighttpd configuration (RHBZ#1812325)

* Mon Mar 02 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.54-1
- Update to 6.2.54 (Fixes CVE-2020-9369).

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.52-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.52-2
- Add upstream patches to fix 2 scenario failures.

* Fri Dec 27 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.52-1
- Update to 6.2.52.

* Sun Dec 22 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.50-1
- Update to 6.2.50.
- Re-enable Crypt::OpenSSL::X509 for EL8.

* Fri Nov 29 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-3
- Add patch to fix compile executables test on F32.
- Add dependency on Socket6 and IO::Socket::IP
  (or alternatively Socket6 and IO::Socket::INET6 on EL6).
- Add patch to fix ldap 2 level query.
- Re-enable Crypt::SMIME for EL8.
- Re-enable all web subpackages for EL8.

* Wed Oct 16 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-2
- Don't require optional perl modules unavailable on EL8.
- Disable httpd and lighttpd support for EL8 until missing bits are available.
- Change sympa localstatedir owner/group to sympa:sympa. Fixes RHBZ#1761455.

* Mon Sep 30 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-1
- Update to 6.2.48.

* Mon Sep 23 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.46-1
- Update to 6.2.46.
- Unbundle foundation-icons font.
- Add dependency on LWP::Protocol::https (RHBZ#1753111).
- Don't unbundle js-respond on EL8 (yet).

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.44-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-3
- Don't build for ix86 on EL6.
- Re-order some parts of spec for better readability.
- Use bcond_with macro instead of custom macros.

* Mon Jul 15 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-2
- Don't package OChangeLog and ONEWS. Saves 5MB.
- Move developers documentation to devel-doc sub-package.
- Compute an accurate License: tag.

* Wed Jun 26 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-1
- Update to 6.2.44.

* Mon Jun 10 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.43-0.2.b.2
- Update to 6.2.43 beta 2.

* Thu May 23 2019 IKEDA Soji <ikeda@conversion.co.jp> 6.2.43-0.1.b.1
- Update to 6.2.43 beta 1.
- Move sympa.conf-dist to doc.

* Thu Mar 21 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.42-1
- Update to 6.2.42.

* Sun Mar 10 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.41-0.2.b.2
- Update to 6.2.41 beta 2.

* Sun Feb 03 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.41-0.1.b.1
- Update to 6.2.41 beta 1.

* Mon Jan 28 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.40-2
- Unbundle jqplot on F29+.
- Use versioned Requires and BuildRequires for unbundled fonts and libs.

* Sat Jan 19 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.40-1
- Update to 6.2.40.

* Fri Jan 11 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.38-2
- Fix fontawesome, jquery-ui and jquery-migrate unbundling on EL7.
- Fix wwsympa/sympasoap not being restarted on update.

* Fri Dec 21 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.38-1
- Update to 6.2.38.

* Sat Dec 08 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.3.b.3
- Update to 6.2.37 beta 3.

* Sat Nov 03 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.2.b.2
- Update to 6.2.37 beta 2.

* Sun Oct 07 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.1.b.1
- Update to 6.2.37 beta 1.

* Sun Sep 23 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.36-1
- Update to 6.2.36.

* Sun Aug 26 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.35-0.1.b.1
- Update to 6.2.35b.1.
- For sympa-httpd with Fedora & EL7: Use mod_proxy_fcgi instead of mod_fcgid.

* Sun Aug 26 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.34-2
- Issue #36: Init scripts for wwsympa/sympasoap were broken.

* Thu Jul 05 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.34-1
- Update to 6.2.34.

* Fri Jun 29 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.33-0.2.b.2
- Update to 6.2.33 beta 2.
  Upstream #170 WWSympa: Switch to Foundation 6
  Upstream #220 static_content directory structure
  Upstream #336 Starting a test framework

* Wed Apr 25 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.32-2
- Add missing Requires on EL6 and EL7.

* Thu Apr 19 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.32-1
- Update to 6.2.32 (Security release).
  See https://sympa-community.github.io/security/2018-001.html

* Mon Mar 26 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.30-1
- Update to 6.2.30.

* Thu Mar 22 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.28-1
- Update to 6.2.28.

* Tue Mar 20 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.26-1
- Update to 6.2.26.
- Fix scriptlet.

* Tue Mar 13 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.3.b.3
- Update to 6.2.25 beta 3.
- Add Requires on optional Crypt::Eksblowfish.

* Mon Mar 05 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.2.b.2
- Update to 6.2.25 beta 2.
- Move static_content to an FHS compliant location.

* Tue Feb 13 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.1.b.1
- Update to 6.2.25 beta 1.
- Remove useless and bogus directories creation for conf override.
- Own the now properly created css and pictures directories.
  Subsequently the above directory doesn't need to be writable anymore.
- Unbundle Raleway font.
- Simplify sysvinit/systemd in configure.

* Tue Dec 26 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.24-2
- Ensure newaliases works out of the box.

* Thu Dec 21 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.24-1
- Update to 6.2.24.

* Thu Dec 14 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.4.b.3
- Update to 6.2.23 beta 3.

* Tue Dec 12 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.4.b.2
- Unbundle jquery (Fedora only).

* Thu Nov 30 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.3.b.2
- Update to 6.2.23 beta 2.

* Wed Nov 22 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.2.b.1
- Specify all build dependencies. Fixes test suite failure on F25/F26.

* Mon Nov 20 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.1.b.1
- Update to 6.2.23 beta 1.
- Drop upstream patches.
- Add missing BuildRequires:.
- Remove duplicate Requires:.
- Fix License: to acknowledge for bundled javascript libraries.
- Track more bundled javascript libraries.

* Wed Nov 08 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-4
- Run autoreconf for jquery patch.

* Wed Oct 25 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-3
- Fix scriplet bug in upgrade_data_structure.
- Unbundle font-awesome.

* Fri Oct 20 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-2
- Add patches from upstream sympa-6.2 branch.

* Tue Oct 03 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-1
- Update to 6.2.22.

* Thu Sep 14 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.19-0.2.b.2
- Rework spec to better comply with Fedora packaging guidelines.

* Sat Aug 19 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.19b.1-1
- Added --bindir to install sympa_smtpc under libexecdir.

* Sun Jun 25 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.18-1
- Updated.

* Thu Jun 15 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.17b.2-1
- Updated README.RPM.md.

* Sun Aug 07 2016 IKEDA Soji <ikeda@conversion.co.jp> 6.2.17-1
- Typos in el6-README.RPM.
- Added a build dependency perl(Test::Harness).
- Added a dependency perl(Unicode::Normalize).
- Added a definition parameter %%{do_autoreconf}.

* Sat Jun 18 2016 IKEDA Soji <ikeda@conversion.co.jp> 6.2.16-1
- Adopted adjustment to Fedora by Xavier Bachelot <xavier@bachelot.org>.
- Avoiding use of buildroot macro in build section.
- Simplified configure option.
- Added patch14 to disable service by default.
- Added unit customization file source129.

* Thu Feb 26 2015 IKEDA Soji <ikeda@conversion.co.jp> 6.2-1
- New minor release sympa-6.2.
