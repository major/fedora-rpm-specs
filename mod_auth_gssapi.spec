Name:           mod_auth_gssapi
Version:        1.6.5
Release:        %autorelease
Summary:        A GSSAPI Authentication module for Apache

License:        MIT
URL:            https://github.com/gssapi/mod_auth_gssapi
Source0:        https://github.com/gssapi/%{name}/releases/download/v%{version}/%name-%{version}.tar.gz

BuildRequires:  httpd-devel, krb5-devel, openssl-devel
BuildRequires:  autoconf, automake, libtool, bison, flex, make
BuildRequires:  git
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       krb5-libs >= 1.11.5

# If you're reading this: NTLM is insecure.  Migrate off it.
%if 0%{?rhel}
%else
BuildRequires: gssntlmssp-devel
%endif

%description
The mod_auth_gssapi module is an authentication service that implements the
SPNEGO based HTTP Authentication protocol defined in RFC4559.

%prep
%autosetup -S git_am

%build
export APXS=%{_httpd_apxs}
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_httpd_moddir}
install -m 755 src/.libs/%{name}.so %{buildroot}%{_httpd_moddir}

# Apache configuration for the module
echo "LoadModule auth_gssapi_module modules/mod_auth_gssapi.so" > 10-auth_gssapi.conf
mkdir -p %{buildroot}%{_httpd_modconfdir}
install -m 644 10-auth_gssapi.conf %{buildroot}%{_httpd_modconfdir}

%files
%doc
%defattr(-,root,root)
%doc README COPYING
%config(noreplace) %{_httpd_modconfdir}/10-auth_gssapi.conf
%{_httpd_moddir}/mod_auth_gssapi.so

%changelog
%autochangelog
