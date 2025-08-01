%global githash 79d751a


Name:		ansible-openstack-modules
Version:	0
Release:	20140924git%{githash}%{?dist}
Summary:	Unofficial Ansible modules for managing Openstack

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/openstack-ansible/openstack-ansible-modules
# git clone https://github.com/openstack-ansible/openstack-ansible-modules.git
# cd openstack-ansible-modules
# git archive --format=tar %%{githash} | gzip > %%{name}-%%{githash}.tar.gz
Source0:	ansible-openstack-modules-%{githash}.tar.gz
BuildArch:      noarch

Requires:	ansible

%description
Unofficial Ansible modules for managing and deployment of OpenStack. Contains
all the necesary Neutron networking modules and also some Cinder, Glance,
Keystone and Nova modules missing in the official modules.


%prep
%setup -q -c


%build


%install
mkdir -p %{buildroot}%{_datadir}/ansible/ansible-openstack-modules
cp -a cinder* glance* keystone* neutron* nova* %{buildroot}%{_datadir}/ansible/ansible-openstack-modules/


%files
%doc LICENSE README.md
%{_datadir}/ansible/ansible-openstack-modules


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140924git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140923git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0-20140922git79d751a
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140921git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140920git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140919git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140918git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140917git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140916git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140915git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140914git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140913git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140912git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140911git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140910git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140909git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140908git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140907git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140906git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140905git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-20140904git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-20140903git79d751a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 02 2014 Adam Samalik <asamalik@redhat.com> 0-20140902git79d751a
- new module: nova_flavor

* Thu Aug 28 2014 Adam Samalik <asamalik@redhat.com> 0-20140828git7611354
- packing with a license file

* Wed Aug 27 2014 Adam Samalik <asamalik@redhat.com> 0-20140827gitf543bea
- initial package
