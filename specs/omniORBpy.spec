Name:           omniORBpy
Version:        4.3.2
Release:        6%{?dist}
Summary:        CORBA ORB for Python

License:        LGPL-2.0-or-later
URL:            http://omniorb.sourceforge.net/
Source0:        http://sourceforge.net/projects/omniorb/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2

# Fix FTBFS with Python 3.7 (error: invalid conversion from 'const char*' to 'char*')
Patch0:         omniORBpy_char.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  omniORB-devel
BuildRequires:  python3-devel
BuildRequires:  openssl-devel

%description
omniORBpy is a robust high-performance CORBA ORB for Python.


%package -n python3-omniORB
Summary:        CORBA ORB for Python 3
# For %%{python3_sitelib}/omniidl_be
Requires:       omniORB
%{?python_provide:%python_provide python3-omniORB}

%description -n python3-omniORB
Robust high-performance CORBA ORB for Python 3.


%package -n omniORBpy-devel
Summary:        C++ API for the CORBA ORB for Python
Requires:       omniORB-devel
BuildArch:      noarch

%description -n omniORBpy-devel
C++ API for the CORBA ORB for Python.


%prep
%autosetup -p1


%build
%global _configure ../configure

mkdir build_py3
pushd build_py3
export PYTHON=%{__python3}
%configure --with-omniorb=%{_prefix} --with-openssl=%{_prefix}
%make_build
popd


%install
%make_install -C build_py3

# Remove files which conflict with pyorbit, their sole purpose is to to export the modules to the global namespace via
# sys.modules["<Module>"] = omniORB.<Module>
rm -f %{buildroot}%{python2_sitelib}/CORBA.py*
rm -f %{buildroot}%{python2_sitelib}/PortableServer.py*
rm -f %{buildroot}%{python3_sitelib}/CORBA.py*
rm -f %{buildroot}%{python3_sitelib}/PortableServer.py*

# Ensure shared libraries are executable, otherwise they are not stripped
chmod +x %{buildroot}%{python3_sitearch}/*.so.*

# Fix directory permissions
find %{buildroot}%{python3_sitelib} -type d -exec chmod 755 {} \;


%files -n python3-omniORB
%doc README.Python README.txt ReleaseNotes.txt update.log
%license COPYING.LIB
%{python3_sitelib}/CosNaming*
%{python3_sitelib}/PortableServer__POA.py*
%{python3_sitelib}/omniORB.pth
%{python3_sitelib}/omniORB/
%{python3_sitelib}/__pycache__/*
%{python3_sitearch}/*_omni*.so*

%files -n omniORBpy-devel
%license COPYING.LIB
# %%{_includedir}/omniORB4 is in omniORB-devel
%{_includedir}/omniORB4/*
%{_includedir}/omniORBpy.h
# %%{python3_sitelib}/omniidl_be/__init__.py is in omniORB
%exclude %{python3_sitelib}/omniidl_be/__init__.py
%exclude %{python3_sitelib}/omniidl_be/__pycache__/__init__.*
%{python3_sitelib}/omniidl_be/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.3.2-4
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Sandro Mani <manisandro@gmail.com> - 4.3.2-1
- Update to 4.3.2

* Mon Sep 04 2023 Sandro Mani <manisandro@gmail.com> - 4.3.1-1
- Update to 4.3.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.3.0-7
- Rebuilt for Python 3.12

* Mon Jan 30 2023 Sandro Mani <manisandro@gmail.com> - 4.3.0-6
- Fix FTBFS with Python 3.12 (distutils removed)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.3.0-3
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Sandro Mani <manisandro@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2.4-5
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.4-2
- Rebuilt for Python 3.9

* Tue Apr 07 2020 Sandro Mani <manisandro@gmail.com> - 4.2.4-1
- Update to 4.2.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 4.2.3-6
- Redefine _configure and use standard %configure macro

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.3-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Sandro Mani <manisandro@gmail.com> - 4.2.3-1
- Update to 4.2.3

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 4.2.2-10
- Drop python2 subpackage (#1627335)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.2-8
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 4.2.2-7
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Sandro Mani <manisandro@gmail.com> - 4.2.2-5
- Fix conflict between omniORBpy-devel and omniORB-devel
- Fix accidentally included %%{python2_sitelib}/omniidl_be/ in python2-omniORB

* Fri Aug 04 2017 Sandro Mani <manisandro@gmail.com> - 4.2.2-4
- Add python3 subpackage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 4.2.2-1
- Update to 4.2.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Sandro Mani <manisandro@gmail.com> - 4.2.1-1
- Update to 4.2.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Sandro Mani <manisandro@gmail.com> - 4.2.0-1
- Update to 4.2.0

* Fri Mar 14 2014 Sandro Mani <manisandro@gmail.com> - 3.7-5
- Don't own %%{_includedir}/omniORB4
- Fix FSF addresses
- Fix directory permissions
- Ensure shared libraries are executable

* Wed Feb 19 2014 Sandro Mani <manisandro@gmail.com> - 3.7-4
- Pass --with-openssl, add openssl-devel BR
- Use versioned python BR
- Remove conflicting files

* Tue Feb 18 2014 Sandro Mani <manisandro@gmail.com> - 3.7-3
- Rework subpackages

* Mon Feb 17 2014 Sandro Mani <manisandro@gmail.com> - 3.7-2
- Fix package name
- Merge libs into python subpackage

* Fri Oct 04 2013 Sandro Mani <manisandro@gmail.com> - 3.7-1
- Initial package
