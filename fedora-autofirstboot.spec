Name:           fedora-autofirstboot
Version:        1
Release:        1%{?dist}
Summary:        Collection of firstboot services for Fedora

License:        GPL-2.0-or-later
URL:            https://pagure.io/fedora-autofirstboot
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  make
Requires:       findutils
%{?systemd_ordering}

BuildArch:      noarch


%description
%{summary}.


%prep
%autosetup


%build
# Nothing to do

%install
%make_install


%preun
%systemd_preun fedora-autofirstboot.service


%post
%systemd_post fedora-autofirstboot.service


%postun
%systemd_postun fedora-autofirstboot.service


%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/fedora-firstboot
%{_libexecdir}/fedora-autofirstboot/
%{_unitdir}/fedora-autofirstboot.service


%changelog
* Fri Sep 09 2022 Neal Gompa <ngompa@fedoraproject.org> - 1-1
- Initial package
