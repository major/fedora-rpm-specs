Name:           pf-bb-config
Version:        22.11
Release:        5%{?dist}
Summary:        PF BBDEV (baseband device) Configuration Application

License:        Apache-2.0
URL:            https://github.com/intel/pf-bb-config
Source0:        %{url}/archive/v%{version}/pf-bb-config-%{version}.tar.gz
Patch0:         %{url}/commit/2b02af16cdd0b704d49fe0cc621a3b5845c2ee2a.patch

# Currently big endian is not supported due to a bug
ExcludeArch:    s390x

BuildRequires:  gcc
BuildRequires:  make


%description
The PF BBDEV (baseband device) Configuration Application "pf_bb_config"
provides a means to configure the baseband device at the host-level.
The program accesses the configuration space and sets the various parameters
through memory-mapped IO read/writes.


%prep
%autosetup -p1
sed -i "s/#VERSION_STRING#/%{version}/g" config_app.c


%build
%make_build CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="${RPM_LD_FLAGS}"


%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/pf-bb-config/acc100/
install -d -m 755 %{buildroot}%{_datadir}/pf-bb-config/acc200/
install -p -D -m 755 pf_bb_config %{buildroot}%{_bindir}/pf_bb_config
cp -a acc100/*.cfg %{buildroot}%{_datadir}/pf-bb-config/acc100/
cp -a acc200/*.cfg %{buildroot}%{_datadir}/pf-bb-config/acc200/


%files
%license LICENSE
%doc README.md
%{_bindir}/pf_bb_config
%{_datadir}/pf-bb-config/


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Maxime Coquelin <maxime.coquelin@redhat.com> - 22.11-3
- Add missing ACC200 (VRB1) data files

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Timothy Redaelli <tredaelli@redhat.com> - 22.11-1
- Update to 22.11

* Mon Oct 03 2022 Timothy Redaelli <tredaelli@redhat.com> - 22.07-1
- Initial import (fedora#2101769)
