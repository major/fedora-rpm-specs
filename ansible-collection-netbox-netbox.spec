%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-netbox-netbox
Version:        3.9.0
Release:        3%{?dist}
Summary:        Netbox modules for Ansible

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url netbox netbox}
%global furl    https://github.com/netbox-community/ansible_modules
Source:         %{furl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Remove unnecessary files from the collection tarball.
# This is a downstream only patch.
Patch:          build_ignore.patch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible_modules-%{version} -p1
sed -i -e '1{\@^#!.*@d}' plugins/modules/*.py

%build
%ansible_collection_build

%install
%ansible_collection_install

%if %{with tests}
%check
%ansible_test_unit
%endif

%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md CHANGELOG.rst

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Igor Raits <igor@gooddata.com> - 3.9.0-1
- Update to 3.9.0

* Mon Oct 24 2022 Maxwell G <gotmax@e.email> - 3.8.1-1
- Update to 3.8.1. Fixes rhbz#2128028.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Maxwell G <gotmax@e.email> - 3.7.1-1
- Update to 3.7.1. Fixes rhbz#2079402.

* Thu May 12 2022 Maxwell G <gotmax@e.email> - 3.7.0-2
- Rebuild for new ansible-packaging.

* Tue Apr 19 2022 Maxwell G <gotmax@e.email> - 3.7.0-1
- Update to 3.7.0. Fixes rhbz#2076449.

* Sat Mar 05 2022 Maxwell G <gotmax@e.email> - 3.6.0-1
- Update to 3.6.0. Fixes rhbz#2059115.

* Mon Feb 21 2022 Maxwell G <gotmax@e.email> - 3.5.1-1
- Update to 3.5.1. Fixes rhbz#2039713.
- Migrate BR to ansible-packaging.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Kevin Fenzi <kevin@scrye.com> - 3.4.0-1
- Update to 3.4.0. Fixes rhbz#2028317

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.2.0-3
- Rebuild against new ansible-generator and allow to be used by ansible-base-2.10.x

* Wed Dec 30 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-2
- Drop runtime dependencies

* Tue Dec 29 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sun Aug 09 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Sun Apr 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Wed Mar 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.1.9-1
- Initial package
