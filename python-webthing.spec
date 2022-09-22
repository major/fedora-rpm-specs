%define realname webthing-python
Name:           python-webthing
Version:        0.15.0
Release:        7%{?dist}
Summary:        HTTP Web Thing implementation in Python
License:        MPLv2.0
URL:            https://github.com/WebThingsIO/webthing-python
Source0:        https://github.com/WebThingsIO/webthing-python/archive/v%{version}.tar.gz#/%{realname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A server implementing the HTTP Web Thing implementation.

%package -n python3-webthing
Summary: HTTP Web Thing implementation in Python
%{?python_provide:%python_provide python3-webthing}

%description -n python3-webthing
A server implementing the HTTP Web Thing implementation.

%prep
%autosetup -p1 -n %{realname}-%{version}
# Remove bundled egg-info
rm -rf %{realname}.egg-info

%build
%py3_build


%install
%py3_install


%files -n python3-webthing
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/webthing/
%{python3_sitelib}/webthing-%{version}-py3.*.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.15.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Sat Oct 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0, update project URLs

* Fri Aug 07 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.2-1
- Update to 0.13.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0

* Tue Jan  7 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.12.0-1
- Update to 0.12.0

* Wed Aug  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-1
- Initial package
