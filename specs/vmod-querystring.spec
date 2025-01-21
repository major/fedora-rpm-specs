%global vmoddir %{_libdir}/varnish/vmods

Name:           vmod-querystring
Version:        2.0.3
Release:        9%{?dist}
Summary:        QueryString module for Varnish Cache
URL:            https://github.com/dridi/libvmod-querystring
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  python
BuildRequires:  varnish >= 6
BuildRequires:  pkgconfig(varnishapi) >= 6

Requires:       varnish >= 6


%description
The purpose of this module is to give you a fine-grained control over a URL's
query-string in Varnish Cache. It's possible to remove the query-string, clean
it, sort its parameters or filter it to only keep a subset of them.

This can greatly improve your hit ratio and efficiency with Varnish, because
by default two URLs with the same path but different query-strings are also
different. This is what the RFCs mandate but probably not what you usually
want for your web site or application.

A query-string is just a character string starting after a question mark in a
URL. But in a web context, it is usually a structured key/values store encoded
with the `application/x-www-form-urlencoded' media type. This module deals
with this kind of query-strings.


%prep
%autosetup -p1


%build
%configure CFLAGS="%{optflags}"
%make_build


%install
%make_install
rm %{buildroot}%{vmoddir}/*.la


%check
%make_build check


%files
%license LICENSE
%{_mandir}/man?/*
%{_docdir}/*
%{vmoddir}/*.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.3-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.3-1
- Bump to 2.0.3
- Drop the temporary patch for 2.0.2-5

* Fri Aug 06 2021 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.2-5
- Add patch for Varnish 6.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.2-2
- Rebuild for Varnish 6.5.1

* Mon Sep 21 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.2-1
- Bump to 2.0.2 for Varnish 6.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.1-1
- Bump to 2.0.1

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.5-1
- Bump to 1.0.5
- Drop rst2man BR
- Add python3 BR
- Simplify %%configure step

* Thu Mar 15 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.3-3
- Explicit python requirements (#1556533)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.3-1
- Bump to 1.0.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.2-1
- Bump to 1.0.2
- Set the optflags at configure time

* Sun Sep 25 2016 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.0.1-1
- Initial spec.
