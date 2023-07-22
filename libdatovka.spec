Name: libdatovka
Version: 0.3.0
Release: 2%{?dist}
Summary: Client library for accessing SOAP services of ISDS (Czech Data Boxes)

License: LGPLv3+ and GPLv3+
URL: https://www.datovka.cz/
Source0: https://secure.nic.cz/files/datove_schranky/%{name}/%{name}-%{version}.tar.xz
BuildRequires: dos2unix
BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: coreutils
BuildRequires: docbook-style-xsl
BuildRequires: libxslt-devel
BuildRequires: gettext-devel
BuildRequires: libxml2-devel
BuildRequires: libcurl-devel
BuildRequires: gpgme-devel
BuildRequires: libgcrypt-devel
BuildRequires: expat-devel
BuildRequires: gnupg2-smime
BuildRequires: gnutls-devel
# partial fix for the https://gitlab.nic.cz/datovka/libdatovka/-/issues/17
# --disable-fatalwarnings can be dropped once correctly fixed upstream
Patch0: libdatovka-0.2.1-gcc-12-build-fix.patch

%description
Client library for accessing SOAP services of ISDS (Informační systém
datových schránek / Data Box Information System) as defined in Czech ISDS Act
(300/2008 Coll.) <http://portal.gov.cz/zakon/300/2008> and implied documents.

%package devel
Summary: Development files for libdatovka
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libxml2-devel%{?_isa}
Requires: pkgconfig%{?_isa}

%description devel
Development files for libdatovka.

%package doc
Summary:          Documentation files for libdatovka
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation files for libdatovka.

%prep
%autosetup -p1
dos2unix src/*.{c,h}

%build
autoreconf -fi
%configure \
  --enable-doc \
  --disable-online-test \
  --disable-static \
  --enable-test \
  --with-libcurl \
  --disable-fatalwarnings

%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name}

%check
make check %{?_smp_mflags}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*

%files doc
%doc client

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.0-1
- New version
  Resolves: rhbz#2170064

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.1-3
- Fixed FTBFS with gcc-12
  Resolves: rhbz#2045792

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov  4 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.1-1
- New version
  Resolves: rhbz#2019910

* Fri Aug 27 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.0-1
- New version
  Resolves: rhbz#1997611

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.2-1
- New version
  Resolves: rhbz#1949982

* Tue Feb  2 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.1-1
- New version

* Mon Feb  1 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.0-2
- Fixed according to the review
  Related: rhbz#1920514

* Thu Jan 28 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.0-1
- Initial release
  Related: rhbz#1920514
