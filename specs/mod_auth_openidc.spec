%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}
%{!?_httpd_moddir: %{expand: %%global _httpd_moddir %%{_libdir}/httpd/modules}}
%{!?_httpd_confdir: %{expand: %%global _httpd_confdir %{_sysconfdir}/httpd/conf.d}}

# Optionally build with hiredis if --with hiredis is passed
%{!?_with_hiredis: %{!?_without_hiredis: %global _without_hiredis --without-hiredis}}
# It is an error if both or neither required options exist.
%{?_with_hiredis: %{?_without_hiredis: %{error: both _with_hiredis and _without_hiredis}}}
%{!?_with_hiredis: %{!?_without_hiredis: %{error: neither _with_hiredis nor _without_hiredis}}}

# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}

%global httpd_pkg_cache_dir /var/cache/httpd/mod_auth_openidc

Name:		mod_auth_openidc
Version:	2.4.17.2
Release:	%autorelease
Summary:	OpenID Connect auth module for Apache HTTP Server

License:	Apache-2.0
URL:		https://github.com/OpenIDC/mod_auth_openidc
Source0:	https://github.com/OpenIDC/mod_auth_openidc/releases/download/v%{version}/mod_auth_openidc-%{version}.tar.gz

BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires:  gcc
BuildRequires:	httpd-devel
BuildRequires:	openssl-devel
BuildRequires:	curl-devel
BuildRequires:	jansson-devel
BuildRequires:	pcre2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cjose-devel
BuildRequires:	jq-devel
%{?_with_hiredis:BuildRequires: hiredis-devel}
Requires:	httpd-mmn = %{_httpd_mmn}

%description
This module enables an Apache 2.x web server to operate as
an OpenID Connect Relying Party and/or OAuth 2.0 Resource Server.

%prep
%setup -q

%build
# workaround rpm-buildroot-usage
export MODULES_DIR=%{_httpd_moddir}
export APXS2_OPTS='-S LIBEXECDIR=${MODULES_DIR}'
autoreconf -vfi
%configure \
  --with-jq=/usr/lib64/ \
  %{?_with_hiredis} \
  %{?_without_hiredis} \
  --with-apxs2=%{_httpd_apxs}

%{make_build}

# (jhrozek): temporarily disable make check to work around a FTBFS issue
%check
export MODULES_DIR=%{_httpd_moddir}
export APXS2_OPTS='-S LIBEXECDIR=${MODULES_DIR}'
%{make_build} test

%install
mkdir -p $RPM_BUILD_ROOT%{_httpd_moddir}
make install DESTDIR=$RPM_BUILD_ROOT MODULES_DIR=$RPM_BUILD_ROOT%{_httpd_moddir}

install -m 755 -d $RPM_BUILD_ROOT%{_httpd_modconfdir}
echo 'LoadModule auth_openidc_module modules/mod_auth_openidc.so' > \
	$RPM_BUILD_ROOT%{_httpd_modconfdir}/10-auth_openidc.conf

install -m 755 -d $RPM_BUILD_ROOT%{_httpd_confdir}
install -m 644 auth_openidc.conf $RPM_BUILD_ROOT%{_httpd_confdir}
# Adjust httpd cache location in install config file
sed -i 's!/var/cache/apache2/!/var/cache/httpd/!' $RPM_BUILD_ROOT%{_httpd_confdir}/auth_openidc.conf
install -m 700 -d $RPM_BUILD_ROOT%{httpd_pkg_cache_dir}
install -m 700 -d $RPM_BUILD_ROOT%{httpd_pkg_cache_dir}/metadata
install -m 700 -d $RPM_BUILD_ROOT%{httpd_pkg_cache_dir}/cache


%files
%if 0%{?rhel} && 0%{?rhel} < 7
%doc LICENSE.txt
%else
%license LICENSE.txt
%endif
%doc ChangeLog
%doc AUTHORS
%doc README.md
%{_httpd_moddir}/mod_auth_openidc.so
%config(noreplace) %{_httpd_modconfdir}/10-auth_openidc.conf
%config(noreplace) %{_httpd_confdir}/auth_openidc.conf
%dir %attr(0700, apache, apache) %{httpd_pkg_cache_dir}
%dir %attr(0700, apache, apache) %{httpd_pkg_cache_dir}/metadata
%dir %attr(0700, apache, apache) %{httpd_pkg_cache_dir}/cache

%changelog
%autochangelog
