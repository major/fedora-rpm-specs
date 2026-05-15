Name:           uberftp
Version:        2.9.1
Release:        %autorelease
Summary:        GridFTP-enabled ftp client

License:        NCSA
URL:            https://gridcf.org/
Source0:        https://repo.gridcf.org/uberftp/sources/uberftp-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  globus-gssapi-gsi-devel

%description
UberFTP is the first interactive, GridFTP-enabled ftp client.
It supports GSI authentication, parallel data channels and
third party transfers.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/uberftp
%{_mandir}/man1/uberftp.1*
%doc Changelog.mssftp ChangeLog
%license COPYING

%changelog
%autochangelog
