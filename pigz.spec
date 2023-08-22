Name:           pigz
Version:        2.8
Release:        %autorelease
Summary:        Parallel implementation of gzip
License:        Zlib
URL:            https://www.zlib.net/pigz/
Source0:        https://www.zlib.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncompress
BuildRequires:  zlib-devel

%description
pigz, which stands for parallel implementation of gzip,
is a fully functional replacement for gzip that exploits
multiple processors and multiple cores to the hilt when
compressing data.

%prep
%autosetup -p1

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
install -p -D pigz $RPM_BUILD_ROOT%{_bindir}/pigz
pushd $RPM_BUILD_ROOT%{_bindir}; ln pigz unpigz; popd
install -p -D pigz.1 -m 0644 $RPM_BUILD_ROOT%{_datadir}/man/man1/pigz.1

%check
make tests CFLAGS="$RPM_OPT_FLAGS"

%files
%doc pigz.pdf README
%{_bindir}/pigz
%{_bindir}/unpigz
%{_datadir}/man/man1/pigz.*

%changelog
%autochangelog
