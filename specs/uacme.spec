Name:           uacme
Version:        1.7.5 
Release:        3%{?dist}
Summary:        Lightweight SSL certificate verification and issue client

License:        GPL-3.0-only
URL:            https://github.com/ndilieto/uacme
Source0:        %{url}/archive/upstream/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  asciidoc
BuildRequires:  gnutls-devel
BuildRequires:  libcurl-devel
BuildRequires:  libev-devel
BuildRequires:  which
Requires:       curl
Requires:       gnutls
Requires:       libev

%description
A lightweight client for the RFC8555 ACMEv2 protocol, 
written in plain C with minimal dependencies. The 
ACMEv2 protocol allows a Certificate Authority and an 
applicant to automate the process of verification and 
certificate issuance. The protocol also provides 
facilities for other certificate management functions, 
such as certificate revocation.

%prep
%autosetup -n %{name}-upstream-%{version}
# remove bundled library
rm -rvf libev

%build
%{set_build_flags}; \
%{_configure} --host=%{_host} --build=%{_build} \
      --program-prefix=%{?_program_prefix} \
      --disable-dependency-tracking \
      --prefix=%{_prefix} \
      --exec-prefix=%{_exec_prefix} \
      --bindir=%{_bindir} \
      --sbindir=%{_sbindir} \
      --sysconfdir=%{_sysconfdir} \
      --datadir=%{_datadir} \
      --includedir=%{_includedir} \
      --libdir=%{_libdir} \
      --libexecdir=%{_libexecdir} \
      --localstatedir=%{_localstatedir} \
      --sharedstatedir=%{_sharedstatedir} \
      --mandir=%{_mandir} \
      --infodir=%{_infodir} \
      --disable-maintainer-mode \
      --without-mbedtls \
      --without-openssl \
      --with-gnutls
%make_build

%install
%make_install

# No tests defined, do a sanity check
# uacme --version and ualpn --version 
%check
${RPM_BUILD_ROOT}%{_bindir}/%{name} --version 2>&1 | grep 'uacme: version %version'
${RPM_BUILD_ROOT}%{_bindir}/ualpn --version 2>&1 | grep 'ualpn: version %version'

%files
%{_bindir}/%{name}
%{_bindir}/ualpn
%{_datadir}/%{name}/%{name}.sh
%{_datadir}/%{name}/ualpn.sh
%{_datadir}/%{name}/nsupdate.sh
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/ualpn.1*
%{_docdir}/%{name}/%{name}.html
%{_docdir}/%{name}/ualpn.html
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Benson Muite <benson_muite@emailplus.org> - 1.7.5-1
- Update to release 1.7.5

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 18 2023 Benson Muite <benson_muite@emailplus.org> 1.7.4-1
- Update to new release

* Mon Feb 13 2023 Benson Muite <benson_muite@emailplus.org> 1.7.3-3
- Use SPDX license identifier

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 03 2022 Benson Muite <benson_muite@emailplus.org> 1.7.3-1
- Update version
- Improve sanity tests based on review

* Tue Jun 07 2022 Benson Muite <benson_muite@emailplus.org> 1.7.1-1
- Initial packaging
