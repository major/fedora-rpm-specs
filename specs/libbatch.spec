Name:           libbatch
Version:        2.4.5
Release:        15%{?dist}
Summary:        Generic batch management library

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://git.salome-platform.org/gitweb/?p=tools/libbatch.git
Source0:        http://files.salome-platform.org/Salome/other/libBatch-%{version}.tar.gz
# Use lib64 on x86_64
Patch0:         libbatch_libdir.patch
# Set a library soversion
Patch1:         libbatch_soversion.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  swig

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# %%{_datadir}/cmake ownership
Requires:       cmake
# %%{_datadir}/autoconf ownership
Requires:       filesystem

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so|%{_datadir}/myapp/.*)$

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n libBatch-%{version}


%build
%cmake -DLIBBATCH_PYTHONPATH=%{python3_sitearch}
%cmake_build


%install
%cmake_install

# Move autoconf macros to correct place
install -Dpm 0644 %{buildroot}%{_datadir}/%{name}/misc/check_libbatch.m4 %{buildroot}%{_datadir}/aclocal/check_libbatch.m4
rm -rf %{buildroot}%{_datadir}/%{name}


%files
%license COPYING
%{_libdir}/%{name}.so.*
%{python3_sitearch}/_%{name}.so
%{python3_sitearch}/%{name}.py*
%{python3_sitearch}/__pycache__/%{name}.*

%files devel
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/aclocal/check_libbatch.m4
%{_libdir}/%{name}.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.5-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.4.5-12
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.4.5-8
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.5-5
- Rebuilt for Python 3.11

* Sat Mar 05 2022 Sandro Mani <manisandro@gmail.com> - 2.4.5-4
- Fix FTBFS with cmake-3.23.0
- Cleanup spec

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Sandro Mani <manisandro@gmail.com> - 2.4.5-1
- Update to 2.4.5

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.4-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Sandro Mani <manisandro@gmail.com> - 2.4.4-1
- Update to 2.4.4

* Fri Dec 04 2020 Jeff Law <law@redhat.com> - 2.4.3-3
- Re-enable C++-14 force which seems to have gotten lost

* Thu Jul 30 2020 Sandro Mani <manisandro@gmail.com> - 2.4.3-2
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Sandro Mani <manisandro@gmail.com> - 2.4.3-1
- Update to 2.4.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Sandro Mani <manisandro@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Tue Jul 17 2018 Sandro Mani <manisandro@gmail.com> - 2.4.0-3
- Switch to python3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Sandro Mani <manisandro@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 2.3.2-3
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 2.3.2-1
- Update to 2.3.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 06 2016 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-3
- Filter private libaries from Provides/Requires.
- Stop excessive linking (unused-direct-shlib-dependency).
- Add library soversion.

* Sun Feb 16 2014 Sandro Mani <manisandro@gmail.com> - 2.1.0-2
- Explicitly specify python2

* Sun Feb 16 2014 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Thu Oct 03 2013 Sandro Mani <manisandro@gmail.com> - 2.0.0-1.git20131003
- Initial package
