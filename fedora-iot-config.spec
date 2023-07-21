Name:           fedora-iot-config
Version:        0.0
Release:        3%{?dist}
Summary:        Fedora IoT Configuration file

License:        MIT
URL:            https://fedoraproject.org/
Source0:        fedora-iot.conf

BuildArch: noarch

BuildRequires: ostree-libs
Requires: ostree-libs

Provides:       fedora-iot-config(%{version}) = %{release}

%description
Fedora IoT configuration file for ostree repositories. 


%prep
# None required

%build
# None required

%install
install -d %{buildroot}%{_sysconfdir}/ostree/remotes.d/
install -pm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/ostree/remotes.d/

%files
%config %{_sysconfdir}/ostree/remotes.d/fedora-iot.conf

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 30 2023 Paul Whalen <pwhalen@fedoraproject.org> - 0.0-2
- Add requires ostree-libs, fix spec

* Tue Mar 07 2023 Paul Whalen <pwhalen@fedoraproject.org> - 0.0-1
- initial packaging
