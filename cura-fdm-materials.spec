Name:           cura-fdm-materials
Version:        4.13.0
Release:        2%{?dist}
Summary:        Cura FDM Material database

# See https://github.com/Ultimaker/Cura/issues/1779 for clarification
License:        Public Domain

URL:            https://github.com/Ultimaker/fdm_materials
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

BuildRequires:  cmake
Requires:       cura >= 1:%{version}

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
Cura material files.

These files are needed to work with printers like Ultimaker 2+ and Ultimaker 3.

%prep
%autosetup -n fdm_materials-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install


%files
%license LICENSE
%{_datadir}/cura/resources/materials/

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 01 2022 Gabriel Féron <feron.gabriel@gmail.com> - 4.13.0-1
- Update to 4.13.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.12.1-1
- Update to 4.12.1

* Wed Sep 15 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.11.0-1
- Update to 4.11.0

* Mon Aug 16 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.10.0-1
- Update to 4.10.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.9.1-1
- Update to 4.9.1

* Mon Apr 26 2021 Gabriel Féron <feron.gabriel@gmail.com> - 4.9.0-1
- Update to 4.9.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Jan Pazdziora <jpazdziora@redhat.com> - 4.8.0-1
- Update to 4.8.0

* Thu Sep 03 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.1-1
- Update to 4.7.1

* Mon Aug 31 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 5 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.1

* Tue Apr 21 2020 Gabriel Féron <feron.gabriel@gmail.com> - 4.6.0-1
- Update to 4.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.4.0-1
- Update to 4.4.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Wed Apr 03 2019 Gabriel Féron <feron.gabriel@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Gabriel Féron <feron.gabriel@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-1
- Update to 3.5.1 (#1644323)

* Tue Aug 28 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-1
- Update to 3.4.1 (#1599711)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-1
- Update to 3.3.0 (#1572931)

* Tue Mar 20 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-1
- Update to 3.2.1 (#1523960)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0 (#1523960)

* Mon Oct 23 2017 Miro Hrončok <mhroncok@redhat.com> - 3.0.3-1
- Update to 3.0.3 (#1504321)

* Wed Aug 30 2017 Miro Hrončok <mhroncok@redhat.com> - 2.7.0-1
- Update to 2.7.0 (#1486725)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-1
- New package

