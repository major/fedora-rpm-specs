%global commit d266daf800f77dd41781af23d25ece513887afc5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20220206git%{shortcommit}

Name:     pdfsign
Version:  0
Release:  %autorelease -s %{snapinfo}
Summary:  Sign PDF (PAdES compatible)
License:  GPLv2
URL:      https://github.com/opensignature/pdfsign
Source0:  https://github.com/opensignature/pdfsign/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: gcc-c++
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: openssl-devel
BuildRequires: podofo0.9-devel

%description
Sign PDF (PAdES compatible)

%prep
%autosetup -n pdfsign-%{commit}

%build
g++ pdfsign.cpp -I/usr/include/podofo/ -lpodofo -ljpeg -lfreetype -lpng -lz -lcrypto -lpthread -lfontconfig %{optflags} %{build_ldflags} -o pdfsign

%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{_builddir}/pdfsign-%{commit}/pdfsign %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/pdfsign

%changelog
%autochangelog
