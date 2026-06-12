Name:           pigz
Version:        2.8
Release:        %autorelease
Summary:        Parallel implementation of gzip
License:        Zlib AND Apache-2.0
URL:            https://www.zlib.net/pigz/
Source:         https://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncompress
BuildRequires:  zlib-devel

Provides:       bundled(zopfli)

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when
compressing data.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
install -D -p -m 0755 pigz %{buildroot}%{_bindir}/pigz
ln -f %{buildroot}%{_bindir}/pigz %{buildroot}%{_bindir}/unpigz
install -D -p -m 0644 pigz.1 %{buildroot}%{_mandir}/man1/pigz.1

%check
%make_build tests CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%files
%license zopfli/COPYING
%doc pigz.pdf README
%{_bindir}/pigz
%{_bindir}/unpigz
%{_mandir}/man1/pigz.1*

%changelog
%autochangelog
