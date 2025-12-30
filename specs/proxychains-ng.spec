%if 0%{?el7}
%global _hardened_build 1
%endif

Name:       proxychains-ng
Version:    4.17
Release:    %autorelease
Summary:    Redirect connections through proxy servers

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://github.com/rofl0r/proxychains-ng
Source0:    http://ftp.barfooze.de/pub/sabotage/tarballs/proxychains-ng-%{version}.tar.xz
# generated using git format-patch --zero-commit --stdout $(git describe --tags --abbrev=0 master) > $(git rev-parse master).patch
Patch1:     979bfef42974f80352566cbad1fd1be4ec33cd70.patch

BuildRequires:  gcc
BuildRequires:  make

%description
ProxyChains NG is based on ProxyChains.

ProxyChains NG hooks network-related (TCP only) libc functions in dynamically
linked programs via a preloaded DSO (dynamic shared object) and redirects the
connections through one or more SOCKS4a/5 or HTTP proxies.

Since Proxy Chains NG relies on the dynamic linker, statically linked binaries
are not supported.

%prep
%autosetup -p1

%build
%configure --disable-static --libdir=%{_libdir}/%{name}
%make_build

%install
%make_install install-config
ln -s ../..%{_bindir}/proxychains4 %{buildroot}%{_bindir}/proxychains
chmod +x %{buildroot}%{_libdir}/%{name}/libproxychains4.so

%files
%license COPYING
%doc AUTHORS README TODO
%config(noreplace) %{_sysconfdir}/proxychains.conf
%{_bindir}/proxychains
%{_bindir}/proxychains4
%{_bindir}/proxychains4-daemon
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libproxychains4.so

%changelog
%autochangelog
