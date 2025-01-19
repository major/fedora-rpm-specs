%global srcname apache-mod-markdown
%global commit 1bf4fb4df6029e8fdfc5ce46f14e99d951230450
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		mod_markdown
Version:	1.0.4
Release:	12.20211115git%{shortcommit}%{?dist}
# Automatically converted from old format: ASL 2.0
License:	Apache-2.0
Summary:	Markdown content filters for the Apache HTTP Server
URL:		https://github.com/hamano/%{srcname}
Source0:	https://github.com/hamano/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
Source1:	71_mod_markdown.conf
# https://github.com/hamano/apache-mod-markdown/issues/36
Patch0:		%{name}.diff
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	httpd-devel
# libmarkdown-devel
BuildRequires:	pkgconfig(libmarkdown)

%description
mod_markdown is Markdown filter module for Apache HTTPD Server.


%prep
%autosetup -n %{srcname}-%{commit}


%build
autoupdate
autoreconf -vfi
%configure \
    --with-apxs=%{_bindir}/apxs \
    --with-discount=%{_prefix}
sed -i "s|/usr/lib$|%{_libdir}|g" Makefile
%make_build


%install
mkdir -p %{buildroot}%{_httpd_moddir}
mkdir -p %{buildroot}%{_httpd_modconfdir}
%{_libdir}/httpd/build/instdso.sh SH_LIBTOOL='%{_libdir}/apr-1/build/libtool' mod_markdown.la %{buildroot}%{_httpd_moddir}
install -Dm 0644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}


%files
%license COPYING
%doc README.md
%{_httpd_moddir}/mod_markdown.so
%config(noreplace) %{_httpd_modconfdir}/71_mod_markdown.conf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-11.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.4-10.20211115git1bf4fb4
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-9.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4.20211115git1bf4fb4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 TI_Eugene <ti.eugene@gmail.com> - 1.0.4-3.20211115git1bf4fb4
- Rebuild with fresh sources

* Tue Mar 30 2021 TI_Eugene <ti.eugene@gmail.com> - 1.0.4-2.20200616git933aa25
- Spec fixes.

* Wed Mar 24 2021 TI_Eugene <ti.eugene@gmail.com> - 1.0.4-1.20200616
- Initial packaging.
