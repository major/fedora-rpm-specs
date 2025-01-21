Name:           squidclamav
Version:        7.3
Release:        5%{?dist}
Summary:        HTTP Antivirus for Squid based on ClamAv and the ICAP protocol
License:        GPL-3.0-or-later
URL:            https://squidclamav.darold.net/

Source0:        https://github.com/darold/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf

BuildRequires:  bzip2-devel
BuildRequires:  c-icap-devel
BuildRequires:  gcc
BuildRequires:  libarchive-devel
BuildRequires:  make
BuildRequires:  zlib-devel

Requires:       c-icap
Requires:       squid

%if 0%{?rhel} == 7
Requires:       httpd
%else
Requires:       httpd-filesystem
%endif

%description
SquidClamav is an antivirus for the Squid proxy based on the ICAP protocol and
the awards-winning ClamAv anti-virus toolkit. Using it will help you secure your
home or enterprise network web traffic. SquidClamav is the most efficient
antivirus tool for HTTP traffic available for free, it is written in C as a
c-icap service and can handle several thousands of connections at once.

%prep
%autosetup

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
%license COPYING
%doc AUTHORS ChangeLog README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/c-icap/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_datadir}/c_icap/templates/squidclamav/
%{_libdir}/c_icap/*.so
%{_libexecdir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Simone Caronni <negativo17@gmail.com> - 7.3-2
- Fix dependencies for el7.

* Sat Nov 11 2023 Simone Caronni <negativo17@gmail.com> - 7.3-1
- Update to 7.3.

* Thu Oct 19 2023 Simone Caronni <negativo17@gmail.com> - 7.2-4
- Review fixes; bundle external GPL license file:
  https://github.com/darold/squidclamav/issues/69

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 7.2-3
- Review fixes.

* Sat Aug 20 2022 Simone Caronni <negativo17@gmail.com> - 7.2-2
- Initial import.
