%global modname gradunwarp

Name:           python-%{modname}
Version:        1.2.0
Release:        9%{?dist}
Summary:        Gradient Unwarping

License:        MIT
URL:            https://github.com/Washington-University/gradunwarp
Source0:        https://github.com/Washington-University/gradunwarp/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  gcc

%description
Python/Numpy package used to unwarp the distorted volumes (due to the gradient
field inhomogenities).

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-nibabel
BuildRequires:  python3-nose
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-nibabel

%description -n python3-%{modname}
Python/Numpy package used to unwarp the distorted volumes (due to the gradient
field inhomogenities).

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py3_build

%install
%py3_install

mv %{buildroot}%{_bindir}/gradient_unwarp.py %{buildroot}%{_bindir}/gradient_unwarp
sed -i -e '1s|^.*$|#!%{__python3}|' %{buildroot}%{_bindir}/gradient_unwarp

find %{buildroot}%{python3_sitearch}/%{modname} -name '*.c' -delete

# remove file which installs into bindir
rm -f %{buildroot}%{python3_sitearch}/%{modname}/core/gradient_unwarp.py*

# fix perms on .so
find %{buildroot}%{python3_sitearch}/%{modname}/ -name '*.so' -exec chmod 755 {} \+

%check
pushd gradunwarp/core/tests/
  PYTHONPATH=%{buildroot}%{python3_sitearch} nosetests-%{python3_version} -v
popd

%files -n python3-%{modname}
%license Copying.md
%doc README.md
%{_bindir}/gradient_unwarp
%{python3_sitearch}/%{modname}*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.2.0-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-1
- Update to new release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-9
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuild for Python 3.6

* Thu Oct 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.2-3
- Drop unused provides_exclude

* Wed Nov 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.2-2
- Fix shebang
- Add python3 version
- Fix perms on so

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.2-1
- Initial package
