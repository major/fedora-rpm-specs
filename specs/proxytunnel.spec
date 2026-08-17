%global forgeurl https://github.com/proxytunnel/proxytunnel
Version:        1.13.0
%global tag     v%{version}
%forgemeta

Name:           proxytunnel
Release:        %autorelease
Summary:        Tool to tunnel a connection through an standard HTTP(S) proxy

# The main code is GPL-2.0-or-later, with OpenSSH parts under BSD-3-Clause and Todd C. Miller's parts under ISC.
License:        GPL-2.0-or-later AND BSD-3-Clause AND ISC
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  asciidoc
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  xmlto

%description
ProxyTunnel is a program that connects stdin and stdout to a server somewhere 
on the network, through a standard HTTPS proxy. We mostly use it to tunnel SSH
sessions through HTTP(S) proxies.
Proxytunnel can currently do the following:
* Create tunnels using HTTP and HTTPS proxies (That understand the HTTP 
  CONNECT command).
* Work as a back-end driver for an OpenSSH client, and create SSH
  connections through HTTP(S) proxies.
* Work as a stand-alone application, listening on a port for connections, 
  and then tunneling these connections to a specified destination. 

%prep
%forgeautosetup
# Fix permissions
chmod -c 644 CHANGES
# Convert docs to UTF-8
for f in CHANGES; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.tmp
    touch -r $f $f.tmp
    mv -f $f.tmp $f
done

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install prefix=%{_prefix} DESTDIR=%{buildroot}

%check
# Upstream does not have a test suite, but we can verify the binary executes
%{buildroot}%{_bindir}/proxytunnel -V

%files
%doc CHANGES CREDITS KNOWN_ISSUES README.md TODO
%license LICENSE.txt
%{_bindir}/proxytunnel
%{_mandir}/man1/proxytunnel.1*

%changelog
%autochangelog
