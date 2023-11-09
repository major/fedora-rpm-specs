Name:           squidclamav
Version:        7.2
Release:        4%{?dist}
Summary:        HTTP Antivirus for Squid based on ClamAv and the ICAP protocol
License:        GPL-3.0-or-later
URL:            https://squidclamav.darold.net/

Source0:        https://github.com/darold/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
# https://github.com/darold/squidclamav/issues/69
Source2:        https://www.gnu.org/licenses/gpl-3.0.txt
Patch0:         https://github.com/darold/%{name}/commit/6c279b74a61507a6e2118cb8796f5647f4166ecd.patch

BuildRequires:  bzip2-devel
BuildRequires:  c-icap-devel
BuildRequires:  gcc
BuildRequires:  libarchive-devel
BuildRequires:  make
BuildRequires:  zlib-devel

Requires:       c-icap
Requires:       httpd-filesystem
Requires:       squid

%description
SquidClamav is an antivirus for the Squid proxy based on the ICAP protocol and
the awards-winning ClamAv anti-virus toolkit. Using it will help you secure your
home or enterprise network web traffic. SquidClamav is the most efficient
antivirus tool for HTTP traffic available for free, it is written in C as a
c-icap service and can handle several thousands of connections at once.

%prep
%autosetup

cp %{SOURCE2} COPYING

%build
%configure \
  --disable-static \
  --enable-shared \
  --with-c-icap \
  --with-libarchive

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Let rpm pick up the docs in the files section
rm -rf %{buildroot}%{_datadir}/%{name}

# Do not add default configuration files
rm -f %{buildroot}%{_sysconfdir}/c-icap/*.default

%files
%doc AUTHORS ChangeLog README
%license COPYING
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/c-icap/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_datadir}/c_icap/templates/squidclamav/
%{_libdir}/c_icap/*.so
%{_libexecdir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Oct 19 2023 Simone Caronni <negativo17@gmail.com> - 7.2-4
- Review fixes; bundle external GPL license file:
  https://github.com/darold/squidclamav/issues/69

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 7.2-3
- Review fixes.

* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 7.2-2
- Initial import.
