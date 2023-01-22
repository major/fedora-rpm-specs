Name:		rnetclient
Version:	2017.1
Release:	13%{?dist}
Summary:	Submit the Brazilian Income Tax Report to the Brazilian Tax Authority

License:	GPLv3+
URL:		http://wiki.libreplanetbr.org/rnetclient/
Source:		http://libreplanetbr.org/files/sw/rnetclient/rnetclient-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	gnutls-devel >= 1.4.0
BuildRequires:	zlib-devel

%description

Rnetclient is a Free Software that can be used to submit the Brazilian
Income Tax Report to the Brazilian Tax Authority (Receita Federal).
It is the outcome of reverse-engineering ReceitaNet, the official and
proprietary software that Receita Federal develops.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc AUTHORS COPYING README TODO NEWS
%{_bindir}/rnetclient
%{_mandir}/man1/*
%{_mandir}/pt_BR/man1/*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 17 2017 Sergio Durigan Junior <sergiodj@sergiodj.net> - 2017.1-1
- New upstream version.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 11 2016 Sergio Durigan Junior <sergiodj@sergiodj.net> - 2016.0-1
- New upstream version.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Sergio Durigan Junior <sergiodj@sergiodj.net> - 2015.1-1
- Update RPM with the latest release.

* Sun Feb 22 2015 Sergio Durigan Junior <sergiodj@sergiodj.net> - 2014.2-1
- First version of the Fedora package.
